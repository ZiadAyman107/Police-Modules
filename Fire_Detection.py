import cv2
import numpy as np
from imageai.Detection.Custom import CustomVideoObjectDetection
class Fire_Detection:
    def __init__(self):
        total_fire_frames = 0
        total_non = 0
        filename = "12.mp4"
        self.detect_from_video(filename)

        if (total_fire_frames / (total_fire_frames + total_non)) * 100 >= 15:
            print("FIRE DETECTED")
        else:
            print("NO FIRE DETECTED")


    def forFrame(self, frame_number, output_array, output_count, frame):
        # cv2.imshow("Streaming", frame)
        # cv2.waitKey(1)
        if bool(output_count):
            global total_fire_frames
            total_fire_frames += 1
        else:
            global total_non
            total_non += 1


    def detect_from_video(self, filename):
        detector = CustomVideoObjectDetection()
        detector.setModelTypeAsYOLOv3()
        detector.setModelPath(detection_model_path="FireModel/detection_model-ex-33--loss-4.97.h5")
        detector.setJsonPath(configuration_json="FireModel/detection_config.json")
        detector.loadModel()

        detected_video_path = detector.detectObjectsFromVideo(input_file_path=filename,
                                                              frames_per_second=30, minimum_percentage_probability=30,
                                                              log_progress=False, save_detected_video=False,return_detected_frame=True,
                                                              per_frame_function=self.forFrame)
