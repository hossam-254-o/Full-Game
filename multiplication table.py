print ("Welcome In Multipliction Table APP.")
print ("Please Enter The First And The Last Number Of The Multiplication Table.")

start = int (input("Enter The First Number:"))
print ("===============")
end = int (input ("Enter The Second Number:"))
print ("===============")

for x in range(start,end + 1):
    for i in range (1,13):
        print (x , " X " , i , " = "  , x * i)
    print ("========================")