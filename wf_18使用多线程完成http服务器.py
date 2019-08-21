import socket
import re
import threading

def service_client(new_socket):
	request = new_socket.recv(1024).encode("utf-8")
	request_lines = request.splitlines()
	print("")
	print(">"*20)
	print(request_lines)

 	# 使用正则表达式获取GET /index.html HTTP/1.1
	file_name = ""
	ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])	
	if ret:
		file_name = ret.group(1)
		print("*"*50, file_name)
		if file_name == "/":
			file_name = "/index.html"

	try:	
		f = open("./html" + file_name, "rb")
	except:
		response = "HTTP/1.1 404 NOT FOUND\r\n"
		response += "\r\n"
		response += "--------File Not Found!"
		new_socket.send(response.encode("utf-8"))
	else:
		html_content = f.read()
		f.close()

		# 2.返回http格式的数据，给浏览器
		response = "HTTP/1.1 200 OK\r\n"
		response += "\r\n"

		# 3.将response body发送给浏览器
		new_socket.send(response.encode("utf-8"))
		new_socket.send(html_content)

	


	# 3.关闭套接字
	new_socket.close()


def main():
	
	tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	# 2.绑定
	tcp_socket.bind(("", 7890))
	# 3.变为监听套接字
	tcp_socket.listen(128)
	while True:

		# 4.等待客户端的链接
		new_socket, client_addr = tcp_socket.accept()
		# 创建一个进程为这个客户端服务：
		p = threading.Thread(target=service_client, args=(new_socket,))
		p.start()


	# 6.关闭套接字
	tcp_socket.close()
if __name__ == "__main__":
	main()
