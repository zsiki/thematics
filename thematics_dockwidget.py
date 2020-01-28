# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ThematicsDockWidget
                                 A QGIS plugin
 open projects and layer groups from list
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2020-01-19
        git sha              : $Format:%H$
        copyright            : (C) 2020 by Zoltan Siki
        email                : siki1958@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from qgis.PyQt import QtGui, QtWidgets, uic
from qgis.PyQt.QtCore import pyqtSignal

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'thematics_dockwidget_base.ui'))

class ThematicsDockWidget(QtWidgets.QDockWidget, FORM_CLASS):

    closingPlugin = pyqtSignal()

    def __init__(self, plugin, parent=None):
        """Constructor."""
        super(ThematicsDockWidget, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://doc.qt.io/qt-5/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        self.plugin = plugin    # for call backs if button pressed
        self.project_button.clicked.connect(self.project)
        self.list_projects.itemDoubleClicked.connect(self.project)
        self.layer_button.clicked.connect(self.layer)
        self.list_layers.itemDoubleClicked.connect(self.layer)
        self.remove_layer_button.clicked.connect(self.remove_layer)

    def project(self):
        i = self.list_projects.currentItem()
        if i:
            self.plugin.open_project(i.text(), self.newwin_check.isChecked())

    def layer(self):
        i = self.list_layers.currentItem()
        if i:
            self.plugin.open_layer_group(i.text())

    def remove_layer(self):
        i = self.list_layers.currentItem()
        if i:
            self.plugin.remove_layer_group(i.text())

    def closeEvent(self, event):
        self.closingPlugin.emit()
        event.accept()
