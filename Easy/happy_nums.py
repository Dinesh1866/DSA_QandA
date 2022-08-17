#Happy Numbers
class Solution:
    def isHappy(self, n: int) -> bool:
        def happy(n):
            if (len(str(n))==1):
                return n
            while(len(str(n))!=1):
                m=str(n)
                #print(len(m))
                sum=0
                for i in m:
                    sum+=(int(i)*int(i))
                    #print(sum)
                n=sum

            return n

        a=happy(n)
        if a==1 or a==7:
            return True
        else:
            return False