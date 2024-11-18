def print_contents(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        print(file_contents)

def print_word_count(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        words = file_contents.split()
        print(len(words))

def print_character_counts(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        lowered_contents = file_contents.lower()
        char_counts = {}
        for char in lowered_contents:
            if char_counts.get(char) is None:
                char_counts[char] = 1
            else:
                char_counts[char] += 1

        print(char_counts)
            

def main(path_to_file):
    #print_contents(path_to_file)
    #print_word_count(path_to_file)
    print_character_counts(path_to_file)

main("books/frankenstein.txt")
