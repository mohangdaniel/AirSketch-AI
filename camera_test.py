import cv2

print("Testing camera indices...")

for i in range(5):
    cap = cv2.VideoCapture(i)

    if cap.isOpened():
        ret, frame = cap.read()

        if ret:
            print("WORKING CAMERA FOUND AT INDEX:", i)

        cap.release()