import face_recognition
import cv2
import time
import os
import numpy as np
import pytesseract

import serial as s
data = s.Serial("COM4", 9600)
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

print("Welcome...")

myList = os.listdir("Imagedata")
datalist = []
identify = []
for cl in myList:
    datalist.append(os.path.splitext(cl)[0])
face = cv2.CascadeClassifier('C:/Users/AMAN KAPOOR/data/haarcascades/haarcascade_frontalface_default.xml')
path = "Imagedata"
Rec_ImageList = os.listdir(path)
Read_Images = []
Read_Images_Name = []
encode_Image_list = []
for ij in Rec_ImageList:
    curImg = cv2.imread(f'{path}/{ij}')
    Read_Images.append(curImg)
    Read_Images_Name.append(os.path.splitext(ij)[0])

time.sleep(5)
img_cvt_color = []
for img in Read_Images:
    convert = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_cvt_color.append(convert)

for ig in img_cvt_color:
    encode_img = face_recognition.face_encodings(ig)[0]
    encode_Image_list.append(encode_img)


def face_recognition_(start_button):
    if start_button == 1:

        cap = cv2.VideoCapture()
        cap.open(1, cv2.CAP_DSHOW)

        while True:
            read, imgc = cap.read()
            # imgc = cv2.resize(imgc, (0, 0), None, 0.25, 0.25)
            imgc = cv2.cvtColor(imgc, cv2.COLOR_BGR2RGB)


            FaceLocation = face_recognition.face_locations(imgc)

            Encodingcurface = face_recognition.face_encodings(imgc, FaceLocation)

            for encodeimg in encode_Image_list:
                matches = face_recognition.compare_faces(encodeimg, Encodingcurface)

                break
            if matches[0] == True:
                for (y1, x2, y2, x1) in FaceLocation:
                    cv2.rectangle(imgc, (x1, y1), (x2, y2), (255, 0, 0), 2)
                    cv2.putText(imgc, "True", (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                    identify.insert(0,(matches[0] == True))
                    idtifylist = [(matches[0] == True)]
                if (idtifylist.count([True])) == 1:
                   #print(identify[0],"++")
                    time.sleep(1)
                    break

            else:
                identify.insert(0, "False")
                print(identify[0],"---")

                break
        cap.release()
        cv2.destroyAllWindows()

def add_img(adduser):
    if adduser == 12341:
        add_cap = cv2.VideoCapture()
        add_cap.open(1, cv2.CAP_DSHOW)
        while True:
            _, frame = add_cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            face_detect = face.detectMultiScale(gray, 1.1, 4)
            for (x, y, w, h) in face_detect:
                p = cv2.rectangle(frame, (x - 100, y - 70), (x + w + 100, y + h + 140), (0, 255, 255))
                new = p[y - 70: y + h + 140, x - 100: x + w + 100]
                time.sleep(2)
                #Imgname = int(datalist[-1]) + 1
                cv2.imwrite('E:/Pycharm/Face Recognation Project/Imagedata/'+str(1)+'.jpg', new)
                #cv2.imwrite('E:/Pycharm/Face Recognation Project/Imagedata/' + str(1+1) + '.jpg', new)
            break
            print(done)
        add_cap.release()
        cv2.destroyAllWindows()
def remove_img(removeUser):
    if removeUser == 12342:
        remove_cap = cv2.VideoCapture()
        remove_cap.open(1, cv2.CAP_DSHOW)
        while True:
            try:
                rep,r_img = remove_cap.read()
                remove_img_ = cv2.resize(r_img, (0, 0), None, 0.25, 0.25)
                remove_img_ = cv2.cvtColor(remove_img_,cv2.COLOR_BGR2RGB)
                faceloc_1 = face_recognition.face_locations(remove_img_)
                encodingcurface_1 = face_recognition.face_encodings(remove_img_,faceloc_1)
                for encodeimg_1 in encode_Image_list:
                    remove_matches = face_recognition.compare_faces(encodeimg_1, encodingcurface_1)
                    facedis = face_recognition.face_distance(encodeimg_1, encodingcurface_1)
                    matchindex = np.argmin(facedis)
                    if remove_matches[0] == True and remove_matches[matchindex]:
                        name = Read_Images_Name[matchindex]
                        try:
                            os.remove("Imagedata/"+str(name)+".jpg")
                            print("remove done")
                            break
                        finally:
                            break
                break
            finally:
                break
        print("Everything is done")
        remove_cap.release()
        cv2.destroyAllWindows()

def changes_img (changeuser):
    if changeuser == 12343:
        cap = cv2.VideoCapture(1)

        rat, frame1 = cap.read()
        rat, frame2 = cap.read()

        while cap.isOpened():
            diff = cv2.absdiff(frame1, frame2)
            gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(gray, (5, 5), 0)
            _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
            dilated = cv2.dilate(thresh, None, iterations=3)
            _, contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            for contour in contours:
                (x, y, w, h) = cv2.boundingRect(contour)
                if cv2.contourArea(contour) < 900:
                    continue
                cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 255), 2)
                cv2.putText(frame1, 'Status : {}'.format('Movement'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

            # cv2.drawContours(frame1,contours,-1,(0,255,255),2)

            cv2.imshow('Video', frame1)

            frame1 = frame2
            ret, frame2 = cap.read()

            if cv2.waitKey(1) == 27:
                break

        cv2.destroyAllWindows()
        cap.release()

def no_plate(no_plate_check):
    if no_plate_check == 12:
        no_plate_face = cv2.CascadeClassifier('C:/Users/AMAN KAPOOR/data/haarcascades/haarcascade_russian_plate_number.xml')
        no_plate_cap = cv2.VideoCapture()
        no_plate_cap.open(1, cv2.CAP_DSHOW)
        while True:
            _, frame = no_plate_cap.read()

            no_plate_face_detect = no_plate_face.detectMultiScale(frame, 1.1, 4)
            for (x, y, w, h) in no_plate_face_detect:
                no_plate_rectangle=cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 210), 2)
                no_cut=no_plate_rectangle[y: y + h, x: x + w]
                imgchar = pytesseract.image_to_string(no_cut)
                print(imgchar)
                cv2.imshow('image', no_cut)
            if cv2.waitKey(1) == 27:
                break
        no_plate_cap.release()
        cv2.destroyAllWindows()

