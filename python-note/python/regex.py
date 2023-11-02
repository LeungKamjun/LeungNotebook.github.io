import re


def repl(temp):
    print(temp)
    num = temp.group()
    num1 = int(num) + 1
    return str(num1)


result = re.sub(r'\d+', repl, 'java:99,python:95')
print(result)
