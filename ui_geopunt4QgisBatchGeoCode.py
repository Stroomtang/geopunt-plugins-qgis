# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_geopunt4QgisBatchGeoCode.ui'
#
# Created: Wed Nov 12 21:16:14 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_batchGeocodeDlg(object):
    def setupUi(self, batchGeocodeDlg):
        batchGeocodeDlg.setObjectName(_fromUtf8("batchGeocodeDlg"))
        batchGeocodeDlg.resize(579, 485)
        batchGeocodeDlg.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/geopunt4Qgis/images/geopuntBatchgeocodeSmall.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        batchGeocodeDlg.setWindowIcon(icon)
        batchGeocodeDlg.setWindowOpacity(1.0)
        batchGeocodeDlg.setSizeGripEnabled(False)
        self.verticalLayout = QtGui.QVBoxLayout(batchGeocodeDlg)
        self.verticalLayout.setContentsMargins(-1, -1, -1, 2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.inputWgt = QtGui.QWidget(batchGeocodeDlg)
        self.inputWgt.setObjectName(_fromUtf8("inputWgt"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.inputWgt)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.inputTxt = QtGui.QLineEdit(self.inputWgt)
        self.inputTxt.setEnabled(True)
        self.inputTxt.setMinimumSize(QtCore.QSize(200, 0))
        self.inputTxt.setObjectName(_fromUtf8("inputTxt"))
        self.horizontalLayout.addWidget(self.inputTxt)
        self.inputBtn = QtGui.QPushButton(self.inputWgt)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputBtn.sizePolicy().hasHeightForWidth())
        self.inputBtn.setSizePolicy(sizePolicy)
        self.inputBtn.setAutoDefault(False)
        self.inputBtn.setDefault(False)
        self.inputBtn.setFlat(False)
        self.inputBtn.setObjectName(_fromUtf8("inputBtn"))
        self.horizontalLayout.addWidget(self.inputBtn)
        self.codecBox = QtGui.QComboBox(self.inputWgt)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.codecBox.sizePolicy().hasHeightForWidth())
        self.codecBox.setSizePolicy(sizePolicy)
        self.codecBox.setObjectName(_fromUtf8("codecBox"))
        self.codecBox.addItem(_fromUtf8(""))
        self.codecBox.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.codecBox)
        self.verticalLayout.addWidget(self.inputWgt)
        self.delimWgt = QtGui.QWidget(batchGeocodeDlg)
        self.delimWgt.setObjectName(_fromUtf8("delimWgt"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.delimWgt)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_1 = QtGui.QLabel(self.delimWgt)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_1.sizePolicy().hasHeightForWidth())
        self.label_1.setSizePolicy(sizePolicy)
        self.label_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_1.setObjectName(_fromUtf8("label_1"))
        self.horizontalLayout_2.addWidget(self.label_1)
        self.delimSelect = QtGui.QComboBox(self.delimWgt)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delimSelect.sizePolicy().hasHeightForWidth())
        self.delimSelect.setSizePolicy(sizePolicy)
        self.delimSelect.setObjectName(_fromUtf8("delimSelect"))
        self.delimSelect.addItem(_fromUtf8(""))
        self.delimSelect.addItem(_fromUtf8(""))
        self.delimSelect.addItem(_fromUtf8(""))
        self.delimSelect.addItem(_fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.delimSelect)
        self.delimEdit = QtGui.QLineEdit(self.delimWgt)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delimEdit.sizePolicy().hasHeightForWidth())
        self.delimEdit.setSizePolicy(sizePolicy)
        self.delimEdit.setMaximumSize(QtCore.QSize(50, 16777215))
        self.delimEdit.setText(_fromUtf8(""))
        self.delimEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.delimEdit.setObjectName(_fromUtf8("delimEdit"))
        self.horizontalLayout_2.addWidget(self.delimEdit)
        self.verticalLayout.addWidget(self.delimWgt)
        self.adresWgt = QtGui.QWidget(batchGeocodeDlg)
        self.adresWgt.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.adresWgt.sizePolicy().hasHeightForWidth())
        self.adresWgt.setSizePolicy(sizePolicy)
        self.adresWgt.setObjectName(_fromUtf8("adresWgt"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.adresWgt)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.chooseWgt = QtGui.QHBoxLayout()
        self.chooseWgt.setObjectName(_fromUtf8("chooseWgt"))
        self.multipleColChk = QtGui.QRadioButton(self.adresWgt)
        self.multipleColChk.setChecked(True)
        self.multipleColChk.setObjectName(_fromUtf8("multipleColChk"))
        self.chooseWgt.addWidget(self.multipleColChk)
        self.singleLineChk = QtGui.QRadioButton(self.adresWgt)
        self.singleLineChk.setObjectName(_fromUtf8("singleLineChk"))
        self.chooseWgt.addWidget(self.singleLineChk)
        self.verticalLayout_2.addLayout(self.chooseWgt)
        self.adresChooseWgt = QtGui.QWidget(self.adresWgt)
        self.adresChooseWgt.setObjectName(_fromUtf8("adresChooseWgt"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.adresChooseWgt)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.adresColLbl = QtGui.QLabel(self.adresChooseWgt)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.adresColLbl.sizePolicy().hasHeightForWidth())
        self.adresColLbl.setSizePolicy(sizePolicy)
        self.adresColLbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.adresColLbl.setObjectName(_fromUtf8("adresColLbl"))
        self.horizontalLayout_4.addWidget(self.adresColLbl)
        self.adresColSelect = QtGui.QComboBox(self.adresChooseWgt)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.adresColSelect.sizePolicy().hasHeightForWidth())
        self.adresColSelect.setSizePolicy(sizePolicy)
        self.adresColSelect.setObjectName(_fromUtf8("adresColSelect"))
        self.horizontalLayout_4.addWidget(self.adresColSelect)
        self.verticalLayout_2.addWidget(self.adresChooseWgt)
        self.huisnrChooseWgt = QtGui.QWidget(self.adresWgt)
        self.huisnrChooseWgt.setObjectName(_fromUtf8("huisnrChooseWgt"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.huisnrChooseWgt)
        self.horizontalLayout_6.setMargin(0)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.huisnrLbl = QtGui.QLabel(self.huisnrChooseWgt)
        self.huisnrLbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.huisnrLbl.setObjectName(_fromUtf8("huisnrLbl"))
        self.horizontalLayout_6.addWidget(self.huisnrLbl)
        self.huisnrSelect = QtGui.QComboBox(self.huisnrChooseWgt)
        self.huisnrSelect.setObjectName(_fromUtf8("huisnrSelect"))
        self.horizontalLayout_6.addWidget(self.huisnrSelect)
        self.verticalLayout_2.addWidget(self.huisnrChooseWgt)
        self.gemeenteChooseWgt = QtGui.QWidget(self.adresWgt)
        self.gemeenteChooseWgt.setObjectName(_fromUtf8("gemeenteChooseWgt"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.gemeenteChooseWgt)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.gemeenteColLbl = QtGui.QLabel(self.gemeenteChooseWgt)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gemeenteColLbl.sizePolicy().hasHeightForWidth())
        self.gemeenteColLbl.setSizePolicy(sizePolicy)
        self.gemeenteColLbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.gemeenteColLbl.setObjectName(_fromUtf8("gemeenteColLbl"))
        self.horizontalLayout_3.addWidget(self.gemeenteColLbl)
        self.gemeenteColSelect = QtGui.QComboBox(self.gemeenteChooseWgt)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gemeenteColSelect.sizePolicy().hasHeightForWidth())
        self.gemeenteColSelect.setSizePolicy(sizePolicy)
        self.gemeenteColSelect.setObjectName(_fromUtf8("gemeenteColSelect"))
        self.horizontalLayout_3.addWidget(self.gemeenteColSelect)
        self.verticalLayout_2.addWidget(self.gemeenteChooseWgt)
        self.verticalLayout.addWidget(self.adresWgt)
        self.tlFrame = QtGui.QFrame(batchGeocodeDlg)
        self.tlFrame.setFrameShape(QtGui.QFrame.NoFrame)
        self.tlFrame.setFrameShadow(QtGui.QFrame.Plain)
        self.tlFrame.setObjectName(_fromUtf8("tlFrame"))
        self.gridLayout = QtGui.QGridLayout(self.tlFrame)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.zoomToSelBtn = QtGui.QPushButton(self.tlFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zoomToSelBtn.sizePolicy().hasHeightForWidth())
        self.zoomToSelBtn.setSizePolicy(sizePolicy)
        self.zoomToSelBtn.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/geopunt4Qgis/images/binocularsSmall.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoomToSelBtn.setIcon(icon1)
        self.zoomToSelBtn.setAutoDefault(False)
        self.zoomToSelBtn.setDefault(True)
        self.zoomToSelBtn.setObjectName(_fromUtf8("zoomToSelBtn"))
        self.gridLayout.addWidget(self.zoomToSelBtn, 2, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 1, 1, 1)
        self.validateSelBtn = QtGui.QPushButton(self.tlFrame)
        self.validateSelBtn.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/geopunt4Qgis/images/select.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.validateSelBtn.setIcon(icon2)
        self.validateSelBtn.setAutoDefault(False)
        self.validateSelBtn.setObjectName(_fromUtf8("validateSelBtn"))
        self.gridLayout.addWidget(self.validateSelBtn, 1, 1, 1, 1)
        self.validateBtn = QtGui.QPushButton(self.tlFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.validateBtn.sizePolicy().hasHeightForWidth())
        self.validateBtn.setSizePolicy(sizePolicy)
        self.validateBtn.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/geopunt4Qgis/images/validAll.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.validateBtn.setIcon(icon3)
        self.validateBtn.setAutoDefault(False)
        self.validateBtn.setObjectName(_fromUtf8("validateBtn"))
        self.gridLayout.addWidget(self.validateBtn, 0, 1, 1, 1)
        self.outPutTbl = QtGui.QTableWidget(self.tlFrame)
        self.outPutTbl.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.outPutTbl.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.outPutTbl.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.outPutTbl.setObjectName(_fromUtf8("outPutTbl"))
        self.outPutTbl.setColumnCount(0)
        self.outPutTbl.setRowCount(0)
        self.gridLayout.addWidget(self.outPutTbl, 0, 0, 6, 1)
        self.adresFromMapBtn = QtGui.QPushButton(self.tlFrame)
        self.adresFromMapBtn.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/geopunt4Qgis/images/prik.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.adresFromMapBtn.setIcon(icon4)
        self.adresFromMapBtn.setAutoDefault(False)
        self.adresFromMapBtn.setObjectName(_fromUtf8("adresFromMapBtn"))
        self.gridLayout.addWidget(self.adresFromMapBtn, 3, 1, 1, 1)
        self.verticalLayout.addWidget(self.tlFrame)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.addToMapKnop = QtGui.QPushButton(batchGeocodeDlg)
        self.addToMapKnop.setEnabled(False)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/geopunt4Qgis/images/addPointLayer.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addToMapKnop.setIcon(icon5)
        self.addToMapKnop.setCheckable(False)
        self.addToMapKnop.setAutoDefault(False)
        self.addToMapKnop.setDefault(False)
        self.addToMapKnop.setFlat(False)
        self.addToMapKnop.setObjectName(_fromUtf8("addToMapKnop"))
        self.horizontalLayout_9.addWidget(self.addToMapKnop)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem1)
        self.buttonBox = QtGui.QDialogButtonBox(batchGeocodeDlg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Help)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout_9.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.line = QtGui.QFrame(batchGeocodeDlg)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.statusBar = QtGui.QWidget(batchGeocodeDlg)
        self.statusBar.setAutoFillBackground(False)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.statusBar)
        self.horizontalLayout_8.setMargin(0)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.statusMsg = QtGui.QLabel(self.statusBar)
        self.statusMsg.setFrameShape(QtGui.QFrame.Panel)
        self.statusMsg.setFrameShadow(QtGui.QFrame.Sunken)
        self.statusMsg.setText(_fromUtf8(""))
        self.statusMsg.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.statusMsg.setObjectName(_fromUtf8("statusMsg"))
        self.horizontalLayout_8.addWidget(self.statusMsg)
        self.statusProgress = QtGui.QProgressBar(self.statusBar)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusProgress.sizePolicy().hasHeightForWidth())
        self.statusProgress.setSizePolicy(sizePolicy)
        self.statusProgress.setMinimumSize(QtCore.QSize(200, 0))
        self.statusProgress.setMaximum(10)
        self.statusProgress.setProperty("value", 0)
        self.statusProgress.setTextVisible(True)
        self.statusProgress.setInvertedAppearance(False)
        self.statusProgress.setTextDirection(QtGui.QProgressBar.TopToBottom)
        self.statusProgress.setObjectName(_fromUtf8("statusProgress"))
        self.horizontalLayout_8.addWidget(self.statusProgress)
        self.verticalLayout.addWidget(self.statusBar)
        self.laraLbl = QtGui.QLabel(batchGeocodeDlg)
        self.laraLbl.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.laraLbl.setMargin(-1)
        self.laraLbl.setOpenExternalLinks(True)
        self.laraLbl.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse)
        self.laraLbl.setObjectName(_fromUtf8("laraLbl"))
        self.verticalLayout.addWidget(self.laraLbl)
        self.actionAddValidToMap = QtGui.QAction(batchGeocodeDlg)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/geopunt4Qgis/images/qgis-icon-16x16.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAddValidToMap.setIcon(icon6)
        self.actionAddValidToMap.setObjectName(_fromUtf8("actionAddValidToMap"))
        self.actionValidateSelection = QtGui.QAction(batchGeocodeDlg)
        self.actionValidateSelection.setIcon(icon2)
        self.actionValidateSelection.setObjectName(_fromUtf8("actionValidateSelection"))
        self.actionValidateAll = QtGui.QAction(batchGeocodeDlg)
        self.actionValidateAll.setIcon(icon3)
        self.actionValidateAll.setObjectName(_fromUtf8("actionValidateAll"))
        self.actionZoomToSelection = QtGui.QAction(batchGeocodeDlg)
        self.actionZoomToSelection.setIcon(icon1)
        self.actionZoomToSelection.setObjectName(_fromUtf8("actionZoomToSelection"))
        self.adresFromMapAction = QtGui.QAction(batchGeocodeDlg)
        self.adresFromMapAction.setIcon(icon4)
        self.adresFromMapAction.setObjectName(_fromUtf8("adresFromMapAction"))
        self.label_1.setBuddy(self.delimSelect)

        self.retranslateUi(batchGeocodeDlg)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), batchGeocodeDlg.reject)
        QtCore.QObject.connect(self.zoomToSelBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.actionZoomToSelection.trigger)
        QtCore.QObject.connect(self.singleLineChk, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.gemeenteChooseWgt.setHidden)
        QtCore.QObject.connect(self.singleLineChk, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.huisnrChooseWgt.setHidden)
        QtCore.QMetaObject.connectSlotsByName(batchGeocodeDlg)

    def retranslateUi(self, batchGeocodeDlg):
        batchGeocodeDlg.setWindowTitle(_translate("batchGeocodeDlg", "CSV-adresbestanden geocoderen", None))
        self.inputBtn.setText(_translate("batchGeocodeDlg", "Open", None))
        self.codecBox.setItemText(0, _translate("batchGeocodeDlg", "ansi", None))
        self.codecBox.setItemText(1, _translate("batchGeocodeDlg", "utf-8", None))
        self.label_1.setText(_translate("batchGeocodeDlg", "Separator: ", None))
        self.delimSelect.setItemText(0, _translate("batchGeocodeDlg", "Puntcomma", None))
        self.delimSelect.setItemText(1, _translate("batchGeocodeDlg", "Comma", None))
        self.delimSelect.setItemText(2, _translate("batchGeocodeDlg", "Tab", None))
        self.delimSelect.setItemText(3, _translate("batchGeocodeDlg", "Ander: ", None))
        self.multipleColChk.setText(_translate("batchGeocodeDlg", "Adres in meerdere kolommen", None))
        self.singleLineChk.setText(_translate("batchGeocodeDlg", "Volledig adres in 1 kolom", None))
        self.adresColLbl.setText(_translate("batchGeocodeDlg", "Straatnaam kolom:", None))
        self.huisnrLbl.setText(_translate("batchGeocodeDlg", "(Optioneel) Huisnummer kolom: ", None))
        self.gemeenteColLbl.setText(_translate("batchGeocodeDlg", "Gemeente of postcode kolom:", None))
        self.zoomToSelBtn.setToolTip(_translate("batchGeocodeDlg", "Zoom naar selectie", None))
        self.validateSelBtn.setToolTip(_translate("batchGeocodeDlg", "Valideer selectie", None))
        self.validateBtn.setToolTip(_translate("batchGeocodeDlg", "Valideer alle adressen", None))
        self.outPutTbl.setSortingEnabled(True)
        self.adresFromMapBtn.setToolTip(_translate("batchGeocodeDlg", "Prik locatie op kaart", None))
        self.addToMapKnop.setText(_translate("batchGeocodeDlg", "Voeg alle gevalideerde adressen toe aan de kaart", None))
        self.laraLbl.setText(_translate("batchGeocodeDlg", "<small><a href=\"http://crab.agiv.be/Lara\">Foute adressen kunt u melden via LARA</a></small>", None))
        self.actionAddValidToMap.setText(_translate("batchGeocodeDlg", "Voeg alle valide adressen toe aan de kaart", None))
        self.actionValidateSelection.setText(_translate("batchGeocodeDlg", "Valideer selectie", None))
        self.actionValidateAll.setText(_translate("batchGeocodeDlg", "Valideer alle Adressen", None))
        self.actionZoomToSelection.setText(_translate("batchGeocodeDlg", "Zoom naar selectie", None))
        self.adresFromMapAction.setText(_translate("batchGeocodeDlg", "Prik locatie op Kaart", None))
        self.adresFromMapAction.setToolTip(_translate("batchGeocodeDlg", "Prik locatie op Kaart", None))

import resources_rc
