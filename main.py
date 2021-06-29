import cv2
import yolo
import face_detection
capture= cv2.VideoCapture(0)

if capture.isOpened() is False:
    print("Error opening camera")
clicked = False
def onMouse(event, x, y, flags, param):
    global clicked
    if event == cv2.EVENT_LBUTTONUP:
        clicked = True
cv2.namedWindow('MyWindow')
cv2.setMouseCallback('MyWindow', onMouse)
print('Showing camera feed. Click window or press any key to stop.')
ret,frame=capture.read()
while ret and cv2.waitKey(1) == -1 and not clicked:
    detected=yolo.humanDetect(frame)
    if detected is not None:
        print("Human Detected")
        face = face_detection.detect_face(detected)   
        if face is not None:     
            mask = face_detection.detect_mask(face)
            cv2.putText(frame,mask,(20,20),cv2.FONT_HERSHEY_SIMPLEX,1,[0,0,255],2)
            cv2.imshow("face", frame)      
    ret,frame=capture.read()
cv2.destroyWindow('MyWindow')
capture.release()

