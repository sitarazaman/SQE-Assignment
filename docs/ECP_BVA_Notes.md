# ECP and BVA Testing Notes — Requests Library

## 1. Module: `requests.utils`

**Selected function:** `to_native_string()`

**Purpose:** Converts a bytes value into a native string using the specified encoding. A string input remains unchanged.

### Equivalence Class Partitioning (ECP)

| Test ID | Input class | Example input | Expected result |
|---|---|---|---|
| UT-ECP-01 | Valid bytes | `b"hello"` | `"hello"` |
| UT-ECP-02 | Empty bytes | `b""` | `""` |
| UT-ECP-03 | Valid string | `"hello"` | `"hello"` |
| UT-ECP-04 | Empty string | `""` | `""` |
| UT-ECP-05 | Bytes containing UTF-8 text | `"café".encode("utf-8")` | `"café"` with UTF-8 encoding |

### Boundary Value Analysis (BVA)

| Test ID | Boundary condition | Example input | Expected result |
|---|---|---|---|
| UT-BVA-01 | Empty input | `b""` | Empty string |
| UT-BVA-02 | One character | `b"A"` | `"A"` |
| UT-BVA-03 | Short string | `b"AB"` | `"AB"` |
| UT-BVA-04 | Longer string | `b"requests"` | `"requests"` |

**Result:** The selected tests check empty, single-character, normal, and encoded string inputs.

---

## 2. Module: `requests.structures`

**Selected class:** `CaseInsensitiveDict`

**Purpose:** Stores dictionary entries and allows keys to be accessed without case sensitivity.

### Equivalence Class Partitioning (ECP)

| Test ID | Input class | Example input | Expected result |
|---|---|---|---|
| ST-ECP-01 | Lowercase key lookup | Store `"Name"`, read `"name"` | Value is returned |
| ST-ECP-02 | Uppercase key lookup | Store `"name"`, read `"NAME"` | Value is returned |
| ST-ECP-03 | Multiple entries | Store `"Name"` and `"City"` | Both values are returned |
| ST-ECP-04 | Missing key | Read `"Age"` when absent | `KeyError` is raised |
| ST-ECP-05 | Empty dictionary | No entries | Length is zero |

### Boundary Value Analysis (BVA)

| Test ID | Boundary condition | Example input | Expected result |
|---|---|---|---|
| ST-BVA-01 | Zero entries | `{}` | Length `0` |
| ST-BVA-02 | One entry | `{"Name": "Sitara"}` | Length `1` |
| ST-BVA-03 | Multiple entries | Three different keys | Length `3` |
| ST-BVA-04 | Empty key | `{"": "empty key"}` | Value can be accessed |
| ST-BVA-05 | Reassign same key with different case | `"Name"` then `"NAME"` | Updated value is returned |

**Result:** The selected tests cover case-insensitive lookup, dictionary size boundaries, missing keys, and reassignment behavior.

---

## 3. Module: `requests.models`

**Selected class:** `Response`

**Selected property:** `ok`

**Purpose:** Returns `True` when `raise_for_status()` does not raise an `HTTPError`, and `False` when it does.

### Equivalence Class Partitioning (ECP)

| Test ID | Input class | Status code | Expected result |
|---|---|---:|---|
| MO-ECP-01 | Successful response | `200` | `True` |
| MO-ECP-02 | Created response | `201` | `True` |
| MO-ECP-03 | Redirect response | `301` | `True` |
| MO-ECP-04 | Client error | `404` | `False` |
| MO-ECP-05 | Server error | `500` | `False` |

### Boundary Value Analysis (BVA)

| Test ID | Boundary condition | Status code | Expected result |
|---|---|---:|---|
| MO-BVA-01 | Informational response example | `100` | `True` |
| MO-BVA-02 | Normal success boundary example | `200` | `True` |
| MO-BVA-03 | Highest tested value below 400 | `399` | `True` |
| MO-BVA-04 | Error boundary | `400` | `False` |
| MO-BVA-05 | High server-error value | `599` | `False` |

**Result:** The tests cover success, redirection, client errors, server errors, and values around the 400 status-code boundary.

---

## Overall Conclusion

Three components from the Requests library were selected for testing: `to_native_string()`, `CaseInsensitiveDict`, and `Response.ok`. Equivalence Class Partitioning was used to group inputs into categories, while Boundary Value Analysis was used to check important edge values. The automated tests are implemented using pytest and use markers to organize tests by component.

The current assignment test files contain 32 test executions in total: 12 for `requests.utils`, 10 for `requests.structures`, and 10 for `requests.models`. All 32 tests passed in the reported run.

**Note:** These are assignment test notes based on the selected test cases, not a claim of complete coverage of the Requests library.
