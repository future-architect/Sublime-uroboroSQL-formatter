# coding:utf-8
'''
@author: ota
'''
from sqlformatter.commentsyntax import UroboroSqlCommentSyntax


class _GlobalConfig(object):
    def __init__(self):
        self.escape_sequence_u005c = False # バックスラッシュによるエスケープシーケンス

class LocalConfig(object):

    __slots__ = ('comment_syntax')

    def __init__(self):
        self.comment_syntax = UroboroSqlCommentSyntax()

    def set_commentsyntax(self, comment_syntax):
        self.comment_syntax = comment_syntax
        return self


# グローバル設定
glb = _GlobalConfig() # pylint: disable=invalid-name
