class Game:
    
    ## Counstructor for the main game
    def __init__(self):
        print("Welcome In The Full Game ...")
        print("Choose Your Game From Our Collection")
        print("Press [1] : Play Even - Odd Game")
        print("Press [2] : Play Sum Average Game")
        print("Press [3] : Play Multiplication Table Game")
        print("Press [X] : To Exit the game")
        
        self.choices()
        
    ## Avilable choices
    def choices (self):
        while True:
            user_choice = input("Enter Your Choice : ")
            
            if user_choice == 'x':
                print ('Closing The Game')
                print ("Thanks")
                break
            try: 
                user_choice = int (user_choice)
                if user_choice == 1:
                    self.Even_Odd_Game()
                elif user_choice == 2:
                    self.Sum_Average_Game()
                elif user_choice == 3:
                    self.Multiplication_Table_Game()
                else:
                    print ("please choose number from 1 , 2 , 3")   
            except ValueError:
                print ("please choose number from 1 , 2 , 3")
            
    ## Even Odd Game
    def Even_Odd_Game(self):
        print ("Welcome In The Event - Odd Game")
        print ("Please Enter A Number ... And I Will Tell You If It Even Or Odd")
        print ("If You Want To Exit Please Enter 'X' ")
        while True:    
            number = input("Enter A Number: ")
            
            if number == 'x':
                print ('Closing The Game')
                print ("Thanks")
                break
            
            try:
                number = int (number)
                if number % 2 == 0:
                    print ("Event Number")
                else:
                    print ("Odd Number")    
            except ValueError:
                print ("Plese Enter Vaalid number")
            print ("===============================")
        
    # Sum_Average_Game
    def Sum_Average_Game(self):
        print ("Welcome In The Average Sum Game")
        print ("This Game Will Take Several Numbers And Print The Average Of Them")
        count = int (input ("How Many Numbers Would You Like To Sum: "))
        current_count = 0
        total = 0
        while current_count < count:
            number = float (input ("Enter The Number:"))
            total += number
            current_count += 1            
        print (" Sum Of All Numbers =  " , total)
        print ("  Average Of All Numbers = " , total / count)
            
    # Multiplication_Table_Game
    def Multiplication_Table_Game(self):
        print ("Welcome In Multipliction Table Game.")
        print ("Please Enter The First And The Last Number Of The Multiplication Table.")
        
        start = int (input("Enter The First Number:"))
        print ("===============")
        end = int (input ("Enter The Second Number:"))
        print ("===============")
        
        for x in range(start,end + 1):
            for i in range (1,13):
                print (x , " X " , i , " = "  , x * i)
            print ("========================")
            
game1 = Game()

























