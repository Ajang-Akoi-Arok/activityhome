from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json


# Math functions
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


# Request handler
class Handler(BaseHTTPRequestHandler):

    def do_GET(self):

        parsed = urlparse(self.path)
        params = parse_qs(parsed.query)

        try:
            a = int(params['a'][0])
            b = int(params['b'][0])

        except (KeyError, ValueError, IndexError):

            self.send_response(400)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()

            error = {
                'error': 'a and b must be integers'
            }

            self.wfile.write(json.dumps(error).encode())

            return


        if parsed.path == '/add':

            result = add(a, b)
            operation = 'addition'


        elif parsed.path == '/subtract':

            result = subtract(a, b)
            operation = 'subtraction'


        elif parsed.path == '/multiply':

            result = multiply(a, b)
            operation = 'multiplication'


        else:

            self.send_response(404)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()

            error = {
                'error': 'Operation not found'
            }

            self.wfile.write(json.dumps(error).encode())

            return


        response = {
            'a': a,
            'b': b,
            'operation': operation,
            'result': result
        }


        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()

        self.wfile.write(json.dumps(response).encode())


# Start the server
server = HTTPServer(('localhost', 5000), Handler)
print('Server running on http://localhost:5000')
server.serve_forever()

