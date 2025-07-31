import cv2
import matplotlib.pyplot as plt
import pyzbar.pyzbar as pyzbar

img = cv2.imread('../img/bh_bar.jpg')
plt.imshow(img)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()