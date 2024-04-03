# class Recurssion():

# *****************
# Recurssion Examples
def recurssion_exp(n):
    if(n == 1):
        return 1 
    else:
        return n * recurssion_exp(n-1)
    
# print(recurssion_exp(5))

    
# ***********
# Hanoi Disks 
# ***********
def hanoi(disks, source, helper, destination):
    # Base condition
    if(disks ==1):
        print('disk {} moves from tower {} to tower {}.'.format(disks,source,destination))
        return
    
    # Recursive Calls in which function calls itself
    hanoi(disks - 1, source, destination, helper)
    print('Disk {} moves from tower {} to tower {}.'.format(disks,source, destination))
    hanoi(disks - 1, helper, source,destination)
    
# driver code
# disks = int(input('Number of disks to be displaced: '))
'''
    Tower names passed as arguments: 
    Source: A
    Helper: B
    Destination: C
'''

# Actual function call
# hanoi(disks, 'A', 'B', 'C')



# ******************
# Reverse String
# ******************

# With slice function
# with slice function
# trial = "reversal"

# new_trial = trial[::-1]
# print(new_trial)


# Recursive 
def string_reverse(str):
    if len(str)== 0:
        return str
    else:
        return string_reverse(str[1:]) + str[0]
    
# str = "reversal"
# new_rv_str = string_reverse(str)



