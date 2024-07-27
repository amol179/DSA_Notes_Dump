# if win gets 2 points for each game 60x of the prize money,
# if lose gets 0 point for each game and 40x of money.
# if Tied then previous winner gets 55x and challenger 45x

Test = int(input())

for _ in range(Test):
    X = int(input())
    R_String = input().strip()
    
    carlsen_wins = R_String.count('C')
    chef_wins = R_String.count('N')
    draws = R_String.count('D')
    
    carlsen_points = carlsen_wins * 2 + draws
    chef_points = chef_wins * 2 + draws
    
    if carlsen_points > chef_points:
        result = 60 * X
    elif carlsen_points == chef_points:
        result = 55 * X
    else:
        result = 40 * X
        
    print(result)
    
    
# ab variables kaafi readable dale hai