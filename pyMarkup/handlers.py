# coding=utf-8


class Handler(object):
    """
    处理从Parser调用的方法的对象

    这个解析器会在每个块的开始部分调用start() 和end() 方法, 使用合适的
    块名称作为参数. sub() 方法会用于正则表达式的替换中. 当使用了'emphasis'
    这样的名字调用时, 会返回合适的替换函数.
    """
    def callback(self, prefix, name, *args):
        method = getattr(self, prefix+name, None)
        if callable(method):
            return method(*args)

    def start(self, name):
        self.callback('start_', name)

    def end(self, name):
        self.callback('end_', name)

    def sub(self, name):
        def substitution(match):
            result = self.callback('sub_', name, match)
            if result is None:
                result = match.group(0)
            return result
        return substitution


class HTMLRenderer(Handler):
    """
    用于生成HTML的具体处理程序.

    HTMLRenderer内的方法都可以通过父类的start(), end() 和 sub() 方法来访问.
    实现了用于HTML文档的基本标签.
    """
    def start_document(self):
        print '<html><head><title>...</title></head><body>'

    def end_document(self):
        print '</body></html>'

    def start_paragraph(self):
        print '<p>'

    def end_paragraph(self):
        print '</p>'

    def start_heading(self):
        print '<h2>'

    def end_heading(self):
        print '</h2>'

    def start_list(self):
        print '<ul>'

    def end_list(self):
        print '</ul>'

    def start_listitem(self):
        print '<li>'

    def end_listitem(self):
        print '</li>'

    def start_title(self):
        print '<h1>'

    def end_title(self):
        print '</h1>'

    def sub_emphasis(self, match):
        return '<em>{}</em>'.format(match.group(1))

    def sub_url(self, match):
        return '<a href="{0}">{0}</a>'.format(match.group(1))

    def sub_email(self, match):
        return '<a href="mailto:{0}">{0}</a>'.format(match.group(1))

    def feed(self, data):
        print data
