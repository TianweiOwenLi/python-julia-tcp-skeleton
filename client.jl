using Sockets

const DBG = false

function handle(x)
  n = parse(Int, x)
  while n % 2 == 0
    n = div(n, 2)
  end
  return n
end

function dbg_print(x)
  if DBG
    println(x)
  end
end

host, port = ARGS[1], parse(Int, ARGS[2])
conn = connect(host, port)

try
  while true
    data = readline(conn)
    
    if data == "close"
      break
    end

    ans = handle(data)
    dbg_print("[client] sending $ans")
    write(conn, "$ans\n")
  end
catch err
  print("connection err: $err")
end

dbg_print("[client] shutting down")
close(conn)
