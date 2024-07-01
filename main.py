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

def main():
    with open('books/frankenstein.txt') as file:
        text = file.read()
    print(text)
    print(f'Number of words: {count_words(text)}')
    print(f'Frequency of characters: {count_characters(text)}')


if __name__ == '__main__':
    main()
