def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    #print(f"{num_words} words found in the document")
    chars_dict = get_chars_dict(text)
    #print(chars_dict)
    get_report(book_path, num_words, chars_dict)

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_report(path, num, chars_dict):
    print(f"--- Begin report of {path} ---")
    print(f"{num} words found in the document")
    for key, value in chars_dict.items():
        if key.isalpha():
            print(f"The '{key}' was found {value} times")
    print("--- End report ---")



main()
