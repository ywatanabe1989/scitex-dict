#!/usr/bin/env python3
"""Tests for listed_dict function."""

from collections import defaultdict

import pytest

from scitex_dict import listed_dict


def test_listed_dict_no_keys_returns_defaultdict_instance():
    # Arrange
    # (no setup needed)

    # Act
    d = listed_dict()

    # Assert
    assert isinstance(d, defaultdict)


def test_listed_dict_no_keys_uses_list_as_default_factory():
    # Arrange
    # (no setup needed)

    # Act
    d = listed_dict()

    # Assert
    assert d.default_factory == list


def test_listed_dict_no_keys_starts_with_empty_container():
    # Arrange
    # (no setup needed)

    # Act
    d = listed_dict()

    # Assert
    assert len(d) == 0


def test_listed_dict_appends_to_unseen_key_creates_singleton_list():
    # Arrange
    d = listed_dict()

    # Act
    d["new_key"].append(1)

    # Assert
    assert d["new_key"] == [1]


def test_listed_dict_multiple_appends_to_same_key_accumulate():
    # Arrange
    d = listed_dict()

    # Act
    d["key2"].append("a")
    d["key2"].append("b")

    # Assert
    assert d["key2"] == ["a", "b"]


def test_listed_dict_with_keys_initializes_all_provided_keys():
    # Arrange
    keys = ["a", "b", "c"]

    # Act
    d = listed_dict(keys)

    # Assert
    assert set(d.keys()) == {"a", "b", "c"}


def test_listed_dict_with_keys_initializes_each_key_to_empty_list():
    # Arrange
    keys = ["a", "b", "c"]

    # Act
    d = listed_dict(keys)

    # Assert
    assert all(d[k] == [] for k in keys)


def test_listed_dict_append_to_existing_initialized_key_accumulates():
    # Arrange
    d = listed_dict(["x", "y"])

    # Act
    d["x"].append(10)
    d["x"].append(20)

    # Assert
    assert d["x"] == [10, 20]


def test_listed_dict_append_to_new_key_outside_init_list_works():
    # Arrange
    d = listed_dict(["x", "y"])

    # Act
    d["z"].append(3.14)

    # Assert
    assert d["z"] == [3.14]


def test_listed_dict_mixed_value_types_coexist_in_same_list():
    # Arrange
    d = listed_dict()

    # Act
    d["mixed"].append(1)
    d["mixed"].append("string")
    d["mixed"].append([1, 2, 3])
    d["mixed"].append({"nested": "dict"})
    d["mixed"].append(None)

    # Assert
    assert d["mixed"] == [1, "string", [1, 2, 3], {"nested": "dict"}, None]


def test_listed_dict_extend_on_value_appends_iterable_items():
    # Arrange
    d = listed_dict(["nums"])

    # Act
    d["nums"].extend([1, 2, 3])

    # Assert
    assert d["nums"] == [1, 2, 3]


def test_listed_dict_insert_on_value_places_item_at_index():
    # Arrange
    d = listed_dict(["nums"])
    d["nums"].extend([1, 2, 3])

    # Act
    d["nums"].insert(1, "inserted")

    # Assert
    assert d["nums"] == [1, "inserted", 2, 3]


def test_listed_dict_remove_on_value_drops_matching_element():
    # Arrange
    d = listed_dict(["nums"])
    d["nums"].extend([1, "inserted", 2, 3])

    # Act
    d["nums"].remove("inserted")

    # Assert
    assert d["nums"] == [1, 2, 3]


def test_listed_dict_pop_on_value_returns_last_element():
    # Arrange
    d = listed_dict(["nums"])
    d["nums"].extend([1, 2, 3])

    # Act
    popped = d["nums"].pop()

    # Assert
    assert popped == 3


def test_listed_dict_pop_on_value_shrinks_list():
    # Arrange
    d = listed_dict(["nums"])
    d["nums"].extend([1, 2, 3])

    # Act
    d["nums"].pop()

    # Assert
    assert d["nums"] == [1, 2]


def test_listed_dict_with_empty_keys_list_creates_empty_defaultdict():
    # Arrange
    # (no setup needed)

    # Act
    d = listed_dict([])

    # Assert
    assert isinstance(d, defaultdict) and len(d) == 0


def test_listed_dict_with_empty_keys_still_lazily_creates_new_keys():
    # Arrange
    d = listed_dict([])

    # Act
    d["new"].append(42)

    # Assert
    assert d["new"] == [42]


