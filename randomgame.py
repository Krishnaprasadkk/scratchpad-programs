import random
LIMIT=10
def random_game():
    num=random.randint(1,LIMIT)
    count=0
    trial='y'
    while(trial.lower()=='y'):
        guess_num=int(input("enter the number "))
        if(guess_num==num):
            print("you have found the number in "+str(count)+"  attempts\n")
        else:
            print("your guess is wrong")
            count+=1
        trial = input ("press Y if you want another chance\n")

def main():
    print("welcome to the guessing game")
    random_game()



if __name__=="__main__":
    main()