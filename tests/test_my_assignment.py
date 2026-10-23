
import pytest
from requests.utils import to_native_string
import csv
from pathlib import Path

@pytest.mark.order(1)
def test_to_native_string():
    result = to_native_string(b"hello")
    assert result == "hello"


def test_to_native_string():
    result = to_native_string(b"hello")
    assert result == "hello"


def test_to_native_string_empty():
    result = to_native_string(b"")
    assert result == ""


def test_to_native_string_single_character():
    result = to_native_string(b"a")
    assert result == "a"


def test_to_native_string_word():
    result = to_native_string(b"requests")
    assert result == "requests"


@pytest.mark.parametrize(
    "input_value, expected",
    [
        (b"hello", "hello"),
        (b"", ""),
        (b"a", "a"),
        (b"requests", "requests"),
        (b"FAST", "FAST"),
    ],
)
def test_to_native_string_parameterized(input_value, expected):
    assert to_native_string(input_value) == expected



def load_csv_test_data():
    csv_path = Path(__file__).with_name("test_data.csv")

    with open(csv_path, newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


@pytest.mark.parametrize(
    "input_value, expected",
    [
        (row["input_value"].encode("ascii"), row["expected"])
        for row in load_csv_test_data()
    ],
)
def test_to_native_string_from_csv(input_value, expected):
    assert to_native_string(input_value) == expected
