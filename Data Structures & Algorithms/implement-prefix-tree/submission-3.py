class PrefixTree:

    class CharNode:

        def __init__(self,val,nxt,end,initial = False):
            self.val = val
            self.end = end
            self.nxt = nxt
            self.initial = initial


    def __init__(self):
        self.nodes=[]
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for c in alphabet:
            newNode = self.CharNode(c,[],False,True)
            if c == 'a' or c =='i':
                newNode.end = True
            self.nodes.append(newNode)

    def insert(self, word: str) -> None:
        cur = self.nodes[ord(word[0].lower()) - ord('a')]
        cur.initial = False
        for i in range(1,len(word)):
            
            flag = True
            for n in cur.nxt:
                if n.val == word[i]:
                    cur = n
                    flag = False
                    break
            if flag:
                newNode = self.CharNode(word[i],[],False)
                cur.nxt.append(newNode)
                cur = newNode
            if i == len(word)-1:
                cur.end = True
        return None
            


    def search(self, word: str) -> bool:
        cur = self.nodes[ord(word[0].lower()) - ord('a')]
        indx = 1
        while cur and indx < len(word):
            found = False
            for n in cur.nxt:
                if n.val == word[indx]:
                    indx +=1
                    cur = n
                    found = True
                    break
            if not found:
                return False
        return cur.end
                

    def startsWith(self, prefix: str) -> bool:
        cur = self.nodes[ord(prefix[0].lower()) - ord('a')]
        indx = 1
        while cur and indx < len(prefix):
            found = False
            for n in cur.nxt:
                if n.val == prefix[indx]:
                    indx +=1
                    cur = n
                    found = True
                    break
            if not found:
                return False
        return not cur.initial
       
        