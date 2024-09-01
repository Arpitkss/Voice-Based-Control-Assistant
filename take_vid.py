import cv2

def vid():
    cam= cv2.VideoCapture(0, cv2.CAP_DSHOW)

    width= int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
    height= int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

    output= cv2.VideoWriter('PY-video.mp4', cv2.VideoWriter_fourcc(*'XVID'), 20, (width,height))


    while True:
        ret,frame= cam.read()

        output.write(frame)

        cv2.imshow('Recording Video', frame)

        if cv2.waitKey(1) & 0xFF == 27:
            print("Escape hit, closing...\nVideo Saved...")
            break


    cam.release()
    output.release()
    cv2.destroyAllWindows()

    
if __name__ == '__main__':
    vid()