import netsentinel


# A test function: pytest runs any function whose name starts with "test_"
def test_version():
    # assert = "this must be true, or the test fails" (replaces JUnit's assertEquals)
    # == compares values; never use "is" for strings
    assert netsentinel.__version__ == "0.0.1"
