#
# A simple webserver MEANT FOR TESTING based off of http.server.
# Invoke with py dars.py serve. Serves from the directory give in the config.
#

import http.server
import socketserver
import os

def serve(PORT=80):
	web_dir = os.path.join(os.path.dirname(__file__), 'serve')
	os.chdir(web_dir)

	Handler = http.server.SimpleHTTPRequestHandler
	httpd = socketserver.TCPServer(("", PORT), Handler)
	print("Serving at port: ", PORT)
	try:
		httpd.serve_forever()
	except KeyboardInterrupt:
		print("^C: Ending serve_forever()...")
