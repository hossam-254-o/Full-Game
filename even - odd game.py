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
        
        