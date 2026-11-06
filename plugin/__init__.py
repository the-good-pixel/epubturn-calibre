# PDF to EPUB (EPUBTurn) calibre plugin
# Copyright (C) 2026 The Good Pixel
# License: GNU GPL v3 or later. See LICENSE.

from calibre.customize import InterfaceActionBase


class EPUBTurnPlugin(InterfaceActionBase):
    name = 'PDF to EPUB (EPUBTurn)'
    description = ('Convert PDFs, including scanned books, into reflowable EPUBs '
                   'without leaving calibre. Free sample, then pay per page.')
    supported_platforms = ['windows', 'osx', 'linux']
    author = 'The Good Pixel'
    version = (0, 1, 0)
    minimum_calibre_version = (6, 0, 0)

    actual_plugin = 'calibre_plugins.epubturn.action:EPUBTurnAction'

    def is_customizable(self):
        return True

    def config_widget(self):
        from calibre_plugins.epubturn.config import ConfigWidget
        return ConfigWidget()

    def save_settings(self, config_widget):
        config_widget.save_settings()
        action = self.actual_plugin_
        if action is not None:
            action.settings_changed()
