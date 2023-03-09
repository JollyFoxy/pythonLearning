def read_from_file(filepath):
    with open(filepath, "r") as file_object:
        return file_object.readlines()
