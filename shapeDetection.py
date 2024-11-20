import cv2 as cv

def main(capture) :

    while True :

        ret, frame = capture.read()

        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        _, thresh = cv.threshold(gray, 225, 255, cv.THRESH_BINARY)
        kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
        thresh = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel)
        contours, _= cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

        for i, contour in enumerate(contours) :
            if i == 0 :
                continue

            
            elif i < 10 :
                epsilon = 0.01*cv.arcLength(contour, True)
                approx = cv.approxPolyDP(contour, epsilon, True)

                cv.drawContours(frame, contour, 0, (0,0,0), 4)

                x, y, w, h = cv.boundingRect(approx)
                x_mid = int(x + w/3)
                y_mid = int(y +h/1.5)

                # coords = (x_mid, y_mid)
                # colour = (0, 255, 0)
                # font = cv.FONT_HERSHEY_SIMPLEX

                if len(approx) == 3 :
                    cv.putText(frame, "Segitiga", (x, y+50), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    cv.rectangle(frame, (x, y), (w+x, h+y), (0, 255,0), 2)
                elif len(approx) == 4 and x == y:
                    cv.putText(frame, "persegi", (x, y+50), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    cv.rectangle(frame, (x, y), (w+x, h+y), (0, 255,0), 2)
                elif len(approx) == 4 and x != y:
                    cv.putText(frame, "persegi panjang", (x, y+50), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    cv.rectangle(frame, (x, y), (w+x, h+y), (0, 255,0), 2)

                elif len(approx) > 10:
                    cv.putText(frame, "lingkaran", (x, y+50), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    cv.rectangle(frame, (x, y), (w+x, h+y), (0, 255,0), 2)
                # else : 
                #     cv.putText(frame, "lingkaran", coords, font, 1, colour, 1)

        cv.imshow('Frame', frame)
        cv.imshow('Gray', gray)
        cv.imshow('Tresh', thresh)

        if cv.waitKey(1) & 0xFF == ord('q') :
            break

    frame.release()
    cv.destroyAllWindows()
    
if __name__ == '__main__' :

    cam = cv.VideoCapture(0)
    main(cam)