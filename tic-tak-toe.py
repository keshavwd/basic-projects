ini_val = [1,2,3,4,5,6,7,8,9]
player = 'X'
win = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
while True:
    print("\n\t\t\t TIC-TAC-TOE")
    print(f"\n\t\t\t {ini_val[0]} | {ini_val[1]} | {ini_val[2]}")
    print("\t\t\t ---------")
    print(f"\t\t\t {ini_val[3]} | {ini_val[4]} | {ini_val[5]}")
    print("\t\t\t ---------")
    print(f"\t\t\t {ini_val[6]} | {ini_val[7]} | {ini_val[8]}")

    print(f"\n\t\t\tPlayer {player} turn : ", end="")
    turn = int(input())
    ini_val[turn-1] = player
    for a,b,c in win:
        if ini_val[a] == ini_val[b] and ini_val[b] == ini_val[a]:
            print(ini_val[a] == ini_val[b] and ini_val[b] == ini_val[a])
            print(f"Player {player} wins.")
    if player == 'X':
        player = 'O'
        #ini_val[turn] = 'X'
    else:
        player = 'X'
        #ini_val[turn] = 'O'
