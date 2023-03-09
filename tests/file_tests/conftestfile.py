import pytest


@pytest.fixture(autouse=True)
def clean_text_file():
    test_file_path = "/home/pavel/PycharmProjects/pythonProject/tests/file_tests/testfile.txt"
    with open(test_file_path, "w"):
        pass
