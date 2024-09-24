# Given a string s consisting of small English letters, find and return the first instance of a non-repeating character in it. If there is no such character, return '_'.
# Using a list but with complexity O(i) as a dict
# reference "a" is the char 97 in ascci value. In a list posiction 0 = "a"


class list_char :
    def __init__(self, string: str) -> None:
        self.values = [0] * 26
        self.string = string
        self.fill_string()

    def fill_string(self) -> None :        # fill the string with the number of letters in the word
        for item in self.string :
            self.values[ord(item)- 97] += 1

    def first_non_dup(self) -> str  :          # returns the first element in the list that isn´t repeated
        for item in self.string :
            if self.values[ord(item) -97 ] == 1 :
                return item
        return "Every char is repeated"
    def is_char_in(self, char: str) -> bool :   # check if a chear (parameter) is in the string using the list of values
        return self.values[ord(char)-97] > 0
    


a = list_char("odemederrimo")

print(a.values)

print("First char repeated:", a.first_non_dup())
print(a.is_char_in("h"))