#!/usr/bin/env python3
"""Tests for DotDict class."""

import json

import pytest

from scitex_dict import DotDict

# --- initialization ---------------------------------------------------------


def test_dotdict_empty_initialization_has_zero_length():
    # Arrange
    # (no setup needed)

    # Act
    dd = DotDict()

    # Assert
    assert len(dd) == 0


def test_dotdict_empty_initialization_has_no_keys():
    # Arrange
    # (no setup needed)

    # Act
    dd = DotDict()

    # Assert
    assert list(dd.keys()) == []


def test_dotdict_init_from_dict_exposes_keys_as_attributes():
    # Arrange
    data = {"key1": "value1", "key2": 2}

    # Act
    dd = DotDict(data)

    # Assert
    assert dd.key1 == "value1"


def test_dotdict_init_from_dict_supports_item_access():
    # Arrange
    data = {"key1": "value1", "key2": 2}

    # Act
    dd = DotDict(data)

    # Assert
    assert dd["key2"] == 2


def test_dotdict_init_from_dict_sets_length_to_input_size():
    # Arrange
    data = {"key1": "value1", "key2": 2}

    # Act
    dd = DotDict(data)

    # Assert
    assert len(dd) == 2


def test_dotdict_init_with_string_raises_type_error():
    # Arrange
    bad_input = "not a dict"

    # Act
    def call():
        return DotDict(bad_input)

    # Assert
    with pytest.raises(TypeError, match="Input must be a dictionary"):
        call()


def test_dotdict_init_with_list_raises_type_error():
    # Arrange
    bad_input = [1, 2, 3]

    # Act
    def call():
        return DotDict(bad_input)

    # Assert
    with pytest.raises(TypeError, match="Input must be a dictionary"):
        call()


# --- attribute access -------------------------------------------------------


def test_dotdict_attribute_get_returns_stored_string_value():
    # Arrange
    dd = DotDict({"name": "test", "value": 42})

    # Act
    got = dd.name

    # Assert
    assert got == "test"


def test_dotdict_attribute_get_returns_stored_int_value():
    # Arrange
    dd = DotDict({"name": "test", "value": 42})

    # Act
    got = dd.value

    # Assert
    assert got == 42


def test_dotdict_attribute_set_overwrites_existing_value():
    # Arrange
    dd = DotDict({"name": "test"})

    # Act
    dd.name = "updated"

    # Assert
    assert dd.name == "updated"


def test_dotdict_attribute_set_creates_new_attribute():
    # Arrange
    dd = DotDict({"name": "test"})

    # Act
    dd.new_attr = "new_value"

    # Assert
    assert dd.new_attr == "new_value"


def test_dotdict_attribute_delete_removes_key():
    # Arrange
    dd = DotDict({"value": 42})

    # Act
    del dd.value

    # Assert
    assert "value" not in dd


def test_dotdict_attribute_access_after_delete_raises_attribute_error():
    # Arrange
    dd = DotDict({"value": 42})
    del dd.value

    # Act
    def call():
        return dd.value

    # Assert
    with pytest.raises(AttributeError):
        call()


# --- item access ------------------------------------------------------------


def test_dotdict_item_set_string_key_stores_value():
    # Arrange
    dd = DotDict()

    # Act
    dd["key1"] = "value1"

    # Assert
    assert dd["key1"] == "value1"


def test_dotdict_item_set_integer_key_stores_value():
    # Arrange
    dd = DotDict()

    # Act
    dd[100] = "integer key"

    # Assert
    assert dd[100] == "integer key"


def test_dotdict_item_set_hyphenated_key_stores_value():
    # Arrange
    dd = DotDict()

    # Act
    dd["invalid-key"] = "hyphenated"

    # Assert
    assert dd["invalid-key"] == "hyphenated"


def test_dotdict_item_delete_removes_integer_key():
    # Arrange
    dd = DotDict()
    dd[100] = "integer key"

    # Act
    del dd[100]

    # Assert
    assert 100 not in dd


def test_dotdict_item_access_after_delete_raises_key_error():
    # Arrange
    dd = DotDict()
    dd[100] = "integer key"
    del dd[100]

    # Act
    def call():
        return dd[100]

    # Assert
    with pytest.raises(KeyError):
        call()


# --- nested conversion ------------------------------------------------------


def test_dotdict_nested_dict_supports_chained_attribute_access():
    # Arrange
    data = {"level1": {"level2": {"level3": "deep_value"}}}

    # Act
    dd = DotDict(data)

    # Assert
    assert dd.level1.level2.level3 == "deep_value"


def test_dotdict_nested_dict_first_level_is_converted_to_dotdict():
    # Arrange
    data = {"level1": {"level2": {"level3": "deep_value"}}}

    # Act
    dd = DotDict(data)

    # Assert
    assert isinstance(dd.level1, DotDict)


