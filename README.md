# Görüntü İşleme Stüdyosu / Image Processing Studio

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PySide6](https://img.shields.io/badge/PySide6-41CD52?style=for-the-badge&logo=qt&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)

---

### 🇹🇷 Türkçe

#### Proje Amacı ve Motivasyon

Bu proje, görüntü işleme (image processing) konularını yeni öğrenen biri olarak bilgilerimi pekiştirmek amacıyla geliştirdiğim bir alıştırma uygulamasıdır. Görüntü işlemenin temellerini ve bu işlemlerin masaüstü bir uygulamada nasıl sunulabileceğini merak ediyordum.

Temel amacım, **PySide6 (Qt for Python)** kullanarak modern bir masaüstü arayüzü (GUI) oluşturmayı ve bu arayüzü **OpenCV** kütüphanesinin temel görüntü filtreleme yetenekleriyle entegre etmeyi öğrenmektir.

Uygulama, temel filtreleme adımlarını içermektedir ve görüntü işleme alanındaki öğrenme yolculuğumun bir parçasıdır.

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
* **PySide6 (Qt):** Masaüstü uygulamasının görsel arayüzü için kullanıldı.
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

#### Project Purpose and Motivation

This is a practice application I developed to reinforce my knowledge, as I am new to the field of image processing. I was curious about the fundamentals of image processing and how these operations could be presented in a desktop application.

My primary goal was to learn how to build a modern desktop GUI using **PySide6 (Qt for Python)** and integrate it with the basic image filtering capabilities of the **OpenCV** library.

The application includes fundamental filtering steps and is a part of my learning journey in image processing.

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
