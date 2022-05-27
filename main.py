# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here
    file = open(filename)
    content = file.read()
    return content


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    text_list = text.split(" ")
    text_dict = {}
    for x in text_list:
        if x in text_dict:
            text_dict[x] += 1
        else:
            text_dict[x] = 1
    print(text_dict)
    return text_dict


count_words()
