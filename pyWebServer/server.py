# coding=utf-8

import sys, os
import BaseHTTPServer


class ServerException(Exception):
    '''
    服务器内部错误
    '''
    pass


class base_case(object):
    '''
    条件处理基类
    '''

    def handle_file(self, handler, full_path):
        try:
            with open(full_path, 'rb') as reader:
                content = reader.read()
            handler.send_content(content)
        except IOError as msg:
            msg = "'{0}' cannot be read: {1}".format(full_path, msg)
            handler.handle_error(msg)

    def index_path(self, handler):
        return os.path.join(handler.full_path, 'index.html')

    def test(self, handler):
        assert False, 'Not implemented.'

    def act(self, handler):
        assert False, 'Not implemented.'


class case_no_file(base_case):
    '''
    路径不存在
    '''

    def test(self, handler):
        return not os.path.exists(handler.full_path)

    def act(self, handler):
        raise ServerException("'{0}' not found".format(handler.path))


class case_exsiting_file(base_case):
    '''
    路径是文件
    '''

    def test(self, handler):
        return os.path.isfile(handler.full_path)

    def act(self, handler):
        self.handle_file(handler, handler.full_path)


class case_always_fail(base_case):
    '''
    默认处理类
    '''

    def test(self, handler):
        return True

    def act(self, handler):
        raise ServerException("Unknown object '{0}'".format(handler.path))


class case_directory_index_file(base_case):
    '''
    根目录
    '''

    def test(self, handler):
        return os.path.isdir(handler.full_path) and \
            os.path.isfile(self.index_path(handler))

    def act(self, handler):
        self.handle_file(handler, self.index_path(handler))


class case_cgi_file(base_case):
    '''
    脚本文件处理
    '''

    def test(self, handler):
        return os.path.isfile(handler.full_path) and \
            handler.full_path.endswith('.py')

    def act(self, handler):
        # 运行脚本
        self.run_cgi(handler)

    def run_cgi(self, handler):
        import subprocess
        data = subprocess.check_output(["python", handler.full_path])
        handler.send_content(data)


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

    Cases = [
        case_no_file(),
        case_cgi_file(),
        case_exsiting_file(),
        case_directory_index_file(),
        case_always_fail()
    ]

    # 处理一个GET请求
    def do_GET(self):
        try:
            self.full_path = os.getcwd() + self.path

            for case in self.Cases:
                handler = case
                if handler.test(self):
                    handler.act(self)
                    break

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
