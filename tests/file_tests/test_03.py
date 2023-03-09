from Func.file_riader import read_from_file


def test_file():
    test_file_path = "/home/pavel/PycharmProjects/pythonProject/tests/file_tests/testfile.txt"
    test_data = ['one\n', 'two\n', 'three\n']
    with open(test_file_path, "a") as f_o:
        f_o.writelines(test_data)
    assert test_data == read_from_file(test_file_path)
