class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        for i in s:
            if i in d.keys():
                d[i]+=1
            else:
                d[i]=1
        s1=""
        dsort=sorted(d.items(), key=lambda x:x[1], reverse=True)
        for i in dsort:
            s1+=i[0]*i[1]
        return s1
       

            