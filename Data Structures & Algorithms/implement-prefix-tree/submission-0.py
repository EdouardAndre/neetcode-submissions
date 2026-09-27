class PrefixTree:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        def sub(word, i, root):
            if i >= len(word):
                root["#"] = True
                return
            if word[i] in root:
                return sub(word, i + 1, root[word[i]])
            else:
                root[word[i]] = {}
                return sub(word, i + 1, root[word[i]])
        return sub(word, 0, self.root)

    def search(self, word: str) -> bool:
        def sub(word, i, root):
            if i == len(word):
                if root.get("#"):
                    return True
                return False
            if word[i] in root:
                return sub(word, i + 1, root[word[i]])
            else:
                return False
        return sub(word, 0, self.root)        

    def startsWith(self, prefix: str) -> bool:
        def sub(word, i, root):
            if i == len(word):
                return True
            if word[i] not in root:
                return False
            else:
                return sub(word, i+1,root[word[i]] )
        return sub(prefix, 0, self.root)
        
        