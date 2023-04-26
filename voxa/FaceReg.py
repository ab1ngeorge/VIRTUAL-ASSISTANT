import threading

import cv2

from deepface import DeepFace

referenceImgAswin = cv2.imread("assets/referenceImg/refAswin.jpg")
referenceImgVinod = cv2.imread("assets/referenceImg/refVinod.jpg")
referenceImgAbin = cv2.imread("assets/referenceImg/refAbin.jpg")
referenceImgAlan = cv2.imread("assets/referenceImg/refAlan.jpg")
referenceImgAthul = cv2.imread("assets/referenceImg/refAthul.jpg")
referenceImgSharon = cv2.imread("assets/referenceImg/refSharon.jpg")
referenceImgSidharth = cv2.imread("assets/referenceImg/refSidharth.jpg")

def startRecognitiion():
    user = ''
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cv2.imwrite("assets/image/currentValidationPic.jpg",frame)
    cap.release()
    cv2.destroyAllWindows()

    validationImg = cv2.imread("assets/image/currentValidationPic.jpg")





    try:
        if DeepFace.verify(validationImg, referenceImgAswin)['verified']:
            print("Aswin")
            user = "Aswin"
        if DeepFace.verify(validationImg, referenceImgVinod)['verified']:
            print("Vinod")
            user = "Vinod"
        elif DeepFace.verify(validationImg, referenceImgAbin)['verified']:
            print("Abin")
            user = "Abin"
        elif DeepFace.verify(validationImg, referenceImgAlan)['verified']:
            print("Alan")
            user = "Alan"
        elif DeepFace.verify(validationImg, referenceImgAthul)['verified']:
            print("Athul")
            user = "Athulraj"
        elif DeepFace.verify(validationImg, referenceImgSharon)['verified']:
            print("Sharon")
            user = "Sharon"
        elif DeepFace.verify(validationImg, referenceImgSidharth)['verified']:
            print("Sidharth")
            user = "Sidharth"
        else:
            print("Dont know!")
            user = "Dont know"
            
    except ValueError:
        print("false except")
        user = "none found"
    return user


