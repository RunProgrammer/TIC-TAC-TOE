#PROJECT NAME : TIC TAC TOE
#CREATED BY : TARUN.N
#GITHUB NAME : RunProgrammer
#DATE OF CREATED : 9/4/2021
print("-----------")
print("TIC TAC TOE")
print("-----------")

#CREATING BOARD
board = {"1": " ","2": " ","3": " ",
         "4": " ","5": " ","6": " ",
         "7": " ","8": " ","9": " "}

#FUNCTION FOR PRINTING BOARD
def print_board(board):

    print(board["1"] + "|" + board["2"] + "|" + board["3"] )
    print("-+-+-")
    print(board["4"] + "|" + board["5"] + "|" + board["6"] )
    print("-+-+-")
    print(board["7"] + "|" + board["8"] + "|" + board["9"] )


#MAIN FUNCTION THAT HANDLES ALL IF,ELIF,ELSE AND LOOPS...TO VALIDATE
#MAIN FUNCTION EVEN GET'S INPUT FROM THE USER...
def main():

    turn_Of = "X"
    count_of = 0
    for i in range(10):
        print_board(board)
        print("It's your turn, " + turn_Of + ".Which place are you going         to move: ")
        move_of_user = input("Move: ")

        if board[move_of_user] == " ":
            board[move_of_user] = turn_Of
            count_of += 1
        else:
            print("This place is already filled by our opponent...")
            continue

        if count_of >= 5:
            #VALIDATING
            if board["1"] == board["2"] == board["3"] != " ":
                print_board(board)
                print("----" + turn_Of + "Won the match... " + "----")
                print("**** GAME OVER ****")
                break
            elif board["4"] == board["5"] == board["6"] != " ":
                print_board(board)        
                print("----" + turn_Of + "Won the match... " + "----")
                print("**** GAME OVER ****")
                break
            elif board["7"] == board["8"] == board["9"] != " ":
                print_board(board)
                print("----" + turn_Of + "Won the match... " + "----")
                print("**** GAME OVER ****")
                break
            elif board["1"] == board["4"] == board["7"] != " ":
                print_board(board)
                print("----" + turn_Of + "Won the match... " + "----")
                print("**** GAME OVER ****")
                break
            elif board["2"] == board["5"] == board["8"] != " ":
                print_board(board)
                print("----" + turn_Of + "Won the match... " + "----")
                print("**** GAME OVER ****")
                break
            elif board["3"] == board["6"] == board["9"] != " ":
                print_board(board)
                print("----" + turn_Of + "Won the match... " + "----")
                print("**** GAME OVER ****")
                break
            elif board["1"] == board["5"] == board["9"] != " ":
                print_board(board)
                print("----" + turn_Of + "Won the match... " + "----")
                print("**** GAME OVER ****")
                break
            elif board["3"] == board["5"] == board["7"] != " ":
                print_board(board)
                print("----" + turn_Of + "Won the match... " + "----")
                print("**** GAME OVER ****")
                break

        #TO VALIDATE IF THE MATCH IS TIE OR NOT        
        if count_of == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")
            break
        
        #TO RETURN THE TURN
        if turn_Of == "X":
            turn_Of = "O"
        else:
            turn_Of = "X"

main()
