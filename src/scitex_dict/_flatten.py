#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Timestamp: "2025-11-10 22:38:40 (ywatanabe)"


def flatten(nested_dict, parent_key="", sep="_"):
    """Recursively flatten a nested dict into a single-level dict.

    Keys are joined with ``sep`` (default ``"_"``). List / tuple values
    are indexed numerically (``key_0``, ``key_1``, …).

    Parameters
    ----------
    nested_dict : dict
        The (possibly nested) dictionary to flatten.
    parent_key : str, optional
        Internal — used during recursion to accumulate the key prefix.
    sep : str, optional
        Separator between parent and child keys (default ``"_"``).

    Returns
    -------
    dict
        Single-level dictionary with joined keys.

    Example
    -------
    >>> flatten({"a": {"b": 1, "c": 2}})
    {'a_b': 1, 'a_c': 2}
    """
    items = []
    for key, value in nested_dict.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict):
            items.extend(flatten(value, new_key, sep=sep).items())
        elif isinstance(value, (list, tuple)):
            for idx, item in enumerate(value):
                items.append((f"{new_key}_{idx}", item))
        else:
            items.append((new_key, value))
    return dict(items)


# EOF
