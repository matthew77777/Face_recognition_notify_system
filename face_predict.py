import face_recognition
import cv2
import numpy as np
import subprocess
import sys

# 閾値
th = 0.5

#名前指定
my_name = 'masu'

#カウンタ変数を定義
cnt = 0

# VideoStreamを使い、カメラの画像取り込み
#video_capture = VideoStream(src=0).start()
video_capture = cv2.VideoCapture(0)

# 画像をimage_oneに読み込む
image_my_photo = cv2.imread('test_data/photo.jpg')

# 画像データをRGB形式で取り扱う
rgb_data = cv2.cvtColor(image_my_photo, cv2.COLOR_BGR2RGB)

# CNNを用いて128次元の顔の特徴量を取得
face_encoding = face_recognition.face_encodings(rgb_data)[0]

# 既知の顔の特徴量の配列
known_face_photo = [
    face_encoding
]

# 既知の顔のラベル配列
face_names = [my_name]

# ハールカスケード分類器を読み込み
face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    # カメラからframeを取得
    ret,frame = video_capture.read()
    print(frame)
 
    # 640幅500ピクセルに縮小
    ratio = 500 / frame.shape[1]
    frame = cv2.resize(frame, dsize=None, fx=ratio, fy=ratio)
 
    # 画像をグレースケールにしgrayに保存
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 
    # 画像をBGRからRGBへ変更しrgbに保存
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
 
    # ハールカスケードで顔検出し座標をface_locationsへ保存
    face_locations = face_detector.detectMultiScale(gray, scaleFactor=1.1,
        minNeighbors=5, minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE)
 
    # ボックス座標の表現形式を変換
    face_locations = [(y, x + w, y + h, x) for (x, y, w, h) in face_locations]
 
    # 見つかったすべての顔をCNNに入力しそれぞれの顔の128次元特徴量をface_encodingsに保存
    face_encodings = face_recognition.face_encodings(rgb, face_locations)

    # 繰り返し顔の特徴量を取得
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):

        name = "UNKNOWN"

        # 保存済みの顔との差を求める
        face_distances = face_recognition.face_distance(known_face_photo, face_encoding)
        
        # 距離が最小の既知の顔のインデックスを取得
        index = np.argmin(face_distances)
        
        # 特徴量の距離が閾値より小さければ
        if face_distances[index] < th:
            # 最も特徴量が近い名前を取得
            name = face_names[index]
        
        if name == 'UNKNOWN':
            cnt += 1
            if cnt > 7:
                subprocess.run("./app_stop.sh")
                subprocess.run("./line_notify.sh")
                path = "./static/cam_photo.jpg"
                cv2.imwrite(path,frame)
                print("データが保存されました")
                subprocess.run("python app.py", shell=True)
                cnt = 0
                cv2.destroyAllWindows()
                video_capture.release()
                sys.exit()

        # 枠を描画
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

        # 枠の下方に名前を描画
        cv2.rectangle(frame, (left, bottom - 20), (right, bottom), (255, 255, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (0, 0, 0), 1)

    # 画像を表示
    cv2.imshow('Video', frame)

    # 「q」が入力されたら終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 終了処理
cv2.destroyAllWindows()
video_capture.stop()

