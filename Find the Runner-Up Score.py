#python3
#Find the Runner-Up Score
#https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split(" ")))
    #print (arr)
    
    arr = set(list(arr))
    #print (arr)
    max_number = max(arr)
    arr.remove(max_number)

    print(max(arr))
