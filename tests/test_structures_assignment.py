
import pytest
from requests.structures import CaseInsensitiveDict


@pytest.mark.structures
def test_lookup_with_lowercase_key():
    data = CaseInsensitiveDict({"Name": "Sitara"})
    assert data["name"] == "Sitara"


@pytest.mark.structures
def test_lookup_with_uppercase_key():
    data = CaseInsensitiveDict({"name": "Sitara"})
    assert data["NAME"] == "Sitara"


@pytest.mark.structures
def test_different_keys():
    data = CaseInsensitiveDict({"Name": "Sitara", "City": "Faisalabad"})
    assert data["name"] == "Sitara"
    assert data["city"] == "Faisalabad"


@pytest.mark.structures
def test_empty_dictionary_length():
    data = CaseInsensitiveDict()
    assert len(data) == 0


@pytest.mark.structures
def test_one_entry_length():
    data = CaseInsensitiveDict({"Name": "Sitara"})
    assert len(data) == 1


@pytest.mark.structures
def test_multiple_entry_length():
    data = CaseInsensitiveDict(
        {"Name": "Sitara", "City": "Faisalabad", "Course": "SE"}
    )
    assert len(data) == 3


@pytest.mark.structures
def test_missing_key_raises_key_error():
    data = CaseInsensitiveDict({"Name": "Sitara"})
    with pytest.raises(KeyError):
        data["Age"]


@pytest.mark.structures
def test_empty_string_key():
    data = CaseInsensitiveDict({"": "empty key"})
    assert data[""] == "empty key"


@pytest.mark.structures
def test_latest_key_capitalization_is_preserved():
    data = CaseInsensitiveDict()
    data["Name"] = "First"
    data["NAME"] = "Updated"
    assert data["name"] == "Updated"
    assert list(data.keys()) == ["NAME"]


@pytest.mark.structures
def test_copy_preserves_values():
    data = CaseInsensitiveDict({"Name": "Sitara", "City": "Faisalabad"})
    copied_data = data.copy()
    assert copied_data["NAME"] == "Sitara"
    assert copied_data["city"] == "Faisalabad"
