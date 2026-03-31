from cli import parse_arguments
from file_utils import detect_path_type, get_files_from_path
from search import find_text_in_files
from output import print_results


def main():
    args = parse_arguments()

    path_type = detect_path_type(args.path)
    if path_type is None:
        return

    file_paths = get_files_from_path(args.path, path_type)
    results = find_text_in_files(file_paths, args.text)

    print_results(results, args.text)


main()
