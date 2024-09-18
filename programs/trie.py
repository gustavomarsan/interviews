# tries
# create a trie node class, add some words and check if other words are in the trie
#crea a function add a word y another function to check if the word exists


    
class TrieNode:
    def __init__(self, letter, ) -> None:
        self.letter = letter
        self.children = {}
        self.is_end_of_word = False


class Trie :
    def __init__(self) -> None:
        self.root = TrieNode("*")

    def add_word(self,word):
        curr_node = self.root
        for letter in word :
            if letter not in curr_node.children :
                curr_node.children[letter] = TrieNode(letter)
            curr_node = curr_node.children[letter]
        curr_node.is_end_of_word = True

    def does_word_exist(self, word) :
        if word == "" :
            return True
        curr_node = self.root
        for letter in word :
            if letter not in curr_node.children :
                return False
            curr_node = curr_node.children[letter]
        return curr_node.is_end_of_word


trie = Trie()
trie.add_word("wind")
trie.add_word("windy")
trie.add_word("winner")
trie.add_word("shopper")
trie.add_word("shop")
trie.add_word("shopping")
trie.add_word("shopper")
trie.add_word("baseball")
trie.add_word("base")
trie.add_word("work")
trie.add_word("workstation")
trie.add_word("local")
trie.add_word("location")
trie.add_word("tropic")
trie.add_word("tropical")
trie.add_word("tropicana")
print("wind ---", trie.does_word_exist("wind"))
print("windy ---", trie.does_word_exist("windy"))
print("shopper ---", trie.does_word_exist("shopper"))
print("super ---", trie.does_word_exist("super"))
print("tropical ---", trie.does_word_exist("tropical"))