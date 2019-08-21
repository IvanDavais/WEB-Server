import re


def main():
	email = input("请输入你的邮箱地址: ")
	ret = re.match(r"[a-zA-Z0-9]{4,20}@(163|126)\.com$", email)
	if ret:
		print("您输入的%s合法" %email)
	else:
		print("你输入的%s不合法" %email)	

if __name__ == "__main__":
	main()
