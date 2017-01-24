# -*- coding: utf-8 -*-
import os
import sys
import sublime
import sublime_plugin
import threading
sys.path.append(os.path.dirname(__file__))
import uroborosqlfmt
from uroborosqlfmt.config import LocalConfig
from uroborosqlfmt.commentsyntax import Doma2CommentSyntax


class UroborosqlFormatCommand(sublime_plugin.TextCommand):
    """SQL Format Command class"""

    def run(self, edit):
        view = self.view
        self.settings = view.settings()
        self.user_settings = sublime.load_settings(
            'sublime-uroborosql-formatter.sublime-settings')
        regions = view.sel()
        # set syntax
        if self.settings.get('syntax') == \
                "Packages/Text/Plain text.tmLanguage":
            view.set_syntax_file("Packages/SQL/SQL.tmLanguage")
        # setting
        self.settings.set("tab_size", self.getval("uf_tab_size"))
        self.settings.set("translate_tabs_to_spaces",
                          self.getval("uf_translate_tabs_to_spaces"))

        config = LocalConfig()
        config.set_uppercase(self.getval("uf_uppercase"))
        uroborosqlfmt.config.glb.escape_sequence_u005c = self.getval("uf_escapesequence_u005c")
        if str(self.getval("uf_comment_syntax")).upper() == "DOMA2":
            config.set_commentsyntax(Doma2CommentSyntax())

        # format selection
        if len(regions) > 1 or not regions[0].empty():
            for region in view.sel():
                if not region.empty():
                    raw_text = view.substr(region)
                    formatted_text = self.format(raw_text, config)
                    view.replace(edit, region, formatted_text)
        else:  # format all
            allregion = sublime.Region(0, view.size())
            raw_text = view.substr(allregion)
            formatted_text = self.format(raw_text, config)
            view.replace(edit, allregion, formatted_text)

    def format(self, raw_text, config):
        return uroborosqlfmt.format_sql(raw_text, config)

    def getval(self, key):
        val = self.user_settings.get(key)
        return val if val != None else self.settings.get(key)
