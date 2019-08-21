import socket
import time 

tcp_server_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server_tcp.bind(("", 7890))
tcp_server_tcp.listen(128)
tcp_server_tcp.setblocking(False)

client_list = list()

while True:
	time.sleep(0.5)
	try:
		new_socket, new_addr = tcp_server_tcp.accept()
	except Exception as ret:
		print("---没有新的客户端到来---")
	else:
		print("---没有产生异常，新的客户端到来---")
		new_socket.setblocking(False)
		client_list.append(new_socket)

	for client_socket in client_list:
		try:
			recv_data = client_socket.recv(1024)
		except Exception as ret:
			print("---客户端虽然到来但是并没有发送数据---")
		else:
			print("---没有异常---")
			print(recv_data.decode("utf-8"))
			if recv_data:
				print("---客户端发送过来了数据")
			else:
				client_socket.close()
				client_list.remove(client_socket)
				print("---客户端关闭---")
