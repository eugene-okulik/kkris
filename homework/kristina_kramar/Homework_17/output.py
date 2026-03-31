def print_results(results, search_text):
    if len(results) == 0:
        print("Совпадения не найдены")
        return

    print("Найдено совпадений:", len(results))

    for result in results:
        words = result["block_text"].split()
        fragment = ""

        for index, word in enumerate(words):
            if search_text.lower() in word.lower():
                start_index = max(0, index - 5)
                end_index = index + 6
                fragment_words = words[start_index:end_index]
                fragment = " ".join(fragment_words)
                break

        print("-" * 60)
        print("Файл:", result["file_path"])
        print("Время ошибки:", result["time"])
        print("Строка:", result["line_number"])
        print("Фрагмент:", fragment)
