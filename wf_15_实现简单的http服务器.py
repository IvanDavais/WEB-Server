import socket


def service_client(new_socket):
	# 1.接受浏览器发过来的请求，即http请求
	request = new_socket.recv(1024)
	print(">>"*50)
	print(request)

	# 2.返回http格式的数据，给浏览器
	response = "HTTP/1.1 200 OK\r\n"
	response += "\r\n"

	f = open("/home/fanwan666/PycharmProjects/web服务器/html/index.html", "rb")
	html_content = f.read()
	f.close()
	
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
		# 5.为这个客户端服务
		service_client(new_socket)

	# 6.关闭套接字
	tcp_socket.close()
if __name__ == "__main__":
	main()
