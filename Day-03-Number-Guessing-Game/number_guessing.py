#task 1 : genetate random number using randiint function btw 1 to 6
import random
num= random.randint(1,6)
'''
#using while loop
chance = 3
while(chance>0):
    #task 2: take a input from user 1 to 6
    user = int(input("Enter the number "))
    #task 3: if user = num-> won program ends {break}
    if(num== user):
         print(" you won!!!")
         break
         #step 4: if noy won but still chance remainining 
    elif(num!=user and chance>1):
        print(f"Try again,you have {chance-1} chance")
        #step 5: if no more chance remaining
    elif(chance==1):
        print("finalyyyy  you lose")
        #step 2,3,4,5 continue till no of chance{ while loop }
    chance= chance-1
      '''  
        
#using  for loop
for i in range(3,0,-1):
              user=int(input("Enter the number btween 1 to 6 ->"))
              if(num ==user):
                  print("You Won!!!!!!!!!")
                  break
              elif(num!= user and i >1):
                   print(f"Tru again {i-1} chance remaininggg")
              elif(i==1):
                   print("You LOST!!!!!")    
                  
                   
              
       
    