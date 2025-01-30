################################## Pattern matching program. ########################################

# n = int(input("Enter the number: "))
# for i in range(0,n):
#     print('*',end=" ")

# * * * * *

    
 
# n = int(input("Enter the number: "))
# for i in range(0,n):
#     print('*')    

# *
# *
# *
# *
# *

    
# n = int(input("Enter the number: "))
# for i in range(n):
#     print("*"*n)  
  
# *****
# *****
# *****
# *****
# *****


# n = int(input("Enter the number: "))
# for i in range(1, n + 1):
#     for j in range(1,n+1):
#         print(i,end=" ")
#     print()    

# 1 1 1 1 1
# 2 2 2 2 2
# 3 3 3 3 3
# 4 4 4 4 4
# 5 5 5 5 5
 
   
# n = int(input("Enter the number: "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(j,end=' ')
#     print()     
   
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5

# n = int(input("Enter the number: "))
# for i in range(n,0,-1):
#     for j in range(1,n+1):
#         print(i,end=" ")
#     print()   

# 5 5 5 5 5 
# 4 4 4 4 4 
# 3 3 3 3 3 
# 2 2 2 2 2 
# 1 1 1 1 1 

# n = int(input("Enter the number: "))
# for i in range(1,n+1):     
#     for j in range(1,n+1):
#         print(i,end=" ")
#     print()
   
# 1 1 1 1 1 
# 2 2 2 2 2 
# 3 3 3 3 3 
# 4 4 4 4 4 
# 5 5 5 5 5      

# n = int(input("Enter the number: "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print((n-j+1),end=" ")
#     print()    

# 5 4 3 2 1 
# 5 4 3 2 1 
# 5 4 3 2 1 
# 5 4 3 2 1 
# 5 4 3 2 1 

# n = int(input("Enter the number: "))
# k = 1
# for i in range(n):
#     for j in range(n):
#         print(k, end=" ")
#         k = k + 1
#     print()    

# 1 2 3 4 5 
# 6 7 8 9 10 
# 11 12 13 14 15 
# 16 17 18 19 20 
# 21 22 23 24 25       

# n = int(input("Enter the number: "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(i%2,end=" ")
#     print()    

# 1 1 1 1 1 
# 0 0 0 0 0 
# 1 1 1 1 1 
# 0 0 0 0 0 
# 1 1 1 1 1 

# n = int(input("Enter the number: "))
# for i in range(n):
#     for j in range(1,n+1):    
#         print(i%2,end=" ")
#     print()   

# 0 0 0 0 0 
# 1 1 1 1 1 
# 0 0 0 0 0 
# 1 1 1 1 1 
# 0 0 0 0 0     

# n = int(input("Enter the number: "))
# for i in range(1,n+1):
#     for j in range(n):
#         print(j%2,end=" ")
#     print()   
 
# 0 1 0 1 0 
# 0 1 0 1 0 
# 0 1 0 1 0 
# 0 1 0 1 0 
# 0 1 0 1 0      

# n = int(input("Enter the number: "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(j%2,end=" ")
#     print()    

# 1 0 1 0 1 
# 1 0 1 0 1 
# 1 0 1 0 1 
# 1 0 1 0 1 
# 1 0 1 0 1 

# n = int(input("Enter the number: "))
# k = 1
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(k%2,end=" ")
#         k = k+1
#     print()   
 
# 1 0 1 0 1 
# 0 1 0 1 0 
# 1 0 1 0 1 
# 0 1 0 1 0 
# 1 0 1 0 1     

############# ASCII stands for (American Standard Code for Information Interchange) ############################
                        # A-Z = 65-90
                        # a-z = 97-122
                        # 0-9 = 48-57
                        # space = 32
                        
                        
                        
# n = int(input("Enter the number: "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(chr(i+64),end=" ")
#     print()

# A A A A A 
# B B B B B 
# C C C C C 
# D D D D D 
# E E E E E  

# n = int(input("Enter the number: "))
# for i in range(n,0,-1):
#     for j in range(1,n+1):
#         print(chr(i+64),end=" ")  
#     print()     

# E E E E E 
# D D D D D 
# C C C C C 
# B B B B B 
# A A A A A       

# n = int(input("Enter the number: "))
# for i in range(1,n+1):
#     for j in range(n,0,-1):
#         print(chr(j+64),end=" ")  
#     print()    

# E D C B A 
# E D C B A 
# E D C B A 
# E D C B A 
# E D C B A     
    
# n = int(input("Enter the number: "))
# k = 1
# for i in range(n):
#     for j in range(n):
#         print(chr(k+64), end=" ")
#         k = k + 1
#     print() 
 
# A B C D E 
# F G H I J 
# K L M N O 
# P Q R S T 
# U V W X Y     

# n = int(input("Enter the number: "))
# k = 1
# for i in range(n):
#     for j in range(n):
#         print(chr((k-1) % 26 + 65), end=" ")
#         k = k + 1
#     print()

# A B C D E F G 
# H I J K L M N 
# O P Q R S T U 
# V W X Y Z A B 
# C D E F G H I 
# J K L M N O P 
# Q R S T U V W     

# n = int(input("Enter the number: "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i%2==0:
#             print(chr(i+96),end=" ")
#         else:
#             print(chr(i+64),end=" ")
#     print()   
         
# A A A A A 
# b b b b b 
# C C C C C 
# d d d d d 
# E E E E E 

# n = int(input("Enter the number: "))
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if j % 2 == 0:
#             print(chr(j + 96), end=" ")
#         else:
#             print(chr(j + 64), end=" ")
#     print()

# A b C d E 
# A b C d E 
# A b C d E 
# A b C d E 
# A b C d E 

############################### Right angle traingle #######################################
############################## Up right angle traingle #####################################


# n = int(input("Enter the number : "))
# for i in range(1,n+1):
#     for j in range(i,0,-1):
#         print('*',end=" ")
#     print()    
# * 
# * * 
# * * * 
# * * * * 
# * * * * *     

# n = int(input("Enter the number: "))
# for i in range(n,0,-1):
#     for j in range(n,i-1,-1):
#         print(j,end=" ")
#     print() 
# 5 
# 5 4 
# 5 4 3 
# 5 4 3 2 
# 5 4 3 2 1        

# n = int(input("Enter the number: "))
# for i in range(1,n+1):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()    
# 1 
# 2 1 
# 3 2 1 
# 4 3 2 1 
# 5 4 3 2 1    

# n = int(input("Enter the number: "))
# for i in range(1,n+1):
#     for j in range(i,0,-1):
#         print((i%2),end=" ")
#     print()    
# 1 
# 0 0 
# 1 1 1 
# 0 0 0 0 
# 1 1 1 1 1     