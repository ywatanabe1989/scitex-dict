#!/usr/bin/env python3
"""Tests for scitex_dict._replace.replace."""

import pytest

from scitex_dict._replace import replace


class TestReplace:
    def test_single_substitution(self):
        assert replace("hello world", {"hello": "hi"}) == "hi world"

    def test_multiple_substitutions(self):
        assert replace("a b c", {"a": "1", "c": "3"}) == "1 b 3"

    def test_empty_dict_returns_unchanged(self):
        assert replace("hello", {}) == "hello"

    def test_no_match_returns_unchanged(self):
        assert replace("hello", {"x": "y"}) == "hello"

    def test_substitutions_chain_predictably(self):
        out = replace("a", {"a": "b", "b": "c"})
        assert out == "c"

    def test_replaces_all_occurrences(self):
        assert replace("aaa", {"a": "b"}) == "bbb"


if __name__ == "__main__":
    import os

    pytest.main([os.path.abspath(__file__), "-v"])

# EOF
