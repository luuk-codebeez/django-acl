import re

_first_cap_re = re.compile("(.)([A-Z][a-z]+)")
_all_cap_re = re.compile("([a-z0-9])([A-Z])")


def camelcase_to_underscore(name: str) -> str:
    """
    convert camelcase to underscore

    Args:
        name: camelcase string

    Returns:
        name: name converted to underscore string
    """
    name = _first_cap_re.sub(r"\1_\2", name)
    name = _all_cap_re.sub(r"\1_\2", name).lower()
    return name


def csv_string_to_list(value: str) -> str:
    if value:
        value_list = value.split(",")
    else:
        value_list = []
    return value_list
