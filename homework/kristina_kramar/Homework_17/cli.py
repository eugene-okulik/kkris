import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description="Поиск текста в логах")

    parser.add_argument("path", type=str, help="Полный путь к файлу или папке с логами")

    parser.add_argument("--text", type=str, required=True, help="Текст для поиска")

    args = parser.parse_args()
    return args
