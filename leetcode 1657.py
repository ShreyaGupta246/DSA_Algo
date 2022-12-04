class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        d1={}
        d2={}
        word1=list(word1)
        word2=list(word2)
        word1.sort()
        word2.sort()
        if word1==word2:
            return True
        else:
            for i in word1:
                if i in d1.keys():
                    d1[i]+=1
                else:
                    d1[i]=1
            for i  in word2:
                if i in d2.keys():
                    d2[i]+=1
                else:
                    d2[i]=1
            l1=[]
            l2=[]
            l3=[]
            l4=[]
            for i in d1:
                l1.append(d1[i])
                l3.append(i)
            for i in d2:
                l2.append(d2[i])
                l4.append(i)
            l1=sorted(l1)
            l2=sorted(l2)
            l3=sorted(l3)
            l4=sorted(l4)
            if l1==l2 and l3==l4:
                return True
            return False
