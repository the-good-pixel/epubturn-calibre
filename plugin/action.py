# PDF to EPUB (EPUBTurn) calibre plugin
# Copyright (C) 2026 The Good Pixel
# License: GNU GPL v3 or later. See LICENSE.

from qt.core import QIcon, QMenu, QUrl

from calibre.gui2 import error_dialog, info_dialog, open_url
from calibre.gui2.actions import InterfaceAction

from calibre_plugins.epubturn.config import server_url


class EPUBTurnAction(InterfaceAction):
    name = 'PDF to EPUB (EPUBTurn)'
    action_spec = ('Convert PDF to EPUB', None,
                   'Convert the selected book\'s PDF into an EPUB with EPUBTurn', None)
    action_type = 'current'
    dont_add_to = frozenset(['context-menu-device'])

    def genesis(self):
        self.qaction.setIcon(QIcon.ic('convert.png'))
        self.qaction.triggered.connect(self.convert_selected)
        self.menu = QMenu(self.gui)
        self.menu.addAction('Convert PDF to EPUB', self.convert_selected)
        self.menu.addSeparator()
        self.menu.addAction('Help', lambda: self.open_site('/resources/'))
        self.menu.addAction('Settings', self.show_settings)
        self.qaction.setMenu(self.menu)

    def settings_changed(self):
        pass

    def show_settings(self):
        self.interface_action_base_plugin.do_user_config(self.gui)

    def open_site(self, path):
        open_url(QUrl(server_url() + path))

    def selected_pdf(self):
        """Return (book_id, title, pdf_path) for the one selected book, or show why not."""
        rows = self.gui.library_view.selectionModel().selectedRows()
        if len(rows) != 1:
            error_dialog(self.gui, 'Select one book',
                         'Select one book that has a PDF, then try again.', show=True)
            return None
        book_id = self.gui.library_view.model().id(rows[0])
        db = self.gui.current_db.new_api
        if 'PDF' not in (db.formats(book_id) or ()):
            error_dialog(self.gui, 'No PDF in this book',
                         'This book has no PDF format. Add a PDF to the book, then try again.',
                         show=True)
            return None
        return book_id, db.field_for('title', book_id), db.format_abspath(book_id, 'PDF')

    def convert_selected(self):
        selected = self.selected_pdf()
        if selected is None:
            return
        _, title, _ = selected
        # Upload, sample and full conversion are built in the next steps.
        info_dialog(self.gui, 'PDF to EPUB (EPUBTurn)',
                    f'"{title}" is ready to convert. Conversion is not available in this '
                    'early version of the plugin yet.', show=True)