def test_dotdict_nested_dict_second_level_is_converted_to_dotdict():
    # Arrange
    data = {"level1": {"level2": {"level3": "deep_value"}}}

    # Act
    dd = DotDict(data)

    # Assert
    assert isinstance(dd.level1.level2, DotDict)


def test_dotdict_nested_set_on_inner_level_persists():
    # Arrange
    dd = DotDict({"level1": {"level2": {"level3": "deep_value"}}})

    # Act
    dd.level1.level2.new_key = "new_value"

    # Assert
    assert dd.level1.level2.new_key == "new_value"


# --- integer / non-identifier keys ------------------------------------------


def test_dotdict_integer_key_is_retrievable_via_item_syntax():
    # Arrange
    # (no setup needed)

    # Act
    dd = DotDict({100: "int_key"})

    # Assert
    assert dd[100] == "int_key"


def test_dotdict_hyphenated_key_is_retrievable_via_item_syntax():
    # Arrange
    # (no setup needed)

    # Act
    dd = DotDict({"invalid-key": "hyphen"})

    # Assert
    assert dd["invalid-key"] == "hyphen"


def test_dotdict_digit_starting_key_is_retrievable_via_item_syntax():
    # Arrange
    # (no setup needed)

    # Act
    dd = DotDict({"123start": "digit_start"})

    # Assert
    assert dd["123start"] == "digit_start"


def test_dotdict_valid_identifier_key_works_via_attribute_syntax():
    # Arrange
    # (no setup needed)

    # Act
    dd = DotDict({"valid_key": "string_key"})

    # Assert
    assert dd.valid_key == "string_key"


def test_dotdict_valid_identifier_key_also_works_via_item_syntax():
    # Arrange
    # (no setup needed)

    # Act
    dd = DotDict({"valid_key": "string_key"})

    # Assert
    assert dd["valid_key"] == "string_key"


# --- standard dict methods --------------------------------------------------


def test_dotdict_keys_returns_view_of_all_keys():
    # Arrange
    dd = DotDict({"a": 1, "b": 2, "c": 3})

    # Act
    got = set(dd.keys())

    # Assert
    assert got == {"a", "b", "c"}


def test_dotdict_values_returns_view_of_all_values():
    # Arrange
    dd = DotDict({"a": 1, "b": 2, "c": 3})

    # Act
    got = set(dd.values())

    # Assert
    assert got == {1, 2, 3}


def test_dotdict_items_returns_view_of_key_value_pairs():
    # Arrange
    dd = DotDict({"a": 1, "b": 2, "c": 3})

    # Act
    got = set(dd.items())

    # Assert
    assert got == {("a", 1), ("b", 2), ("c", 3)}


def test_dotdict_get_existing_key_returns_value():
    # Arrange
    dd = DotDict({"a": 1, "b": 2, "c": 3})

    # Act
    got = dd.get("a")

    # Assert
    assert got == 1


def test_dotdict_get_missing_key_returns_default():
    # Arrange
    dd = DotDict({"a": 1})

    # Act
    got = dd.get("z", "default")

    # Assert
    assert got == "default"


def test_dotdict_pop_existing_key_returns_value():
    # Arrange
    dd = DotDict({"b": 2})

    # Act
    got = dd.pop("b")

    # Assert
    assert got == 2


def test_dotdict_pop_removes_key_from_dict():
    # Arrange
    dd = DotDict({"b": 2})

    # Act
    dd.pop("b")

    # Assert
    assert "b" not in dd


def test_dotdict_pop_missing_key_with_default_returns_default():
    # Arrange
    dd = DotDict({"a": 1})

    # Act
    got = dd.pop("z", "default")

    # Assert
    assert got == "default"


def test_dotdict_pop_missing_key_without_default_raises_key_error():
    # Arrange
    dd = DotDict({"a": 1})

    # Act
    def call():
        return dd.pop("nonexistent")

    # Assert
    with pytest.raises(KeyError):
        call()


# --- update -----------------------------------------------------------------


def test_dotdict_update_with_dict_adds_first_new_key():
    # Arrange
    dd = DotDict({"a": 1})

    # Act
    dd.update({"b": 2, "c": 3})

    # Assert
    assert dd.b == 2


def test_dotdict_update_with_dict_adds_second_new_key():
    # Arrange
    dd = DotDict({"a": 1})

    # Act
    dd.update({"b": 2, "c": 3})

    # Assert
    assert dd.c == 3


def test_dotdict_update_with_iterable_pairs_adds_first_key():
    # Arrange
    dd = DotDict({"a": 1})

    # Act
    dd.update([("d", 4), ("e", 5)])

    # Assert
    assert dd.d == 4


def test_dotdict_update_with_iterable_pairs_adds_second_key():
    # Arrange
    dd = DotDict({"a": 1})

    # Act
    dd.update([("d", 4), ("e", 5)])

    # Assert
    assert dd.e == 5


