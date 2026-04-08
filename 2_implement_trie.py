class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end

    def startsWith(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True

# Test Cases
trie = Trie()
trie.insert("apple")
print("Test 1:", trie.search("apple"))      # Expected: True
print("Test 2:", trie.search("app"))        # Expected: False
print("Test 3:", trie.startsWith("app"))    # Expected: True
trie.insert("app")
print("Test 4:", trie.search("app"))        # Expected: True
