from http.server import BaseHTTPRequestHandler, HTTPServer
import logging

class RenderRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"Hello, World!")
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(f"Error: {str(e)}".encode())

def run_server(server_address=('localhost', 8080)):
    httpd = HTTPServer(server_address, RenderRequestHandler)
    logging.basicConfig(level=logging.INFO)
    logging.info(f'Starting httpd on {server_address[0]}:{server_address[1]}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()