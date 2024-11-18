import sys

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
            

def main(path_to_file):
    file_contents = get_contents(path_to_file)

    word_count = get_word_count(file_contents)
    character_counts = format_character_counts(get_character_counts(file_contents))

    print(f"--- Begin report of {path_to_file} ---")
    print(f"{word_count} words found in the document\r\n")
    for char_dict in character_counts:
        print(f"The '{char_dict["char"]}' character was found {char_dict["char"]} times")
    print("--- End report ---")

if __name__ == '__main__':
    file_path = sys.argv[1]
    
    main(file_path)
