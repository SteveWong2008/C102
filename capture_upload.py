import cv2
import dropbox
import time
import random

start_time = time.time()

def take_snapshot():
    num = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret, frame = videoCaptureObject.read()
        img_name = "img" + str(num) + ".png"
        cv2.imwrite(img_name, frame)
        star_time = time.time
        result = False

    print("snapshot_taken")
    
    videoCaptureObject.release()
    cv2.destroyAllWindows()
    return img_name


def upload_file(img_name):
    access_token = 'sl.BudKVp323wwKmoJlwEJ80vK9UjjFDjOhdOusoheyPU2e-4Fa-Er_sfZU8fMci9FceUM-2QfdbtnUJZRM8ujGRluulnxgLyMAgNxOQgSyHuAYpIoMin85DSxYTMd0l9yIqbnrVwGWJGAVX3I'
    file = img_name
    file_from = "C:/Python/C102/"+file
    file_to = "/TestFolder/" + (img_name)
    dbx = dropbox.Dropbox(access_token)
    
    
    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print('file uploaded')
    
def main():
    while (True):
        if((time.time()-start_time)>=5):
            name = take_snapshot()
            upload_file(name)
        

main()


