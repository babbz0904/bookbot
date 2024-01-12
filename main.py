def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letter_count = count_letters(text)
    letter_sorted_list = sort_letters(letter_count)

    print(f"---Begin report of {book_path}---")
    print(f"{num_words} words found in the document\n")
    print(f"---Begin report of {book_path}")
    print(f"{num_words} words found in the document")
   
    for item in letter_sorted_list:
        print(f"The '{item[0]}' character was found {item[1]} times")
    



def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_letters(text):
    words = text.split()
    letter_count = {}
    
    for word in words:
        word = word.lower()

        for letter in word:
            if letter.isalpha():
                if letter in letter_count:
                    letter_count[letter] += 1
                else:
                    letter_count[letter] = 1


    

    return letter_count

def sort_letters(letter_count):
    return sorted(letter_count.items(), key=lambda x: x[1], reverse=True)  



        




main()