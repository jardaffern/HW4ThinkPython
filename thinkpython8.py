

#not sure the export to .py worked as intended, I am using VS Code
# %%
print("banana".count("a"))

# %%
#oops did this during the last hw, didn't realize we were meant to use a for loop last time

def is_palindrome(input):
    if input == input[::-1]:
        return True
    else:
        return False
    
is_palindrome("racecar")


