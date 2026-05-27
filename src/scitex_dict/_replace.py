#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Timestamp: "2025-11-10 22:40:21 (ywatanabe)"


def replace(string, dict):
    """Perform multiple string substitutions from a mapping dictionary.

    Parameters
    ----------
    string : str
        Input string to transform.
    dict : dict
        Mapping of substring → replacement. Each key found in *string*
        is replaced with its corresponding value, applied in iteration
        order.

    Returns
    -------
    str
        String with all substitutions applied.

    Example
    -------
    >>> replace("hello $name", {"$name": "world"})
    'hello world'
    """
    for k, v in dict.items():
        string = string.replace(k, v)
    return string


# EOF
