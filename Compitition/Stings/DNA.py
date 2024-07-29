#https://www.codechef.com/practice/course/strings/STRINGS/problems/DNASTORAGE

for _ in range(int(input())): #test cases searches
    N = int(input())  # Length of the string
    S = input()  # String
    
    for i in range(0, N, 2 ): # 2 is for the input of binary string
        if S[i] == "0" and S[i+1] == "0":
            print("A", end = "")
        if S[i] == "0" and S[i+1] == "1":
            print("T", end = "")
        if S[i] == "1" and S[i+1] == "0":
            print("C", end = "")
        if S[i] == "1" and S[i+1] == "1":
            print("G", end = "")
            
    print()
            