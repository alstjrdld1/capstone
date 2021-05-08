from picamera import PiCamera
from time import sleep
import socket 
import cv2

buf = 1024
address = ('192.168.50.1', 8080)

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print('Sender Socket Initialized')
except:
    print("fail")  
    
#camera = PiCamera()
vid = cv2.VideoCapture(-1)

i = 0
while(True):
    ret, frame = vid.read()
    cv2.imshow('frame', frame)
    cv2.imwrite('/home/pi/Desktop/frames/{}.jpg'.format(i), frame)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.sendto('{}.jpg'.format(i).encode(), address)
    print('sending file_name to server....')
    f = open('/home/pi/Desktop/frames/{}.jpg'.format(i), 'rb')
    i += 1
    if(f):
        print("yes")
    data = f.read(buf)
    while(data):
        if(s.sendto(data,address)):
            print('sending...')
            data = f.read(buf)
    s.close()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
vid.release()
cv2.destroyAllWindows()