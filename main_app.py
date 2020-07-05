from Character import characters_board
board = characters_board

def draw_pixel(message):
    try:
        for j in range(5):
            for char in list(message):
                for i in range(3):
                    if board[char][j][i] == 1:
                        print('(*)',end='')
                    else:
                        print('   ',end='')
                print('  ',end='')
            print()
    except:
        print('TYPE MESSAGE ONLY IN UPPER CASE ')

print("********| YOUR ARE NOW ONLINE  |***************")
while True:
    print("TYPE MESSAGE (UPPER-CASE/SPACE) PRESS 'DONE' TO EXIT ")
    message = input()
    if message == 'DONE' :
        print("********| YOUR ARE NOW OFFLINE  |***************")
        exit()
    draw_pixel(message)
