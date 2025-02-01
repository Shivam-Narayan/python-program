'''################################## Pattern matching program. ########################################
   #####################################################################################################'''
'---------------------------------------------------------'

# n = int(input("Enter the number: "))
# for i in range(0,n):
#     print('*',end=" ")

# * * * * *

'---------------------------------------------------------'  
# n = int(input("Enter the number: "))
# for i in range(0,n):
#     print('*')    

# *
# *
# *
# *
# *
'---------------------------------------------------------'
    
# n = int(input("Enter the number: "))
# for i in range(n):
#     print("*"*n)  
  
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

'----------------------------------------------------------'

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
 
'-------------------------------------------------------------'   
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

'--------------------------------------------------------------'

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

'---------------------------------------------------------------'

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

'-----------------------------------------------------------------'

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

'-------------------------------------------------------------------'

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

'---------------------------------------------------------------------'

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

'----------------------------------------------------------------------'

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

'----------------------------------------------------------------------'

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

'------------------------------------------------------------------------'

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

'--------------------------------------------------------------------------'

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
'---------------------------------------------------------------------------------------------------------------'

'############# ASCII stands for (American Standard Code for Information Interchange) ###########'
                        # A-Z = 65-90
                        # a-z = 97-122
                        # 0-9 = 48-57
                        # space = 32
                        
'----------------------------------------------------------'                       
                        
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

'------------------------------------------------------------'

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

'---------------------------------------------------------------'

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
'-----------------------------------------------------------------'    
    
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

'--------------------------------------------------------------------'

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
    
'------------------------------------------------------------------------'

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

'----------------------------------------------------------------------------'

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


'''############################### Right angle traingle #######################################
   ############################## Up right angle traingle #####################################'''


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

'------------------------------------------------------------------------------'

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

'------------------------------------------------------------------------------'

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
    
'-------------------------------------------------------------------------------'

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

'--------------------------------------------------------------------------------'
############################### Extra question #############################

# n = int(input("Enter the number: "))
# for i in range(1,n+1):
#     for j in range(i,0,-1):
#         print((j%2),end=" ")
#     print() 
    
# 1 
# 0 1 
# 1 0 1 
# 0 1 0 1 
# 1 0 1 0 1     

'---------------------------------------------------------------------------------'
 
# n = int(input("Enter the number: "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j%2,end=" ")
#     print()      
    
# 1 
# 1 0 
# 1 0 1 
# 1 0 1 0 
# 1 0 1 0 1     
'------------------------------------------------------------------------------------'

# n = int(input("Enter the number: "))
# for i in range(n, 0, -1):
#     for j in range(i, n + 1):
#         print(j, end=" ")
#     print()

# 5 
# 4 5 
# 3 4 5 
# 2 3 4 5 
# 1 2 3 4 5 
'------------------------------------------------------------------------------------'

# n = int(input("Enter the number: "))
# for i in range(1, n + 1):
#     num = i
#     for j in range(1, i + 1):
#         print(num, end=" ")
#         num += (n - j)
#     print()

# 1 
# 2 6 
# 3 7 10 
# 4 8 11 13 
# 5 9 12 14 15 

'-----------------------------------------------------------------------------------------'

# n = int(input("Enter the number: "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(chr(j+64),end=" ")
#     print()    
    
# A 
# A B 
# A B C 
# A B C D 
# A B C D E     

'-------------------------------------------------------------------------------------------'

# n = int(input("Enter the number: "))
# for i in range(1,n+1):
#     for j in range(i,0,-1):
#         print(chr(j+64),end=" ")
#     print() 

# A 
# B A 
# C B A 
# D C B A 
# E D C B A 

'------------------------------------------------------------------------------------------------'

# n = int(input("Enter the number: "))
# for i in range(n,0,-1):
#     for j in range(n,i-1,-1):
#         print(chr(j+64),end=" ")
#     print() 
    
# E 
# E D 
# E D C 
# E D C B 
# E D C B A    

'---------------------------------------------------------------------------------------------------'

