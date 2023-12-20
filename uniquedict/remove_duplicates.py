from typing import Any, Dict, Hashable, List


def make_hashable(value: Any) -> Hashable:
    """
    Convert a value into a hashable form. This function is used for handling
    embedded lists or dictionaries in the deduplication key. It ensures that
    the value can be used in a set for identifying duplicates.
    """
    if isinstance(value, (int, float, str, bool, type(None))):
        return value  # Primitives are already hashable
    if isinstance(value, list):
        # Convert list to tuple for hashability
        return tuple(make_hashable(item) for item in value)
    if isinstance(value, dict):
        # Convert dict to sorted tuple of key-value pairs for consistent hashability
        return tuple(sorted((k, make_hashable(v)) for k, v in value.items()))
    # Fallback for other types, ensuring they are converted to a string
    return str(value)


def remove_duplicates(
    users: List[Dict[str, Any]], deduplication_key: str
) -> List[Dict[str, Any]]:
    """
    Remove duplicate dictionaries from a list based on a specific key.
    Handles keys with embedded values like lists or dictionaries.

    :param users: List of dictionaries with user data.
    :param deduplication_key: The key used to identify duplicates.
    :return: A list of dictionaries without duplicates based on the deduplication key.
    """
    unique_users = []
    seen_values = set()

    for user in users:
        if deduplication_key in user:
            value = make_hashable(user[deduplication_key])
            if value not in seen_values:
                unique_users.append(user)
                seen_values.add(value)
        else:
            # If the deduplication key is not present, add the user as unique
            unique_users.append(user)

    return unique_users
