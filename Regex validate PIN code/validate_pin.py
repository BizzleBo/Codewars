# Goal - ATM machines allow 4 or 6 digit PIN 
# codes and PIN codes cannot contain anything 
# but exactly 4 digits or exactly 6 digits.

# Given code - 
# def validate_pin(pin):
    #return true or false

# Solution -
def validate_pin(pin):
    if pin.isnumeric():
        if len(pin) == 4 or len(pin) == 6:
            return True
        else:
            return False
    else:
        return False

