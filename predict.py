import cv2 as cv
from ultralytics import YOLO

model = YOLO('grafik/detect/train4/weights/best.pt')
cam = cv.VideoCapture(1)

while cam.isOpened():
    ret,frame = cam.read()
    if not ret:
        print("Kamera gagal Diakses")
        break
    results = model.predict(frame,conf=0.5,verbose=False)
    anotated_frame = results[0].plot()

    cv.imshow("Yolo Deteksi Custom Dataset",anotated_frame)
    if cv.waitKey(1) & 0xFF == ord("q"):
        print("Program Terhenti Manual")
        break

cam.release()
cv.destroyAllWindows()