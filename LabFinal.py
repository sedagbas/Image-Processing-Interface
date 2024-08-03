path = "d:/sedat/Desktop/151220192063_SedatAgbas_LabFinal/Icons/"

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel


class Ui_LabFinal(object):
    def __init__(self):
        super().__init__()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("LabFinal")
        MainWindow.resize(1375, 561)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.widget = QtWidgets.QWidget(MainWindow)
        self.widget.setObjectName("widget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.window = QtWidgets.QGridLayout()
        self.window.setObjectName("window")
        self.output = QtWidgets.QGroupBox(self.widget)
        self.output.setMinimumSize(QtCore.QSize(500, 500))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.output.setFont(font)
        self.output.setObjectName("output")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.output)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_output = QtWidgets.QFrame(self.output)
        self.frame_output.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_output.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_output.setObjectName("frame_output")
        self.gridLayout_2.addWidget(self.frame_output, 0, 0, 1, 1)
        self.window.addWidget(self.output, 0, 1, 1, 1)
        self.source = QtWidgets.QGroupBox(self.widget)
        self.source.setMinimumSize(QtCore.QSize(500, 500))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.source.setFont(font)
        self.source.setObjectName("source")
        self.gridLayout = QtWidgets.QGridLayout(self.source)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_source = QtWidgets.QFrame(self.source)
        self.frame_source.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_source.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_source.setObjectName("frame_source")
        self.gridLayout.addWidget(self.frame_source, 0, 0, 1, 1)
        self.window.addWidget(self.source, 0, 0, 1, 1)
        self.properties = QtWidgets.QGroupBox(self.widget)
        self.properties.setMinimumSize(QtCore.QSize(250, 250))
        self.properties.setMaximumSize(QtCore.QSize(250, 389))
        self.properties.setObjectName("properties")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.properties)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.segmentation = QtWidgets.QGroupBox(self.properties)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.segmentation.setFont(font)
        self.segmentation.setObjectName("segmentation")

        # Segmentation buttons
        self.pb_mot = QtWidgets.QPushButton(self.segmentation)
        self.pb_mot.setGeometry(QtCore.QRect(30, 50, 31, 31))
        self.pb_mot.setText("")
        self.pb_mot.setObjectName("pb_mot")
        self.pb_mot.setEnabled(False)

        self.pb_cvs = QtWidgets.QPushButton(self.segmentation)
        self.pb_cvs.setGeometry(QtCore.QRect(90, 50, 31, 31))
        self.pb_cvs.setText("")
        self.pb_cvs.setObjectName("pb_cvs")
        self.pb_cvs.setEnabled(False)

        self.pb_ms = QtWidgets.QPushButton(self.segmentation)
        self.pb_ms.setGeometry(QtCore.QRect(150, 50, 31, 31))
        self.pb_ms.setText("")
        self.pb_ms.setObjectName("pb_ms")
        self.pb_ms.setEnabled(False)

        self.gridLayout_3.addWidget(self.segmentation, 1, 0, 1, 1)

        # Conversion buttons
        self.conversion = QtWidgets.QGroupBox(self.properties)
        self.conversion.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.conversion.setFont(font)
        self.conversion.setObjectName("conversion")

        self.pb_grayscale = QtWidgets.QPushButton(self.conversion)
        self.pb_grayscale.setGeometry(QtCore.QRect(60, 50, 31, 31))
        self.pb_grayscale.setText("")
        self.pb_grayscale.setObjectName("pb_grayscale")
        self.pb_grayscale.setEnabled(False)

        self.pb_hsv = QtWidgets.QPushButton(self.conversion)
        self.pb_hsv.setGeometry(QtCore.QRect(130, 50, 31, 31))
        self.pb_hsv.setText("")
        self.pb_hsv.setObjectName("pb_hsv")
        self.pb_hsv.setEnabled(False)

        self.gridLayout_3.addWidget(self.conversion, 0, 0, 1, 1)

        # Edge detection buttons
        self.edgeDetection = QtWidgets.QGroupBox(self.properties)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.edgeDetection.setFont(font)
        self.edgeDetection.setObjectName("edgeDetection")

        self.pb_roberts = QtWidgets.QPushButton(self.edgeDetection)
        self.pb_roberts.setGeometry(QtCore.QRect(20, 50, 31, 31))
        self.pb_roberts.setText("")
        self.pb_roberts.setObjectName("pb_roberts")
        self.pb_roberts.setEnabled(False)

        self.pb_sobel = QtWidgets.QPushButton(self.edgeDetection)
        self.pb_sobel.setGeometry(QtCore.QRect(70, 50, 31, 31))
        self.pb_sobel.setText("")
        self.pb_sobel.setObjectName("pb_sobel")
        self.pb_sobel.setEnabled(False)

        self.pb_scharr = QtWidgets.QPushButton(self.edgeDetection)
        self.pb_scharr.setGeometry(QtCore.QRect(120, 50, 31, 31))
        self.pb_scharr.setText("")
        self.pb_scharr.setObjectName("pb_scharr")
        self.pb_scharr.setEnabled(False)

        self.pb_prewitt = QtWidgets.QPushButton(self.edgeDetection)
        self.pb_prewitt.setGeometry(QtCore.QRect(170, 50, 31, 31))
        self.pb_prewitt.setText("")
        self.pb_prewitt.setObjectName("pb_prewitt")
        self.pb_prewitt.setEnabled(False)

        self.gridLayout_3.addWidget(self.edgeDetection, 2, 0, 1, 1)
        self.window.addWidget(self.properties, 0, 2, 1, 1)
        self.gridLayout_5.addLayout(self.window, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.widget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1375, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuExport_As = QtWidgets.QMenu(self.menuFile)
        self.menuExport_As.setObjectName("menuExport_As")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuClear = QtWidgets.QMenu(self.menuEdit)
        self.menuClear.setObjectName("menuClear")
        self.menuConversion = QtWidgets.QMenu(self.menubar)
        self.menuConversion.setObjectName("menuConversion")
        self.menuSegmentation = QtWidgets.QMenu(self.menubar)
        self.menuSegmentation.setObjectName("menuSegmentation")
        self.menuEdge_Detection = QtWidgets.QMenu(self.menubar)
        self.menuEdge_Detection.setObjectName("menuEdge_Detection")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar)

        # Actions in menu bar and toolbar
        self.actionOpenSource = QtWidgets.QAction(MainWindow)
        self.actionOpenSource.setObjectName("actionOpenSource")
        self.actionSaveOutput = QtWidgets.QAction(MainWindow)
        self.actionSaveOutput.setEnabled(False)
        self.actionSaveOutput.setObjectName("actionSaveOutput")
        self.actionSaveAsOutput = QtWidgets.QAction(MainWindow)
        self.actionSaveAsOutput.setEnabled(False)
        self.actionSaveAsOutput.setObjectName("actionSaveAsOutput")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExportSource = QtWidgets.QAction(MainWindow)
        self.actionExportSource.setEnabled(False)
        self.actionExportSource.setObjectName("actionExportSource")
        self.actionExportOutput = QtWidgets.QAction(MainWindow)
        self.actionExportOutput.setEnabled(False)
        self.actionExportOutput.setObjectName("actionExportOutput")
        self.actionClearSource = QtWidgets.QAction(MainWindow)
        self.actionClearSource.setEnabled(False)
        self.actionClearSource.setObjectName("actionClearSource")
        self.actionClearOutput = QtWidgets.QAction(MainWindow)
        self.actionClearOutput.setEnabled(False)
        self.actionClearOutput.setObjectName("actionClearOutput")
        self.actionUndoOutput = QtWidgets.QAction(MainWindow)
        self.actionUndoOutput.setEnabled(False)
        self.actionUndoOutput.setObjectName("actionUndoOutput")
        self.actionRedoOutput = QtWidgets.QAction(MainWindow)
        self.actionRedoOutput.setEnabled(False)
        self.actionRedoOutput.setObjectName("actionRedoOutput")
        
        """ Conversion actions """
        self.actionRGBtoGrayscale = QtWidgets.QAction(MainWindow)
        self.actionRGBtoGrayscale.setEnabled(False)
        self.actionRGBtoGrayscale.setObjectName("actionRGBtoGrayscale")
        self.actionRGBtoHSV = QtWidgets.QAction(MainWindow)
        self.actionRGBtoHSV.setEnabled(False)
        self.actionRGBtoHSV.setObjectName("actionRGBtoHSV")
        
        """ Segmentation actions """
        self.actionMultiOtsuThresholding = QtWidgets.QAction(MainWindow)
        self.actionMultiOtsuThresholding.setEnabled(False)
        self.actionMultiOtsuThresholding.setObjectName("actionMultiOtsuThresholding")
        self.actionChanVeseSegmentation = QtWidgets.QAction(MainWindow)
        self.actionChanVeseSegmentation.setEnabled(False)
        self.actionChanVeseSegmentation.setObjectName("actionChanVeseSegmentation")
        self.actionMorphologicalSnakes = QtWidgets.QAction(MainWindow)
        self.actionMorphologicalSnakes.setEnabled(False)
        self.actionMorphologicalSnakes.setObjectName("actionMorphologicalSnakes")
        
        """ Edge detection actions """
        self.actionRoberts = QtWidgets.QAction(MainWindow)
        self.actionRoberts.setEnabled(False)
        self.actionRoberts.setObjectName("actionRoberts")
        self.actionSobel = QtWidgets.QAction(MainWindow)
        self.actionSobel.setEnabled(False)
        self.actionSobel.setObjectName("actionSobel")
        self.actionScharr = QtWidgets.QAction(MainWindow)
        self.actionScharr.setEnabled(False)
        self.actionScharr.setObjectName("actionScharr")
        self.actionPrewitt = QtWidgets.QAction(MainWindow)
        self.actionPrewitt.setEnabled(False)
        self.actionPrewitt.setObjectName("actionPrewitt")
        
        """ Adding actions to menus"""
        self.menuExport_As.addAction(self.actionExportSource)
        self.menuExport_As.addAction(self.actionExportOutput)
        self.menuFile.addAction(self.actionOpenSource)
        self.menuFile.addAction(self.actionSaveOutput)
        self.menuFile.addAction(self.actionSaveAsOutput)
        self.menuFile.addAction(self.menuExport_As.menuAction())
        self.menuFile.addAction(self.actionExit)
        self.menuClear.addAction(self.actionClearSource)
        self.menuClear.addAction(self.actionClearOutput)
        self.menuEdit.addAction(self.menuClear.menuAction())
        self.menuEdit.addAction(self.actionUndoOutput)
        self.menuEdit.addAction(self.actionRedoOutput)
        self.menuConversion.addAction(self.actionRGBtoGrayscale)
        self.menuConversion.addAction(self.actionRGBtoHSV)
        self.menuSegmentation.addAction(self.actionMultiOtsuThresholding)
        self.menuSegmentation.addAction(self.actionChanVeseSegmentation)
        self.menuSegmentation.addAction(self.actionMorphologicalSnakes)
        self.menuEdge_Detection.addAction(self.actionRoberts)
        self.menuEdge_Detection.addAction(self.actionSobel)
        self.menuEdge_Detection.addAction(self.actionScharr)
        self.menuEdge_Detection.addAction(self.actionPrewitt)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuConversion.menuAction())
        self.menubar.addAction(self.menuSegmentation.menuAction())
        self.menubar.addAction(self.menuEdge_Detection.menuAction())
        self.toolBar.addAction(self.actionOpenSource)
        self.toolBar.addAction(self.actionSaveOutput)
        self.toolBar.addAction(self.actionSaveAsOutput)
        self.toolBar.addAction(self.actionUndoOutput)
        self.toolBar.addAction(self.actionRedoOutput)
        
        """ Setting icons for actions and buttons"""
        icon_openSource = MainWindow.style().standardIcon(QtWidgets.QStyle.SP_DirOpenIcon)
        self.actionOpenSource.setIcon(icon_openSource)
        
        icon_saveOutput = MainWindow.style().standardIcon(QtWidgets.QStyle.SP_DialogSaveButton)
        self.actionSaveOutput.setIcon(icon_saveOutput)
        
        icon_saveAs = QtGui.QIcon(path + "save_as.png")
        self.actionSaveAsOutput.setIcon(icon_saveAs)
        
        icon_export = QtGui.QIcon(path + "export.png")
        self.actionExportSource.setIcon(icon_export)
        self.actionExportOutput.setIcon(icon_export)
        
        icon_clear = QtGui.QIcon(path + "clear.png")
        self.actionClearSource.setIcon(icon_clear)
        self.actionClearOutput.setIcon(icon_clear)
        
        icon_undo = QtGui.QIcon(path + "undo.png")
        self.actionUndoOutput.setIcon(icon_undo)
        
        icon_redo = QtGui.QIcon(path + "redo.png")
        self.actionRedoOutput.setIcon(icon_redo)
        
        icon_exit = MainWindow.style().standardIcon(QtWidgets.QStyle.SP_DialogCloseButton)
        self.actionExit.setIcon(icon_exit)
          
        icon_grayscale = QtGui.QIcon(path + "grayscale.png")
        self.pb_grayscale.setIcon(icon_grayscale)
        self.actionRGBtoGrayscale.setIcon(icon_grayscale)
        
        icon_hsv = QtGui.QIcon(path + "hsv.png")
        self.pb_hsv.setIcon(icon_hsv)
        self.actionRGBtoHSV.setIcon(icon_hsv)
        
        icon_mot = QtGui.QIcon(path + "mot.png")
        self.pb_mot.setIcon(icon_mot)
        self.actionMultiOtsuThresholding.setIcon(icon_mot)
        
        icon_cvs = QtGui.QIcon(path + "cvs.png")
        self.pb_cvs.setIcon(icon_cvs)
        self.actionChanVeseSegmentation.setIcon(icon_cvs)
        
        icon_ms = QtGui.QIcon(path + "ms.png")
        self.pb_ms.setIcon(icon_ms)
        self.actionMorphologicalSnakes.setIcon(icon_ms)
        
        icon_roberts = QtGui.QIcon(path + "roberts.png")
        self.pb_roberts.setIcon(icon_roberts)
        self.actionRoberts.setIcon(icon_roberts)
        
        icon_so = QtGui.QIcon(path + "sobel.png")
        self.pb_sobel.setIcon(icon_so)
        self.actionSobel.setIcon(icon_so)
        
        icon_scharr = QtGui.QIcon(path + "scharr.png")
        self.pb_scharr.setIcon(icon_scharr)
        self.actionScharr.setIcon(icon_scharr)
        
        icon_prewitt = QtGui.QIcon(path + "prewitt.png")
        self.pb_prewitt.setIcon(icon_prewitt)
        self.actionPrewitt.setIcon(icon_prewitt)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        """ Connecting actions to their respective functions """
        self.actionOpenSource.triggered.connect(self.open_source)
        self.actionSaveOutput.triggered.connect(self.saveOutput)
        self.actionSaveAsOutput.triggered.connect(self.saveOutput)
        self.actionExit.triggered.connect(self.close_application)
        self.actionExportSource.triggered.connect(self.export)
        self.actionExportOutput.triggered.connect(self.export)
        self.actionClearOutput.triggered.connect(self.clear)
        self.actionClearSource.triggered.connect(self.clear)
        self.actionRedoOutput.triggered.connect(self.redo_output)
        self.actionUndoOutput.triggered.connect(self.undo_output)
        
        self.actionRGBtoGrayscale.triggered.connect(self.rgbToGrayscale)
        self.actionRGBtoHSV.triggered.connect(self.rgbToHsv)
        self.actionMultiOtsuThresholding.triggered.connect(self.multiOtsuThresholding)
        self.actionMorphologicalSnakes.triggered.connect(self.morphologicalSnakes)
        self.actionChanVeseSegmentation.triggered.connect(self.chanVeseSegmentation)
        self.actionRoberts.triggered.connect(self.roberts)
        self.actionSobel.triggered.connect(self.sobel)
        self.actionScharr.triggered.connect(self.scharr)
        self.actionPrewitt.triggered.connect(self.prewitt)
        
        """ Connecting buttons to their respective functions """
        self.pb_grayscale.clicked.connect(self.rgbToGrayscale)
        self.pb_hsv.clicked.connect(self.rgbToHsv)
        self.pb_mot.clicked.connect(self.multiOtsuThresholding)
        self.pb_ms.clicked.connect(self.morphologicalSnakes)
        self.pb_cvs.clicked.connect(self.chanVeseSegmentation)
        self.pb_roberts.clicked.connect(self.roberts)
        self.pb_sobel.clicked.connect(self.sobel)
        self.pb_scharr.clicked.connect(self.scharr)
        self.pb_prewitt.clicked.connect(self.prewitt)
        
        """ Setting up a QLabel to display mouse position in the status bar """
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)
        
        """ Adding a QLabel to display mouse position """
        self.mouse_position_label = QLabel("Mouse Position: (0,0)")
        self.statusbar.addPermanentWidget(self.mouse_position_label)
        
        """ Enabling mouse tracking for frames to update mouse position """
        self.frame_source.setMouseTracking(True)
        self.frame_source.mouseMoveEvent = self.update_mouse_position_source
        self.frame_output.setMouseTracking(True)
        self.frame_output.mouseMoveEvent = self.update_mouse_position_output
                
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    """ This method retranslates the user interface """
    def retranslateUi(self, LabFinal):
        _translate = QtCore.QCoreApplication.translate
        LabFinal.setWindowTitle(_translate("LabFinal", "MainWindow"))
        self.output.setTitle(_translate("LabFinal", "Output"))
        self.source.setTitle(_translate("LabFinal", "Source"))
        self.properties.setTitle(_translate("LabFinal", "Properties"))
        self.segmentation.setTitle(_translate("LabFinal", "Segmentation"))
        self.conversion.setTitle(_translate("LabFinal", "Conversion"))
        self.edgeDetection.setTitle(_translate("LabFinal", "Edge Detection"))
        self.menuFile.setTitle(_translate("LabFinal", "File"))
        self.menuExport_As.setTitle(_translate("LabFinal", "Export As"))
        self.menuEdit.setTitle(_translate("LabFinal", "Edit"))
        self.menuClear.setTitle(_translate("LabFinal", "Clear"))
        self.menuConversion.setTitle(_translate("LabFinal", "Conversion"))
        self.menuSegmentation.setTitle(_translate("LabFinal", "Segmentation"))
        self.menuEdge_Detection.setTitle(_translate("LabFinal", "Edge Detection"))
        self.toolBar.setWindowTitle(_translate("LabFinal", "toolBar"))
        self.actionOpenSource.setText(_translate("LabFinal", "&Open Source"))
        self.actionOpenSource.setShortcut(_translate("LabFinal", "Ctrl+O"))
        self.actionSaveOutput.setText(_translate("LabFinal", "&Save Output"))
        self.actionSaveOutput.setShortcut(_translate("LabFinal", "Ctrl+S"))
        self.actionSaveAsOutput.setText(_translate("LabFinal", "&Save As Output"))
        self.actionSaveAsOutput.setShortcut(_translate("LabFinal", "Ctrl+Shift+S"))
        self.actionExit.setText(_translate("LabFinal", "&Exit"))
        self.actionExit.setShortcut(_translate("LabFinal", "Shift+F4"))
        self.actionExportSource.setText(_translate("LabFinal", "&Source"))
        self.actionExportSource.setShortcut(_translate("LabFinal", "Ctrl+E"))
        self.actionExportOutput.setText(_translate("LabFinal", "&Output"))
        self.actionExportOutput.setShortcut(_translate("LabFinal", "Ctrl+Shift+E"))
        self.actionClearSource.setText(_translate("LabFinal", "&Source"))
        self.actionClearSource.setShortcut(_translate("LabFinal", "Ctrl+L"))
        self.actionClearOutput.setText(_translate("LabFinal", "&Output"))
        self.actionClearOutput.setShortcut(_translate("LabFinal", "Ctrl+Shift+L"))
        self.actionUndoOutput.setText(_translate("LabFinal", "&Undo Output"))
        self.actionUndoOutput.setShortcut(_translate("LabFinal", "Ctrl+Z"))
        self.actionRedoOutput.setText(_translate("LabFinal", "&Redo Output"))
        self.actionRedoOutput.setShortcut(_translate("LabFinal", "Ctrl+Y"))
        self.actionRGBtoGrayscale.setText(_translate("LabFinal", "&RGB to Grayscale"))
        self.actionRGBtoGrayscale.setShortcut(_translate("LabFinal", "Ctrl+G"))
        self.actionRGBtoHSV.setText(_translate("LabFinal", "&RGB to HSV"))
        self.actionRGBtoHSV.setShortcut(_translate("LabFinal", "Ctrl+H"))
        self.actionMultiOtsuThresholding.setText(_translate("LabFinal", "&Multi-Otsu Thresholding"))
        self.actionMultiOtsuThresholding.setShortcut(_translate("LabFinal", "Ctrl+M"))
        self.actionChanVeseSegmentation.setText(_translate("LabFinal", "&Chan-Vese Segmentation"))
        self.actionChanVeseSegmentation.setShortcut(_translate("LabFinal", "Ctrl+Shift+C"))
        self.actionMorphologicalSnakes.setText(_translate("LabFinal", "&Morphological Snakes"))
        self.actionMorphologicalSnakes.setShortcut(_translate("LabFinal", "Ctrl+Shift+M"))
        self.actionRoberts.setText(_translate("LabFinal", "&Roberts"))
        self.actionRoberts.setShortcut(_translate("LabFinal", "Ctrl+R"))
        self.actionSobel.setText(_translate("LabFinal", "&Sobel"))
        self.actionSobel.setShortcut(_translate("LabFinal", "Ctrl+Shift+S"))
        self.actionScharr.setText(_translate("LabFinal", "&Scharr"))
        self.actionScharr.setShortcut(_translate("LabFinal", "Shift+S"))
        self.actionPrewitt.setText(_translate("LabFinal", "&Prewitt"))
        self.actionPrewitt.setShortcut(_translate("LabFinal", "Ctrl+P"))

    """ Function to enable source-related actions and buttons """
    def __enableSource__(self):
        self.actionClearSource.setEnabled(True)
        self.actionRGBtoGrayscale.setEnabled(True)
        self.actionExportSource.setEnabled(True)
        self.actionRGBtoHSV.setEnabled(True)
        self.actionMultiOtsuThresholding.setEnabled(True)
        self.actionRoberts.setEnabled(True)
        self.actionSobel.setEnabled(True)
        self.actionScharr.setEnabled(True)
        self.actionPrewitt.setEnabled(True)
        self.actionChanVeseSegmentation.setEnabled(True)
        self.actionMorphologicalSnakes.setEnabled(True)
        self.pb_grayscale.setEnabled(True)
        self.pb_hsv.setEnabled(True)
        self.pb_mot.setEnabled(True)
        self.pb_cvs.setEnabled(True)
        self.pb_ms.setEnabled(True)
        self.pb_roberts.setEnabled(True)
        self.pb_sobel.setEnabled(True)
        self.pb_scharr.setEnabled(True)
        self.pb_prewitt.setEnabled(True)
        
    """ Function to disable source-related actions and buttons """
    def __disableSource__(self):
        self.actionClearSource.setEnabled(False)
        self.actionRGBtoGrayscale.setEnabled(False)
        self.actionExportSource.setEnabled(False)
        self.actionRGBtoHSV.setEnabled(False)
        self.actionMultiOtsuThresholding.setEnabled(False)
        self.actionRoberts.setEnabled(False)
        self.actionSobel.setEnabled(False)
        self.actionScharr.setEnabled(False)
        self.actionPrewitt.setEnabled(False)
        self.actionChanVeseSegmentation.setEnabled(False)
        self.actionMorphologicalSnakes.setEnabled(False)
        self.pb_grayscale.setEnabled(False)
        self.pb_hsv.setEnabled(False)
        self.pb_mot.setEnabled(False)
        self.pb_cvs.setEnabled(False)
        self.pb_ms.setEnabled(False)
        self.pb_roberts.setEnabled(False)
        self.pb_sobel.setEnabled(False)
        self.pb_scharr.setEnabled(False)
        self.pb_prewitt.setEnabled(False)
        
    """ Function to enable output-related actions and buttons """
    def __enableOutput__(self):
        self.actionSaveOutput.setEnabled(True)
        self.actionSaveAsOutput.setEnabled(True)
        self.actionClearOutput.setEnabled(True)
        self.actionExportOutput.setEnabled(True)
        
    """ Function to disable output-related actions and buttons """
    def __disableOutput__(self):
        self.actionSaveOutput.setEnabled(False)
        self.actionSaveAsOutput.setEnabled(False)
        self.actionClearOutput.setEnabled(False)
        self.actionExportOutput.setEnabled(False)