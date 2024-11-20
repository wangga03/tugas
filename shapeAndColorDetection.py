import cv2 as cv

def main(cap) :

    while True :
        ret, frame = cap.read()

        # COLOR

        rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

        red = (210, 0, 0)

        blue = (0, 0, 210)

        thresh_RedColor = cv.inRange(rgb, red, (255, 255, 255))
        thresh_BlueColor = cv.inRange(rgb, blue, (255, 255, 255))

        kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
        thresh_RedColor = cv.morphologyEx(thresh_RedColor, cv.MORPH_OPEN, kernel)
        thresh_BlueColor = cv.morphologyEx(thresh_BlueColor, cv.MORPH_OPEN, kernel)

        contour_red,_ = cv.findContours(thresh_RedColor, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        contour_blue,_ = cv.findContours(thresh_BlueColor, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)


        # SHAPE
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        _, thress = cv.threshold(gray, 220, 255, cv.THRESH_BINARY)
        kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
        thresh = cv.morphologyEx(thress, cv.MORPH_OPEN, kernel)
        contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        

        for i, contour in enumerate(contours):
            if i == 0:
                continue
            
            epsilon = 0.01*cv.arcLength(contour, True)
            approx = cv.approxPolyDP(contour, epsilon, True)

            cv.drawContours(frame, contour, 0, (0, 0, 0), 4)

            x, y, w, h = cv.boundingRect(approx)
            x_mid = int(x + w / 3)
            y_mid = int(y + h / 1.5)

            coords = (x_mid, y_mid)
            

        if contour_blue  :

            colour = (255, 0, 0)
            font = cv.FONT_HERSHEY_SIMPLEX

            largest_contours = max(contour_blue, key=cv.contourArea)

            x, y, w, h = cv.boundingRect(largest_contours)

            if len(approx) == 3 :

                cv.putText(frame, 'SEGITIGA BIRU', (x, y+50), font, 1, colour, 2)
                cv.rectangle(frame, (x, y), (w + x, h + y), (255, 0,0), 2)
            elif len(approx) == 4 and x == y:
                cv.putText(frame, "PERSEGI BIRU", (x, y+50), font, 1, colour, 2)
                cv.rectangle(frame, (x, y), (w+x, h+y), (0, 255,0), 2)
            elif len(approx) == 4 and x != y:
                cv.putText(frame, "PERSEGI PANJANG BIRU", (x, y+50), font, 1, colour, 2)
                cv.rectangle(frame, (x, y), (w+x, h+y), (0, 255,0), 2)
            elif len(approx) <= 10 and x != y :
                cv.putText(frame, "LINGKARAN BIRU", (x, y+50), font, 1, colour, 2)
                cv.rectangle(frame, (x, y), (w+x, h+y), (0, 255,0), 2)

        if contour_red :
            colour = (0, 0, 255)
            font = cv.FONT_HERSHEY_SIMPLEX

            largest_contours2 = max(contour_red, key=cv.contourArea)

            x, y, w, h = cv.boundingRect(largest_contours2)
            

            if len(approx) == 3 :

                cv.putText(frame, 'SEGITIGA MERAH', (x, y+50), font, 1, (255, 0, 0), 3)
                cv.rectangle(frame, (x, y), (w + x, h + y), (0, 0,255), 2)
            elif len(approx) == 4 and x == y:
                cv.putText(frame, "PERSEGI MERAH", (x, y+50), font, 1, colour, 3)
                cv.rectangle(frame, (x, y), (w+x, h+y), (0, 0,255), 2)
            elif len(approx) == 4 and x != y:
                cv.putText(frame, "PERSEGI PANJANG MERAH", (x, y+50), font, 1, colour, 3)
                cv.rectangle(frame, (x, y), (w+x, h+y), (0, 0,255), 2)
            elif len(approx) <= 10 and x != y :
                cv.putText(frame, "LINGKARAN MERAH", (x, y+50), font, 1, colour, 3)
                cv.rectangle(frame, (x, y), (w+x, h+y), (0, 0,255), 2)


        cv.imshow('FRAME' , frame)
        cv.imshow('HSV' , rgb)

        if cv.waitKey(1) & 0xFF == ord('q') :
            break
    
    frame.release()
    cv.destroyAllWindows()



if __name__== '__main__' :


    cap = cv.VideoCapture(0)
    main(cap)