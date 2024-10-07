import Trie

Trie1 = Trie.Trie()
arr = ["and", "ant", "do", "geek", "dad", "ball"]

for s in arr:
    Trie1.insert_key(s)

search_keys = ["do", "gee", "bat"]

for s in search_keys:
    is_present = Trie1.search_word(s)
    if is_present:
        print("present: " + s)
    else:
        print("NOT PRESENT " + s)







