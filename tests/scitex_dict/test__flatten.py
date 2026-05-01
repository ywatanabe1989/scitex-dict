#!/usr/bin/env python3
"""Tests for scitex_dict._flatten.flatten."""

import pytest

from scitex_dict._flatten import flatten


class TestFlatten:
    def test_flat_dict_unchanged(self):
        assert flatten({"a": 1, "b": 2}) == {"a": 1, "b": 2}

    def test_nested_dict_uses_underscore_sep(self):
        assert flatten({"a": {"b": 1}}) == {"a_b": 1}

    def test_deeply_nested(self):
        assert flatten({"a": {"b": {"c": 42}}}) == {"a_b_c": 42}

    def test_custom_separator(self):
        assert flatten({"a": {"b": 1}}, sep=".") == {"a.b": 1}

    def test_list_values_become_indexed(self):
        out = flatten({"items": [10, 20, 30]})
        assert out == {"items_0": 10, "items_1": 20, "items_2": 30}

    def test_tuple_values_become_indexed(self):
        out = flatten({"x": (4, 5)})
        assert out == {"x_0": 4, "x_1": 5}

    def test_mixed_nested_and_list(self):
        out = flatten({"meta": {"tags": ["a", "b"]}})
        assert out == {"meta_tags_0": "a", "meta_tags_1": "b"}

    def test_parent_key_prefix(self):
        out = flatten({"x": 1}, parent_key="root")
        assert out == {"root_x": 1}

    def test_empty_dict_returns_empty(self):
        assert flatten({}) == {}


if __name__ == "__main__":
    import os

    pytest.main([os.path.abspath(__file__), "-v"])

# EOF
