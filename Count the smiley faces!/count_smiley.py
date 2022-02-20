# Goal -
# Given an array (arr) as an argument complete the function count
# Smileys that should return the total number of smiling faces.

# Rules for a smiling face:

# Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
# A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
# Every smiling face must have a smiling mouth that should be marked with either ) or D
# No additional characters are allowed except for those mentioned.

# Valid smiley face examples: :) :D ;-D :~)
# Invalid smiley faces: ;( :> :} :]

# Example
# countSmileys([':)', ';(', ';}', ':-D']);       // should return 2;
# countSmileys([';D', ':-(', ':-)', ';~)']);     // should return 3;
# countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1;

# Given code - 
# def count_smileys(arr):
    # return #the number of valid smiley faces in array/list

# Solution -
def count_smileys(arr):
    eyes = [':', ';']
    nose = ['-', '~']
    mouth = [')', 'D']
    smileys = 0
    if eyes in arr and mouth in arr:
        smileys = smileys + 1
    return smileys