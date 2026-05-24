#!/usr/bin/env python3
"""Tests for pop_keys function."""

import pytest

from scitex_dict import pop_keys


def test_pop_keys_removes_specified_keys_from_basic_list():
    # Arrange
    keys_list = ["a", "b", "c", "d", "e"]
    keys_to_pop = ["b", "d"]

    # Act
    result = pop_keys(keys_list, keys_to_pop)

    # Assert
    assert result == ["a", "c", "e"]


def test_pop_keys_does_not_mutate_input_list():
    # Arrange
    keys_list = ["a", "b", "c", "d", "e"]
    keys_to_pop = ["b", "d"]

    # Act
    pop_keys(keys_list, keys_to_pop)

    # Assert
    assert keys_list == ["a", "b", "c", "d", "e"]


def test_pop_keys_with_empty_input_list_returns_empty_result():
    # Arrange
    keys_list = []
    keys_to_pop = ["a", "b"]

    # Act
    result = pop_keys(keys_list, keys_to_pop)

    # Assert
    assert result == []


def test_pop_keys_with_empty_pop_list_returns_input_unchanged():
    # Arrange
    keys_list = ["a", "b", "c"]
    keys_to_pop = []

    # Act
    result = pop_keys(keys_list, keys_to_pop)

    # Assert
    assert result == ["a", "b", "c"]


def test_pop_keys_when_no_keys_match_returns_input_unchanged():
    # Arrange
    keys_list = ["a", "b", "c"]
    keys_to_pop = ["x", "y", "z"]

    # Act
    result = pop_keys(keys_list, keys_to_pop)

    # Assert
    assert result == ["a", "b", "c"]


def test_pop_keys_when_all_keys_match_returns_empty_list():
    # Arrange
    keys_list = ["a", "b", "c"]
    keys_to_pop = ["a", "b", "c"]

    # Act
    result = pop_keys(keys_list, keys_to_pop)

    # Assert
    assert result == []


def test_pop_keys_removes_all_duplicates_in_input_list():
    # Arrange
    keys_list = ["a", "b", "a", "c", "b", "d"]
    keys_to_pop = ["a", "b"]

    # Act
    result = pop_keys(keys_list, keys_to_pop)

    # Assert
    assert result == ["c", "d"]


def test_pop_keys_with_duplicate_keys_in_pop_list_works_correctly():
    # Arrange
    keys_list = ["a", "b", "c", "d"]
    keys_to_pop = ["b", "b", "d", "d"]

    # Act
    result = pop_keys(keys_list, keys_to_pop)

    # Assert
    assert result == ["a", "c"]


def test_pop_keys_with_mixed_types_preserves_remaining_elements():
    # Arrange
    keys_list = ["a", 1, "b", 2, "c", 3.14]
    keys_to_pop = [1, "b"]

    # Act
    result = pop_keys(keys_list, keys_to_pop)

    # Assert
    assert result == ["a", 2, "c", 3.14]


def test_pop_keys_with_numeric_keys_returns_correct_subset():
    # Arrange
    keys_list = [1, 2, 3, 4, 5]
    keys_to_pop = [2, 4]

    # Act
    result = pop_keys(keys_list, keys_to_pop)

    # Assert
    assert result == [1, 3, 5]


def test_pop_keys_partial_string_match_does_not_remove_element():
    # Arrange
    keys_list = ["apple", "app", "application", "apply"]
    keys_to_pop = ["app"]

    # Act
    result = pop_keys(keys_list, keys_to_pop)

    # Assert
    assert result == ["apple", "application", "apply"]


def test_pop_keys_matching_is_case_sensitive():
    # Arrange
    keys_list = ["Apple", "apple", "APPLE", "aPpLe"]
    keys_to_pop = ["apple"]

    # Act
    result = pop_keys(keys_list, keys_to_pop)

    # Assert
    assert result == ["Apple", "APPLE", "aPpLe"]


def test_pop_keys_removes_all_none_occurrences():
    # Arrange
    keys_list = ["a", None, "b", None, "c"]
    keys_to_pop = [None]

    # Act
    result = pop_keys(keys_list, keys_to_pop)

    # Assert
    assert result == ["a", "b", "c"]


def test_pop_keys_boolean_pop_also_matches_integer_equivalents():
    # Arrange
    # Note: In Python, True == 1 and False == 0
    keys_list = [True, False, "true", "false", 1, 0]
    keys_to_pop = [True, False]

    # Act
    result = pop_keys(keys_list, keys_to_pop)

    # Assert
    assert result == ["true", "false"]


def test_pop_keys_docstring_example_returns_expected_subset():
    # Arrange
    keys_list = ["a", "b", "c", "d", "e", "bde"]
    keys_to_pop = ["b", "d"]

    # Act
    result = pop_keys(keys_list, keys_to_pop)

    # Assert
    assert result == ["a", "c", "e", "bde"]


def test_pop_keys_preserves_relative_order_of_kept_elements():
    # Arrange
    keys_list = ["z", "a", "y", "b", "x", "c"]
    keys_to_pop = ["y", "x"]

    # Act
    result = pop_keys(keys_list, keys_to_pop)

    # Assert
    assert result == ["z", "a", "b", "c"]


def test_pop_keys_with_tuple_elements_removes_matching_tuples():
    # Arrange
    keys_list = [("a", 1), ("b", 2), ("c", 3), ("d", 4)]
    keys_to_pop = [("b", 2), ("d", 4)]

    # Act
    result = pop_keys(keys_list, keys_to_pop)

    # Assert
    assert result == [("a", 1), ("c", 3)]


def test_pop_keys_single_element_when_popped_returns_empty():
    # Arrange
    keys_list = ["only"]
    keys_to_pop = ["only"]

    # Act
    result = pop_keys(keys_list, keys_to_pop)

    # Assert
    assert result == []


def test_pop_keys_single_element_when_not_popped_returns_unchanged():
    # Arrange
    keys_list = ["only"]
    keys_to_pop = ["other"]

    # Act
    result = pop_keys(keys_list, keys_to_pop)

    # Assert
    assert result == ["only"]


if __name__ == "__main__":
    import os

    pytest.main([os.path.abspath(__file__)])

# EOF
