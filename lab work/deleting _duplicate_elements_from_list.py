'''----------------------------------------delete elements from the list---------------------------------'''
#creating a blank list
#creating blank list
numbers = []
print("Enter only 10 numbers : ")
for x in range(10):
    #input of elements from user
    num = int(input())
    #inserting data at the end of list
    numbers.append(num)
#--------------------------------------------------------------------------------------------------------
#dislay the original list to the user
print("List of numbers are : ",numbers)
#to delete last element from the list

#last = print("The last element deleted from the list : ",numbers.pop())
#input of index number by user to delete the element

index_to_delete = input("Enter the index from which uh want to delete the element or press enter to delete last element : ")

if index_to_delete =="":
    print("The last element deleted from the list : ",numbers.pop())
    
else :
    delete == int(index_to_delete)

    if index_to_delete<len(numbers) and index_to_delete >= (-len(numbers)):
        print("The element deleted from the list : ",numbers.pop(index_to_deletedelete))
    else:
        print("Enter a valid index")
print("List after deletion : ",numbers)