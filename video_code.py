import cv2

# Load the videos
video1 = cv2.VideoCapture("orgdog.mp4")
video2 = cv2.VideoCapture("dogwithtext.mp4")
# video2 = cv2.VideoCapture("orgdog.mp4")

# Check if the videos were successfully loaded
if not video1.isOpened() or not video2.isOpened():
    print("Error opening video file(s)")

# Get the frame width and height
frame_width = int(video1.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(video1.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*"H264")
out = cv2.VideoWriter("difference.mp4", fourcc, 30.0, (frame_width, frame_height))

while True:
    # Read the next frame from each video
    success1, frame1 = video1.read()
    success2, frame2 = video2.read()

    # If either video has reached the end, break the loop
    if not success1 or not success2:
        break

    # Compare the frames and write the difference to the output video
   
    difference = cv2.absdiff(frame1, frame2)
    # print(type(difference))
    
    # if difference.any():
    #     a=0
    #     for i in difference:
    #         # print(difference)
    #         # print(difference.any())
    #         # print('its not same')
    #         cv2.imwrite('frame{}.jpg'.format(a),difference)
    #         print(f"created file{a}")
    #         a = a+1
    # else:
        
    #     print(difference)
    #     print(difference.any())
    #     print("its same")
    out.write(difference)

# Release the video capture and write objects
video1.release()
video2.release()
out.release()
