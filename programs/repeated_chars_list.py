# Given a string s consisting of small English letters, find and return the first instance of a non-repeating character in it. If there is no such character, return '_'.
# Using a list but with complexity O(i) as a dict
# reference "a" is the char 97 in ascci value. In a list posiction 0 = "a"


class list_char :
    def __init__(self, string: str) -> None:
        self.values = [0] * 26
        self.string = string
        self.fill_string()
        print(f"Mapping fo small letters {self.values}")

    def fill_string(self) -> None :        # fill the string with the number of letters in the word
        for item in self.string :
            self.values[ord(item)- 97] += 1

    def first_non_repeated(self) -> str  :          # returns the first element in the list that isn´t repeated
        for item in self.string :
            if self.values[ord(item) -97 ] == 1 :
                return item
        return "Every char is repeated"
    def is_char_in(self, char: str) -> bool :   # check if a char (parameter) is in the string using the list of values
        return self.values[ord(char)-97] > 0
    
    def is_missing(self)-> list[str]:
        result = []
        for i , val in enumerate(self.values):
            if val == 0:
                result.append(chr(97 + i))

        return result

    


a = list_char("aodemederhclquwxyfgrimoz")

print(f"First char non-repeated: {a.first_non_repeated()}")
print(f"All missing chars are: {a.is_missing()}")
char_to_search = "a"
print(f"Is '{char_to_search}' in the string: {a.is_char_in(char_to_search)}")