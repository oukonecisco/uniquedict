from uniquedict.remove_duplicates import remove_duplicates


def test_mixed_presence_of_key():
    users = [
        {"id": 1, "name": "Alice"},
        {"name": "Bob"},
        {"id": 1, "name": "Alice"},
    ]
    assert remove_duplicates(users, "id") == [
        {"id": 1, "name": "Alice"},
        {"name": "Bob"},
    ]


def test_all_elements_as_duplicates():
    users = [{"id": 1}, {"id": 1}, {"id": 1}]
    assert remove_duplicates(users, "id") == [{"id": 1}]


def test_complex_nested_structures():
    users = [
        {"id": 1, "data": {"nested": {"a": 1, "b": [1, 2]}}},
        {"id": 2, "data": {"nested": {"a": 1, "b": [1, 2]}}},
    ]
    assert remove_duplicates(users, "data") == [
        {"id": 1, "data": {"nested": {"a": 1, "b": [1, 2]}}}
    ]


def test_empty_dictionaries():
    users = [{}, {}, {"id": 1}]
    assert remove_duplicates(users, "id") == [{}, {"id": 1}]


def test_non_string_keys():
    users = [{1: "Alice"}, {1: "Alice"}, {2: "Bob"}]
    assert remove_duplicates(users, 1) == [{1: "Alice"}, {2: "Bob"}]


def test_immutable_mutable_mix():
    users = [
        {"id": 1, "data": "immutable"},
        {"id": 1, "data": ["mutable"]},
        {"id": 2, "data": "immutable"},
    ]
    assert remove_duplicates(users, "data") == [
        {"id": 1, "data": "immutable"},
        {"id": 1, "data": ["mutable"]},
    ]


def test_stability():
    users = [{"id": 2}, {"id": 3}, {"id": 2}]
    assert remove_duplicates(users, "id") == [{"id": 2}, {"id": 3}]


# Additional tests can be added as needed.
