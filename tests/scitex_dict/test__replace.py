#!/usr/bin/env python3
"""Tests for scitex_dict._replace.replace."""

import pytest

from scitex_dict._replace import replace


def test_replace_single_key_substitutes_in_string():
    # Arrange
    text = "hello world"
    mapping = {"hello": "hi"}

    # Act
    out = replace(text, mapping)

    # Assert
    assert out == "hi world"


def test_replace_multiple_keys_substitutes_each_independently():
    # Arrange
    text = "a b c"
    mapping = {"a": "1", "c": "3"}

    # Act
    out = replace(text, mapping)

    # Assert
    assert out == "1 b 3"


def test_replace_empty_mapping_returns_input_unchanged():
    # Arrange
    text = "hello"
    mapping = {}

    # Act
    out = replace(text, mapping)

    # Assert
    assert out == "hello"


def test_replace_no_matching_keys_returns_input_unchanged():
    # Arrange
    text = "hello"
    mapping = {"x": "y"}

    # Act
    out = replace(text, mapping)

    # Assert
    assert out == "hello"


def test_replace_chained_substitutions_apply_sequentially():
    # Arrange
    text = "a"
    mapping = {"a": "b", "b": "c"}

    # Act
    out = replace(text, mapping)

    # Assert
    assert out == "c"


def test_replace_repeated_occurrences_are_all_replaced():
    # Arrange
    text = "aaa"
    mapping = {"a": "b"}

    # Act
    out = replace(text, mapping)

    # Assert
    assert out == "bbb"


if __name__ == "__main__":
    import os

    pytest.main([os.path.abspath(__file__), "-v"])

# EOF
