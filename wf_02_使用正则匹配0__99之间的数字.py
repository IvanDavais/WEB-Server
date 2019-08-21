import re

num_list = [1, 0, 56, 98, 120, 999]

for num in num_list:
	# 注意：要先将列表中的数字转换成字符串然后才能使用正则表达式，因为正则表达式就是用来匹配字符串
	ret = re.match("[1-9]?\d" ,str(num))
	if ret:
		print(ret.group())