# n = int(input("Enter the number: "))
# for i in range(n,0,-1):
#     for j in range(i,n+1):
#         print(chr(j+96),end=" ")
#     print() 
    
# e 
# d e 
# c d e 
# b c d e 
# a b c d e     

'-------------------------------------------------------------------------------------------------------'

'######################################## Down-right-angle traingle #######################################'

# n = int(input("Enter the number : "))
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print() 
    
# * * * * * 
# * * * * 
# * * * 
# * * 
# *    
'----------------------------------------------------------------------------------'

# n = int(input("Enter the number : "))
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print() 
    
# 1 2 3 4 5 
# 1 2 3 4 
# 1 2 3 
# 1 2 
# 1      
'-------------------------------------------------------------------------------------'  

# n = int(input("Enter the number: "))
# for i in range(1, n+1):
#     for j in range(n, i-1, -1):
#         print(j, end=" ")
#     print()

# 5 4 3 2 1 
# 5 4 3 2 
# 5 4 3 
# 5 4 
# 5 

'---------------------------------------------------------------------------------------'

# n = int(input("Enter the number: "))
# for i in range(1, n+1):
#     for j in range(i,n+1):
#         print(j, end=" ")
#     print()
    
# 1 2 3 4 5 
# 2 3 4 5 
# 3 4 5 
# 4 5 
# 5     
 
'--------------------------------------------------------------------------------------------'

# n = int(input("Enter the number: "))
# for i in range(0, n):
#    for j in range(n, i, -1):
#       print(j, end=" ")
#    print()

# 5 4 3 2 1 
# 5 4 3 2 
# 5 4 3 
# 5 4 
# 5 

'-------------------------------------------------------------------------------------------------'

# n = int(input("Enter the number: "))
# for i in range(n,0,-1):
#    for j in range(i,0,-1):
#       print(j, end=" ")
#    print()
   
# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1    

 
'-------------------------------------------------------------------------------------------'

# n = int(input("Enter the number: "))
# for i in range(n,0,-1):
#    for j in range(1,i+1):
#       print(j,end=" ")
#    print()    
   
# 1 2 3 4 5 
# 1 2 3 4 
# 1 2 3 
# 1 2 
# 1    

'--------------------------------------------------------------------------------------------'

# n = int(input("Enter the number: "))
# for i in range(0, n):
#    for j in range(n, i, -1):
#       print(j, end=" ")
#    print()

# 5 4 3 2 1 
# 5 4 3 2 
# 5 4 3 
# 5 4 
# 5 

'-----------------------------------------------------------------------------------------------'

# n = int(input("Enter the number: "))
# for i in range(1,n+1):
#    for j in range(i,n+1):
#       print(j, end=" ")
#    print()
   
# 1 2 3 4 5 
# 2 3 4 5 
# 3 4 5 
# 4 5 
# 5    

'-------------------------------------------------------------------------------------------------'

# n = int(input("Enter the number: "))
# for i in range(n,0,-1):
#    for j in range(i,0,-1):
#       print(j, end=" ")
#    print()
   
# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1    

'--------------------------------------------------------------------------------------------------'

'############################### Right right angle traingle ##################################'

# n = int(input("Enter the number: "))
# for i in range(1,n+1):
    
#     #Space loop
#     for j in range(0,n-i):
#         print(" ",end=" ")
        
#     #Star loop    
#     for k in range(1,i+1):
#         print("*",end=" ")
#     print()        
    
#         * 
#       * * 
#     * * * 
#   * * * * 
# * * * * *     

'---------------------------------------------------------------------------------------------'

# n = int(input("Enter the number: "))
# for i in range(1,n+1):
    
#     #Space loop
#     for j in range(0,n-i):
#         print(" ",end=" ")
        
#     #Star loop    
#     for k in range(1,i+1):
#         print(k,end=" ")
#     print() 
    
#         1 
#       1 2 
#     1 2 3 
#   1 2 3 4 
# 1 2 3 4 5 

