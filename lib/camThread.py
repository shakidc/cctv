import cv2
import threading
import time


class camThread(threading.Thread):
    def __init__(self, previewName, camID, filename, fps=30):
        threading.Thread.__init__(self)
        self.previewName = previewName
        self.camID = camID
        self.filename = filename
        self.fps = fps

    def run(self):
        print("Recording: " + self.previewName)
        camPreview(self.previewName, self.camID, self.fps, self.filename)


def printf(*text):
    print(*text, end='\r', flush=True)


def camPreview(previewName, camID, fps, filename):
    nm = filename
    cv2.namedWindow(previewName)
    cam = cv2.VideoCapture(camID)
    if cam.isOpened():
        rval, frame = cam.read()
    else:
        rval = False
    frame_width = int(cam.get(3))
    frame_height = int(cam.get(4))
    out = cv2.VideoWriter(nm + str(camID) + '.avi', cv2.VideoWriter_fourcc(*"MJPG"), fps, (frame_width, frame_height))
    start_rec = time.time()
    while rval:
        cv2.imshow(previewName, frame)
        rval, frame = cam.read()
        out.write(frame)
        key = cv2.waitKey(20)

        currentTime = int(time.time() - start_rec)
        printf("Recording:", currentTime * 30 / fps, 'seconds')

        if key == 27:
            print("Recording:", currentTime * 30 / fps, 'seconds')
            break
    cam.release()
    out.release()
    cv2.destroyWindow(previewName)
