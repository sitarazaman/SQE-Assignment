
import pytest
from requests.utils import to_native_string


@pytest.mark.utils
def test_bytes_to_native_string():
    assert to_native_string(b"hello") == "hello"


@pytest.mark.utils
def test_string_remains_string():
    assert to_native_string("hello") == "hello"


@pytest.mark.utils
def test_empty_bytes():
    assert to_native_string(b"") == ""


@pytest.mark.utils
def test_empty_string():
    assert to_native_string("") == ""


@pytest.mark.utils
def test_single_character():
    assert to_native_string(b"A") == "A"


@pytest.mark.utils
def test_word_value():
    assert to_native_string(b"requests") == "requests"


@pytest.mark.utils
@pytest.mark.parametrize(
    "value, expected",
    [
        (b"hello", "hello"),
        (b"requests", "requests"),
        (b"FAST", "FAST"),
        (b"12345", "12345"),
        (b"test case", "test case"),
    ],
)
def test_parametrized_values(value, expected):
    assert to_native_string(value) == expected


@pytest.mark.utils
def test_utf8_bytes():
    assert to_native_string("café".encode("utf-8"), "utf-8") == "café"
