# Model Deteksi Objek

Script Python ini mengimplementasikan program sederhana untuk deteksi objek, mengidentifikasi objek umum dalam sebuah gambar.

Library yang digunakan: `cv2`, `numpy`, `cvlib`, `PIL`, `matplotlib`<br><br>
Program ini menggunakan model YOLOv3 untuk mendeteksi objek.<br><br>
YOLO (You Only Look Once) adalah model deteksi objek waktu nyata yang terkenal karena kecepatan dan akurasinya yang luar biasa.<br><br>
Untuk informasi lebih lanjut tentang YOLO, lihat dokumentasinya: [Dokumentasi YOLO](https://pjreddie.com/darknet/yolo/)

## Menjalankan Proyek Secara Lokal

Instal library yang dibutuhkan:

```bash
pip install -r requirements.txt
```

### Menjalankan di Terminal

```bash
python objectdetection.py
```

Program ini dirancang untuk memproses satu gambar pada satu waktu. Jika Anda ingin bereksperimen dengan gambar yang berbeda, berikan gambar tersebut sebagai input ke program.

Untuk wawasan lebih lanjut tentang Deteksi Objek dengan OpenCV, jelajahi sumber daya berikut:<br><br>
[PyImageSearch - Deteksi Objek YOLO dengan OpenCV](https://www.pyimagesearch.com/2018/11/12/yolo-object-detection-with-opencv/)
