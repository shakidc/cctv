import cv2
import threading
import argparse

# Cara Kerja:
# Jika memiliki Python2 dan Python3: python3 rekam.py -n nama_berkas (tanpa ekstensi dll)
# Jika hanya memiliki Python3: python rekam.py -n nama_berkas (tanpa ekstensi dll)

ap = argparse.ArgumentParser()
ap.add_argument("-n", "--namaberkas", required=True, help="Nama Berkas Video Luaran Program")
ap.add_argument("-k", "--jmlkamera", required=True, help="Jumlah Kamera yang Digunakan")
args = vars(ap.parse_args())
nm = args["namaberkas"]
jk = int(args["jmlkamera"])

class camThread(threading.Thread):
    def __init__(self, previewName, camID):
        threading.Thread.__init__(self)
        self.previewName = previewName
        self.camID = camID
    def run(self):
        print("Mulai " + self.previewName)
        camPreview(self.previewName, self.camID)

def camPreview(previewName, camID, nm=nm):
    cv2.namedWindow(previewName)
    cam = cv2.VideoCapture(camID)
    if cam.isOpened():
        rval, frame = cam.read()
    else:
        rval = False
    frame_width = int(cam.get(3))
    frame_height = int(cam.get(4))
    out = cv2.VideoWriter(nm+str(camID)+'.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 30, (frame_width,frame_height))
    while rval:
        cv2.imshow(previewName, frame)
        rval, frame = cam.read()
        out.write(frame)
        key = cv2.waitKey(20)
        if key == 27:
            break
    cam.release()
    out.release()
    cv2.destroyWindow(previewName)

for i in range(0,jk):
    thread = camThread("Kamera "+str(i), i)
    thread.start()