
"""
Copyright by
| Alvin Sengkey
| 001202000115
| President University
| Faculty of Computing
| Major of Informatics
| MAY 2023

"""

import cv2
import random
from imutils.video import WebcamVideoStream



class doDetection(object):
    def __init__(self):
        self.stream = WebcamVideoStream(src=0).start()

    def __del__(self):
        self.stream.stop()


    # Initialize these components
    names = "data\obj.names"
    cfg = "cfg\yolov4-obj.cfg"
    weights = "yolov4-obj_best.weights"
    thresh = 0.25

    label = ""

    NMS_THRESHOLD = 0.4

    # Read Object names and store in Array
    NAMES = []
    with open(names, "r") as f:
        NAMES = [cname.strip() for cname in f.readlines()]

    # Bounding Box Colors
    global COLORS
    COLORS = [[random.randint(0, 255) for _ in range(3)] for _ in NAMES]

    # Load Model YOLOv4
    net = cv2.dnn.readNet(weights, cfg)
    model = cv2.dnn_DetectionModel(net)

    model.setInputParams(size=(512, 512), scale=1 / 255, swapRB=True)


    def get_frame(self):
        frame = self.stream.read()
        global label

        # Object Detection
        classes, scores, boxes = self.model.detect(
            frame, self.thresh, self.NMS_THRESHOLD
        )

        # Draw detection result
        for classid, score, box in zip(classes, scores, boxes):
            color = COLORS[int(classid)]
            label = "%s : %0.2f" % (self.NAMES[int(classid)], score)
            # Box = x, y, width, height
            cv2.rectangle(frame, box, color, 2)
            cv2.putText(
                frame,
                label,
                (box[0], box[1] - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                color,
                2,
            )

            print("Classes: %s : %0.2f" % (self.NAMES[int(classid)], score))

        jpeg = cv2.imencode(".jpg", frame)[1]
        data = []
        data.append(jpeg.tobytes())
        if self.label != "":
            print("LABEL: ", self.label)
            data.append(self.label)
        return data
    

    def get_result():
        # get_frame(object)
        if label != "":
            predict_result = label
        else:
            predict_result = ""
        print("LABEL-2: ", predict_result)
        return predict_result
