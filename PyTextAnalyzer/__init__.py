import statistics as st
import math


def isascii(text):

    special_list = list(Analyzer.special_characters)
    if text in special_list:
        return True
    else:
        return False
        pass

class Analyzer:

    #useful variables
    characters_lower = "abcdefghijklmnopqrstuvwxyz"
    characters_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number_string = 1234567890
    special_characters = "!£$%^&*()_+=-`¬{}[]#~?/>.<,:;@'"
    mixed_string = characters_lower + characters_upper + str(number_string) + special_characters


    analyzer_count = 0
    def __init__(self):
        Analyzer.analyzer_count = self.analyzer_count + 1



    #whole analysing of the text
    def analyze(self, text, includeSpaces=True):
        #number of characters
        if includeSpaces:
            no_of_characters = self.characters(text)
        else:
            no_of_characters = int(self.characters(text)) - self.spaces(text)

        #number of words
        no_of_words = self.words(text)

        #number of spaces 
        no_of_spaces = self.spaces(text)

        #numbers in text
        no_of_numbers = self.numbers(text)

        #number of special characters
        no_of_specials = self.specials(text)

        #number of capital letters
        no_of_capitals = self.caps(text)

        #number of lower letters
        no_of_lowers = self.lows(text)

        #frequency of the words
        no_of_frequent_words =self.frequency(text)

        #number of paragraphs
        no_of_paras = self.paragraphs(text)

        #average word length
        average_word_length = self.averageLength(text)

        #dictionary with main data
        analyzed_dict = {'characters':no_of_characters, 'words':no_of_words, 'spaces':no_of_spaces, 'numbers':no_of_numbers, 'specials':no_of_specials, 'capital_letters':no_of_capitals, 'lower_letters':no_of_lowers, 'frequency_of_words':no_of_frequent_words, 'paragraphs':no_of_paras, 'average_word_length':average_word_length}


        return analyzed_dict

    #total no. of words in the text
    def characters(self, text : str, includeSpaces=True):
        #creating the list of the letters present in the text
        list_of_letters = list(text)

        #returning the length of the list
        return len(list_of_letters)

    def words(self, text : str):
        #list of all words in text
        list_of_words = text.split()

        #returning len of list
        return len(list_of_words)

    def spaces(self, text):
        #list of all characters
        list_of_chars = list(text)

        #list comprehension for collecting all spaces in the text
        spaces_list = [space for space in list_of_chars if space == " "]

        #returning the length of the spaces_list
        return len(spaces_list)

    def numbers(self, text : str):
        #list of all characters
        list_of_chars = list(text)

        #number list
        number_list = [nums for nums in list_of_chars if nums.isnumeric()]

        #returning the length of number list
        return len(number_list)

    def specials(self, text : str):
        #number of spacial characters
        special_length = [spec for spec in text if isascii(spec)
        ]

        return len(special_length)

    #function for getting the number of occurences for a word
    def occurences(self, searchStr, text, isLetter = False):

        #number of occurences found
        words_found = 0

        #check if the input is just a letter or a word
        if isLetter:
            word_list = list(searchStr)
        else:
            word_list = searchStr.split()

        #check for the occcurences
        for word in word_list:
            if word == text:
                words_found+=1

            else:
                pass

        return words_found


    #returns the number of capital letters
    def caps(self, text : str):
        
        #seperating the letters
        all_letters = list(text)

        #number of capital letters
        capital_list = [cap for cap in all_letters if cap.isupper()]

        return len(capital_list)

    #returns the number of lower letters
    def lows(self, text : str):
        
        #seperating the letters
        all_letters = list(text)

        #number of lower letters
        lower_list = [low for low in all_letters if low.islower()]

        return len(lower_list)

    #to check the frequency(times they occur) of all the words in the text
    def frequency(self, text : str):
    
        #splittiing the whole text for all the words
        splitted_words = text.split()

        #empty list for keeping the unique qords(words should exist only once even if there are more occurences)
        unique_list = []

        #empty dict for appending all the words as 'keys' and their occurences as 'value'
        data_dict = {}

        #for loop for appending 'unique_list' for unique words
        for words in splitted_words:
    
            if words not in unique_list:
                unique_list.append(words)

        #addind the 'keys' and 'value' in the data_dict as per the length of the 'unique_list'
        for i in range(0, len(unique_list)):
            data_dict[unique_list[i]] = splitted_words.count(unique_list[i])

        return data_dict

    #function for getting paragraphs
    def paragraphs(self, text : str):
        return len(text.splitlines())


    #average word length
    def averageLength(self, text : str):

        #list of words
        list_of_chars = self.characters(text)
        list_of_words = self.words(text)

        return math.trunc(list_of_chars / list_of_words)



analyzer = Analyzer()

s = "1)This is the string for the testing.\nand i am abhay"
inp = input('Enter text : ')

print(analyzer.analyze(s))


