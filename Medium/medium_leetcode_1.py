'''1561. Maximum Number of Coins You Can Get'''

#normal lap code trial
def my_choice(arr,arr_choices,length_of_array):
      arr.sort()
      my_array = []
      for i in range(arr_choices,length_of_array,2):
            #Ele = arr[i]
            my_array.append(arr[i])
      print(my_array)
      #print(sum(my_array))

class main():
      arr = list(map(int,input().split()))
      #newarr = arr.split("[]")
      print(type(arr))
      print(arr)
      #arr_choices = len(arr)//3
      #my_choice(arr,arr_choices,len(arr))


if __name__ =="__main__":
      main()


#LeetCode Ans
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        counter, ans, times = 0, 0, len(piles)//3 
        piles.sort(reverse = True)
        for i in range(1,len(piles),2) : 
            ans += piles[i]
            counter += 1 
            if counter == times :
                break
        return ans 


#Even more sorted
def maxCoins(piles):
    piles.sort()
    n = len(piles) // 3
    sum = piles[n]
    for i in range(n+2, len(piles), 2):
        sum += piles[i]
    return sum