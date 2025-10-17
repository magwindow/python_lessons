import datetime
import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.created_at = datetime.datetime.now()

    def __str__(self):
        return f'{self.__class__}: email - {self.email}, created_at - {self.created_at}'


def format_datetime(obj):
    if isinstance(obj, datetime.datetime):
        return obj.strftime('%Y:%m:%d %H:%M:%S')
    return datetime.datetime.strptime(obj, '%Y:%m:%d %H:%M:%S')


def user_serializer(user: User):
    return {
        'email': user.email,
        'created_at': format_datetime(user.created_at)
    }


def user_deserializer(user: dict):
    assert len(user.keys()) == 2
    assert 'email' in user
    assert 'password' in user
    return User(**user)


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        user = User(email="test@email.ru", password="*****")
        json_response = json.dumps(user_serializer(user))

        self.wfile.write(json_response.encode())

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        post_data = json.loads(post_data)

        self.send_response(201)

        new_user = user_deserializer(post_data)

        self.send_header('Content-type', 'application/json')
        self.end_headers()

        json_response = json.dumps(user_serializer(new_user))

        self.wfile.write(json_response.encode())


if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Server is running on port', server_address[1])
    httpd.serve_forever()
