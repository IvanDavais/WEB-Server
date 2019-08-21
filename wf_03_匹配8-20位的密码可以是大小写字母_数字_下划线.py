import re
# 注意：\w 是可以匹配中文字符的，所以在这里应该不用\w,而是用[a-zA-Z0-9_]来代替
password_list = ["12a3g45678", "1ad12f23s34455ff66", "我12a"]

for pwd in password_list:

	# ret = re.match(r"\w{8,20}", pwd)
	ret = re.match(r"[a-zA-Z0-9_]{8,20}",pwd)
	if ret:	
		print(ret.group())
