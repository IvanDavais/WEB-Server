import re

ret = re.findall(r"\d+", "python = 9999, c = 10000, java = 666")
print(ret)