'----------------------------------------------------------------------------------------------'
    
# n = int(input("Enter the number: "))
# for i in range(1,n+1):
    
#     #Space loop
#     for j in range(0,n-i):
#         print(" ",end=" ")
        
#     #Star loop    
#     for k in range(1,i+1):
#         print(k%2,end=" ")
#     print()     
    
#         1 
#       1 0 
#     1 0 1 
#   1 0 1 0 
# 1 0 1 0 1     

'----------------------------------------------------------------------------------------------'

# n = int(input("Enter the number: "))
# for i in range(0,n+1):
#     for j in range(0,n-i):
#         print(" ",end=" ")
#     for k in range(i,0,-1):
#         print(chr(k+64),end=" ")
#     print()        
#         A 
#       B A 
#     C B A 
#   D C B A 
# E D C B A     

'-----------------------------------------------------------------------------------------------'

# def print_pattern(n):
#     for i in range(n):
#         for j in range(n-i-1):
#             print(" ", end=" ")
#         for k in range(n-i, n+1):
#             print(chr(64+k), end=" ")
#         print()

# n = int(input("Enter the number : "))
# print_pattern(n)

#         E 
#       D E 
#     C D E 
#   B C D E 
# A B C D E     

'-----------------------------------------------------------------------------------------------'

# def print_pattern(n):
#     for i in range(n):
#         for j in range(n-i-1):
#             print(" ", end=" ")
#         for k in range(i+1):
#             print(chr(65+k), end=" ")
#         print()

# n = int(input("Enter the number: "))
# print_pattern(n)

#         A 
#       A B 
#     A B C 
#   A B C D 
# A B C D E 

'-----------------------------------------------------------------------------------------------'

# def print_pattern(n):
#     for i in range(n):
#         for j in range(n-i-1):
#             print(" ", end=" ")
#         for k in range(i+1):
#             print(n-k, end=" ")
#         print()

# n = int(input("Enter the number of rows: "))
# print_pattern(n)

#         5 
#       5 4 
#     5 4 3 
#   5 4 3 2 
# 5 4 3 2 1 

'##############################################################################################'
 
# n = int(input("Enter the number: "))
# for i in range(n,0,-1):
#    for j in range(1,n-i+1):
#       print(' ',end=" ")
#    for k in range(1,i+1):
#       print("*",end=" ")
#    print()          
             
# * * * * * 
#   * * * * 
#     * * * 
#       * * 
#         * 

'-----------------------------------------------------------------------------------------------'

# n = int(input("Enter the number: "))
# for i in range(n, 0, -1):
#    for j in range(n, i, -1):
#       print(" ", end=" ")
#    for k in range(1, i+1):
#       print(k, end=" ")
#    print()
 
# 1 2 3 4 5 
#   1 2 3 4 
#     1 2 3 
#       1 2 
#         1      

'-------------------------------------------------------------------------------------------------'

# n = int(input("Enter the number: "))
# for i in range(n, 0, -1):
#     for j in range(n, i, -1):
#         print(" ", end=" ")
#     for k in range(n-i+1, n+1):
#         print(k, end=" ")
#     print()
     
# 1 2 3 4 5 
#   2 3 4 5 
#     3 4 5 
#       4 5 
#         5      

'--------------------------------------------------------------------------------------------------'

# n = int(input("Enter the number: "))
# for i in range(0, n+1):
#     for j in range(0, i+1):
#         print(" ", end=" ")
#     for k in range(n,i,-1):
#         print(k, end=" ")
#     print()
 
#   4 3 2 1 
#     4 3 2 
#       4 3 
#         4    

'--------------------------------------------------------------------------------------------------'

# n = int(input("Enter the number: "))
# for i in range(n):
#     for j in range(i):
#         print(" ", end=" ")
#     for k in range(n-i, 0, -1):
#         print(k, end=" ")
#     print()

# 5 4 3 2 1 
#   4 3 2 1 
#     3 2 1 
#       2 1 
#         1 

