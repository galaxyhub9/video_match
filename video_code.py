import cv2

video1 = cv2.VideoCapture("orgdog.mp4")
video2 = cv2.VideoCapture("dogwithtext.mp4")
if not video1.isOpened() or not video2.isOpened():
    print("Error occured to open file")
frame_width = int(video1.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(video1.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*"H264")
out = cv2.VideoWriter("difference.mp4", fourcc, 30.0, (frame_width, frame_height))
while True:
    success1, frame1 = video1.read()
    success2, frame2 = video2.read()

    if not success1 or not success2:
        break   
    difference = cv2.absdiff(frame1, frame2)
    out.write(difference)
video1.release()
video2.release()
out.release()
