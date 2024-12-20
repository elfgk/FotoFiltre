import cv2
import numpy as np
import gradio as gr

# Farklı filtre fonksiyonları
def apply_gaussian_blur(frame):
    return cv2.GaussianBlur(frame, (15, 15), 0)

def apply_sharpening_filter(frame):
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    return cv2.filter2D(frame, -1, kernel)

def apply_edge_detection(frame):
    return cv2.Canny(frame, 100, 200)

def apply_invert_filter(frame):
    return cv2.bitwise_not(frame)

def adjust_brightness_contrast(frame, alpha=1.0, beta=50):
    return cv2.convertScaleAbs(frame, alpha=alpha, beta=beta)

def apply_grayscale_filter(frame):
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

def apply_sepia_filter(frame):
    sepia_filter = np.array([[0.272, 0.534, 0.131],
                             [0.349, 0.686, 0.168],
                             [0.393, 0.769, 0.189]])
    return cv2.transform(frame, sepia_filter)

def apply_fall_filter(frame):
    fall_filter = np.array([[0.393, 0.769, 0.189],
                            [0.349, 0.686, 0.168],
                            [0.272, 0.534, 0.131]])
    return cv2.transform(frame, fall_filter)

# Yeni filtre fonksiyonları
def apply_emboss_filter(frame):
    kernel = np.array([[-2, -1, 0], 
                       [-1, 1, 1], 
                       [0, 1, 2]])
    return cv2.filter2D(frame, -1, kernel)

def apply_sketch_filter(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    inv_gray = cv2.bitwise_not(gray)
    blur = cv2.GaussianBlur(inv_gray, (21, 21), 0)
    sketch = cv2.divide(gray, 255 - blur, scale=256)
    return sketch

def apply_median_blur_filter(frame):
    return cv2.medianBlur(frame, 15)

def adjust_contrast(frame, alpha=2.0, beta=0):
    return cv2.convertScaleAbs(frame, alpha=alpha, beta=beta)

def adjust_hue(frame, delta=30):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsv[:, :, 0] = (hsv[:, :, 0] + delta) % 180
    return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

# Filtre uygulama fonksiyonu
def apply_filter(filter_type, input_image=None):
    if input_image is not None:
        frame = input_image
    else:
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cap.release()
        if not ret:
            return "Web kameradan görüntü alınamadı"

    if filter_type == "Gaussian Blur":
        return apply_gaussian_blur(frame)
    elif filter_type == "Sharpen":
        return apply_sharpening_filter(frame)
    elif filter_type == "Edge Detection":
        return apply_edge_detection(frame)
    elif filter_type == "Invert":
        return apply_invert_filter(frame)
    elif filter_type == "Brightness":
        return adjust_brightness_contrast(frame, alpha=1.0, beta=50)
    elif filter_type == "Grayscale":
        return apply_grayscale_filter(frame)
    elif filter_type == "Sepia":
        return apply_sepia_filter(frame)
    elif filter_type == "Sonbahar":
        return apply_fall_filter(frame)
    elif filter_type == "Emboss":
        return apply_emboss_filter(frame)
    elif filter_type == "Sketch":
        return apply_sketch_filter(frame)
    elif filter_type == "Median Blur":
        return apply_median_blur_filter(frame)
    elif filter_type == "Contrast Adjustment":
        return adjust_contrast(frame, alpha=2.0, beta=0)
    elif filter_type == "Hue Adjustment":
        return adjust_hue(frame, delta=30)

# Gradio arayüzü
with gr.Blocks() as demo:
    gr.Markdown("# Fotoğraf Filtreleme")

    # Filtre seçenekleri
    filter_type = gr.Dropdown(
        label="Filtre Seçin",
        choices=["Gaussian Blur", "Sharpen", "Edge Detection", "Invert", "Brightness", "Grayscale", "Sepia", "Sonbahar",
                 "Emboss", "Sketch", "Median Blur", "Contrast Adjustment", "Hue Adjustment"],
        value="Gaussian Blur"
    )

    # Görüntü yükleme alanı
    input_image = gr.Image(label="Resim Yükle", type="numpy")

    # Çıktı için görüntü
    output_image = gr.Image(label="Filtre Uygulandı")

    # Filtre uygula butonu
    apply_button = gr.Button("Filtreyi Uygula")

    # Butona tıklanınca filtre uygulama fonksiyonu
    apply_button.click(fn=apply_filter, inputs=[filter_type, input_image], outputs=output_image)

# Gradio arayüzünü başlat
demo.launch()
