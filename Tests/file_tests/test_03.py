from Func.file_riader import read_from_file


def test_file():
    test_data = ['one\n', 'two\n', 'three\n']
    assert test_data == read_from_file("/home/pavel/PycharmProjects/pythonProject/Tests/file_tests/testfile.txt")
