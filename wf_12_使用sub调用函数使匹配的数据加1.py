import re

def add(temp):
	strNum = temp.group()
	num = int(strNum) + 1
	return str(num)

ret = re.sub(r"\d+", add, "python = 999")
print(ret)
