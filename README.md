# Image-Processing-Interface
The aim of this project is to develop a class hierarchy capable of performing various operations on RGB images. An interface specifically designed to execute these operations has been created using Qt Designer.
  1.	The "Ui_LabFinal" class encompasses the properties of a user interface created with PyQt5 and defines the behaviors of the interface. Additionally, it includes helper methods to access and manage specific features of the interface. These methods enable the activation or deactivation of certain functionalities related to either source image processing operations or output image processing operations.
  2.	The "Actions" class enables the user to manage the created interface. The interface provides functions such as acquiring a source image, processing it, displaying the output, and managing the operation history for undoing or redoing actions. Users can upload a source image, save or export the processed output, and if necessary, undo or redo these operations.
  3.	The “ImageProcessing” class enables a user to perform image processing operations using a PyQt5 interface. It provides functions including acquiring a source image, converting it to grayscale, changing color space, performing multi-Otsu thresholding, Chan-Vese segmentation, morphological Chan-Vese segmentation, and various edge detection operations. It displays the resulting outputs and manages the user's undo/redo history.


OUTPUTS

Grayscale:
![grayscale](https://github.com/user-attachments/assets/319858e1-719b-4303-9d38-6891ac66b1f3)

Prewitt:
![prewitt](https://github.com/user-attachments/assets/f26da896-9692-4dc5-9fb4-43317e74225e)

Save As:
![saveAs](https://github.com/user-attachments/assets/07e8c9d4-830e-46bf-966d-982e67fca972)
