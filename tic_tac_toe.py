
def player(s):
    count_o=0
    count_x=0
    for row in s:
        count_o+=row.count("O")
        count_x+=row.count("X")
    if count_o>count_x:
        return "X"
    if(count_o==count_x):
        return "O"
def result(s,a):
    copy_board=s.copy()
    i=a[0]
    j=a[1]
    player_turn=player(s)
    if (player_turn=="O"):
            copy_board[i][j]="O"
    if(player_turn=="X"):
        copy_board[i][j]="X"
    return  copy_board
def actions(s):
    action_list=[]
    for i in range (3):
        for j in range(3):
            if (s[i][j]==""):
                action_list.append([i,j])
    return action_list

def check_wins(board,player):
    #check for row 
    for row in board:
        if all(cell==player for cell in row ):
            return True
    
    #check for col
    for col in range(3):
        if all(board[row][col]==player for row in range(3)):
            return True
    
    #check for diagonal
  
    if all(board[col][col]==player for col in range (3)) or all(board[col][2-col]==player for col in range(3)):
        return True
    return False
def check_draw(board):
    if  not check_wins(board,"X") and  not check_wins(board,"O") and all([board[i][j]!= "" for i in range (3) for j in range(3)]):
        return True
    else:
        return False
def terminal(board):
    return check_wins(board,"X") or check_wins(board,"O") or check_draw(board)
     
def Utility(board):
    if(check_wins(board,"X")):
        return 1
    elif(check_wins(board,"O")):
        return -1
    else:
        #draw
        return 0
def Max_value(state):
    if terminal(state):
        return Utility(state),None
    best_move=float("-inf")
    best_action=None
    for action in actions(state):
        score, _ =Min_value(result(state,action))
        state[action[0]][action[1]]=""
        if(best_move<score):
            best_move=score
            best_action=action
    return best_move,best_action
def Min_value(state):
    if terminal(state):
        return Utility(state),None
    best_move=float("inf")
    best_action=None
    for action in actions(state):
        score, _ =Max_value(result(state,action))
        state[action[0]][action[1]]=""
        if(best_move>score):
            best_move=score
            best_action=action  
    return best_move,best_action
def Game_tic_tac():
    board=[["","",""] for i in range(3)]
    while(not terminal(board)):
        turn=player(board)
        print("TURN: ",turn)
        if(turn=="O"):
            action=list(map(int,input("Enter position: ").split()))
        if(turn=="X"):
            score,action=Max_value(board)
            
        board=result(board,action)
        for row in board :
            print(row)
        print("\n\n Next move:\n ")
    if(check_wins(board,"X")):
        print("\nTHE WINNER IS : X")
    if(check_wins(board,"O")):
        print("\n\n THE WINNER iS : O")
    if(check_draw(board)):
        print("\n\n MATCH IS DRAWN")
    
if __name__=="__main__":
    Game_tic_tac()


        
    







