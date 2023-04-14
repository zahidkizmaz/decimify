from decimal import Decimal, InvalidOperation


def decimify(str_number: str) -> Decimal:
    seperators = {".", ","}
    cleanup_characters = {" "}

    if separator := _find_separator(str_number, seperators):
        seperators.remove(separator)
        cleanup_characters = cleanup_characters.union(seperators)
        str_number = _cleanup(str_number, cleanup_characters)
        str_number = str_number.replace(separator, ".")

    return Decimal(str_number)


def _find_separator(str_number: str, seperators: set[str]) -> str:
    found_separator = ""
    found_separator_idx = -1
    for separator in seperators:
        separator_idx = str_number.rfind(separator)
        if separator_idx > found_separator_idx:
            found_separator = separator
            found_separator_idx = separator_idx

    if found_separator and str_number.find(found_separator) != found_separator_idx:
        raise InvalidOperation(
            f"Floating point separator:'{found_separator}' exists multiple times."
        )

    return found_separator


def _cleanup(str_number: str, clean_up_strings: set[str]) -> str:
    for clean_up_string in clean_up_strings:
        str_number = str_number.replace(clean_up_string, "")

    return str_number
