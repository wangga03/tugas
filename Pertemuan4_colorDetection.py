import cv2
import numpy as np

def callback(_) :
    pass


def init_trackbars():
    #HSV 
    # Bikin Window
    cv2.namedWindow('HSV Trackbar')
    cv2.createTrackbar('LH', 'HSV Trackbar', 0, 255, callback)
    cv2.createTrackbar('LS', 'HSV Trackbar', 0, 255, callback)
    cv2.createTrackbar('LV', 'HSV Trackbar', 0, 255, callback)

    cv2.createTrackbar('UH', 'HSV Trackbar', 255, 255, callback)
    cv2.createTrackbar('US', 'HSV Trackbar', 255, 255, callback)
    cv2.createTrackbar('UV', 'HSV Trackbar', 255, 255, callback)

    cv2.namedWindow('HSV Trackbar2')
    cv2.createTrackbar('LH2', 'HSV Trackbar', 0, 255, callback)
    cv2.createTrackbar('LS2', 'HSV Trackbar', 0, 255, callback)
    cv2.createTrackbar('LV2', 'HSV Trackbar', 0, 255, callback)

    cv2.createTrackbar('UH2', 'HSV Trackbar', 255, 255, callback)
    cv2.createTrackbar('US2', 'HSV Trackbar', 255, 255, callback)
    cv2.createTrackbar('UV2', 'HSV Trackbar', 255, 255, callback)

def get_lower_hsv() :
    lower_hue= cv2.getTrackbarPos('LH', 'HSV Trackbar')
    lower_sat= cv2.getTrackbarPos('LS', 'HSV Trackbar')
    lower_val= cv2.getTrackbarPos('LV', 'HSV Trackbar')

    return (lower_hue, lower_sat, lower_val)


def get_lower_hsv2() :
    lower_hue2= cv2.getTrackbarPos('LH2', 'HSV Trackbar')
    lower_sat2= cv2.getTrackbarPos('LS2', 'HSV Trackbar')
    lower_val2= cv2.getTrackbarPos('LV2', 'HSV Trackbar')

    return (lower_hue2, lower_sat2, lower_val2)

def get_upper_hsv() :
    upper_hue= cv2.getTrackbarPos('UH', 'HSV Trackbar')
    upper_sat= cv2.getTrackbarPos('US', 'HSV Trackbar')
    upper_val= cv2.getTrackbarPos('UV', 'HSV Trackbar')


    return (upper_hue, upper_sat, upper_val)

def get_upper_hsv2() :

    upper_hue2= cv2.getTrackbarPos('UH2', 'HSV Trackbar')
    upper_sat2= cv2.getTrackbarPos('US2', 'HSV Trackbar')
    upper_val2= cv2.getTrackbarPos('UV2', 'HSV Trackbar')

    return (upper_hue2, upper_sat2, upper_val2)



def main(capture) :

    while True :
        # print(capture.read())
        ret, frame = capture.read()



        lowerHSV = get_lower_hsv()
        upperHSV = get_upper_hsv()

        lowerHSV2 = get_lower_hsv2()
        upperHSV2 = get_upper_hsv2()
        # print(lowerHSV)
        # print(upperHSV)

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        thresh = cv2.inRange(hsv, lowerHSV, upperHSV)
        thresh2 = cv2.inRange(hsv, lowerHSV2, upperHSV2)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
        contour, _= cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        thresh2 = cv2.morphologyEx(thresh2, cv2.MORPH_OPEN, kernel)
        contour2, _= cv2.findContours(thresh2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if contour :
            largest_contours = max(contour, key=cv2.contourArea)
            


        # x dan y adalah koordinat/w dan h adalah ukuran
            x, y, w, h = cv2.boundingRect(largest_contours)
            

            cv2.putText(frame, 'BLUE', (x, y+50), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 3)
            

            cv2.rectangle(frame, (x, y), (w + x, h + y), (255, 0,0), 2)

        if contour2 : 

            largest_contours2 = max(contour2, key=cv2.contourArea)

            a, b, c, d= cv2.boundingRect(largest_contours2)

            cv2.putText(frame, 'GREEN', (a, b+50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
            cv2.rectangle(frame, (a, b), (c + a, d + b), (0, 255,0), 2)

        # print(x, y, w, h)


        cv2.imshow('kernel', kernel)
        cv2.imshow('thresh', thresh)
        cv2.imshow('thresh2', thresh2)

        cv2.imshow('HSV', hsv)
        cv2.imshow('Frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q') :
            break
            
    frame.release()
    cv2.destroyAllWindows()


if __name__ == '__main__' :
    init_trackbars()


    camera = cv2.VideoCapture(0)
    main(camera)