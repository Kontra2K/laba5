import string
from collections import Counter
import re


def read_and_process_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()

        sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
        if sentences:
            first_sentence = sentences[0]
            print("Перше речення:")
            print(first_sentence)

        translator = str.maketrans('', '', string.punctuation)
        words = text.translate(translator).lower().split()

        ukrainian_words = [word for word in words if re.match(r'[\u0400-\u04FF]+', word)]
        english_words = [word for word in words if re.match(r'[a-zA-Z]+', word)]

        # Сортування
        ukrainian_words_sorted = sorted(set(ukrainian_words))
        english_words_sorted = sorted(set(english_words))

        print("\nСлова українською:")
        print("\n".join(ukrainian_words_sorted))

        print("\nСлова англійською:")
        print("\n".join(english_words_sorted))

        word_count = len(words)
        print(f"\nКількість слів: {word_count}")

    except FileNotFoundError:
        print("Помилка: Файл не знайдено.")
    except Exception as e:
        print(f"Сталася помилка: {e}")


file_path = 'text_file.txt'
read_and_process_file(file_path)
