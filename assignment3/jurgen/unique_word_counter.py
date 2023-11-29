def remove_punctuation(paragraph):
    punctuation = [".", ",", "?", "!", ":"]
    new_paragraph = ""
    for letter in paragraph:
        if letter not in punctuation:
            new_paragraph += letter.lower()
    
    return new_paragraph


def unique_words(paragraph):
    splited_paragraph = paragraph.split(" ")
    obj = {}
    for word in splited_paragraph:
        if obj.get(word) == None:
            obj[word] = 1
        
        else:
            obj[word] += 1

    return obj



def main():
    paragraph = input("Write a paragraph")
    print(unique_words(remove_punctuation(paragraph)))


main()

# The quick brown fox jumps over the lazy dog. The dog barks, and the fox runs away.