Test = int(input())

for _ in range(Test):
    String =  str(input())
    Words = String.split()
    T_case = []
    
    for Word in Words:
        if Word.isupper():
            T_case.append(Word) 
        else:
            T_case.append(Word.capitalize())
            
    print(' '.join(T_case))
