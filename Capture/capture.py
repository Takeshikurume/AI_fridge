import serial
import cv2
import datetime
import time
import os
ser = serial.Serial('COM3', 9600) # ここのポート番号を変更
ser.readline()
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
count = 0
print("Plase Enter Filename")
filename = input()

 
if not os.path.exists(filename):# ディレクトリが存在しない場合、ディレクトリを作成する
    os.makedirs(filename)

print("Start Capturing")
while(count<10):
    val_arduino = ser.readline()
    val_decoded = int(repr(val_arduino.decode())[1:-5]) #arudino から値取得
    

    if(val_decoded>100):
        ret,frame = cap.read() # 画像保存
        nowtime = datetime.datetime.now()
        timestr = nowtime.strftime("%Y_%m_%d_%H_%M_%S")
        print(filename + "/"+str(timestr) + ".png")
        cv2.imwrite(filename + "/"+str(timestr) + ".png", frame) #画像保存

    
    time.sleep(1)
    count+=1
print("Finish Capturing")
ser.close()
cap.release()
cv2.destroyAllWindows()


