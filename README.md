Highway Lane Detection

--EN

🚗 **Lane Detection Project for Autonomous Vehicles** 🚗

In this project, I developed an algorithm using OpenCV to detect lane lines in a video. Here are the steps:

1. **Video Loading and Reading**: Loaded the video file and read each frame.
2. **Image Processing**: Applied Gaussian blur to reduce noise and converted the image to HSV color space.
3. **White Line Masking**: Masked white lines using a specific HSV range.
4. **Region of Interest (ROI)**: Masked only the road region by using the lower half of the image.
5. **Histogram Equalization**: Enhanced contrast using histogram equalization.
6. **Edge Detection**: Detected edges using the Sobel operator.
7. **Line Detection**: Detected lines using the Hough transform and drew green lines.
8. **Displaying the Image**: Displayed the original and edge-detected images.

--TR
🚗 **Otonom Araçlar İçin Yol Çizgisi Algılama Projesi** 🚗

Bu projede, OpenCV kullanarak bir video üzerinde yol çizgilerini algılayan bir algoritma geliştirdim. İşte adımlar:

1. **Video Yükleme ve Okuma**: Video dosyasını yükleyip her kareyi okudum.
2. **Görüntü İşleme**: Gürültüyü azaltmak için bulanıklaştırma ve HSV renk uzayına dönüştürme işlemleri yaptım.
3. **Beyaz Çizgileri Maskeleme**: Belirli bir HSV aralığında beyaz çizgileri maskeledim.
4. **ROI (Region of Interest)**: Yalnızca yol bölgesini maskeledim.
5. **Histogram Eşitleme**: Kontrastı artırmak için histogram eşitleme uyguladım.
6. **Kenar Algılama**: Sobel operatörü ile kenarları algıladım.
7. **Çizgi Algılama**: Hough dönüşümü ile çizgileri algılayıp yeşil çizgilerle çizdim.
8. **Görüntü Gösterimi**: Orijinal ve kenar algılama sonuçlarını gösterdim.