'--------------------------------------------------------------------------------------------------'

# n = int(input("Enter the number: "))
# for i in range(n):
#     for j in range(i):
#         print(" ", end=" ")
#     for k in range(n-i, 0, -1):
#         print(chr(k+96), end=" ")
#     print()

# e d c b a 
#   d c b a 
#     c b a 
#       b a 
#         a 

'---------------------------------------------------------------------------------------------------------'

# n = int(input("Enter the number: "))
# for i in range(n):
#     for j in range(i):
#         print(" ", end=" ")
#     for k in range(n-i):
#         print((i+k) % 2, end=" ")
#     print()

# 0 1 0 1 0 
#   1 0 1 0 
#     0 1 0 
#       1 0 
#         0 
'----------------------------------------------------------------------------------------------------------'
        
# n = int(input("Enter the number: "))
# for i in range(n):
#     for j in range(i):
#         print(" ", end=" ")
#     for k in range(n-i):
#         print((k + (i % 2)) % 2, end=" ")
#     print()

# 0 1 0 1 0 
#   1 0 1 0 
#     0 1 0 
#       1 0 
#         0 

'------------------------------------------------------------------------------------------------------------'

# n = int(input("Enter the number: "))
# for i in range(n, 0, -1):
#     for j in range(n, i, -1):
#         print(" ", end=" ")
#     for k in range(1, i+1):
#         print(chr(k+96), end=" ")
#     print()

# a b c d e 
#   a b c d 
#     a b c 
#       a b 
#         a

'------------------------------------------------------------------------------------------------------------'

# def print_pattern(n):
#     C = 65
#     for i in range(n):
#         for j in range(i):
#             print(" ", end=" ")
#         for k in range(n-i):
#             print(chr(C), end=" ")
#             C += 1
#             if C > 90:  # Reset to 'A' after 'Z'
#                 C = 65
#         print()

# n = int(input("Enter the number of rows: "))
# print_pattern(n)

# A B C D E F G 
#   H I J K L M 
#     N O P Q R 
#       S T U V 
#         W X Y 
#           Z A 
#             B 

'-----------------------------------------------------------------------------------------------------'
'####################################### Pyramid pattern program #####################################'

# n = int(input("Enter the number: "))
# for i in range(1,n+1):
#    for j in range(1,n-i+1):
#       print(" ",end=" ")
#    for k in range(1,2*i):
#       print("*",end=" ")
#    print()      
   
#         * 
#       * * * 
#     * * * * * 
#   * * * * * * * 
# * * * * * * * * *

'------------------------------------------------------------------------------------------------------'

# n = int(input("Enter the number: "))
# for i in range(1,n+1):
#    for j in range(1,n-i+1):
#       print(" ",end=" ")
#    for k in range(1,2*i):
#       print(k,end=" ")
#    print()          
   
#         1 
#       1 2 3 
#     1 2 3 4 5 
#   1 2 3 4 5 6 7 
# 1 2 3 4 5 6 7 8 9    

'------------------------------------------------------------------------------------------------------'

# n = int(input("Enter the number: "))
# for i in range(1,n+1):
#    for j in range(1,n-i+1):
#       print(" ",end=" ")
#    for k in range(1,2*i):
#       print(i%2,end=" ")
#    print()      
   
#         1 
#       0 0 0 
#     1 1 1 1 1 
#   0 0 0 0 0 0 0 
# 1 1 1 1 1 1 1 1 1    

'-------------------------------------------------------------------------------------------------------'

# n = int(input("Enter the number: "))
# for i in range(1,n+1):
#    for j in range(1,n-i+1):
#       print(" ",end=" ")
#    for k in range(1,2*i):
#       print(k%2,end=" ")
#    print() 
   
#         1 
#       1 0 1 
#     1 0 1 0 1 
#   1 0 1 0 1 0 1 
# 1 0 1 0 1 0 1 0 1   

'------------------------------------------------------------------------------------------------------' 

