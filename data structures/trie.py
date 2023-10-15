class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word
    
    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    
    def delete(self, word):
        def _delete_recursive(node, word, index):
            if index == len(word):
                if not node.is_end_of_word:
                    return False
                node.is_end_of_word = False
                return not bool(node.children)

            char = word[index]
            if char not in node.children:
                return False

            should_delete = _delete_recursive(node.children[char], word, index + 1)

            if should_delete:
                del node.children[char]
                return not bool(node.children)

            return False

        _delete_recursive(self.root, word, 0)
            


trie = Trie()
trie.insert("ca")
trie.insert("car")
trie.insert("carr")
trie.insert("apple")
trie.insert("cobra")

print(trie.search("ca"))
print(trie.search("car"))
print(trie.search("carr"))

print(trie.starts_with("ap"))
print(trie.starts_with("co"))

trie.delete("car")
print(trie.search("car"))
print(trie.search("carr"))

