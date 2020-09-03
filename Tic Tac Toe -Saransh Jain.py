import random
global list1,list2,result
#Display the game
def display(list1):
    temp=0
    print("\t\t",list1[0],"\t||\t",list1[1],"\t||\t",list1[2])
    print("\t\t--------------------------------------")
    print("\t\t",list1[3],"\t||\t",list1[4],"\t||\t",list1[5])
    print("\t\t--------------------------------------")
    print("\t\t",list1[6],"\t||\t",list1[7],"\t||\t",list1[8],"\n")
#Check whether the game has been won by anyone
def check(list1):
    if ((list1[0]==list1[1] and list1[0]==list1[2]) or (list1[0]==list1[3] and list1[0]==list1[6])
        or (list1[0]==list1[4] and list1[0]==list1[8]) or (list1[8]==list1[7] and list1[8]==list1[6])
        or (list1[8]==list1[5] and list1[8]==list1[2]) or (list1[3] == list1[4] and list1[3]==list1[5])
        or (list1[1]==list1[4] and list1[1]==list1[7]) or (list1[2]==list1[4] and list1[2]==list1[6]) ):
        return 1
    else:
        return 0
#after choosing singleplayer
def players(player):
    if player==0:
        print("You win")
    else:
        print("1 st player Win")
#main function
def game(decision,opposition,player):
    list1=[1,2,3,4,5,6,7,8,9]
    list2=[1,2,3,4,5,6,7,8,9]
    result=0
    #display(list1)
    while result==0:
        try:
            user=int(input("1st Player  : - "))#1st person chance to play
        except:
            print("Only Numeric Values are allowed - 1 chance left")
            try:    user=int(input("1st Player   : - "))
            except:
                print("You have exhausted your all chances\n\n")
                break
        while (user not in list1):
            user=int(input("Write the valid command:-    "))
        list1=[decision if x==list1[int(user)+-1] else x for x in list1]
        list2.remove(user)
        result=check(list1)
        if result==1:
            display(list1)
            players(player)
            break
        elif len(list2)==0:
            if result==1:
                display(list1)
                players(player)
                break
            else:
                display(list1)
                print("Draw")
                break
        if player==1:
            display(list1)
            try:
                comp=int(input("2nd Player:-    "))#2nd person chance to play
            except:
                print("Only Numeric Values are allowed - 1 chance left")
                comp=int(input("2nd Player:-    "))#Second person's chance to play
                try:    comp=int(input("2nd Player   : - "))
                except:
                    print("You have exhausted your all chances\n\n")
                    break
                while (comp not in list2):
                    print("Invalid")
                    comp=int(input("Write the valid command:-   "))
        else:
            comp=random.choice(list2)
        list1=[opposition if x==list1[comp+-1] else x for x in list1]
        list2.remove(comp)
        display(list1)
        result=check(list1)
        if result==1:
            if player==0:
                print("Computer Wins the Game")
            else:
                print("Congo 2nd Player Win")
def main():
    list1=[1,2,3,4,5,6,7,8,9]
    repeat=0
    while repeat==0:
        player=int(input("Choose 0 for Single Player\t\t\tChoose 1 for Multiplayer\n -  "))
        decision=str(input("Choose your lucky sign between X or O for first player : - "))
        if decision=='X':   #1st player
            opposition='O'     #2nd player
            display(list1)
            game(decision,opposition,player)
                    #display(list1)
        else:
            opposition='X'
            display(list1)
            game(decision,opposition,player)
        repeat=int(input("Choose 0 to play again\t\t\tChosse 1 to exit\n - "))
    if repeat!=0:
        print("Closing......")

if __name__ == '__main__':
    main()
