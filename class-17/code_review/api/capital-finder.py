from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        url_componenets = parse.urlsplit(s)
        url_query = parse.parse_qsl(url_componenets.query)
        dic = dict(url_query)

        if 'country' in dic:
            value = dic['country'].capitalize()
            url = 'https://restcountries.com/v2/name/'
            r = requests.get(url + value)
            data = r.json()
            capital = data[0]['capital']
            message = f'The capital of {value} is {capital}.'
        elif 'capital' in dic:
            pass

        else:
            message = "Please provide me with a country name or a capital city name"

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode())
        return


def main():
    port = 8000
    server_address = ('localhost', port)
    server = HTTPServer(server_address, handler)
    print(f'Server is running')
    server.serve_forever()

if __name__ == "__main__":
    main()

