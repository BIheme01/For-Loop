"""
MY PSEUDOCODE:

START

1. Create a variable that counts the number of iterations
2. Create another variable "reverse_iteration" to reverse the number of stars per row
3. Create a loop that runs 10 times
4. For the first 5 iterations multiply '*' by the number of iterations

5. Once the iteration is >5, for the remaining iterations use the "reverse_iteration" variable.
6. Subract 1 from the "reverse_iteration" variable after each iteration
7. Multiply the "reverse_iteration" variable by "*" after each iteration.

END

""" 


# EXAMPLE 1 - USING 1 FOR LOOP (AS REQUESTED BY TASK)

iteration = 0           # This variable is used to count the number of iterations. 
reverse_iteration = 5   # Once the number of iterations is >5, this variable will display the *'s in descending order (from 4 to 1). 
 
for iteration in range (10): # Run the loop 10 times
    if iteration <= 5:
        print(iteration * "*")  # For the first 5 iterations the row length will increase in size (from 1 star to 5 stars) 
   
    else: 
       iteration > 5   #This statement kicks in when the iteration is greater than 5
       reverse_iteration -= 1  # Use this variable to reduce the row length by 1 each iteration (from 4 stars to 1 star) 
       print("*" * reverse_iteration)  
       

"""    
EXAMPLE 2 - USING 2 FOR LOOPS TO PRODUCE THE SAME RESULT (FOR MY INTEREST)

for i in range(1,6):
    print("*" * i)
    
if i == 5:
    for i in range(4, 0, -1):
        print('*' * i)
  

"""
      

 
  
   