def test_listed_dict_duplicate_keys_are_deduplicated_via_dict_semantics():
    # Arrange
    keys = ["a", "b", "a", "c", "b"]

    # Act
    d = listed_dict(keys)

    # Assert
    assert sorted(d.keys()) == ["a", "b", "c"]


def test_listed_dict_handles_none_as_a_valid_key():
    # Arrange
    keys = ["a", None, "b"]

    # Act
    d = listed_dict(keys)

    # Assert
    assert None in d and d[None] == []


def test_listed_dict_append_to_none_key_accumulates_in_list():
    # Arrange
    d = listed_dict(["a", None, "b"])

    # Act
    d[None].append("none_value")

    # Assert
    assert d[None] == ["none_value"]


def test_listed_dict_numeric_keys_are_supported_directly():
    # Arrange
    keys = [1, 2.5, 3]

    # Act
    d = listed_dict(keys)

    # Assert
    assert d[1] == [] and d[2.5] == [] and d[3] == []


def test_listed_dict_numeric_key_append_accumulates_normally():
    # Arrange
    d = listed_dict([1, 2.5, 3])

    # Act
    d[1].append("one")
    d[2.5].append("two-point-five")

    # Assert
    assert d[1] == ["one"] and d[2.5] == ["two-point-five"]


def test_listed_dict_keys_iteration_yields_all_initialized_keys():
    # Arrange
    keys = ["first", "second", "third"]
    d = listed_dict(keys)

    # Act
    collected = set(d.keys())

    # Assert
    assert collected == set(keys)


def test_listed_dict_items_iteration_yields_list_values():
    # Arrange
    d = listed_dict(["first", "second", "third"])
    d["first"].extend([1, 2])
    d["second"].append("data")

    # Act
    types = {type(v) for _, v in d.items()}

    # Assert
    assert types == {list}


def test_listed_dict_delete_removes_key_from_container():
    # Arrange
    d = listed_dict(["a", "b", "c"])
    d["a"].append(1)
    d["b"].extend([2, 3])

    # Act
    del d["a"]

    # Assert
    assert "a" not in d


def test_listed_dict_after_delete_re_appending_starts_fresh_list():
    # Arrange
    d = listed_dict(["a", "b", "c"])
    d["a"].append(1)
    del d["a"]

    # Act
    d["a"].append(99)

    # Assert
    assert d["a"] == [99]


def test_listed_dict_direct_assignment_creates_shared_reference():
    # Arrange
    d1 = listed_dict(["x"])
    d1["x"].append(1)
    d2 = d1

    # Act
    d2["x"].append(2)

    # Assert
    assert d1["x"] == [1, 2]


def test_listed_dict_shallow_copy_shares_list_references():
    # Arrange
    d1 = listed_dict(["x"])
    d1["x"].append(1)
    d3 = d1.copy()

    # Act
    d3["x"].append(3)

    # Assert
    assert d1["x"] == [1, 3]


def test_listed_dict_deepcopy_isolates_nested_lists_from_original():
    # Arrange
    import copy

    d1 = listed_dict(["x"])
    d1["x"].extend([1, 2])
    d4 = copy.deepcopy(d1)

    # Act
    d4["x"].append(4)

    # Assert
    assert d1["x"] == [1, 2] and d4["x"] == [1, 2, 4]


def test_listed_dict_real_world_grouping_pattern_produces_expected_groups():
    # Arrange
    items_by_category = listed_dict(["fruits", "vegetables", "dairy"])
    items = [
        ("apple", "fruits"),
        ("carrot", "vegetables"),
        ("banana", "fruits"),
        ("milk", "dairy"),
        ("lettuce", "vegetables"),
        ("cheese", "dairy"),
        ("orange", "fruits"),
    ]

    # Act
    for item, category in items:
        items_by_category[category].append(item)

    # Assert
    assert items_by_category == {
        "fruits": ["apple", "banana", "orange"],
        "vegetables": ["carrot", "lettuce"],
        "dairy": ["milk", "cheese"],
    }


def test_listed_dict_dynamic_new_category_can_be_added_after_init():
    # Arrange
    items_by_category = listed_dict(["fruits", "vegetables", "dairy"])

    # Act
    items_by_category["grains"].append("bread")

    # Assert
    assert items_by_category["grains"] == ["bread"]


if __name__ == "__main__":
    import os

    pytest.main([os.path.abspath(__file__)])

# EOF
