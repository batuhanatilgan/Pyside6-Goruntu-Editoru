# Görüntü İşleme Stüdyosu / Image Processing Studio

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PySide6](https://img.shields.io/badge/PySide6-41CD52?style=for-the-badge&logo=qt&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)

---

### 🇹🇷 Türkçe

Python, PySide6 ve OpenCV kullanılarak oluşturulmuş basit bir masaüstü görüntü işleme uygulaması.

Bu proje, bir masaüstü uygulamasında temel görüntü işleme filtrelerinin nasıl uygulanacağını ve PySide6 (Qt for Python) kütüphanesinin OpenCV ile nasıl entegre edileceğini göstermek amacıyla geliştirilmiştir.

#### Özellikler

* **Resim Yükle:** Bilgisayarınızdan `.png`, `.jpg`, `.bmp` formatındaki resimleri yükleyin.
* **Resim Kaydet:** İşlenmiş görüntüyü bilgisayarınıza kaydedin.
* **Filtreler:**
    * Gri Tonlama (Grayscale)
    * Bulanıklaştır (Gaussian Blur)
    * Keskinleştir (Sharpen)
    * Gürültü Ekle (Noise)
* **Sıfırla:** Uygulanan tüm filtreleri temizleyerek görüntüyü orijinal haline döndürün.

#### Kullanılan Teknolojiler

* **Python 3:** Ana programlama dili.
* **PySide6 (Qt):** Masaüstü uygulamasının görsel arayüzü (GUI) için kullanıldı.
* **OpenCV-Python:** Görüntüleri okuma, yazma ve filtreleme işlemleri için kullanıldı.
* **NumPy:** Görüntü matrisleri ve gürültü filtresi için gerekli matematiksel hesaplamalarda kullanıldı.

#### Nasıl Çalıştırılır?

1.  Projeyi klonlayın veya indirin.
2.  Gerekli kütüphaneleri yükleyin:
    ```bash
    pip install PySide6 opencv-python numpy
    ```
3.  Ana script'i çalıştırın:
    ```bash
    python GoruntuStudyosu.py
    ```
    *(Dosya adınız farklıysa, `python dosya_adin.py` şeklinde çalıştırın.)*

---

### 🇬🇧 English

A simple desktop image processing application built with Python, PySide6, and OpenCV.

This project was developed to demonstrate how to apply basic image processing filters in a desktop application and how to integrate the PySide6 (Qt for Python) library with OpenCV.

#### Features

* **Load Image:** Load images from your computer in `.png`, `.jpg`, or `.bmp` formats.
* **Save Image:** Save the processed image to your computer.
* **Filters:**
    * Grayscale
    * Gaussian Blur
    * Sharpen
    * Add Noise
* **Reset:** Clear all applied filters and revert the image to its original state.

#### Technologies Used

* **Python 3:** The core programming language.
* **PySide6 (Qt):** Used for the graphical user interface (GUI) of the desktop app.
* **OpenCV-Python:** Used for reading, writing, and filtering images.
* **NumPy:** Used for image matrix operations and mathematical calculations, especially for the noise filter.

#### How to Run

1.  Clone or download the project.
2.  Install the required libraries:
    ```bash
    pip install PySide6 opencv-python numpy
    ```
3.  Run the main script:
    ```bash
    python GoruntuStudyosu.py
    ```
    *(If your file name is different, run it as `python your_file_name.py`.)*
