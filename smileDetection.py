import cv2
import firebase_admin
from firebase_admin import credentials, db

# Inisialisasi Firebase
cred = credentials.Certificate("/home/wgg/Pematerian_Robotic_SAS_2023/smile-project-206bd-firebase-adminsdk-qm4pz-334feccd9a.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://smile-project-206bd-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

def send_to_firebase(smile_detected):
    ref = db.reference('state/smile_status')
    ref.set(smile_detected)

def main(capture):
    face_dataset = 'haarcascade_frontalface_default.xml'
    eye_dataset = '/home/wgg/Pematerian_Robotic_SAS_2023/haarcascade_eye.xml'
    upperBody_dataset = 'haarcascade_upperbody.xml'
    smile_dataset = '/home/wgg/Pematerian_Robotic_SAS_2023/haarcascade_smile.xml'

    fase_cascade = cv2.CascadeClassifier(face_dataset)
    eye_cascade = cv2.CascadeClassifier(eye_dataset)
    upperBody_cascade = cv2.CascadeClassifier(upperBody_dataset)
    smile_cascade = cv2.CascadeClassifier(smile_dataset)

    while True:
        ret, frame = capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)

        # Deteksi Haar Cascade
        upperBody = upperBody_cascade.detectMultiScale(gray)
        faces = fase_cascade.detectMultiScale(gray)

        smile_detected = 0  # Default tidak senyum

        for (x3, y3, w3, h3) in upperBody:
            for (x, y, w, h) in faces:
                smile = smile_cascade.detectMultiScale(gray)
                for (a, b, c, d) in smile:
                    print(len(smile))
                    if len(smile) > 11:  # Jika senyum terdeteksi
                        smile_detected = 1
                        cv2.putText(frame, f'Senyum {len(smile)}', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                        cv2.rectangle(frame, (x, y), (w + x, h + y), (0, 255, 0), 2)
                    else:  # Tidak senyum
                        smile_detected = 0
                        cv2.putText(frame, 'Tidak Senyum', (x, y+50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                        cv2.rectangle(frame, (x, y), (w + x, h + y), (0, 0, 255), 2)

        # Kirim status ke Firebase
        send_to_firebase(smile_detected)

        cv2.imshow('Frame', frame)
        cv2.imshow('GRAY', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
    capture.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    camera = cv2.VideoCapture(0)
    main(camera)
