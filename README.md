# Fotoğraf Filtreleme Uygulaması

Bu proje, kullanıcıların çeşitli filtreleri fotoğraflarına uygulayabileceği bir Python tabanlı web uygulamasıdır. Gradio arayüzü kullanarak kolayca filtreler arasında seçim yapabilir ve yüklediğiniz fotoğraflara anında efektler ekleyebilirsiniz. Uygulama, farklı görsel efektlerle fotoğrafları düzenlemeyi sağlar. --> https://huggingface.co/spaces/elfgk/foto-filter

## Özellikler

Uygulama, aşağıdaki filtreleri içerir:

- **Gaussian Blur**: Görüntüye bulanıklık ekler.
- **Sharpen**: Görüntüyü keskinleştirir.
- **Edge Detection**: Görüntüde kenarları tespit eder.
- **Invert**: Görüntü renklerini tersine çevirir.
- **Brightness**: Görüntünün parlaklık ve kontrastını ayarlar.
- **Grayscale**: Görüntüyü siyah-beyaz yapar.
- **Sepia**: Görüntüye sepya efekti ekler.
- **Sonbahar (Fall Filter)**: Görüntüyü sonbahar tonlarına dönüştürür.
- **Emboss**: Görüntüyü kabartma efekti ile dönüştürür.
- **Sketch**: Görüntüye çizim efekti ekler.
- **Median Blur**: Görüntüdeki gürültüyü giderir ve bulanıklaştırır.
- **Contrast Adjustment**: Görüntü kontrastını artırır.
- **Hue Adjustment**: Görüntünün renk tonunu ayarlar.

## Gereksinimler

Bu projeyi çalıştırmak için aşağıdaki Python kütüphanelerine ihtiyaç vardır:

- `opencv-python`: Görüntü işleme kütüphanesi.
- `numpy`: Sayısal hesaplamalar için.
- `gradio`: Kullanıcı arayüzü için.

Gerekli kütüphaneleri yüklemek için şu komutu çalıştırabilirsiniz:

```bash
pip install opencv-python numpy gradio
