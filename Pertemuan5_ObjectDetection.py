import cv2



def main(capture) :

    face_dataset = 'haarcascade_frontalface_default.xml'
    eye_dataset = '/home/wgg/Pematerian_Robotic_SAS_2023/haarcascade_eye.xml'
    upperBody_dataset = 'haarcascade_upperbody.xml'
    smile_dataset = '/home/wgg/Pematerian_Robotic_SAS_2023/haarcascade_smile.xml'

    fase_cascade = cv2.CascadeClassifier(face_dataset)
    eye_cascade = cv2.CascadeClassifier(eye_dataset)
    upperBody_cascade =cv2.CascadeClassifier(upperBody_dataset)
    smile_cascade = cv2.CascadeClassifier(smile_dataset)
    

    while True :
        # print(capture.read())
        ret, frame = capture.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)


## Deteksi Haar cascade

        upperBody = upperBody_cascade.detectMultiScale(gray)
        faces = fase_cascade.detectMultiScale(gray)

        for (x3, y3, w3, h3) in upperBody :

        # Untuk setiap wajah yang terdeteksi
            for (x, y, w, h) in faces :

                smile = smile_cascade.detectMultiScale(gray)
                print(len(smile))

                for (a, b, c, d) in smile :
                # Simpan koordinat titik tengah wajah

                    if len(smile) > 15 :
                        center = ((x + w //2, y + h //2))
                        # Tampilkan lingkaran
                        cv2.putText(frame, f'Senyum {len(smile)}', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                        cv2.rectangle(frame, (x, y), (w + x, h + y), (0, 255,0), 2)
                        # Tentukan wilayah awajah yang terdeteksi
                        # face_roi = gray[y:y+h, x:x+w]
                        # # print(face_roi)
                        # eyes = eye_cascade.detectMultiScale(face_roi)
                        # Untuk Setiap Mata Yang terdeteksi
                        # for (x2, y2, w2, h2) in eyes :
                        #     # Tentukan koordinat tengah mata
                        #     eye_center = (x+x2+w2//2, y + y2 + h2//2)
                        #     # Simpan nilai jari2 dari mata yang terdeteksi
                        #     radius = int(round((w2+h2) * 0.25))
                        #     # Tampilkan lingkaran
                        #     frame = cv2.circle(frame, eye_center, radius, (0, 255, 0), 2)

                    else :
                        cv2.putText(frame, 'Tidak Senyum', (x, y+50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                        cv2.rectangle(frame, (x, y), (w + x, h + y), (0, 0,255), 2)


        # print(faces)

        cv2.imshow('Frame', frame)
        cv2.imshow('GRAY', gray)

        if cv2.waitKey(1) & 0xFF == ord('q') :
            break
            
    frame.release()
    cv2.destroyAllWindows()


if __name__ == '__main__' :


    camera = cv2.VideoCapture(0)
    main(camera)