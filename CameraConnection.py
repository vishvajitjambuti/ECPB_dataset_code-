"""Access IP Camera in Python OpenCV"""
import cv2


def captureVideo():
    camera_front = cv2.VideoCapture('rtsp://172.16.128.10:8554/jpeg')
    camera_back = cv2.VideoCapture('rtsp://172.16.128.11:8554/jpeg')
    camera_left = cv2.VideoCapture('rtsp://172.16.128.12:8554/jpeg')
    camera_right = cv2.VideoCapture('rtsp://172.16.128.13:8554/jpeg')

    width = int(camera_front.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(camera_front.get(cv2.CAP_PROP_FRAME_HEIGHT))

    filename = 40;
    out1 = cv2.VideoWriter("1.avi", cv2.VideoWriter_fourcc(*'MJPG'), 25, (width, height))
    out2 = cv2.VideoWriter("2.avi", cv2.VideoWriter_fourcc(*'MJPG'), 25, (width, height))
    out3 = cv2.VideoWriter("3.avi", cv2.VideoWriter_fourcc(*'MJPG'), 25, (width, height))
    out4 = cv2.VideoWriter("4.avi", cv2.VideoWriter_fourcc(*'MJPG'), 25, (width, height))

    while (True):
        ret1, image_front = camera_front.read()
        ret2, image_back = camera_back.read()
        ret3, image_left = camera_left.read()

        ret4, image_right = camera_right.read()

        ret1, frame1 = camera_front.read()
        out1.write(frame1)
        ret2, frame2 = camera_back.read()
        out2.write(frame2)
        ret3, frame3 = camera_left.read()
        out3.write(frame3)
        ret4, frame4 = camera_right.read()
        out4.write(frame4)
        continue

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera_front.release()
    camera_back.release()
    camera_left.release()
    camera_right.release()

    cv2.destroyAllWindows()


captureVideo()