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

        raw_text = ""
        region = None

        # format selection
        if len(regions) > 1 or not regions[0].empty():
            for region in view.sel():
                if not region.empty():
                    raw_text = view.substr(region)
        else:  # format all
            region = sublime.Region(0, view.size())
            raw_text = view.substr(region)

        threading.Thread(target=self.run_format, args=(edit, raw_text, region, config, )).start()

    def run_format(self, edit, raw_text, region, config):
        formatted_text = uroborosqlfmt.format_sql(raw_text, config)
        self.view.run_command("uroborosql_format_view", {"formatted_text": formatted_text})

    def getval(self, key):
        val = self.user_settings.get(key)
        return val if val != None else self.settings.get(key)


class UroborosqlFormatViewCommand(sublime_plugin.TextCommand):
    def run(self, edit, **args):
        regions = self.view.sel()
        # format selection
        if len(regions) > 1 or not regions[0].empty():
            for region in self.view.sel():
                if not region.empty():
                    break
        else:  # format all
            region = sublime.Region(0, self.view.size())

        self.view.replace(edit, region, args["formatted_text"])
