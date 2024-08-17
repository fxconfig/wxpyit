# coding: utf-8

class Article(object):
    def __init__(self):
        """
        公众号推送中的单篇文章内容 (一次可推送多篇)
        """

        # 标题
        self.title = None
        # 摘要
        self.summary = None
        # 文章 URL
        self.url = None
        # 封面图片 URL
        self.cover = None

    def __repr__(self):
        return self.__unicode__()

    def __unicode__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.title)

    def __hash__(self):
        return hash((Article, self.url))

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __cmp__(self, other):
        if hash(self) == hash(other):
            return 0
        return 1
