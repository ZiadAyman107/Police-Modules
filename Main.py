# from Fire_Detection import
from Car_Plate_Detection import *
from Get_Plate_Characters import *
from Recognize_Faces import *
from Mask_Detection import *

# Detect_fire = Fire_Detection()
Car_Plate_Detection = Car_Plate_Detection()
Get_Plate_Characters = Get_Plate_Characters()
Recognize_Faces = Recognize_Faces()
Mask_Detection = Mask_Detection()


Frame_Number_For_Plate = 0
Frame_Number_For_Face = 0
Plate_Number = 0
Face_Number = 0
camera = cv2.VideoCapture("11.mp4")
while camera.isOpened():
    ret, frame = camera.read()
    Frame_Number_For_Plate += 1
    Frame_Number_For_Face += 1
    if ret:
        #Detect Plates
        if Frame_Number_For_Plate == 20:
            Plate_Found = Car_Plate_Detection.Detect_Plate(frame, Plate_Number)
            if Plate_Found:
                Get_Plate_Characters.GetPlateChars(Plate_Number)
                Plate_Number += 1
            Frame_Number_For_Plate = 0

        #Detect Mask
        frame, Face_Found = Mask_Detection.Detect_Mask(frame, Face_Number, Frame_Number_For_Face)
        if Face_Found == True:
            Recognize_Faces.Recognize_Face(Face_Number)
            Face_Number += 1
            Frame_Number_For_Face = 0

        frame = cv2.resize(frame, (1000, 700))
        cv2.imshow("Streaming", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cv2.waitKey()
cv2.destroyAllWindows()
