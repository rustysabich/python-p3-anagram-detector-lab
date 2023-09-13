# your code goes here!

class Anagram:
    
    def __init__(self, word):
        self.word = word
        
    def match(self, word_list):
        # define an empty list to store the anagrams
        anagrams = []
        
        # get the letters in the original word
        orig_word_letters = [letter for letter in self.word]
        
        # loop over the words in the list
        for my_word in word_list:
            # get a list of the letters in the word
            letters = [letter for letter in my_word]
            
            # check if the sorted version of the letters matches the initial word
            if sorted(letters) == sorted(orig_word_letters):
                anagrams.append(my_word)
                
        # return the anagrams
        return anagrams
        