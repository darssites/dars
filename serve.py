import http.server
import socketserver
import os

def serve(PORT=80):
	web_dir = os.path.join(os.path.dirname(__file__), 'serve')
	os.chdir(web_dir)

	Handler = http.server.SimpleHTTPRequestHandler
	httpd = socketserver.TCPServer(("", PORT), Handler)
	print("Serving at port: ", PORT)
	httpd.serve_forever()