# Recursive 
def string_reverse(str):
    if len(str)== 0:
        return str
    else:
        return string_reverse(str[1:]) + str[0]
    
# str = "reversal"
# new_rv_str = string_reverse(str)