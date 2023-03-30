# Write your code here
import re

def collect_links(string):
    collect = re.findall(r'<a href="(.*)"', string)
    return collect