import sys
import os

def get_contents(file_path):
    with open(file_path) as f:
        return f.read()

def get_word_count(file_contents):
    words = file_contents.split()
    return len(words)

def get_character_counts(file_contents):
    lowered_contents = file_contents.lower()
    char_counts = {}
    for char in lowered_contents:
        if char_counts.get(char) is None:
            char_counts[char] = 1
        else:
            char_counts[char] += 1

    return char_counts

def sort_on_count(single_char_dict):
    return single_char_dict["count"]

def format_character_counts(char_count_dict):
    char_count_list = []
    for char in char_count_dict.keys():
        if char.isalpha():
            char_count_list.append({ "char": char, "count": char_count_dict[char] })
    
    char_count_list.sort(reverse = True, key = sort_on_count)

    return char_count_list
            
def print_report(file_path, word_count, character_counts):
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document\r\n")
    for char_dict in character_counts:
        print(f"The '{char_dict["char"]}' character was found {char_dict["count"]} times")
    print("--- End report ---")

def main(args):
    if len(args) == 1:
        print("Please provide a file path (ex: python main.py books/frankenstein.txt)")
        exit(1)
    elif not os.path.exists(args[1]):
        print(f"File not found: {args[1]}")
        exit(1)

    file_path = args[1]
    file_contents = get_contents(file_path)
    word_count = get_word_count(file_contents)
    character_counts = format_character_counts(get_character_counts(file_contents))
    
    print_report(file_path, word_count, character_counts)
    
if __name__ == '__main__':
    main(sys.argv)
