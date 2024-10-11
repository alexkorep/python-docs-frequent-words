import os
import argparse
from collections import defaultdict
import re

def count_words_in_file(filepath):
    word_count = defaultdict(int)
    with open(filepath, 'r', encoding='utf-8') as file:
        text = file.read()
        # Using regex to find words, ignoring punctuation, excluding words with digits or underscores
        words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
        for word in words:
            word_count[word] += 1
    return word_count

def scan_directory(directory):
    total_word_count = defaultdict(int)
    # Recursively scan for txt files
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                file_word_count = count_words_in_file(file_path)
                # Merge word counts from each file
                for word, count in file_word_count.items():
                    total_word_count[word] += count
    return total_word_count

def filter_frequent_words(word_count, threshold=10):
    return {word: count for word, count in word_count.items() if count > threshold}

def main(directory):
    word_count = scan_directory(directory)
    frequent_words = filter_frequent_words(word_count)

    print("Words appearing more than 10 times (sorted by frequency):")
    sorted_words = sorted(frequent_words.items(), key=lambda item: item[1], reverse=True)
    for word, count in sorted_words:
        print(f"{word}: {count}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Count words in Python documentation")
    parser.add_argument("directory", help="Directory to scan for txt files (e.g., doc)")
    args = parser.parse_args()

    main(args.directory)