# PDF to EPUB (EPUBTurn) calibre plugin
# Copyright (C) 2026 The Good Pixel
# License: GNU GPL v3 or later. See LICENSE.

from qt.core import QFormLayout, QLabel, QLineEdit, QWidget

from calibre.utils.config import JSONConfig

DEFAULT_SERVER = 'https://epubturn.com'

prefs = JSONConfig('plugins/epubturn')
prefs.defaults['server_url'] = DEFAULT_SERVER
# The plugin token is stored here once sign-in exists. It never holds a password.
prefs.defaults['token'] = ''
prefs.defaults['account_email'] = ''


def server_url():
    value = (prefs['server_url'] or DEFAULT_SERVER).strip().rstrip('/')
    return value if value.startswith('https://') else DEFAULT_SERVER


class ConfigWidget(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        layout = QFormLayout(self)
        email = prefs['account_email']
        self.account = QLabel(email if email else 'Not signed in. The free sample works without an account.')
        layout.addRow('Account:', self.account)
        self.server = QLineEdit(self)
        self.server.setText(prefs['server_url'])
        self.server.setToolTip('Leave as https://epubturn.com unless EPUBTurn support asks you to change it.')
        layout.addRow('Server:', self.server)

    def save_settings(self):
        value = self.server.text().strip().rstrip('/')
        prefs['server_url'] = value if value.startswith('https://') else DEFAULT_SERVER
