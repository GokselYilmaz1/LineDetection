import cv2
import numpy as np

video = cv2.VideoCapture("driveday.mp4")  # Video dosyasını yükler.

while True:
    ret, orig_frame = video.read()
    if not ret:
        video = cv2.VideoCapture("driveday.mp4")
        continue

    frame = cv2.GaussianBlur(orig_frame, (5, 5), 0)  # Gürültüyü azaltmak için görüntüyü bulanıklaştırır.
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # Görüntüyü HSV renk uzayına dönüştürür.
    
    # Beyaz çizgileri maskelemek için HSV aralığı
    lower_white = np.array([0, 0, 200])     # Alt sınır: H: 0-180, S: 0-30, V: 200-255
    upper_white = np.array([180, 30, 255])  # Üst sınır: H: 0-180, S: 0-30, V: 200-255
    
    mask = cv2.inRange(hsv, lower_white, upper_white)  # Beyaz çizgileri maskelemek için belirli bir HSV aralığını kullanır.
    
    # Yalnızca yol bölgesini maskelemek için görüntünün alt yarısını kullanır.
    # (Region of Interest)
    height, width = mask.shape
    roi = mask[int(height/2):, :]  # Yalnızca alt yarıyı kullan
    
    # Histogram eşitleme
    equalized = cv2.equalizeHist(roi)  # Kontrastı artırmak için histogram eşitleme uygular.
    
    # Kenar algılama (Sobel)
    # Sobel operatörü ile kenarları algılar.
    sobelx = cv2.Sobel(equalized, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(equalized, cv2.CV_64F, 0, 1, ksize=5)

    # Kenarların büyüklüğünü hesaplar.
    edges = cv2.magnitude(sobelx, sobely)
    edges = np.uint8(edges)
    
    # HoughLinesP ile çizgileri algılama
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, minLineLength=50, maxLineGap=50) #Hough dönüşümü ile çizgileri algılar ve yeşil çizgilerle çizer.

    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(frame, (x1, y1 + int(height/2)), (x2, y2 + int(height/2)), (0, 255, 0), 5)  # Yeşil çizgiler
    
    # Orijinal ve kenar algılama sonuçlarını gösterir
    cv2.imshow("frame", frame) 
    cv2.imshow("edges", edges) 

    # Belirli bir tuşa basılana kadar bekler.
    key = cv2.waitKey(25)
    if key == 27:
        break

video.release()
cv2.destroyAllWindows()