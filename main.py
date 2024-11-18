def print_contents(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        print(file_contents)

def print_word_count(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        words = file_contents.split()
        print(len(words))

def main(path_to_file):
    #print_contents(path_to_file)
    print_word_count(path_to_file)

main("books/frankenstein.txt")
