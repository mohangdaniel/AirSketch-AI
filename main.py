import cv2
import numpy as np
from collections import deque
from hand_tracking.tracker import HandTracker

tracker = HandTracker()

cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("❌ Camera failed")
    exit()

canvas = np.zeros((720, 1280, 3), dtype=np.uint8)

strokes = []
current_stroke = []

smooth_buffer = deque(maxlen=12)

MIN_DISTANCE = 4

while True:

    ret, frame = cap.read()

    if not ret:
        continue

    frame = cv2.resize(frame, (1280, 720))

    frame, fingertip, draw_mode = tracker.process_frame(frame)

    # -----------------------------------
    # DRAW MODE
    # -----------------------------------

    if draw_mode and fingertip:

        smooth_buffer.append(fingertip)

        # weighted smoothing
        avg_x = int(sum(p[0] for p in smooth_buffer) / len(smooth_buffer))
        avg_y = int(sum(p[1] for p in smooth_buffer) / len(smooth_buffer))

        point = (avg_x, avg_y)

        if len(current_stroke) == 0:

            current_stroke.append(point)

        else:

            prev = current_stroke[-1]

            dist = np.linalg.norm(
                np.array(point) - np.array(prev)
            )

            # ignore tiny noise
            if dist > MIN_DISTANCE:

                # interpolate missing points for fast movement
                steps = int(dist / 10)

                for s in range(1, steps + 1):

                    interp_x = int(
                        prev[0] + (point[0] - prev[0]) * s / steps
                    )

                    interp_y = int(
                        prev[1] + (point[1] - prev[1]) * s / steps
                    )

                    current_stroke.append((interp_x, interp_y))

                current_stroke.append(point)

    else:

        # finalize stroke
        if len(current_stroke) > 5:
            strokes.append(current_stroke)

        current_stroke = []
        smooth_buffer.clear()

    # -----------------------------------
    # DRAW ALL STROKES
    # -----------------------------------

    for stroke in strokes:

        for i in range(1, len(stroke)):

            cv2.line(
                canvas,
                stroke[i - 1],
                stroke[i],
                (255, 0, 255),
                5,
                cv2.LINE_AA
            )

    # active stroke
    for i in range(1, len(current_stroke)):

        cv2.line(
            canvas,
            current_stroke[i - 1],
            current_stroke[i],
            (0, 255, 255),
            5,
            cv2.LINE_AA
        )

    output = cv2.addWeighted(frame, 0.75, canvas, 1, 0)

    status = "DRAW MODE" if draw_mode else "STOP MODE"

    cv2.putText(
        output,
        status,
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0) if draw_mode else (0, 0, 255),
        2
    )

    cv2.imshow("AirDraw Ultimate", output)

    key = cv2.waitKey(1)

    if key == ord('c'):

        canvas = np.zeros((720, 1280, 3), dtype=np.uint8)

        strokes = []
        current_stroke = []

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()