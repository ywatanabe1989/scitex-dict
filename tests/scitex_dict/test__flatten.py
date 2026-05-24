#!/usr/bin/env python3
"""Tests for scitex_dict._flatten.flatten."""

import pytest

from scitex_dict._flatten import flatten


def test_flatten_flat_dict_returns_input_unchanged():
    # Arrange
    inp = {"a": 1, "b": 2}

    # Act
    out = flatten(inp)

    # Assert
    assert out == {"a": 1, "b": 2}


def test_flatten_nested_dict_uses_underscore_separator_by_default():
    # Arrange
    inp = {"a": {"b": 1}}

    # Act
    out = flatten(inp)

    # Assert
    assert out == {"a_b": 1}


def test_flatten_deeply_nested_dict_joins_all_levels():
    # Arrange
    inp = {"a": {"b": {"c": 42}}}

    # Act
    out = flatten(inp)

    # Assert
    assert out == {"a_b_c": 42}


def test_flatten_custom_separator_replaces_underscore():
    # Arrange
    inp = {"a": {"b": 1}}

    # Act
    out = flatten(inp, sep=".")

    # Assert
    assert out == {"a.b": 1}


def test_flatten_list_value_becomes_indexed_keys():
    # Arrange
    inp = {"items": [10, 20, 30]}

    # Act
    out = flatten(inp)

    # Assert
    assert out == {"items_0": 10, "items_1": 20, "items_2": 30}


def test_flatten_tuple_value_becomes_indexed_keys():
    # Arrange
    inp = {"x": (4, 5)}

    # Act
    out = flatten(inp)

    # Assert
    assert out == {"x_0": 4, "x_1": 5}


def test_flatten_mixed_nested_dict_and_list_combines_indexing():
    # Arrange
    inp = {"meta": {"tags": ["a", "b"]}}

    # Act
    out = flatten(inp)

    # Assert
    assert out == {"meta_tags_0": "a", "meta_tags_1": "b"}


def test_flatten_parent_key_prefix_is_prepended_to_top_level_keys():
    # Arrange
    inp = {"x": 1}

    # Act
    out = flatten(inp, parent_key="root")

    # Assert
    assert out == {"root_x": 1}


def test_flatten_empty_input_returns_empty_dict():
    # Arrange
    inp = {}

    # Act
    out = flatten(inp)

    # Assert
    assert out == {}


if __name__ == "__main__":
    import os

    pytest.main([os.path.abspath(__file__), "-v"])

# EOF
