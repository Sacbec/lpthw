# para crear una funcion necesito 
# usar la palabra reservada def
# poner el nombre que tendra la funcion 
# abrir parentesis 
# colocar los parametros de los que dependera la funcion, separados por comas
# cerrar parentesis
# dos puntos 
def break_words(stuff):
    """ This fuction will break up  word for us.
    It creates a list, each element is from a blank space"""
    words = stuff.split(' ') 
    return words 

def sort_words(words):
    """Sorts the words."""
    return sorted(words) # return all the words but sorted

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0) # gets the word of that index, it needs a list
    print(word) 
    

def print_last_word(words):
    """Prints the last word after poppin it off."""
    word = words.pop(-1)
    print(word) 

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and the last one."""
    words  = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
