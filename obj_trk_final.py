import cv2
import time
import math
p1=530
p2=300
xaxis=[]
yaxis=[]

video = cv2.VideoCapture("footvolleyball.mp4")
tracker=cv2.TrackerCSRT_create()

returned, img=video.read()
det=cv2.selectROI("Tracking",img,False)
tracker.init(img,det)
print(det)
def drawRect(img,det):
    x,y,w,h=int(det[0]),int(det[1]),int(det[2]),int(det[3])
    cv2.rectangle(img,(x,y),(x+w,y+h),(176,10,243),3,1)
    cv2.putText(img,"Tracking",(70,100),cv2.FONT_HERSHEY_COMPLEX,0.7,(3,156,201),2)
    

def drawPath(img,det):
    x,y,w,h=int(det[0]),int(det[1]),int(det[2]),int(det[3])
    c1=x+int(w/2)
    c2=y+int(h/2)
    cv2.circle(img,(c1,c2),2,(34,123,179),5)
    cv2.circle(img,(int(p1),int(p2)),2,(105,234,2),3)
    distance=math.sqrt(((c1-p1)**2) + (c2-p2)**2)
    print(distance)
    if(distance<=20):
        cv2.putText(img,"Goal",(200,100),cv2.FONT_HERSHEY_COMPLEX,0.7,(32,146,1),2)
    xaxis.append(c1)
    yaxis.append(c2)
    for i in range (len(xaxis)-1):
        cv2.circle(img,(xaxis[i],yaxis[i]),2,(56,142,222),4)


while True:
    check,img = video.read()   
    success,det=tracker.update(img)
    if success:
        drawRect(img,det)
    else:
        cv2.putText(img,"Can't find",(70,100),cv2.FONT_HERSHEY_COMPLEX,0.7,(3,156,201),2)
    drawPath(img,det)

    cv2.imshow("result",img)
            
    key = cv2.waitKey(1)

    if key == ord('q'):
        print("closing")
        break


video.release()
cv2.destroyALLwindows()



