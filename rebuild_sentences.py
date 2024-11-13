""" Rebuild Sentences project

Used to rebuild the word by length number
"""

def rebuild_sentence(words, lengths):
    """
    :param words: a list of string that will be stored
    :param lengths: a list of integer to change the word sentence
    :return: rebuilding the list words by the value of list lengths
    """
    if not words:
        return "Enter any words in your mind"

    new_word = []
    for i in range(len(words)):
        text = words[i][:lengths[i]]   # word[0][:lengths[0]] and it will separate each word
        new_word.append(text)
    return ' '.join(new_word)   # it will remove the double quotation and add spaces

Words = ['jad','haj','ali']
Lengths = [2,2,1]
print("The result to your new Word : "+rebuild_sentence(Words,Lengths))
