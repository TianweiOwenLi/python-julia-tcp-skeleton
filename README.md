# Python-Julia TCP Server-Client Pair Skeleton
This folder contains the skeleton code of a python-julia TCP server, in which some python instance spawns a julia client and proceeds to communicate with it. 

## Connection
Connection between Python and Julia instance involves the following steps: 

1. `serv.py` creates a socket and starts `client.jl` in a sub-process
2. `client.jl` connects to the socket created previously
3. `serv.py` accepts the connection from `client.jl`

## Exchange Loop
When connection succeeds, `serv.py` and `client.jl` exchanges information with each other. When one instance sends over a message, it waits for a response. 

## Termination
When `serv.py` wishes to terminate the connection, it tells `client.jl` to stop by sending the string "close", joins the julia subprocess, and closes the socket. 