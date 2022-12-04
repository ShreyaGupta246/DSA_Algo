class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        c1=0
        c2=0
        for i in range(len(s)):
            s1=s[0:len(s)//2]
            s2=s[len(s)//2:]
            #print(s1)
            #print(s2)
            vowel=['a','e','i','o','u','A','E','I','O','U']
            for i in s1:
                if i in vowel:
                    c1+=1
            for i in s2:
                if i in vowel:
                    c2+=1
            if c1==c2:
                return True
            else:
                return False