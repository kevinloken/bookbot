#!/usr/bin/env python3

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    freq = {}
    low = text.lower()
    for ch in low:
        if not ch.isalpha():
            continue
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    return freq

def sort_on(dict):
    return dict["count"]

def freq_to_list(freq):
    freq_list = []
    for char, count in freq.items():
        freq_list.append({"char": char, "count": count})
    return freq_list

def generate_report(text):
    words = count_words(text)
    freq = count_characters(text)
    characters = freq_to_list(freq)
    characters.sort(key=sort_on, reverse=True)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document")
    print()
    for item in characters:
        print(f"The character \'{item['char']}\' was found {item['count']} times.")
    print("--- End of report ---")

def main():
    with open('books/frankenstein.txt') as file:
        text = file.read()
    generate_report(text)


if __name__ == '__main__':
    main()
