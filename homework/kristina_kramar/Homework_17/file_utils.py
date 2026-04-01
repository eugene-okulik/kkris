import os


def detect_path_type(path):
    if not os.path.exists(path):
        print("Указанный путь не существует")
        return None

    if os.path.isfile(path):
        return "file"

    if os.path.isdir(path):
        return "folder"


def get_files_from_path(path, path_type):
    files = []

    if path_type == "file":
        files.append(path)

    elif path_type == "folder":
        for name in os.listdir(path):
            full_path = os.path.join(path, name)

            if os.path.isfile(full_path):
                files.append(full_path)

    return files
