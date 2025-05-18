import cv2
import winsound
import threading

# Load Haar Cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Custom sound function
def play_custom_sound():
    winsound.PlaySound("https://www.jiosaavn.com/song/upavasa/NQMBUyR2WQE", winsound.SND_FILENAME)

cap = cv2.VideoCapture(0)
face_detected = False

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    if len(faces) > 0 and not face_detected:
        print("Face detected - Playing custom sound!")
        threading.Thread(target=play_custom_sound).start()
        face_detected = True
    elif len(faces) == 0:
        face_detected = False

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('Smart doorbell', frame)

    if cv2.waitKey(5) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
