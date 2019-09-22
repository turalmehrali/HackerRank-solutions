
def count_substring(string, sub_string):
    say = 0
    for i in range(0, len(string)):
        if string[i:i+len(sub_string)] == sub_string:
            say += 1
    return say

