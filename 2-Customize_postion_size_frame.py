import cv2

width = 1280
height = 720

cam = cv2.VideoCapture(1)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)

 
while True:
    rows = int(input("Enter rows: "))     
    columns = int(input("Enter columns: "))   
    if columns > 0 and rows > 0:
        break
    print("Rows and columns must be > 0")

while True:
    ret, frame = cam.read()
    if not ret:
        break

    # Calculate frame size
    frame_width = int(width / columns)   # 1280/2 = 640
    frame_height = int(height / rows)    # 720/2 = 360

    # Resize frame
    frame = cv2.resize(frame, (frame_width, frame_height))

    # Show multiple windows in grid
    for i in range(rows):
        for j in range(columns):
            windNam=f'Window{i}x{j}'
            cv2.imshow(windNam, frame)
            cv2.moveWindow(windNam, frame_width * j, (frame_height+30)* i  )

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()

'''


i:0 j:0 : cv2.movewindow('frame',0,0)
i:0 j:1 : cv2.movewindow('frame',640,0) 
i:1 j:0 : (0,360)
i:1 j:1:    (640,360)
'''
