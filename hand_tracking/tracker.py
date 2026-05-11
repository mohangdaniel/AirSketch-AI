import cv2
import mediapipe as mp
from mediapipe.tasks.python import vision
from mediapipe.tasks.python import BaseOptions


# Manual hand connections
HAND_CONNECTIONS = [

    (0,1),(1,2),(2,3),(3,4),

    (0,5),(5,6),(6,7),(7,8),

    (5,9),(9,10),(10,11),(11,12),

    (9,13),(13,14),(14,15),(15,16),

    (13,17),(17,18),(18,19),(19,20),

    (0,17)
]


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

    def draw_landmarks(self, frame, landmarks):

        h, w, _ = frame.shape

        # DRAW CONNECTIONS
        for connection in HAND_CONNECTIONS:

            start_idx = connection[0]
            end_idx = connection[1]

            start = landmarks[start_idx]
            end = landmarks[end_idx]

            x1 = int(start.x * w)
            y1 = int(start.y * h)

            x2 = int(end.x * w)
            y2 = int(end.y * h)

            cv2.line(
                frame,
                (x1, y1),
                (x2, y2),
                (0, 255, 255),
                2,
                cv2.LINE_AA
            )

        # DRAW NODES
        for idx, landmark in enumerate(landmarks):

            x = int(landmark.x * w)
            y = int(landmark.y * h)

            if idx in [4, 8, 12, 16, 20]:

                cv2.circle(
                    frame,
                    (x, y),
                    10,
                    (0, 255, 0),
                    -1
                )

            else:

                cv2.circle(
                    frame,
                    (x, y),
                    5,
                    (255, 0, 255),
                    -1
                )

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

            hand = result.hand_landmarks[0]

            # Draw mesh
            self.draw_landmarks(frame, hand)

            h, w, _ = frame.shape

            # Finger landmarks
            index_tip = hand[8]
            index_pip = hand[6]

            middle_tip = hand[12]
            middle_pip = hand[10]

            ring_tip = hand[16]
            ring_pip = hand[14]

            pinky_tip = hand[20]
            pinky_pip = hand[18]

            # Finger states
            index_up = self.finger_up(index_tip, index_pip)

            middle_up = self.finger_up(middle_tip, middle_pip)

            ring_up = self.finger_up(ring_tip, ring_pip)

            pinky_up = self.finger_up(pinky_tip, pinky_pip)

            # ONLY INDEX FINGER = DRAW
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

                cv2.circle(
                    frame,
                    fingertip,
                    15,
                    (0, 255, 0),
                    -1
                )

        return frame, fingertip, draw_mode