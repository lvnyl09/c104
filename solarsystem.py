import cv2

img = cv2.imread("solar-system.jpg")

font = cv2.FONT_HERSHEY_SIMPLEX
color = (255, 255, 255)

cv2.putText(img, "Sun", (50, 250), font, 0.45, color, 2)
cv2.putText(img, "Mercury", (125, 250), font, 0.45, color, 2)
cv2.putText(img, "Venus", (200, 250), font, 0.45, color, 2)
cv2.putText(img, "Earth", (290, 250), font, 0.45, color, 2)
cv2.putText(img, "Moon", (295, 170), font, 0.45, color, 2)
cv2.putText(img, "Mars", (380, 250), font, 0.45, color, 2)
cv2.putText(img, "Jupiter", (590, 250), font, 0.45, color, 2)
cv2.putText(img, "Saturn", (775, 250), font, 0.45, color, 2)
cv2.putText(img, "Uranus", (975, 250), font, 0.45, color, 2)
cv2.putText(img, "Neptune", (1125, 250), font, 0.45, color, 2)

cv2.imshow("output", img)

cv2.waitKey(0)

cv2.imwrite("Solar_systemwithname.jpg", img)
