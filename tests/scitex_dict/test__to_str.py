#!/usr/bin/env python3
"""Tests for to_str function."""

from collections import OrderedDict

import pytest

from scitex_dict import to_str


def test_to_str_basic_dict_uses_dash_and_underscore_format():
    # Arrange
    d = OrderedDict([("a", 1), ("b", 2), ("c", 3)])

    # Act
    result = to_str(d)

    # Assert
    assert result == "a-1_b-2_c-3"


def test_to_str_empty_dict_returns_empty_string():
    # Arrange
    d = {}

    # Act
    result = to_str(d)

    # Assert
    assert result == ""


def test_to_str_single_item_dict_returns_single_pair():
    # Arrange
    d = {"key": "value"}

    # Act
    result = to_str(d)

    # Assert
    assert result == "key-value"


def test_to_str_custom_pipe_delimiter_replaces_underscore():
    # Arrange
    d = OrderedDict([("x", 10), ("y", 20)])

    # Act
    result = to_str(d, delimiter="|")

    # Assert
    assert result == "x-10|y-20"


def test_to_str_multi_character_delimiter_replaces_underscore():
    # Arrange
    d = OrderedDict([("x", 10), ("y", 20)])

    # Act
    result = to_str(d, delimiter=" AND ")

    # Assert
    assert result == "x-10 AND y-20"


def test_to_str_with_numeric_values_renders_repr_form():
    # Arrange
    d = OrderedDict([("int", 42), ("float", 3.14), ("negative", -10), ("zero", 0)])

    # Act
    result = to_str(d)

    # Assert
    assert result == "int-42_float-3.14_negative--10_zero-0"


def test_to_str_with_string_values_preserves_spaces_and_empty():
    # Arrange
    d = OrderedDict([("name", "John"), ("city", "New York"), ("empty", "")])

    # Act
    result = to_str(d)

    # Assert
    assert result == "name-John_city-New York_empty-"


def test_to_str_special_characters_in_keys_and_values_pass_through():
    # Arrange
    d = OrderedDict(
        [
            ("key-with-dash", "value"),
            ("key_with_underscore", "value"),
            ("key", "value-with-dash"),
        ]
    )

    # Act
    result = to_str(d)

    # Assert
    assert result == (
        "key-with-dash-value_key_with_underscore-value_key-value-with-dash"
    )


def test_to_str_unicode_characters_render_literally():
    # Arrange
    d = OrderedDict([("Hello", "World"), ("你好", "世界"), ("こんにちは", "世界")])

    # Act
    result = to_str(d)

    # Assert
    assert result == "Hello-World_你好-世界_こんにちは-世界"


def test_to_str_boolean_values_use_python_repr():
    # Arrange
    d = OrderedDict([("true", True), ("false", False)])

    # Act
    result = to_str(d)

    # Assert
    assert result == "true-True_false-False"


def test_to_str_none_value_renders_as_literal_None():
    # Arrange
    d = {"key": None}

    # Act
    result = to_str(d)

    # Assert
    assert result == "key-None"


def test_to_str_mixed_value_types_each_use_their_str_repr():
    # Arrange
    d = OrderedDict(
        [
            ("str", "hello"),
            ("int", 123),
            ("float", 45.6),
            ("bool", True),
            ("none", None),
        ]
    )

    # Act
    result = to_str(d)

    # Assert
    assert result == "str-hello_int-123_float-45.6_bool-True_none-None"


def test_to_str_numeric_keys_render_as_their_str_form():
    # Arrange
    d = OrderedDict([(1, "one"), (2, "two"), (3, "three")])

    # Act
    result = to_str(d)

    # Assert
    assert result == "1-one_2-two_3-three"


def test_to_str_empty_delimiter_concatenates_pairs_without_separator():
    # Arrange
    d = OrderedDict([("a", 1), ("b", 2)])

    # Act
    result = to_str(d, delimiter="")

    # Assert
    assert result == "a-1b-2"


def test_to_str_newline_delimiter_separates_pairs_with_newline():
    # Arrange
    d = OrderedDict([("x", 1), ("y", 2)])

    # Act
    result = to_str(d, delimiter="\n")

    # Assert
    assert result == "x-1\ny-2"


def test_to_str_tab_delimiter_separates_pairs_with_tab():
    # Arrange
    d = OrderedDict([("x", 1), ("y", 2)])

    # Act
    result = to_str(d, delimiter="\t")

    # Assert
    assert result == "x-1\ty-2"


def test_to_str_complex_values_use_python_str_representation():
    # Arrange
    d = OrderedDict(
        [("list", [1, 2, 3]), ("tuple", (4, 5, 6)), ("dict", {"nested": "value"})]
    )

    # Act
    result = to_str(d)

    # Assert
    assert result == "list-[1, 2, 3]_tuple-(4, 5, 6)_dict-{'nested': 'value'}"


def test_to_str_preserves_dict_insertion_order_in_python_37_plus():
    # Arrange
    d = {"z": 1, "y": 2, "x": 3}

    # Act
    result = to_str(d)

    # Assert
    assert result == "z-1_y-2_x-3"


def test_to_str_large_dict_produces_expected_number_of_pairs():
    # Arrange
    d = OrderedDict((f"key{i}", f"value{i}") for i in range(100))

    # Act
    result = to_str(d)

    # Assert
    assert len(result.split("_")) == 100


def test_to_str_large_dict_first_pair_renders_correctly():
    # Arrange
    d = OrderedDict((f"key{i}", f"value{i}") for i in range(100))

    # Act
    result = to_str(d)

    # Assert
    assert result.split("_")[0] == "key0-value0"


def test_to_str_large_dict_last_pair_renders_correctly():
    # Arrange
    d = OrderedDict((f"key{i}", f"value{i}") for i in range(100))

    # Act
    result = to_str(d)

    # Assert
    assert result.split("_")[99] == "key99-value99"


def test_to_str_delimiter_inside_values_does_not_corrupt_output():
    # Arrange
    d = OrderedDict([("key1", "value_with_underscore"), ("key2", "normal_value")])

    # Act
    result = to_str(d)

    # Assert
    assert result == "key1-value_with_underscore_key2-normal_value"


def test_to_str_whitespace_in_keys_and_values_is_preserved_literally():
    # Arrange
    d = OrderedDict([(" key ", " value "), ("key\n", "value\t")])

    # Act
    result = to_str(d)

    # Assert
    assert result == " key - value _key\n-value\t"


if __name__ == "__main__":
    import os

    pytest.main([os.path.abspath(__file__)])

# EOF
