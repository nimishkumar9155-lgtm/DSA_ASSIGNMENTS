# Trie Node
class TrieNode:

    def __init__(self):

        self.children = {}

        self.end_of_word = False


# Trie Class
class Trie:

    def __init__(self):

        self.root = TrieNode()

    # Insert Word
    def insert(self, word):

        node = self.root

        for char in word:

            if char not in node.children:

                node.children[char] = TrieNode()

            node = node.children[char]

        node.end_of_word = True

    # Search Exact Word
    def search(self, word):

        node = self.root

        for char in word:

            if char not in node.children:
                return False

            node = node.children[char]

        return node.end_of_word

    # Prefix Search
    def startsWith(self, prefix):

        node = self.root

        for char in prefix:

            if char not in node.children:
                return False

            node = node.children[char]

        return True


# Main Program
trie = Trie()

# Insert Words
words = ["cat", "car", "cart", "dog", "doll"]

for word in words:
    trie.insert(word)

# Exact Search
print("Search 'cat':", trie.search("cat"))
print("Search 'cow':", trie.search("cow"))

# Prefix Search
print("StartsWith 'ca':", trie.startsWith("ca"))
print("StartsWith 'do':", trie.startsWith("do"))
print("StartsWith 'ap':", trie.startsWith("ap"))