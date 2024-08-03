# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 19:48:39 2024

@author: sedat
"""

from PyQt5.QtWidgets import QMainWindow, QFileDialog, QLabel, QProgressBar
from PyQt5 import QtWidgets, QtGui, QtCore
from collections import deque
from LabFinal import Ui_LabFinal
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QCoreApplication
import os
import time

class Actions(QMainWindow, Ui_LabFinal):
    def __init__(self, source=None, output=None, height=0, width=0, undo=deque(), redo=deque()):
        """ Initializes the actions class. """
        super().__init__()
        self.__undo = undo
        self.__redo = redo
        self.__source = source
        self.__output = output
        self.__height = height
        self.__width = width
        
    """ Updates the mouse position label for the output frame. """
    def update_mouse_position_output(self, event):
        pos = event.pos()
        self.mouse_position_label.setText(f"Mouse Position (Output): ({pos.x()}, {pos.y()})")

    """ Updates the mouse position label for the source frame. """
    def update_mouse_position_source(self, event):
        pos = event.pos()
        self.mouse_position_label.setText(f"Mouse Position (Source): ({pos.x()}, {pos.y()})")
        
    """ Sets the source image."""
    def setSource(self, source):
        self.__source = source
        self.__setHeight__()
        self.__setWidth__()
       
    """Sets the height of the source image."""
    def __setHeight__(self):
        self.__height = self.getSource().height()
        
    """Sets the width of the source image."""
    def __setWidth__(self):
        self.__width = self.getSource().width()
 
    """ Returns the source image."""
    def getSource(self):
        return self.__source

    """Returns the height of the source image."""
    def getHeight(self):
        return self.__height
    
    """Returns the width of the source image."""
    def getWidth(self):
        return self.__width
    
    """Appends an image to the undo deque."""
    def __setUndo__(self, image):
        self.__undo.append(image)
    
    """Appends an image to the redo deque."""
    def __setRedo__(self, image):
        self.__redo.append(image)
        
    def getUndo(self):
        """
        @brief Returns the undo deque.
        
        @return The undo deque.
        """
        return self.__undo
    
    """ Returns the redo deque """
    def getRedo(self):
        return self.__redo 

    """ Opens a source image file. """
    def open_source(self):
        file_dialog = QtWidgets.QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, 'Dosya Seç', '.', 'Resim Dosyaları (*.png *.jpg *.bmp)')

        if not file_path:
            QMessageBox.warning(self, "Warning", "No file selected.")
            return

        label_source = self.frame_source.findChild(QtWidgets.QLabel, "label_source")
        if label_source:
            label_source.deleteLater()
            
        pixmap_source = QtGui.QPixmap(file_path)
        scaled_pixmap_source = pixmap_source.scaled(self.frame_source.size(), aspectRatioMode=QtCore.Qt.KeepAspectRatio)

        self.setSource(pixmap_source)
        
        progress_bar = QProgressBar(self.frame_source)
        progress_bar.setGeometry(0, self.frame_source.height() - 20, self.frame_source.width(), 20)
        progress_bar.setObjectName("progress_bar")
        progress_bar.setRange(0, 100) 
        progress_bar.setValue(0) 
        progress_bar.show()    

        self.statusbar.showMessage("Loading...")        

        for i in range(101):
            progress_bar.setValue(i)
            time.sleep(0.005)  

        self.statusbar.clearMessage()
        progress_bar.deleteLater()
        
        source = QtWidgets.QLabel(self.frame_source)
        source.setPixmap(scaled_pixmap_source)
        source.setGeometry(0, 0, self.frame_source.width(), self.frame_source.height())
        source.setObjectName("label_source")
        source.show()

        self.__enableSource__()
        self.statusbar.showMessage("Source image opened successfully", 1000)
    
    """ Displays the output image. """
    def __showOutput__(self, pixmap):
        labels = self.frame_output.findChildren(QtWidgets.QLabel, "label_output")
        for label in labels:
            label.deleteLater()  

        progress_bar = QProgressBar(self.frame_output)
        progress_bar.setGeometry(0, self.frame_output.height() - 20, self.frame_output.width(), 20)
        progress_bar.setObjectName("progress_bar")
        progress_bar.setRange(0, 100)  
        progress_bar.setValue(0)  
        progress_bar.show()            

        self.statusbar.showMessage("Loading...") 
        
        for i in range(101):
            progress_bar.setValue(i)
            time.sleep(0.005)  

        self.statusbar.clearMessage()
        progress_bar.deleteLater()
        
        output = QLabel(self.frame_output)
        output.setPixmap(pixmap)
        output.setGeometry(0, 0, self.frame_output.width(), self.frame_output.height())
        output.setObjectName("label_output")
        output.show()

        self.actionUndoOutput.setEnabled(True)
        self.__enableOutput__()
        self.statusbar.showMessage("Output image loaded successfully", 1000)

    """ Saves the output image. """
    def saveOutput(self):
        sender = self.sender()
        current_image_label = self.frame_output.findChild(QLabel, "label_output")
        current_image_pixmap = current_image_label.pixmap()
        if current_image_pixmap.isNull():
            QMessageBox.critical(self, "Error", "No image to save.")
            return 
        
        if sender == self.actionSaveOutput:
            file_path = os.path.join(os.getcwd(), "output_image.png")
            status_message = "Output saved to '{}'".format(file_path)
                 
        elif sender == self.actionSaveAsOutput:
            file_dialog = QFileDialog()
            file_path, _ = file_dialog.getSaveFileName(self, "Save As", ".", "PNG Files (*.png)")
            if not file_path:
                return  
            status_message = "Output saved as '{}'".format(file_path)
        
        current_image_pixmap.save(file_path)    
        file_name = os.path.basename(file_path)
        self.statusbar.showMessage(status_message + " as '{}".format(file_name), 1000)
            
    """ Close the application """
    def close_application(self):
        choice = QMessageBox.question(self, 'Exit', "Are you sure you want to exit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if choice == QMessageBox.Yes:
            QCoreApplication.instance().quit()

    """"Exports the source or output image."""
    def export(self):
        sender = self.sender()
        if sender == self.actionExportSource:
            current_image_label = self.frame_source.findChild(QLabel, "label_source")
            current_image_pixmap = current_image_label.pixmap()
            if current_image_pixmap.isNull():
                QMessageBox.critical(self, "Error", "No image to export from source.") 
                return
            
        elif sender == self.actionExportOutput:
            current_image_label = self.frame_output.findChild(QLabel, "label_output")
            current_image_pixmap = current_image_label.pixmap()
            if current_image_pixmap.isNull():
                QMessageBox.critical(self, "Error", "No image to export from output.")
                return
        
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getSaveFileName(self, "Export As", ".", "PNG Files (*.png);;JPEG Files (*.jpg);;BMP Files (*.bmp)")
        if not file_path:
            return  

        file_name, file_extension = os.path.splitext(file_path)
        if file_extension.lower() == ".png":
            export_file_path = file_name + ".jpg"
        elif file_extension.lower() in [".jpg", ".jpeg"]:
            export_file_path = file_name + ".png"
        else:
            return
        
        current_image_pixmap.save(export_file_path)
        self.statusbar.showMessage("Image exported as '{}'".format(export_file_path))

    """ Clears the source or output frame. """
    def clear(self):
        sender = self.sender()
        if sender == self.actionClearSource:
            for widget in self.frame_source.findChildren(QtWidgets.QWidget):
                widget.deleteLater()
            
            self.__disableSource__()
            self.statusbar.showMessage("The source image has been removed.", 1000)

        elif sender == self.actionClearOutput:
            for widget in self.frame_output.findChildren(QtWidgets.QWidget):
                widget.deleteLater()
            
            self.__disableOutput__()
            self.statusbar.showMessage("The output image has been removed.", 1000)

    """ Performs undo action for the output. """
    def undo_output(self):
        self.actionRedoOutput.setEnabled(True)
    
        self.__setRedo__(self.getUndo().pop())
        status_message = "Undone action for output"
        
        if self.getUndo():
            self.__showOutput__(self.getUndo()[-1])
        
        else:
            for widget in self.frame_output.findChildren(QtWidgets.QWidget):
                widget.deleteLater()
            self.actionUndoOutput.setEnabled(False)
            self.__disableOutput__()
            status_message += " (No more undo available)"
        self.statusbar.showMessage(status_message, 1000)

    """ Performs redo action for the output. """
    def redo_output(self):
        last = self.getRedo().pop()
        self.__showOutput__(last)
        self.__setUndo__(last)
        status_message = "Redone action for output"
        
        if not self.getRedo():
            self.actionRedoOutput.setEnabled(False)
            status_message += " (No more redo available)"
            
        self.statusbar.showMessage(status_message, 1000)
