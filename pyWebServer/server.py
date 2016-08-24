# coding=utf-8

import BaseHTTPServer

class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    '''
    处理请求并返回页面
    '''

    # 页面模板
    Page = '''\
    <html>
    <body>
    <table>
    <tr>
        <td>Header</td>
        <td>Value</td>
    </tr>
    <tr>
        <td>Date and time</td>
        <td>{date_time}</td>
    </tr>
    <tr>
        <td>Client Host</td>
        <td>{client_host}</td>
    </tr>
    <tr>
        <td>Client Port</td>
        <td>{client_port}</td>
    </tr>
    <tr>
        <td>Command</td>
        <td>{command}</td>
    </tr>
    <tr>
        <td>Path</td>
        <td>{path}</td>
    </tr>
    </table>
    </body>
    </html>
    '''

    # 处理一个GET请求
    def do_GET(self):
        page = self.create_page()
        self.send_content(page)

    def create_page(self):
        values = {
            'date_time': self.date_time_string(),
            'client_host': self.client_address[0],
            'client_port': self.client_address[1],
            'command': self.command,
            'path': self.path
        }
        page = self.Page.format(**values)
        return page

    def send_content(self, page):
        self.send_response(200)
        self.send_header("Content-Type", 'text/html')
        self.send_header("Content-Length", str(len(page)))
        self.end_headers()
        self.wfile.write(page)


# -----------------------------------------------------------------
if __name__ == '__main__':
    serverAddress = ('', 8080)
    server = BaseHTTPServer.HTTPServer(serverAddress, RequestHandler)
    server.serve_forever()