def test_dotdict_update_with_nested_dict_converts_to_dotdict():
    # Arrange
    dd = DotDict({"a": 1})

    # Act
    dd.update({"nested": {"key": "value"}})

    # Assert
    assert isinstance(dd.nested, DotDict)


def test_dotdict_update_with_nested_dict_preserves_inner_value():
    # Arrange
    dd = DotDict({"a": 1})

    # Act
    dd.update({"nested": {"key": "value"}})

    # Assert
    assert dd.nested.key == "value"


# --- setdefault -------------------------------------------------------------


def test_dotdict_setdefault_returns_existing_value_when_key_present():
    # Arrange
    dd = DotDict({"a": 1})

    # Act
    got = dd.setdefault("a", 10)

    # Assert
    assert got == 1


def test_dotdict_setdefault_does_not_overwrite_existing_value():
    # Arrange
    dd = DotDict({"a": 1})
    dd.setdefault("a", 10)

    # Act
    got = dd.a

    # Assert
    assert got == 1


def test_dotdict_setdefault_returns_new_default_when_key_absent():
    # Arrange
    dd = DotDict({"a": 1})

    # Act
    got = dd.setdefault("b", 2)

    # Assert
    assert got == 2


def test_dotdict_setdefault_inserts_new_default_when_key_absent():
    # Arrange
    dd = DotDict({"a": 1})
    dd.setdefault("b", 2)

    # Act
    got = dd.b

    # Assert
    assert got == 2


def test_dotdict_setdefault_with_dict_default_converts_to_dotdict():
    # Arrange
    dd = DotDict({"a": 1})

    # Act
    dd.setdefault("nested", {"key": "value"})

    # Assert
    assert isinstance(dd.nested, DotDict)


# --- contains ---------------------------------------------------------------


def test_dotdict_contains_string_key_returns_true():
    # Arrange
    dd = DotDict({"a": 1, 100: "int_key"})

    # Act
    got = "a" in dd

    # Assert
    assert got is True


def test_dotdict_contains_integer_key_returns_true():
    # Arrange
    dd = DotDict({"a": 1, 100: "int_key"})

    # Act
    got = 100 in dd

    # Assert
    assert got is True


def test_dotdict_contains_unknown_key_returns_false():
    # Arrange
    dd = DotDict({"a": 1})

    # Act
    got = "nonexistent" in dd

    # Assert
    assert got is False


# --- iteration --------------------------------------------------------------


def test_dotdict_iteration_yields_all_keys():
    # Arrange
    data = {"a": 1, "b": 2, "c": 3}
    dd = DotDict(data)

    # Act
    keys = set(iter(dd))

    # Assert
    assert keys == set(data.keys())


def test_dotdict_for_loop_visits_all_items_pairs():
    # Arrange
    data = {"a": 1, "b": 2, "c": 3}
    dd = DotDict(data)

    # Act
    collected = {(k, dd[k]) for k in dd}

    # Assert
    assert collected == set(data.items())


# --- copy -------------------------------------------------------------------


def test_dotdict_shallow_copy_top_level_changes_do_not_affect_original():
    # Arrange
    dd = DotDict({"a": 1, "nested": {"b": 2}})
    dd_copy = dd.copy()

    # Act
    dd_copy.a = 10

    # Assert
    assert dd.a == 1


def test_dotdict_shallow_copy_new_top_level_key_does_not_appear_in_original():
    # Arrange
    dd = DotDict({"a": 1, "nested": {"b": 2}})
    dd_copy = dd.copy()

    # Act
    dd_copy.c = 3

    # Assert
    assert "c" not in dd


def test_dotdict_shallow_copy_shares_nested_object_with_original():
    # Arrange
    dd = DotDict({"a": 1, "nested": {"b": 2}})
    dd_copy = dd.copy()

    # Act
    dd_copy.nested.b = 20

    # Assert
    assert dd.nested.b == 20


# --- to_dict ----------------------------------------------------------------


def test_dotdict_to_dict_returns_plain_dict_instance():
    # Arrange
    dd = DotDict({"a": 1, "nested": {"b": 2, "deep": {"c": 3}}, 100: "int_key"})

    # Act
    result = dd.to_dict()

    # Assert
    assert isinstance(result, dict) and not isinstance(result, DotDict)


def test_dotdict_to_dict_preserves_string_keyed_value():
    # Arrange
    dd = DotDict({"a": 1, 100: "int_key"})

    # Act
    result = dd.to_dict()

    # Assert
    assert result["a"] == 1


def test_dotdict_to_dict_preserves_integer_keyed_value():
    # Arrange
    dd = DotDict({"a": 1, 100: "int_key"})

    # Act
    result = dd.to_dict()

    # Assert
    assert result[100] == "int_key"


