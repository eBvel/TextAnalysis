def get_text():
    while True:
        text = input("\nВведите текст: ")
        if not text:
            print("Ошибка: поле пустое. Введите, пожалуйста, текст!")
        else:
            return text


def remove_punctuation_marks(text):
    result = ""
    punctuation_marks = {'!', '"', ';', ':', '?', '-', '.', ',', '\'', '—', '\''}

    for letter in text:
        is_mark = False
        for mark in punctuation_marks:
            if letter == mark:
                is_mark = True
                continue
        if not is_mark:
            result += letter

    return result


def get_longest_word(words):
    longest_word = ""
    for word in words:
        if len(longest_word) < len(word):
            longest_word = word
    return longest_word


def vowels_counter(text):
    vowels_count = 0
    vowels = {'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я'}

    for letter in text:
        for vowel in vowels:
            if letter == vowel:
                vowels_count += 1
                continue
    return vowels_count


def word_repetition_counter(words):
    unique_words = set(words)

    for unique_word in unique_words:
        count = 0
        for word in words:
            if unique_word == word:
                count += 1
        yield f"{unique_word} - {count}"


def description():
    print("""ОПИСАНИЕ: 
    Программа анализирует текст и выводит следующую информацию:
    количество слов в тексте, самое длинное слово, количество гласных букв
    и количество раз, которое каждое слово встречается в тексте.
    Для начала работы введите текст для анализа. 
    Чтобы завершить работу введите - "стоп".""")


def main():
    at_work = True

    while at_work:
        text = get_text().lower()
        if text == "стоп":
            at_work = False
            print("\nПрограмма завершена!")
            continue

        text_without_punctuation_mars = remove_punctuation_marks(text)
        words = text_without_punctuation_mars.split()
        vowels_count = vowels_counter(text_without_punctuation_mars)

        print(f"\nКоличество слов в тексте: {len(words)}")
        print(f"Самое длинное слово: {get_longest_word(words)}")
        print(f"Количество гласных букв: {vowels_count}")

        print("\nПОВТОРЕНИЕ СЛОВ:")
        for repeated_word in word_repetition_counter(words):
            print(repeated_word)


description()
main()
