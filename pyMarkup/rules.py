# coding=utf-8


class Rule(object):
    """
    基础规则类
    """

    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block)
        handler.end(self.type)
        return True


class HeadingRule(Rule):
    """
    标题规则类
    """

    type = 'heading'

    def condition(self, block):
        return not '\n' in block and len(block) <= 70 and not block[-1] == ':'


class TitleRule(Rule):
    """
    文档名称规则类
    """

    type = 'title'
    first = True

    def condition(self, block):
        if not self.first:
            return False

        self.first = False
        return HeadingRule.condition(self, block)


class ListItemRule(Rule):
    """
    列表项规则类
    """

    type = 'listitem'

    def condition(self, block):
        return block[0] == '-'

    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block[1:].strip())
        handler.end(self.type)
        return True


class ListRule(Rule):
    """
    列表规则类
    """

    type = 'list'
    inside = False

    def condition(self, block):
        return True

    def action(self, block, handler):
        if not self.inside and ListItemRule.condition(self, block):
            handler.start(self.type)
            self.inside = True
        elif self.inside and not ListItemRule.condition(self, block):
            handler.end(self.type)
            self.inside = False
        return False


class ParagraphRule(Rule):
    """
    段落规则类
    """

    type = 'paragraph'

    def condition(self, block):
        return True
