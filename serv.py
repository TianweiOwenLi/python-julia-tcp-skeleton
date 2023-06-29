import socket, subprocess, random
from multiprocessing import Process

host, port = socket.gethostname(), 5000
BLOCK_SIZE = 1024
DBG = False

def start_julia_client(host, port):
  subprocess.run(["julia", "client.jl", host, str(port)])

def handle(x):
  """ Handles parsed client input """
  n = int(x)
  return 3*n + 1

def dbg_print(x):
  if DBG:
    print(x)

serv_socket = socket.socket()
serv_socket.bind((host, port))
serv_socket.listen(1)
serv_socket.settimeout(2)
serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

dbg_print(f"[server] Established socket, starting Julia subroutine")

julia_client = Process(target=start_julia_client, args=([host, port]))
julia_client.start()

conn, addr = serv_socket.accept()

dbg_print(f"[server] accepted connection from {addr}")

num, count = 750, 0
old_num = num
while num >= 5:
  count += 1
  dbg_print(f"[server] sending {str(num)}")
  conn.send((str(num) + "\n").encode())

  data = conn.recv(BLOCK_SIZE).decode()
  num = handle(data)

conn.send("close\n".encode())
dbg_print("[server] request client to close")

# make sure connection is unused before closing
julia_client.join()
conn.close()

print(f"[server] Computation of collatz({old_num}) ended in {count} iterations")
