from Extract_Character import *
from Character_Recognizer import *
from digit_recognizer_ import *
import Check_Stolen_Plates
class Get_Plate_Characters:
    def __init__(self):
        self.cr = Character_Recognizer()
        self.nr = Number_Recognizer()
        self.Ec = Extract_Characters()

    def GetPlateChars(self, PlateNumber):
        image = cv2.imread("Plates From Model/" + str(PlateNumber) + ".png")
        numbers, characters = self.Ec.extract(image)
        word = []
        for i in range(len(numbers)):
            word.append(self.nr.ocr(numbers[i]))

        for i in range(len(characters)):
            word.append(self.cr.ocr(characters[i]))
        word.reverse()
        Found = Check_Stolen_Plates.Compare_Plates(word)
        if Found:
            print("Is Stolen" + str(word))