class Face_model:

    def __init__(self):

        while True:
            self.val = str(data.readline())
            self.new_val = self.val[2:7].split(',')

            if self.new_val == ['12341']:
                self.Add_data = self.new_val[0][0:5]

                if self.Add_data != 12341:
                    self.Add_data = add_img(12341)
                    print(data.write("100".encode("utf-8")))
                    time.sleep(5)
                    data.write("101".encode("utf-8"))

            elif self.new_val == ['12342']:
                self.Remove_data = self.new_val[0][0:5]
                if self.Remove_data != 12342:
                    self.Remove_data = remove_img(12342)
                    data.write("1000".encode("utf-8"))
                    time.sleep(5)
                    data.write("1001".encode("utf-8"))

            elif self.new_val == ['12343']:
                self.Change_data = self.new_val[0][0:5]

                if self.Change_data != 12343:
                    self.Change_data = changes_img(12343)
                    print(data.write("10000".encode("utf-8")))
                    time.sleep(5)
                    data.write("10001".encode("utf-8"))

            elif self.new_val == ['12\\r\\']:
                self.No_plate_data = self.new_val[0][0:2]
                if self.No_plate_data != 12:
                    self.No_plate_data = no_plate(12)
                    print("No_plate")

            else:

                self.face_data = self.new_val[0][0]
                if self.face_data != 1:
                    self.face_data = face_recognition_(1)
                    if identify[0] == True:
                        print(identify[0],"t")
                        data.write("10".encode("utf-8"))
                        time.sleep(5)
                        data.write("11".encode("utf-8"))
                    else:
                        data.write("20".encode("utf-8"))
                        print(identify[0],"f")
                        time.sleep(5)
                        data.write("21".encode("utf-8"))



window = Face_model()