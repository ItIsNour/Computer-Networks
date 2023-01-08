from socket import *
import sys
import webbrowser

# if len(sys.argv) <= 1:
    # print('Usage : "python ProxyServer.py server_ip"\n[server_ip : It is the IP Address Of Proxy Server')
#     sys.exit(2)

# Create a server socket, bind it to a port and start listening
tcpSerSock = socket(AF_INET, SOCK_STREAM)      #For a TCP socket
# Fill in start.
portNumber = 4089
tcpSerSock.bind(('', portNumber))
tcpSerSock.listen(11)
# Fill in end.
try:
    while 1:
        # Strat receiving data from the client
        print('\nReady to serve...')
        tcpCliSock, addr = tcpSerSock.accept()
        print('Received a connection from:', addr)
        # Fill in start.
        message = tcpCliSock.recv(2048)
        # Fill in end.
        print(message)

        # Handle an empty message error
        if message == b'':
            print("Message is empty")
            
        

        # Extract the filename from the given message and put it in cache
        if message != b'':
            fileName = message.split()[1].decode("utf-8").rpartition("/")[2]
            hostName = message.split()[4].decode("utf-8")
            URL = message.split()[1].decode("utf-8")

        print("File Name: "+ fileName)
        print("Host Name: " + hostName)
        print("URL : " + URL)
        fileExist = "false"
        fileToUse = "./Cache" + fileName
        print(fileToUse)

        # Check for the URL if blocked
        flag = 1
        with open('ListOfBlockedURLs.txt') as f:
            for line in f:
                if URL in line:
                    print("THIS URL IS BLOCKED")
                    webbrowser.open_new_tab('BlockedURL.html')
                    flag = 0
                    break
                else:
                    flag = 1
        if flag == 0:
            break


        try:
            # Check wether the file exist in the cache
            f = open(fileToUse[1:], "rb")
            outputdata = f.readlines()
            fileExist = "true"

            # ProxyServer finds a cache hit and generates a response message
            tcpCliSock.send(b"HTTP/1.0 200 OK\r\n")
            tcpCliSock.send(b"Content-Type:text/html\r\n")
            # Fill in start.
            for i in range(0, len(outputdata)):
                tcpCliSock.send(outputdata[i])
            # Fill in end.
                print('Read from cache')
            f.close()

        # Error handling for file not found in cache
        except IOError:
            try:
                if fileExist == "false":
                    # Create a socket on the proxyserver
                    # Fill in start.
                    proxySocket = socket(AF_INET, SOCK_STREAM)
                    # Fill in end.
                    print(hostName)
                    # Connect to the socket to port 80
                    # Fill in start.
                    proxySocket.connect((hostName, 80))
                    # Fill in end.

                    # Create a temporary file on this socket and ask port 80 for the file requested by the client
                    fileobj = proxySocket.makefile('w', None)
                    fileobj.write("GET " + message.split()[1].decode("utf-8") + " HTTP/1.0\n\n")
                    fileobj.close()
                    # Read the response into buffer
                    # Fill in start.
                    fileobj = proxySocket.makefile('rb',None)
                    buffer = fileobj.readlines()
                    # Fill in end.

                    # Create a new file in the cache for the requested file.
                    # Also send the response in the buffer to client socket and the corresponding file in the cache
                    cacheFile = open("./Cache/" + fileName, "wb+")
                    # Fill in start.
                    for line in buffer:
                        cacheFile.write(line)
                        tcpCliSock.send(line)
                    cacheFile.close()
                    proxySocket.close()
                    # Fill in end.

            except:
                print("Illegal request")
    else:
        # HTTP response message for file not found
        # Fill in start.
        tcpCliSock.send("HTTP/1.0 404 sendError\r\n")
        tcpCliSock.send("Content-Type:text/html\r\n")
        # Fill in end.

        # Close the client and the server sockets
        tcpCliSock.close()
    # Fill in start.
        print("Socket is Closed")
        sys.exit("File Not Found")
except:
    print('Connection is Blocked')
    tcpCliSock.close()
    sys.exit("No Message")     
tcpSerSock.close()
    # Fill in end.
