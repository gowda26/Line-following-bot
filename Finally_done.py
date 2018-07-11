import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('test5.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
font = cv2.FONT_HERSHEY_SIMPLEX
ret,thresh = cv2.threshold(gray,127,255,1)
#contours,h = cv2.findContours(thresh,1,2)
image, contours, h = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#cv2.imshow('aasd',thresh)

for cnt in contours:

    
    approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
    print len(approx)
    if len(approx)==5:
        print "pentagon"
     #   cv2.drawContours(img,[cnt],-1,(0,201,255),3)
        M = cv2.moments(cnt)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        px=img[cy,cx]
        print px
        if(px[0]>100):
            color="Blue"
        elif(px[1]>100):
            color="Green"
        elif(px[2]>100):
            color="Red"
        cv2.putText(img,"Pentagon",(cx-30,cy-25),font,.5,(0,0,0),2)
        cv2.putText(img,"(%d,%d)"%(cx,cy),(cx,cy),font,.5,(0,0,0),2)
        cv2.putText(img,"%s"%color,(cx-50,cy-50),font,.5,(0,0,0),2)





    elif len(approx)==6:
        print "HEXAGON"
      #  cv2.drawContours(img,[cnt],-1,(0,201,255),3)
        M = cv2.moments(cnt)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        px=img[cy,cx]
        print px
        if(px[0]>100):
            color="Blue"
        elif(px[1]>100):
            color="Green"
        elif(px[2]>100):
            color="Red"
        cv2.putText(img,"Hexagon",(cx-30,cy-25),font,.5,(0,0,0),2)
        cv2.putText(img,"(%d,%d)"%(cx,cy),(cx,cy),font,.5,(0,0,0),2)
        cv2.putText(img,"%s"%color,(cx-50,cy-50),font,.5,(0,0,0),2)






        
    elif len(approx)==3:
        print "triangle"
       # cv2.drawContours(img,[cnt],-1,(0,205,255),3)
        M = cv2.moments(cnt)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        px=img[cy,cx]
        print px
        if(px[0]>100):
            color="Blue"
        elif(px[1]>100):
            color="Green"
        elif(px[2]>100):
            color="Red"
        cv2.putText(img,"Triangle",(cx-25,cy-20),font,.5,(0,0,0),2)
        cv2.putText(img,"(%d,%d)"%(cx,cy),(cx-10,cy),font,.5,(0,0,0),2)
        cv2.putText(img,"%s"%color,(cx-40,cy-40),font,.5,(0,0,0),2)

        




        
    elif len(approx)==4:        
        (x, y, w, h) = cv2.boundingRect(approx)
        imarea=cv2.contourArea(approx)
        area1=w*h
        ext = float(imarea)/area1
        print ext
        if(ext>.89):
            ar = w / float(h)
            if ar >= 0.95 and ar <= 1.05:
                print "square"
                M = cv2.moments(cnt)
                cx = int(M['m10']/M['m00'])
                cy = int(M['m01']/M['m00'])
                px=img[cy,cx]
                print px
                if(px[0]>100):
                    color="Blue"
                elif(px[1]>100):
                    color="Green"
                elif(px[2]>100):
                    color="Red"
                cv2.putText(img,"Square",(cx-30,cy-25),font,.5,(0,0,0),2)
                cv2.putText(img,"(%d,%d)"%(cx,cy),(cx,cy),font,.5,(0,0,0),2)
                cv2.putText(img,"%s"%color,(cx-50,cy-50),font,.5,(0,0,0),2)



                
            else:
                print "rectangle"
                M = cv2.moments(cnt)
                cx = int(M['m10']/M['m00'])
                cy = int(M['m01']/M['m00'])
                px=img[cy,cx]
                print px
                if(px[0]>100):
                    color="Blue"
                elif(px[1]>100):
                    color="Green"
                elif(px[2]>100):
                    color="Red"
                cv2.putText(img,"Rectangle",(cx-30,cy-25),font,.5,(0,0,0),2)
                cv2.putText(img,"(%d,%d)"%(cx,cy),(cx,cy),font,.5,(0,0,0),2)
                cv2.putText(img,"%s"%color,(cx-50,cy-50),font,.5,(0,0,0),2)
                
        elif(ext>0.74 and ext <0.9):
            M = cv2.moments(cnt)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            px=img[cy,cx]
            print px
            if(px[0]>100):
                color="Blue"
            elif(px[1]>100):
                color="Green"
            elif(px[2]>100):
                color="Red"
            cv2.putText(img,"Trepizium",(cx-30,cy-25),font,.5,(0,0,0),2)
            cv2.putText(img,"(%d,%d)"%(cx,cy),(cx,cy),font,.5,(0,0,0),2)
            cv2.putText(img,"%s"%color,(cx-50,cy-50),font,.5,(0,0,0),2)






            
        elif(ext>.6 and ext <.74):
            print "rombus"           
        #    cv2.drawContours(img,[cnt],-1,(0,123,255),3)
            M = cv2.moments(cnt)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            px=img[cy,cx]
            print px
            if(px[0]>100):
                color="Blue"
            elif(px[1]>100):
                color="Green"
            elif(px[2]>100):
                 color="Red"
            cv2.putText(img,"Rombus",(cx-30,cy-25),font,.5,(0,0,0),2)
            cv2.putText(img,"(%d,%d)"%(cx,cy),(cx,cy),font,.5,(0,0,0),2)
            cv2.putText(img,"%s"%color,(cx-50,cy-50),font,.5,(0,0,0),2)        



        
    elif len(approx) == 9:
        print "half-circle"
       # cv2.drawContours(img,[cnt],-1,(0,123,255),3)
        M = cv2.moments(cnt)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        cv2.putText(img,"Circle",(cx-100,cy),font,.5,(0,0,0),2)
        cv2.putText(img,"(%d,%d)"%(cx,cy),(cx,cy),font,.5,(0,0,0),2)




        
    elif len(approx) > 15:
        print "circle"
        #cv2.drawContours(img,[cnt],-1,(0,123,255),3)
        M = cv2.moments(cnt)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        px=img[cy,cx]
        print px
        if(px[0]>100):
            color="Blue"
        elif(px[1]>100):
            color="Green"
        elif(px[2]>100):
             color="Red"
        cv2.putText(img,"Circle",(cx-30,cy-25),font,.5,(0,0,0),2)
        cv2.putText(img,"(%d,%d)"%(cx,cy),(cx,cy),font,.5,(0,0,0),2)
        cv2.putText(img,"%s"%color,(cx-50,cy-50),font,.5,(0,0,0),2)


cv2.imwrite('task1A.png',img)
cv2.imshow('img',img)
#plt.imshow(img)
#plt.show()
#cv2.imshow('asd',img)
cv2.waitKey(0)
cv2.destroyAllWindows()










