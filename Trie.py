class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_end: bool = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    #dodawanie nowego slowa do struktury
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

        ##Tu bedzie znajdowac wszystkie wyzsze wyrazy z danym prefiksem
        #for char, char_node in node.children.items():
        #    self.search(char_node,prefix + char,result)


    def starts_with(self,prefix):
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return []
            curr = curr.children[char]

        result = []
        self.search(curr,prefix,result)
        return result




