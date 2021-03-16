import http.server #this should work as basic http server idk man lets see
import socketserver #lol socket

PORT = 8080   #the port from this ummm "super nice laptop" that the website uses to host
Handler = http.server.SimpleHTTPRequestHandler #recieves the info and does dirty magic with it hashing it and stuff

with socketserver.TCPServer(("", PORT), Handler) as httpd: #TCP address is passed as a tuple of (ip address, port number)
    print("serving at port", PORT) #im a nerd at this point necva gonna get smashed
    httpd.serve_forever()
