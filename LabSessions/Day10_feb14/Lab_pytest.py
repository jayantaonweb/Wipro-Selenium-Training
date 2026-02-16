#
#1.Write a test that is skipped because a feature is not implemented yet.
import pytest

@pytest.mark.skip(reason="Feature not implemented yet")
def test_new_feature():
    # Placeholder for future implementation
    assert False



#2.write a test that runs only on Linux and skips on Windows.

import sys

@pytest.mark.skipif(sys.platform.startswith("win"), reason="Does not run on Windows")
def test_linux_only():
    assert True


#3.Write a test that checks an API health endpoint.
#If status code is not 200 → skip the test dynamically.

import requests

def test_api_health():
    response = requests.get("https://api.example.com/health")

    if response.status_code != 200:
        pytest.skip(f"API not healthy. Status code: {response.status_code}")

    assert response.status_code == 200


#4.Mark a failing test as xfail with reason: "Bug #123".

import pytest

@pytest.mark.xfail(reason="Bug #123")
def test_known_bug():
    assert 1 == 2


#5.You have 5 parameterized cases.
#   2 are known bugs.
#   Mark only those 2 cases as xfail without marking entire test.

@pytest.mark.parametrize("number", [1 ,2, 3 ,4 ,5])
def test_even(number):
    assert number%2 == 0