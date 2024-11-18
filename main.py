def get_contents(file_path):
    with open(file_path) as f:
        return f.read()
    

def print_contents(file_contents):
   print(file_contents)

def print_word_count(file_contents):
    words = file_contents.split()
    print(len(words))

def print_character_counts(file_contents):
    lowered_contents = file_contents.lower()
    char_counts = {}
    for char in lowered_contents:
        if char_counts.get(char) is None:
            char_counts[char] = 1
        else:
            char_counts[char] += 1

    print(char_counts)
            

def main(path_to_file):
    file_contents = get_contents(path_to_file)
    #print_contents(file_contents)
    #print_word_count(file_contents)
    print_character_counts(file_contents)

if __name__ == '__main__':
    main("books/frankenstein.txt")
