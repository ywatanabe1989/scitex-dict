"""scitex-dict quickstart: dict utilities (DotDict, flatten, listed_dict)."""

import scitex_dict


def main():
    # 1. DotDict — attribute access on nested dicts.
    cfg = scitex_dict.DotDict(
        {"db": {"host": "localhost", "port": 5432}, "debug": True}
    )
    print("cfg.db.host:", cfg.db.host)
    assert cfg.db.host == "localhost"
    assert cfg.debug is True

    # 2. flatten — collapse nested dict to dotted keys.
    flat = scitex_dict.flatten({"a": {"b": {"c": 1}}, "d": 2})
    print("flatten:", flat)

    # 3. listed_dict — invert mapping into list-valued buckets.
    grouped = scitex_dict.listed_dict([("a", 1), ("b", 2), ("a", 3)])
    print("listed_dict:", dict(grouped))

    # 4. pop_keys — remove and return multiple keys at once.
    d = {"x": 1, "y": 2, "z": 3}
    rest = scitex_dict.pop_keys(d, ["x", "z"])
    print("pop_keys remaining:", rest)

    # 5. to_str — pretty stringification.
    s = scitex_dict.to_str({"alpha": 1, "beta": 2})
    print("to_str:", s)


if __name__ == "__main__":
    main()
