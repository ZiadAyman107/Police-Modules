# Police-Modules
A Survillence system for Police it contains features like Arabic Car plate recognition to recognize characters of plates and compare it with database for stolen plates, capture Unmasked people faces for later pay Fine for not wearing mask, Recognize faces from our database of criminal faces and alert the police and Fire detection to alert Fire department

# How to use:
First you need to Download the models from this link:
second you need to add Car plate numbers in the Excel file and criminal pictures in the "Wanted Criminals Folder" and add their Data in "Recognize_Faces.py" line 5
Next you need to run Main.py and add Path to video in "cv2.VideoCapture()" or Pass parameter 0 if you want WebCam
