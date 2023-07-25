import cv2

def edge_detection(frame):
  gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
  edges=cv2.Canny(gray_frame , 79, 78)
  return edges

vid = cv2.VideoCapture(0)
while(True):	
    ret, frame = vid.read()
    #print(ret)
    edges=edge_detection(frame)
    combined_frames=cv2.hconcat([frame, cv2.cvtColor(edges,cv2.COLOR_GRAY2BGR)])
    cv2.imshow("framewin", combined_frames)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
vid.release()
cv2.destroyAllWindows()
