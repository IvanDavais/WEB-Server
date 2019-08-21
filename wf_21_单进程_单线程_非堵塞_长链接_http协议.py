import socket 
import re
import time


def service_client(new_socket, request):
	
	request_lines =request.splitlines()
	print("")
	print(">"*20)
	print(request_lines)

	# 使用正则表达式提取服务器想要获取的网页
	ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
	file_name = ""

	if ret:
		file_name = ret.group(1)
		if file_name == "/":
			file_name = "/index.html"

	try:
		f = open("./html"+file_name, "rb")
	except:
		response = "HTTP/1.1 404 NOT FOUND!\r\n"
		response += "\r\n"
		response += "-----File Not Found-----"
		new_socket.send(response.encode("utf-8"))
	else:
		html_content = f.read()
		f.close()
		
		# 准备发送给浏览器的数据
		response_body = html_content

		response_header = "HTTP/1.1 200 OK\r\n"
		response_header += "Content-Length:%d\r\n" %len(response_body)
		response_header += "\r\n"
		response = response_header.encode("utf-8") + response_body

		# 将response header发送给浏览器
		new_socket.send(response)
		

def main():

	# 1 创建套接字
	tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

	# 绑定
	tcp_server_socket.bind(("", 7890))

	# 变为监听套接字
	tcp_server_socket.listen(128)
	tcp_server_socket.setblocking(False) #将套接字变为非堵塞

	client_socket_list = list()
	time.sleep(0.5)
	while True:
		try:
			#等待新客户端的到来
			new_socket, client_addr = tcp_server_socket.accept()
		except Exception as ret:
			print("-----没有客户端的到来-----")
		else:
			new_socket.setblocking(False)
			client_socket_list.append(new_socket)
			
		for client_socket in client_socket_list:
			try:
				recv_data = client_socket.recv(1024).decode("utf-8")
			except Exception as ret:
				print("----客户端虽然链接，但是没有发送数据----")
			else:
				if recv_data:
					service_client(client_socket, recv_data)
				else:
					client_socket.close()
					client_socket_list.remove(client_socket)
			
		# 为这个客户端服务
		# service_client(new_socket)
		
	tcp_server_socket.close()


if __name__ == "__main__":
	main()  
