# coding=utf-8

import sys, os
import BaseHTTPServer


class ServerException(Exception):
    '''
    服务器内部错误
    '''
    pass


class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    '''
    处理请求并返回页面
    '''

    # 页面模板
    Error_Page = """\
    <html>
    <body>
    <h1>Error accessing {path}</h1>
    </body>
    </html>
    """

    # 处理一个GET请求
    def do_GET(self):
        try:
            full_path = os.getcwd() + self.path

            if not os.path.exists(full_path):
                raise ServerException("'{0}' not found".format(self.path))
            elif os.path.isfile(full_path):
                self.handle_file(full_path)
            else:
                raise ServerException("Unknown object '{0}'".format(self.path))

        except Exception as msg:
            self.handle_error(msg)

    def handle_file(self, full_path):
        try:
            with open(full_path, 'rb') as reader:
                content = reader.read()
            self.send_content(content)
        except IOError as msg:
            msg = "'{0}' cannot be read: {1}".format(self.path, msg)
            self.handle_error(msg)

    def handle_error(self, msg):
        content = self.Error_Page.format(path=self.path, msg=msg)
        self.send_content(content, 404)

    def send_content(self, page, status=200):
        self.send_response(status)
        self.send_header("Content-Type", 'text/html')
        self.send_header("Content-Length", str(len(page)))
        self.end_headers()
        self.wfile.write(page)


# -----------------------------------------------------------------
if __name__ == '__main__':
    serverAddress = ('', 8080)
    server = BaseHTTPServer.HTTPServer(serverAddress, RequestHandler)
    server.serve_forever()
