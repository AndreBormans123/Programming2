# Write your code here
import re

def remove_repeated_words(string):
    return re.sub(r'(.)\1\1', "", string)