import re

def main():
	label_name = input("请输入一个html中的嵌入式标签: ")
	ret = re.match(r"<(?P<g1>\w*)><(?P<g2>\w*)>.*</(?P=g2)></(?P=g1)>", label_name)
	if ret:
		print("你输入了一对正确的html标签:%s" %label_name)
	else:
		print("你输入的标签不对")

if __name__ == "__main__":
	main()

