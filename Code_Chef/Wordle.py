Test = int(input())

for _ in range(Test):
    S = input().strip() # Hidden word
    T = input().strip() #guess_word 
    M = "" # it is the sting fromed by hit and miss of guesses
    for i in range(5):
        if S[i] == T[i]:
            M += 'G'
        else:
            M += 'B'
            
    print(M)


