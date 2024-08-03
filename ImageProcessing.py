# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 20:53:39 2024

@author sedat
"""

from Actions import Actions
from collections import deque
from PyQt5.QtGui import QPixmap, QImage
import numpy as np
from skimage.color import rgb2hsv, rgb2gray, hsv2rgb
from skimage.filters import threshold_multiotsu
from skimage.segmentation import chan_vese, morphological_chan_vese
from skimage import filters, color, img_as_ubyte
from LabFinal import Ui_LabFinal 

""" ImageProcessing class. Derived from Actions class. """
class ImageProcessing(Actions):
    """ Constructor for imageProcessing class. """
    def __init__(self, source=None, output=None, height=0, width=0, undo=deque(), redo=deque(), qImage=None):
        super().__init__(source, output, height, width, undo, redo)
        self.__qImage = qImage
        
        
    """ Returns the image in QImage format. """
    def getQImage(self):
        return self.getSource().toImage()


    """ Converts a color image to grayscale. """
    def rgbToGrayscale(self):
        qImage = self.getQImage()
        grayscale = qImage.convertToFormat(QImage.Format_Grayscale8)
        pixmap_output = QPixmap.fromImage(grayscale)
        
        self.__showOutput__(pixmap_output)
        self.__setUndo__(pixmap_output)


    """ Converts an RGB image to the HSV color space. """
    def rgbToHsv(self):
        ptr = self.getQImage().bits()
        ptr.setsize(self.getQImage().byteCount())
        arr = np.array(ptr).reshape(self.getHeight(), self.getWidth(), 4)
        rgb_image = arr[:, :, :3] / 255.0
        hsv_image = rgb2hsv(rgb_image)
        rgb_output = (hsv2rgb(hsv_image) * 255).astype(np.uint8)
        output_image = QImage(rgb_output, self.getWidth(), self.getHeight(), QImage.Format_RGB888)
        output_pixmap = QPixmap.fromImage(output_image)
        
        self.__showOutput__(output_pixmap)
        self.__setUndo__(output_pixmap)


    """ Applies multi-Otsu thresholding to the image."""
    def multiOtsuThresholding(self):
        ptr = self.getQImage().bits()
        ptr.setsize(self.getQImage().byteCount())
        arr = np.array(ptr).reshape(self.getHeight(), self.getWidth(), 4)
        rgb_image = arr[:, :, :3]
        thresholds = threshold_multiotsu(rgb_image)
        segmented = np.zeros_like(rgb_image)
        for i in range(len(thresholds) + 1):
            if i == 0:
                segmented[rgb_image <= thresholds[i]] = i * 255 / len(thresholds)
            elif i == len(thresholds):
                segmented[rgb_image > thresholds[i - 1]] = i * 255 / len(thresholds)
            else:
                segmented[(rgb_image > thresholds[i - 1]) & (rgb_image <= thresholds[i])] = i * 255 / len(thresholds)
        segmented_image = img_as_ubyte(segmented)
        output_image = QPixmap.fromImage(QImage(segmented_image, self.getWidth(), self.getHeight(), QImage.Format_RGB888))

        self.__showOutput__(output_image)
        self.__setUndo__(output_image)


    """ Applies Chan-Vese segmentation to the image. """
    def chanVeseSegmentation(self):
        ptr = self.getQImage().bits()
        ptr.setsize(self.getQImage().byteCount())
        arr = np.array(ptr).reshape(self.getHeight(), self.getWidth(), 4)
        gray_image = rgb2gray(arr[:, :, :3])
        segmented_img = chan_vese(gray_image, mu=0.25, lambda1=1, lambda2=1, tol=1e-3, max_num_iter=200, dt=0.5)
        segmented_img = (segmented_img * 255).astype(np.uint8)
        output_pixmap = QPixmap.fromImage(QImage(segmented_img.data, self.getWidth(), self.getHeight(), segmented_img.strides[0], QImage.Format_Grayscale8))

        self.__showOutput__(output_pixmap)
        self.__setUndo__(output_pixmap)


    """ Applies morphological snakes to the image."""
    def morphologicalSnakes(self):
        ptr = self.getQImage().bits()
        ptr.setsize(self.getQImage().byteCount())
        arr = np.array(ptr).reshape(self.getHeight(), self.getWidth(), 4)
        gray_image = rgb2gray(arr[:, :, :3])
        init_ls = np.zeros(gray_image.shape, dtype=bool)
        init_ls[10:-10, 10:-10] = True  
        segmented_img = morphological_chan_vese(gray_image, num_iter=200, init_level_set=init_ls, smoothing=1)
        segmented_img = (segmented_img * 255).astype(np.uint8)
        output_pixmap = QPixmap.fromImage(QImage(segmented_img.data, self.getWidth(), self.getHeight(), segmented_img.strides[0], QImage.Format_Grayscale8))

        self.__showOutput__(output_pixmap)
        self.__setUndo__(output_pixmap)


    """ Applies the Scharr edge detection filter to the image. """
    def scharr(self):
        ptr = self.getQImage().bits()
        ptr.setsize(self.getQImage().byteCount())
        arr = np.array(ptr).reshape(self.getHeight(), self.getWidth(), 4)
        gray_image = color.rgb2gray(arr[:, :, :3])
        edge_scharr = filters.scharr(gray_image)
        output_pixmap = QPixmap.fromImage(QImage((edge_scharr * 255).astype(np.uint8), self.getWidth(), self.getHeight(), QImage.Format_Grayscale8))

        self.__showOutput__(output_pixmap)
        self.__setUndo__(output_pixmap)


    """ Applies the Prewitt edge detection filter to the image. """       
    def prewitt(self):
        ptr = self.getQImage().bits()
        ptr.setsize(self.getQImage().byteCount())
        arr = np.array(ptr).reshape(self.getHeight(), self.getWidth(), 4)
        gray_image = color.rgb2gray(arr[:, :, :3])
        edge_prewitt = filters.prewitt(gray_image)
        output_image = (edge_prewitt * 255).astype(np.uint8)
        output_qimage = QImage(output_image.data, self.getWidth(), self.getHeight(), QImage.Format_Grayscale8)
        output_pixmap = QPixmap.fromImage(output_qimage)

        self.__showOutput__(output_pixmap)
        self.__setUndo__(output_pixmap)


    """ Applies the Sobel edge detection filter to the image. """
    def sobel(self):
        ptr = self.getQImage().bits()
        ptr.setsize(self.getQImage().byteCount())
        arr = np.array(ptr).reshape(self.getHeight(), self.getWidth(), 4)
        gray_image = color.rgb2gray(arr[:, :, :3])
        edge_sobel = filters.sobel(gray_image)
        sobel = QPixmap.fromImage(QImage((edge_sobel * 255).astype(np.uint8), self.getWidth(), self.getHeight(), QImage.Format_Grayscale8))

        self.__showOutput__(sobel)
        self.__setUndo__(sobel)


    """ Applies the Roberts edge detection filter to the image. """
    def roberts(self):
        ptr = self.getQImage().bits()
        ptr.setsize(self.getQImage().byteCount())
        arr = np.array(ptr).reshape(self.getHeight(), self.getWidth(), 4)

        gray_image = color.rgb2gray(arr[:, :, :3])        
        edge_roberts = filters.roberts(gray_image)

        max_value = np.max(edge_roberts)
        if max_value != 0 and not np.isnan(max_value) and not np.isinf(max_value):
            edge_roberts_norm = edge_roberts / max_value
            edge_roberts_norm = np.clip(edge_roberts_norm, 0, 1)  # Clip values between 0 and 1
        else:
            edge_roberts_norm = np.zeros_like(edge_roberts)  # Handle special case

        output_image = (edge_roberts_norm * 255).astype(np.uint8)
        output_pixmap = QPixmap.fromImage(QImage(output_image, self.getWidth(), self.getHeight(), QImage.Format_Grayscale8))
        
        self.__showOutput__(output_pixmap)
        self.__setUndo__(output_pixmap)