# n = int(input("Enter the number: "))
# c = 1
# for i in range(1,n+1):
#    for j in range(1,n-i+1):
#       print(" ",end=" ")
#    for k in range(1,2*i):
#       print(c%2,end=" ")
#       c = c+1
#    print() 
   
#         1 
#       0 1 0 
#     1 0 1 0 1 
#   0 1 0 1 0 1 0 
# 1 0 1 0 1 0 1 0 1    

'-------------------------------------------------------------------------------------------------------'

# n = int(input("Enter the number: "))
# for i in range(1,n+1):
#    for j in range(1,n-i+1):
#       print(" ",end=" ")
#    for k in range(2*i-1,0,-1):
#       print(k,end=" ")
#    print() 
   
#         1 
#       3 2 1 
#     5 4 3 2 1 
#   7 6 5 4 3 2 1 
# 9 8 7 6 5 4 3 2 1

'-------------------------------------------------------------------------------------------------------'

# n = int(input("Enter the number: "))
# for i in range(1,n+1):
#    for j in range(1,n-i+1):
#       print(" ",end=" ")
#    x = 1
#    for k in range(1,2*i):
#       print(x,end=" ")
#       if k<i:
#          x = x+1
#       else:
#          x = x-1
#    print()                
   
#         1 
#       1 2 1 
#     1 2 3 2 1 
#   1 2 3 4 3 2 1 
# 1 2 3 4 5 4 3 2 1    
  
'-------------------------------------------------------------------------------------------------------'

# n = int(input("Enter the number: "))
# for i in range(1,n+1):
#    for j in range(1,n-i+1):
#       print(" ",end=" ")
#    x = i
#    for k in range(1,2*i):
#       print(x,end=" ")
#       if k<i:
#          x = x-1
#       else:
#          x = x+1
#    print()      
   
#         1 
#       2 1 2 
#     3 2 1 2 3 
#   4 3 2 1 2 3 4 
# 5 4 3 2 1 2 3 4 5    

'-----------------------------------------------------------------------------------------------------------'

# n = int(input("Enter the number: "))
# for i in range(1,n+1):
#    for j in range(1,n-i+1):
#       print(" ",end=" ")
#    x = n -i + 1
#    for k in range(1,2*i):
#       print(x,end=" ")
#       if k<i:
#          x = x+1
#       else:
#          x = x-1
#    print()   
   
#         5 
#       4 5 4 
#     3 4 5 4 3 
#   2 3 4 5 4 3 2 
# 1 2 3 4 5 4 3 2 1    

'-------------------------------------------------------------------------------------------------'

# def print_pattern(n):
#     for i in range(n):
#         # Print leading spaces
#         for j in range(n - i - 1):
#             print(" ", end=" ")
        
#         # Print increasing characters
#         for j in range(i + 1):
#             print(chr(65 + j), end=" ")
        
#         # Print decreasing characters
#         for j in range(i, 0, -1):
#             print(chr(64 + j), end=" ")
        
#         # Move to the next line
#         print()

# # Define the number of rows
# rows = int(input("Enter the number: "))
# print_pattern(rows)

#         A 
#       A B A 
#     A B C B A 
#   A B C D C B A 
# A B C D E D C B A 

'-----------------------------------------------------------------------------------------------'

# def print_pattern(n: int):
#     # Start from 'D' which is ASCII 68 (corresponding to row 4)
#     for i in range(n):
#         # Print leading spaces
#         for _ in range(n - i - 1):
#             print(" ", end=" ")
        
#         # Print ascending characters
#         for j in range(i, -1, -1):
#             print(chr(65 + j), end=" ")
        
#         # Print descending characters
#         for j in range(1, i + 1):
#             print(chr(65 + j), end=" ")
        
#         print()  # Move to the next line

# # Call the function for 4 rows as in the example
# print_pattern(6)

#          A 
#         B A B 
#       C B A B C 
#     D C B A B C D 
#   E D C B A B C D E 
# F E D C B A B C D E F

'---------------------------------------------------------------------------------------------------'