class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        root = self.root
        for char in word:
            search_dict = root.children
            if char not in search_dict: 
                search_dict[char] = TrieNode()
            root.children = search_dict
            root = root.children[char]
        root.isWord = True
        
class Solution: 
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(node, row, col, path):
            if self.num_words == 0:
                return 
            #accumulate the found words and update the number of words to be searched
            if node.isWord:
                result.append(path)
                node.isWord = False
                self.num_words -= 1

            #check boundry conditions
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]): 
                return 
            char = board[row][col]
            if char not in node.children: 
                return
            #mark visited for backtracking
            board[row][col] = "#"
            #recursively check all the 4 sides of a char to trace the existence of the word
            dfs(node.children[char], row, col-1, path+char)
            dfs(node.children[char], row, col+1, path+char)
            dfs(node.children[char], row+1, col, path+char)
            dfs(node.children[char], row-1, col, path+char)

            board[row][col] = char
            
        self.num_words = len(words)    
        result, trie = [], Trie()
        for word in words:
            trie.insert(word) 

        for row in range(len(board)):
            for col in range(len(board[0])):
                #run dfs on every work to search in the trie 
                dfs(trie.root, row, col, "")
        return result
    
    
