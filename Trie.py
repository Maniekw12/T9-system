class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_end: bool = False

class Trie:

    def __init__(self):
        self.root = TrieNode()


    def insert_key(self,word:str) -> None:
        curr = self.root

        for char in word:
            if char not in curr.children:
                new_node = TrieNode()
                curr.children[char] = new_node
            curr = curr.children[char]

        curr.word_end = True


    def search(self,node:TrieNode,prefix,result:list):
        if node.word_end:
            result.append(prefix)

        ##To nie wiem czy jest w ogole potrzebne bo znajduje
        #nam cala reszte wyrazow - za duzo liter w sumie
        for char, char_node in node.children:
            self.search(char_node,prefix + char,result)

    def starts_with(self,prefix):
        curr = self.root
        for char in prefix:

            if char not in curr.children:
                return []
            curr = curr.children[char]



        result = []
        self.search_word(curr,prefix,result)
        return result




