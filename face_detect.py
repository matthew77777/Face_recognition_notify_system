import cv2
import numpy as np


#Webカメラから入力を開始
cap = cv2.VideoCapture(1)
cnt = 0 

#顔の検出器を作成
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#カメラから連続して映像を取得
while True:

    #カメラの画像を読み込む
    ret, frame = cap.read()
    
    #画像のサイズを変更（リサイズ）
    frame = cv2.resize(frame, (500, 300))
    
    #グレイスケールに変換
    gray_flame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #print(gray_flame)
    
    #顔認証を実行(minNeighboreは信頼性のパラメータ)
    face_list = face_cascade.detectMultiScale(gray_flame, minNeighbors=20)
    print(face_list)
    print(type(face_list))
    
    #顔を四角で囲む
    for (x,y,w,h) in face_list:
        
        red = (0,0,255)

        #赤色の枠で囲む
        cv2.rectangle(frame, (x,y), (x+w,y+h), red, 1)

    if(face_list != 0):
        print("HELLO")             
        
    #ウィンドウに画像を出力
    cv2.imshow("My_Face", frame)
    
    
    #もし，Enterキーが押されたら終了
    exit_wind = cv2.waitKey(1)

    if exit_wind == 13: break


#------------------------------------------------
    
#カメラを終了
cap.release()

#ウィンドウを閉じる
cv2.destroyAllWindows()

#------------------------------------------------

 
