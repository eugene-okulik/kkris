from datetime import datetime


def extract_time_from_line(line):
    if len(line) >= 23:
        possible_time = line[:23]

        try:
            datetime.strptime(possible_time, "%Y-%m-%d %H:%M:%S.%f")
            return possible_time
        except ValueError:
            pass

    if len(line) >= 19:
        possible_time = line[:19]

        try:
            datetime.strptime(possible_time, "%Y-%m-%d %H:%M:%S")
            return possible_time
        except ValueError:
            pass

    return None


def find_text_in_files(file_paths, search_text):
    results = []
    search_text_lower = search_text.lower()

    for file_path in file_paths:
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                current_time = None
                current_block_lines = []
                block_start_line = None
                current_line_number = 0

                for line in file:
                    current_line_number += 1
                    line = line.rstrip("\n")

                    new_time = extract_time_from_line(line)

                    if new_time is not None:
                        if current_time is not None:
                            block_text = "\n".join(current_block_lines)

                            if search_text_lower in block_text.lower():
                                found_line_number = block_start_line

                                for index, block_line in enumerate(current_block_lines):
                                    if search_text_lower in block_line.lower():
                                        found_line_number = block_start_line + index
                                        break

                                result = {
                                    "file_path": file_path,
                                    "time": current_time,
                                    "line_number": found_line_number,
                                    "block_text": block_text
                                }
                                results.append(result)

                        current_time = new_time
                        current_block_lines = [line]
                        block_start_line = current_line_number

                    else:
                        if current_time is not None:
                            current_block_lines.append(line)

                if current_time is not None:
                    block_text = "\n".join(current_block_lines)

                    if search_text_lower in block_text.lower():
                        found_line_number = block_start_line

                        for index, block_line in enumerate(current_block_lines):
                            if search_text_lower in block_line.lower():
                                found_line_number = block_start_line + index
                                break

                        result = {
                            "file_path": file_path,
                            "time": current_time,
                            "line_number": found_line_number,
                            "block_text": block_text
                        }
                        results.append(result)

        except Exception as error:
            print(f"Не удалось прочитать файл: {file_path}")
            print(f"Причина: {error}")

    return results