def test_dotdict_to_dict_converts_nested_dotdict_back_to_plain_dict():
    # Arrange
    dd = DotDict({"nested": {"b": 2, "deep": {"c": 3}}})

    # Act
    result = dd.to_dict()

    # Assert
    assert isinstance(result["nested"], dict) and not isinstance(
        result["nested"], DotDict
    )


def test_dotdict_to_dict_preserves_deeply_nested_value():
    # Arrange
    dd = DotDict({"nested": {"b": 2, "deep": {"c": 3}}})

    # Act
    result = dd.to_dict()

    # Assert
    assert result["nested"]["deep"]["c"] == 3


# --- string representation --------------------------------------------------


def test_dotdict_repr_contains_key_names():
    # Arrange
    dd = DotDict({"name": "test", "value": 42})

    # Act
    repr_str = repr(dd)

    # Assert
    assert "'name'" in repr_str or '"name"' in repr_str


def test_dotdict_repr_contains_string_values():
    # Arrange
    dd = DotDict({"name": "test", "value": 42})

    # Act
    repr_str = repr(dd)

    # Assert
    assert "test" in repr_str


def test_dotdict_str_returns_valid_json_with_correct_string_value():
    # Arrange
    dd = DotDict({"name": "test", "value": 42})

    # Act
    parsed = json.loads(str(dd))

    # Assert
    assert parsed["name"] == "test"


def test_dotdict_str_returns_valid_json_with_correct_numeric_value():
    # Arrange
    dd = DotDict({"name": "test", "value": 42})

    # Act
    parsed = json.loads(str(dd))

    # Assert
    assert parsed["value"] == 42


def test_dotdict_str_falls_back_to_str_for_non_json_serializable_values():
    # Arrange
    class CustomObj:
        def __str__(self):
            return "CustomObject"

    dd = DotDict({"obj": CustomObj()})

    # Act
    str_repr = str(dd)

    # Assert
    assert "CustomObject" in str_repr


# --- dir() ------------------------------------------------------------------


def test_dotdict_dir_includes_valid_identifier_keys():
    # Arrange
    dd = DotDict({"valid_key": 1, "another_key": 2})

    # Act
    dir_result = dir(dd)

    # Assert
    assert {"valid_key", "another_key"}.issubset(dir_result)


def test_dotdict_dir_includes_standard_dict_methods():
    # Arrange
    dd = DotDict({"valid_key": 1})

    # Act
    dir_result = dir(dd)

    # Assert
    assert {"keys", "items"}.issubset(dir_result)


def test_dotdict_dir_excludes_integer_keys():
    # Arrange
    dd = DotDict({100: "int_key"})

    # Act
    dir_result = dir(dd)

    # Assert
    assert 100 not in dir_result


def test_dotdict_dir_excludes_hyphenated_keys():
    # Arrange
    dd = DotDict({"invalid-key": 3})

    # Act
    dir_result = dir(dd)

    # Assert
    assert "invalid-key" not in dir_result


# --- protected attributes ---------------------------------------------------


def test_dotdict_underscore_attribute_lookup_raises_attribute_error_when_missing():
    # Arrange
    dd = DotDict()

    # Act
    def call():
        return dd._nonexistent

    # Assert
    with pytest.raises(AttributeError):
        call()


def test_dotdict_underscore_attribute_can_be_set_and_retrieved():
    # Arrange
    dd = DotDict()

    # Act
    dd._custom = "value"

    # Assert
    assert dd._custom == "value"


# --- edge cases -------------------------------------------------------------


def test_dotdict_empty_string_key_stores_and_retrieves_value():
    # Arrange
    dd = DotDict()

    # Act
    dd[""] = "empty"

    # Assert
    assert dd[""] == "empty"


def test_dotdict_method_name_collision_stores_via_item_syntax():
    # Arrange
    dd = DotDict()

    # Act
    dd["keys"] = "not_a_method"

    # Assert
    assert dd["keys"] == "not_a_method"


def test_dotdict_method_name_collision_keeps_callable_method_accessible():
    # Arrange
    dd = DotDict()
    dd["keys"] = "not_a_method"

    # Act
    got = callable(dd.keys)

    # Assert
    assert got is True


def test_dotdict_none_as_key_stores_and_retrieves_value():
    # Arrange
    dd = DotDict()

    # Act
    dd[None] = "none_value"

    # Assert
    assert dd[None] == "none_value"


def test_dotdict_complex_nested_update_preserves_deep_list_dict_mixture():
    # Arrange
    dd = DotDict()

    # Act
    dd.update({"level1": {"level2": {"data": [1, 2, {"nested": "value"}]}}})

    # Assert
    assert dd.level1.level2.data[2]["nested"] == "value"


if __name__ == "__main__":
    import os

    pytest.main([os.path.abspath(__file__)])

# EOF
