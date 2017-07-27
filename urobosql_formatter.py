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

    """SQL format command class"""

    def run(self, edit, sync=False):
        view = self.view
        view.window().status_message('formatting...')
        self.settings = view.settings()
        self.user_settings = sublime.load_settings(
            'sublime-uroborosql-formatter.sublime-settings')
        # set syntax
        if self.settings.get('syntax') == \
                "Packages/Text/Plain text.tmLanguage":
            view.set_syntax_file("Packages/SQL/SQL.tmLanguage")
        # setting
        self.settings.set("tab_size", self.getval("uf_tab_size"))
        self.settings.set("translate_tabs_to_spaces",
                          self.getval("uf_translate_tabs_to_spaces"))

        config = LocalConfig()
        config.set_case(self.getval("uf_case"))
        config.set_reserved_case(self.getval("uf_reserved_case"))
        # set reserved words
        input_reserved_words_list = self.getval("uf_reserved_words")
        reserved_words = input_reserved_words_list.split(",").lower()
        config.set_input_reserved_words(reserved_words)

        uroborosqlfmt.config.glb.escape_sequence_u005c = self.getval(
            "uf_escapesequence_u005c")
        if str(self.getval("uf_comment_syntax")).upper() == "DOMA2":
            config.set_commentsyntax(Doma2CommentSyntax())

        raw_text = ""
        regions = view.sel()
        # format selection
        if len(regions) > 1 or not regions[0].empty():
            for region in view.sel():
                if not region.empty():
                    raw_text = view.substr(region)
        else:  # format all
            region = sublime.Region(0, view.size())
            raw_text = view.substr(region)

        if sync:
            self.run_format(edit, raw_text, config, region.a, region.b)
        else:
            threading.Thread(target=self.run_format, args=(
                edit, raw_text, config, region.a, region.b)).start()

    def run_format(self, edit, raw_text, config, region_a, region_b):
        formatted_text = uroborosqlfmt.format_sql(raw_text, config)
        self.view.run_command("uroborosql_format_replace", {
            "region_a": region_a,
            "region_b": region_b,
            "formatted_text": formatted_text
        })

    def getval(self, key):
        val = self.user_settings.get(key)
        return val if val != None else self.settings.get(key)


class UroborosqlFormatReplaceCommand(sublime_plugin.TextCommand):

    """SQL format replace command class"""

    def run(self, edit, **args):
        region = sublime.Region(args["region_a"], args["region_b"])
        self.view.replace(edit, region, args["formatted_text"])
        self.view.window().status_message('formatting... complete!!')


class UroborosqlFormatListener(sublime_plugin.EventListener):

    """Event listner"""

    def on_pre_save(self, view):
        self.settings = view.settings()
        self.user_settings = sublime.load_settings(
            'sublime-uroborosql-formatter.sublime-settings')
        if self.getval("uf_save_on_format") != True:
            return

        filepath = view.file_name()
        if filepath.endswith(tuple(self.getval("uf_save_on_format_extensions"))):
            view.run_command("uroborosql_format", {"sync": True})

    def getval(self, key):
        val = self.user_settings.get(key)
        return val if val != None else self.settings.get(key)
