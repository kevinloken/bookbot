#!/usr/bin/env python3

def main():
    with open('books/frankenstein.txt') as file:
        text = file.read()
    print(text)

if __name__ == '__main__':
    main()
