b_list = [1,2,3,4,5,6,7,8,9]
player = 'X'
win = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
flag = 0
count = 0

while True:
    print("\nTIK TAC TOE")
    #playground grid
    print('\n-------------')
    print(f'  {b_list[0]} | {b_list[1]} | {b_list[2]}  ')
    print('-------------')
    print(f'  {b_list[3]} | {b_list[4]} | {b_list[5]}  ')
    print('-------------')
    print(f'  {b_list[6]} | {b_list[7]} | {b_list[8]}  ')
    print('-------------')
    print('\n')

    #exit game if player wins
    if flag == 1:
        break
    if count == 9:
        print("Match draw")
        break
    
    
         
    #player input
    print(f"Player {player} turn : ", end="")
    playerInput = int(input())

    if playerInput in b_list:        
        #grid player entry
        b_list[playerInput-1] = player
        #counter
        count = count+1

        for a,b,c in win:
            if b_list[a] == b_list[b] and b_list[b] == b_list[c]:
                print(f"Player {player} wins! Congratulations.")
                flag = 1;
        
        #player switch
        if player == 'X':
            player = 'O'
        else:
            player = 'X'
    else:
        print("Please enter the correct value.")
