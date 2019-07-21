import glob
import cv2
import os

def getflist():
    qn=glob.glob("BOOT1/*jpg")
    flst=[]
    #print(qn)
    for k in range(1,len(qn)+1):
        nj='{:04d}'.format(k)+".jpg"
        for j in qn:
            if j.find(nj)!=-1:
                #print(nj,j)
                flst.append(j)
    return flst
def main():
     
    video_name = 'test.avi'
    images=getflist()
    frame = cv2.imread(images[0])
    height, width, layers = frame.shape
    video = cv2.VideoWriter(video_name, 0, 10, (width,height))
    for image in images:
        video.write(cv2.imread(image))

    cv2.destroyAllWindows()
    video.release()





main()

