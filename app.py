import sys
import cv2
import numpy as np
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, 
    QPushButton, QLabel, QVBoxLayout, 
    QHBoxLayout, QFileDialog, QGroupBox
)
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Qt

class GoruntuStudyosu(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Temel Görüntü İşleme Stüdyosu (PySide6 + OpenCV)")
        self.setGeometry(100, 100, 1000, 700)

        self.ana_bilesen = QWidget()
        self.setCentralWidget(self.ana_bilesen)
        
        self.ana_duzen = QHBoxLayout()
        self.ana_bilesen.setLayout(self.ana_duzen)

        # --- Sol Taraf: Kontroller ---
        self.kontrol_duzeni = QVBoxLayout()
        self.kontrol_kutusu = QGroupBox("İşlemler")
        self.kontrol_kutusu.setLayout(self.kontrol_duzeni)
        self.kontrol_kutusu.setMaximumWidth(250)

        self.btn_resim_yukle = QPushButton("Resim Yükle")
        self.btn_resim_yukle.clicked.connect(self.resim_yukle)
        self.kontrol_duzeni.addWidget(self.btn_resim_yukle)

        self.btn_resim_kaydet = QPushButton("Resim Kaydet")
        self.btn_resim_kaydet.clicked.connect(self.resim_kaydet)
        self.kontrol_duzeni.addWidget(self.btn_resim_kaydet)
        
        self.kontrol_duzeni.addSpacing(20)

        self.btn_gri_tonlama = QPushButton("Gri Tonlama")
        self.btn_gri_tonlama.clicked.connect(self.filtre_gri_tonlama_uygula)
        self.kontrol_duzeni.addWidget(self.btn_gri_tonlama)

        self.btn_bulaniklastir = QPushButton("Bulanıklaştır")
        self.btn_bulaniklastir.clicked.connect(self.filtre_bulaniklastir_uygula)
        self.kontrol_duzeni.addWidget(self.btn_bulaniklastir)

        self.btn_keskinlestir = QPushButton("Keskinleştir")
        self.btn_keskinlestir.clicked.connect(self.filtre_keskinlestir_uygula)
        self.kontrol_duzeni.addWidget(self.btn_keskinlestir)
        
        self.btn_gurultu_ekle = QPushButton("Gürültü Ekle")
        self.btn_gurultu_ekle.clicked.connect(self.filtre_gurultu_ekle_uygula)
        self.kontrol_duzeni.addWidget(self.btn_gurultu_ekle)
        
        self.kontrol_duzeni.addSpacing(40)

        self.btn_sifirla = QPushButton("Sıfırla (Orijinale Dön)")
        self.btn_sifirla.setStyleSheet("background-color: #ffc107; color: black;")
        self.btn_sifirla.clicked.connect(self.resmi_sifirla)
        self.kontrol_duzeni.addWidget(self.btn_sifirla)

        self.kontrol_duzeni.addStretch(1)

        # --- Sağ Taraf: Resim Alanı ---
        self.resim_etiketi = QLabel("Lütfen bir resim yükleyin...")
        self.resim_etiketi.setAlignment(Qt.AlignCenter)
        self.resim_etiketi.setMinimumSize(400, 400)
        self.resim_etiketi.setStyleSheet("border: 1px solid #ccc; background-color: #f0f0f0;")

        self.ana_duzen.addWidget(self.kontrol_kutusu)
        self.ana_duzen.addWidget(self.resim_etiketi, 1) # '1' -> bu alan genişlesin

        # Görüntü verileri
        self.orijinal_goruntu = None
        self.islenmis_goruntu = None
        self.mevcut_pixmap = None

    # --- Ana Fonksiyonlar ---

    def resim_yukle(self):
        dosya_adi, _ = QFileDialog.getOpenFileName(self, "Resim Aç", "", "Resim Dosyaları (*.png *.jpg *.bmp)")
        
        if dosya_adi:
            self.orijinal_goruntu = cv2.imread(dosya_adi)
            if self.orijinal_goruntu is None:
                print(f"Hata: Resim okunamadı! Dosya yolu: {dosya_adi}")
                return
            
            self.islenmis_goruntu = self.orijinal_goruntu.copy()
            
            self.cv_goruntuden_pixmap_guncelle(self.islenmis_goruntu)
            self.pixmapi_olceklendir_ve_goster()

    def resim_kaydet(self):
        if self.islenmis_goruntu is None:
            print("Kaydedilecek bir resim yok.")
            return

        dosya_adi, _ = QFileDialog.getSaveFileName(self, "Resim Kaydet", "", "PNG Dosyası (*.png);;JPEG Dosyası (*.jpg)")

        if dosya_adi:
            cv2.imwrite(dosya_adi, self.islenmis_goruntu)
            print(f"Resim şuraya kaydedildi: {dosya_adi}")

    def cv_goruntuden_pixmap_guncelle(self, cv_goruntu):
        
        if len(cv_goruntu.shape) == 2: # Gri tonlamalı
            h, w = cv_goruntu.shape
            bytes_per_line = w
            q_resim = QImage(cv_goruntu.data, w, h, bytes_per_line, QImage.Format_Grayscale8)
        elif len(cv_goruntu.shape) == 3: # Renkli (BGR)
            # OpenCV BGR kullanır, QImage RGB ister -> çevrim şart
            rgb_goruntu = cv2.cvtColor(cv_goruntu, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_goruntu.shape
            bytes_per_line = ch * w
            q_resim = QImage(rgb_goruntu.data, w, h, bytes_per_line, QImage.Format_RGB888)
        else:
            return

        self.mevcut_pixmap = QPixmap.fromImage(q_resim)

    def pixmapi_olceklendir_ve_goster(self):
        if self.mevcut_pixmap:
            self.resim_etiketi.setPixmap(self.mevcut_pixmap.scaled(
                self.resim_etiketi.size(), 
                Qt.KeepAspectRatio, 
                Qt.SmoothTransformation
            ))

    def resizeEvent(self, event):
        # Ekranda bir resim varsa, onu yeni boyuta göre yeniden ölçekle
        self.pixmapi_olceklendir_ve_goster()
        super().resizeEvent(event)
        
    def _resim_yuklendi_mi(self):
        if self.islenmis_goruntu is None:
            print("Lütfen önce bir resim yükleyin.")
            return False
        return True
        
    # --- Filtre Fonksiyonları ---

    def filtre_gri_tonlama_uygula(self):
        if not self._resim_yuklendi_mi(): return
        
        gri_goruntu = cv2.cvtColor(self.islenmis_goruntu, cv2.COLOR_BGR2GRAY)
        # Diğer filtrelerle uyumluluk için 3 kanala geri çevir
        self.islenmis_goruntu = cv2.cvtColor(gri_goruntu, cv2.COLOR_GRAY2BGR)
        
        self.cv_goruntuden_pixmap_guncelle(self.islenmis_goruntu)
        self.pixmapi_olceklendir_ve_goster()

    def filtre_bulaniklastir_uygula(self):
        if not self._resim_yuklendi_mi(): return

        # (21, 21) kernel boyutu, tek sayı olmalı
        self.islenmis_goruntu = cv2.GaussianBlur(self.islenmis_goruntu, (21, 21), 0)
        
        self.cv_goruntuden_pixmap_guncelle(self.islenmis_goruntu)
        self.pixmapi_olceklendir_ve_goster()

    def filtre_keskinlestir_uygula(self):
        if not self._resim_yuklendi_mi(): return
            
        # Keskinleştirme için özel kernel matrisi
        kernel_matrisi = np.array([
            [ 0, -1,  0],
            [-1,  5, -1],
            [ 0, -1,  0]
        ])
        
        self.islenmis_goruntu = cv2.filter2D(self.islenmis_goruntu, -1, kernel_matrisi)
        
        self.cv_goruntuden_pixmap_guncelle(self.islenmis_goruntu)
        self.pixmapi_olceklendir_ve_goster()
        
    def filtre_gurultu_ekle_uygula(self):
        if not self._resim_yuklendi_mi(): return
            
        goruntu_float = self.islenmis_goruntu.astype(np.float32)
        
        ortalama = 0
        standart_sapma = 25
        gurultu_matrisi = np.random.normal(ortalama, standart_sapma, goruntu_float.shape).astype(np.float32)
        
        gurultulu_goruntu = goruntu_float + gurultu_matrisi
        
        # Değerleri 0-255 aralığına geri "kırp" 
        gurultulu_goruntu = np.clip(gurultulu_goruntu, 0, 255)
        
        self.islenmis_goruntu = gurultulu_goruntu.astype(np.uint8)
        
        self.cv_goruntuden_pixmap_guncelle(self.islenmis_goruntu)
        self.pixmapi_olceklendir_ve_goster()

    def resmi_sifirla(self):
        if self.orijinal_goruntu is None: return
        
        self.islenmis_goruntu = self.orijinal_goruntu.copy()
        
        self.cv_goruntuden_pixmap_guncelle(self.islenmis_goruntu)
        self.pixmapi_olceklendir_ve_goster()


# --- Uygulamayı Başlatma ---
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GoruntuStudyosu()
    window.show()
    sys.exit(app.exec())