#!/usr/bin/env python
# coding=UTF-8
#
# Generated by pykdeuic4 from enginesettings.ui on Sun Mar  4 11:39:39 2012
#
# WARNING! All changes to this file will be lost.
from PyKDE4 import kdecore
from PyKDE4 import kdeui
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 300)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.folderLabel = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.folderLabel.sizePolicy().hasHeightForWidth())
        self.folderLabel.setSizePolicy(sizePolicy)
        self.folderLabel.setObjectName(_fromUtf8("folderLabel"))
        self.horizontalLayout.addWidget(self.folderLabel)
        self.browseButton = QtGui.QPushButton(self.groupBox)
        self.browseButton.setObjectName(_fromUtf8("browseButton"))
        self.horizontalLayout.addWidget(self.browseButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.groupBox)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(kdecore.i18n(_fromUtf8("Form")))
        self.groupBox.setTitle(kdecore.i18n(_fromUtf8("User Module Folder")))
        self.label.setText(kdecore.i18n(_fromUtf8("Any Python modules placed in this folder will be available for import by scripts.")))
        ### TODO                                                                _____  where is  "this" ???                                      
        
        self.folderLabel.setText(kdecore.i18n(_fromUtf8("None selected")))
        self.browseButton.setText(kdecore.i18n(_fromUtf8("Browse")))

