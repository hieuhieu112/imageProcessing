import cv2
import pandas as pd
import numpy as np
from ultralytics import YOLO
from tracker import *
import time
def run_speed():
    # Khởi tạo mô hình YOLO từ tệp 'yolov8s.pt'
    model = YOLO('yolov8s.pt')

    # Hàm xử lý sự kiện di chuyển chuột
    def RGB(event, x, y, flags, param):
        if event == cv2.EVENT_MOUSEMOVE:
            colorsBGR = [x, y]
            #print(colorsBGR)

    # Tạo một cửa sổ OpenCV có tên 'RGB' và thiết lập hàm gọi lại chuột cho cửa sổ đó
    cv2.namedWindow('RGB')
    cv2.setMouseCallback('RGB', RGB)

    # Mở tệp video 'veh2.mp4'
    cap = cv2.VideoCapture('veh2.mp4')

    # Đọc dữ liệu từ tệp 'tctc.txt' và tạo danh sách các lớp
    my_file = open("D:\\document\\unknow\\nam 4\\hk1\\XLA\\FinalImageProcessing\\FinalImageProcessing\\tctc.txt", "r")
    data = my_file.read()
    class_list = data.split("\n")
    # print(class_list)

    # Khởi tạo biến đếm và tracker
    count = 0
    tracker = Tracker()

    # Khai báo các biến liên quan đến đo tốc độ và theo dõi hướng di chuyển
    cy1 = 322
    cy2 = 368

    offset = 6# sai số

    vh_down = {}
    counter = []

    vh_up = {}
    counter1 = []

    while True:
        # Đọc một khung hình từ video
        ret, frame = cap.read()
        if not ret:
            break
        count += 1
        if count % 3 != 0:
            continue
        frame = cv2.resize(frame, (1020, 500))

        # Dự đoán đối tượng trong khung hình bằng mô hình YOLO
        results = model.predict(frame) # truyền ảnh vô ->
        # print(results)
        a = results[0].boxes.data
        #print("a:",a)
        px = pd.DataFrame(a).astype("float")
        #print(px)
        list = []

        # Lọc ra các đối tượng là xe trong khung hình
        for index, row in px.iterrows():
            #        print(row)

            x1 = int(row[0])
            y1 = int(row[1])
            x2 = int(row[2])
            y2 = int(row[3])
            d = int(row[5])
            c = class_list[d]

            if 'car' in c:
                list.append([x1, y1, x2, y2])

        # Cập nhật thông tin về đối tượng từ tracker
        bbox_id = tracker.update(list)
        # print(bbox_id)


        for bbox in bbox_id:
            x3, y3, x4, y4, id = bbox
            cx = int(x3 + x4) // 2
            cy = int(y3 + y4) // 2

            # Vẽ hình chữ nhật xung quanh đối tượng và thông tin tốc độ
            cv2.rectangle(frame, (x3, y3), (x4, y4), (0, 0, 255), 2)

            # Xác định hướng di chuyển của đối tượng và tính tốc độ
            if cy1 < (cy + offset) and cy1 > (cy - offset):
                vh_down[id] = time.time()
            if id in vh_down:

                if cy2 < (cy + offset) and cy2 > (cy - offset):
                    elapsed_time = time.time() - vh_down[id]    # tgian di chuyển L1-L2
                    if counter.count(id) == 0:
                        counter.append(id)                      # cho id xe đó vào counter
                        distance = 10  # meters
                        a_speed_ms = distance / elapsed_time
                        a_speed_kh = a_speed_ms * 3.6
                        cv2.circle(frame, (cx, cy), 4, (0, 0, 255), -1)
                        cv2.putText(frame, str(id), (x3, y3), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 255, 255), 1)
                        cv2.putText(frame, str(int(a_speed_kh)) + 'Km/h', (x4, y4), cv2.FONT_HERSHEY_COMPLEX, 0.8,
                                    (0, 255, 255), 2)
                        #vẽ hình tròn + mấy thông số của cái xe

            #####going UP#####
            # Xác định hướng di chuyển và tính tốc độ khi xe đi lên, tương tự phía trên
            if cy2 < (cy + offset) and cy2 > (cy - offset):
                vh_up[id] = time.time()
            if id in vh_up:

                if cy1 < (cy + offset) and cy1 > (cy - offset):
                    elapsed1_time = time.time() - vh_up[id]

                    if counter1.count(id) == 0:
                        counter1.append(id)
                        distance1 = 10  # meters
                        a_speed_ms1 = distance1 / elapsed1_time
                        a_speed_kh1 = a_speed_ms1 * 3.6
                        cv2.circle(frame, (cx, cy), 4, (0, 0, 255), -1)
                        cv2.putText(frame, str(id), (x3, y3), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 255, 255), 1)
                        cv2.putText(frame, str(int(a_speed_kh1)) + 'Km/h', (x4, y4), cv2.FONT_HERSHEY_COMPLEX, 0.8,
                                    (0, 255, 255), 2)

        cv2.line(frame, (274, cy1), (814, cy1), (255, 255, 255), 1)

        cv2.putText(frame, ('L1'), (277, 320), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 255), 2)

        cv2.line(frame, (177, cy2), (927, cy2), (255, 255, 255), 1)

        cv2.putText(frame, ('L2'), (182, 367), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 255), 2)
        d = (len(counter))
        u = (len(counter1))
        print("D: ", d)
        print("U: ", u)
        cv2.putText(frame, ('goingdown:-') + str(d), (60, 90), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 255), 2)

        cv2.putText(frame, ('goingup:-') + str(u), (60, 130), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 255), 2)
        cv2.imshow("RGB", frame)
        if cv2.waitKey(1) & 0xFF ==ord('s'):
            break
    cap.release()
    cv2.destroyAllWindows()

