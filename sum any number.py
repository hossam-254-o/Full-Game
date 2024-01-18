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

