#!/usr/bin/env python3
"""Tests for safe_merge function."""

import pytest

from scitex_dict import safe_merge


def test_safe_merge_two_disjoint_dicts_returns_union():
    # Arrange
    dict1 = {"a": 1, "b": 2}
    dict2 = {"c": 3, "d": 4}

    # Act
    result = safe_merge(dict1, dict2)

    # Assert
    assert result == {"a": 1, "b": 2, "c": 3, "d": 4}


def test_safe_merge_does_not_mutate_first_input_dict():
    # Arrange
    dict1 = {"a": 1, "b": 2}
    dict2 = {"c": 3, "d": 4}

    # Act
    safe_merge(dict1, dict2)

    # Assert
    assert dict1 == {"a": 1, "b": 2}


def test_safe_merge_does_not_mutate_second_input_dict():
    # Arrange
    dict1 = {"a": 1, "b": 2}
    dict2 = {"c": 3, "d": 4}

    # Act
    safe_merge(dict1, dict2)

    # Assert
    assert dict2 == {"c": 3, "d": 4}


def test_safe_merge_all_empty_dicts_returns_empty():
    # Arrange
    # (no setup needed)

    # Act
    result = safe_merge({}, {}, {})

    # Assert
    assert result == {}


def test_safe_merge_empty_then_populated_returns_populated_copy():
    # Arrange
    # (no setup needed)

    # Act
    result = safe_merge({}, {"a": 1})

    # Assert
    assert result == {"a": 1}


def test_safe_merge_populated_then_empty_returns_populated_copy():
    # Arrange
    # (no setup needed)

    # Act
    result = safe_merge({"a": 1}, {})

    # Assert
    assert result == {"a": 1}


def test_safe_merge_single_dict_argument_returns_equal_dict():
    # Arrange
    dict1 = {"a": 1, "b": 2}

    # Act
    result = safe_merge(dict1)

    # Assert
    assert result == {"a": 1, "b": 2}


def test_safe_merge_single_dict_argument_returns_fresh_object():
    # Arrange
    dict1 = {"a": 1, "b": 2}

    # Act
    result = safe_merge(dict1)

    # Assert
    assert result is not dict1


def test_safe_merge_with_no_arguments_returns_empty_dict():
    # Arrange
    # (no setup needed)

    # Act
    result = safe_merge()

    # Assert
    assert result == {}


def test_safe_merge_overlapping_keys_raises_value_error():
    # Arrange
    dict1 = {"a": 1, "b": 2}
    dict2 = {"b": 3, "c": 4}

    # Act
    def call():
        return safe_merge(dict1, dict2)

    # Assert
    with pytest.raises(ValueError, match="Overlapping keys found"):
        call()


def test_safe_merge_four_disjoint_dicts_returns_full_union():
    # Arrange
    dict1 = {"a": 1}
    dict2 = {"b": 2}
    dict3 = {"c": 3}
    dict4 = {"d": 4}

    # Act
    result = safe_merge(dict1, dict2, dict3, dict4)

    # Assert
    assert result == {"a": 1, "b": 2, "c": 3, "d": 4}


def test_safe_merge_preserves_list_value_unchanged():
    # Arrange
    dict1 = {"list": [1, 2, 3]}
    dict2 = {"other": 0}

    # Act
    result = safe_merge(dict1, dict2)

    # Assert
    assert result["list"] == [1, 2, 3]


def test_safe_merge_preserves_nested_dict_value_unchanged():
    # Arrange
    dict1 = {"nested": {"inside": True}}
    dict2 = {"other": 0}

    # Act
    result = safe_merge(dict1, dict2)

    # Assert
    assert result["nested"] == {"inside": True}


def test_safe_merge_preserves_set_value_unchanged():
    # Arrange
    dict1 = {"other": 0}
    dict2 = {"s": {4, 5, 6}}

    # Act
    result = safe_merge(dict1, dict2)

    # Assert
    assert result["s"] == {4, 5, 6}


def test_safe_merge_preserves_none_value():
    # Arrange
    dict1 = {"other": 0}
    dict2 = {"none": None}

    # Act
    result = safe_merge(dict1, dict2)

    # Assert
    assert result["none"] is None


def test_safe_merge_preserves_false_bool_value():
    # Arrange
    dict1 = {"other": 0}
    dict2 = {"bool": False}

    # Act
    result = safe_merge(dict1, dict2)

    # Assert
    assert result["bool"] is False


