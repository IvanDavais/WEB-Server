import re

names = ["name1", "_name", "2_name", "__name__"]
for name in names:
	# 注意字母，下划线开头的都合法
	ret = re.match(r"[a-zA-Z_]+[\w]*", name)
	if ret:
		print(ret.group())
