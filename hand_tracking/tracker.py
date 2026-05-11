import cv2
import mediapipe as mp
from mediapipe.tasks.python import vision
from mediapipe.tasks.python import BaseOptions


class HandTracker:

    def __init__(self):

        base_options = BaseOptions(
            model_asset_path="models/hand_landmarker.task"
        )

        options = vision.HandLandmarkerOptions(
            base_options=base_options,
            num_hands=1,
            min_hand_detection_confidence=0.35,
            min_tracking_confidence=0.35,
            running_mode=vision.RunningMode.IMAGE
        )

        self.hands = vision.HandLandmarker.create_from_options(options)

    def finger_up(self, tip, pip):
        return tip.y < pip.y

    def process_frame(self, frame):

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=rgb
        )

        result = self.hands.detect(mp_image)

        fingertip = None
        draw_mode = False

        if result.hand_landmarks:

            h, w, _ = frame.shape

            hand = result.hand_landmarks[0]

            # Finger landmarks
            index_tip = hand[8]
            index_pip = hand[6]

            middle_tip = hand[12]
            middle_pip = hand[10]

            ring_tip = hand[16]
            ring_pip = hand[14]

            pinky_tip = hand[20]
            pinky_pip = hand[18]

            # finger states
            index_up = self.finger_up(index_tip, index_pip)

            middle_up = self.finger_up(middle_tip, middle_pip)

            ring_up = self.finger_up(ring_tip, ring_pip)

            pinky_up = self.finger_up(pinky_tip, pinky_pip)

            # DRAW ONLY IF:
            # ONLY index finger is up
            if (
                index_up and
                not middle_up and
                not ring_up and
                not pinky_up
            ):

                x = int(index_tip.x * w)
                y = int(index_tip.y * h)

                fingertip = (x, y)

                draw_mode = True

                cv2.circle(frame, fingertip, 12, (0, 255, 0), -1)

        return frame, fingertip, draw_mode