def test_safe_merge_numeric_keys_merge_correctly():
    # Arrange
    dict1 = {1: "one", 2: "two"}
    dict2 = {3: "three", 4: "four"}

    # Act
    result = safe_merge(dict1, dict2)

    # Assert
    assert result == {1: "one", 2: "two", 3: "three", 4: "four"}


def test_safe_merge_mixed_key_types_disjoint_merge_correctly():
    # Arrange
    dict1 = {"a": 1, 1: "one"}
    dict2 = {"b": 2, 2: "two"}

    # Act
    result = safe_merge(dict1, dict2)

    # Assert
    assert result == {"a": 1, 1: "one", "b": 2, 2: "two"}


def test_safe_merge_none_as_key_value_pair_merges_correctly():
    # Arrange
    dict1 = {None: "none_value", "a": 1}
    dict2 = {"b": 2, "c": 3}

    # Act
    result = safe_merge(dict1, dict2)

    # Assert
    assert result == {None: "none_value", "a": 1, "b": 2, "c": 3}


def test_safe_merge_overlap_on_none_key_raises_value_error():
    # Arrange
    dict1 = {None: "value1"}
    dict2 = {None: "value2"}

    # Act
    def call():
        return safe_merge(dict1, dict2)

    # Assert
    with pytest.raises(ValueError, match="Overlapping keys found"):
        call()


def test_safe_merge_third_dict_overlapping_first_raises_value_error():
    # Arrange
    dict1 = {"a": 1}
    dict2 = {"b": 2}
    dict3 = {"a": 3}

    # Act
    def call():
        return safe_merge(dict1, dict2, dict3)

    # Assert
    with pytest.raises(ValueError, match="Overlapping keys found"):
        call()


def test_safe_merge_multiple_overlapping_keys_raises_value_error():
    # Arrange
    dict1 = {"a": 1, "b": 2, "c": 3}
    dict2 = {"a": 10, "b": 20, "d": 4}

    # Act
    def call():
        return safe_merge(dict1, dict2)

    # Assert
    with pytest.raises(ValueError, match="Overlapping keys found"):
        call()


def test_safe_merge_preserves_left_to_right_insertion_order():
    # Arrange
    dict1 = {"z": 1, "y": 2}
    dict2 = {"x": 3, "w": 4}
    dict3 = {"v": 5, "u": 6}

    # Act
    result = safe_merge(dict1, dict2, dict3)

    # Assert
    assert list(result.keys()) == ["z", "y", "x", "w", "v", "u"]


def test_safe_merge_large_dicts_total_size_is_sum_of_parts():
    # Arrange
    dict1 = {f"a{i}": i for i in range(100)}
    dict2 = {f"b{i}": i for i in range(100)}
    dict3 = {f"c{i}": i for i in range(100)}

    # Act
    result = safe_merge(dict1, dict2, dict3)

    # Assert
    assert len(result) == 300


def test_safe_merge_large_dicts_sample_values_preserved():
    # Arrange
    dict1 = {f"a{i}": i for i in range(100)}
    dict2 = {f"b{i}": i for i in range(100)}
    dict3 = {f"c{i}": i for i in range(100)}

    # Act
    result = safe_merge(dict1, dict2, dict3)

    # Assert
    assert (result["a50"], result["b75"], result["c99"]) == (50, 75, 99)


def test_safe_merge_unicode_keys_disjoint_merge_correctly():
    # Arrange
    dict1 = {"Hello": 1, "世界": 2}
    dict2 = {"你好": 3, "Bonjour": 4}

    # Act
    result = safe_merge(dict1, dict2)

    # Assert
    assert result == {"Hello": 1, "世界": 2, "你好": 3, "Bonjour": 4}


def test_safe_merge_frozenset_keys_merge_correctly():
    # Arrange
    dict1 = {frozenset([1, 2]): "frozen1"}
    dict2 = {frozenset([3, 4]): "frozen2"}

    # Act
    result = safe_merge(dict1, dict2)

    # Assert
    assert result == {
        frozenset([1, 2]): "frozen1",
        frozenset([3, 4]): "frozen2",
    }


if __name__ == "__main__":
    import os

    pytest.main([os.path.abspath(__file__)])

# EOF
