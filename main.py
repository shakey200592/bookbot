def get_book_text(path_to_book):
    try:
        with open(path_to_book) as book:
            return book.read()
            
    except FileNotFoundError as file_not_found:
        print(f"ERROR!: File path {path_to_book} does not exist")
        
def count_each_word(book_text):
    book_text = book_text.split(" ")
    return len(book_text)

def to_lower_case(book_text):
    return book_text.lower()



def count_each_character(book_text):
    character_count_dict = {}
    book_text = book_text.replace(" ","")
    book_text = book_text.replace("\n","")
    
    for character in book_text:
        if character in character_count_dict:
            character_count_dict[character] += 1
        else:
            character_count_dict[character] = 1
            
    return character_count_dict

def convert_dictionary_to_list_of_dictionaries(dict_to_convert):
    list_of_dict = []
    
    for char, count in dict_to_convert.items():
        if char.isalpha():
            list_of_dict.append({"char": char, "num": count})

    return list_of_dict


    
def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    book_text_lower = to_lower_case(book_text)
    book_word_Count = count_each_word(book_text)
    book_character_count = count_each_character(book_text_lower)
    print(convert_dictionary_to_list_of_dictionaries(book_character_count))
    
    
    
    
main()