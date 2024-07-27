no_students = 76
practicals = 8
a = 73

b = a - 1
assigned_prac = []

for roll in range(1 , no_students +1 ):
    for  pracs in range(1, practicals +1):
        assigned_prac.append(pracs)
        
print(assigned_prac[b]) #roll no -1 == index