# Linkedin Agent

LinkedIn için **AI destekli içerik ve görsel üretim aracı**.  
Kullanıcıdan alınan konuya göre:
- Gemini ile profesyonel Türkçe gönderi metni oluşturur,
- Hugging Face FLUX modeli ile görsel üretir,
- Sonuçları `outputs/` klasörüne kaydeder.

## Özellikler

- Konu bazlı LinkedIn post metni üretimi (Türkçe)
- Stable Diffusion uyumlu görsel prompt üretimi (İngilizce)
- FLUX.1-schnell ile 1024x1024 görsel üretimi
- Zaman damgalı çıktı dosyaları (`post_*.txt`, `flux_*.png`)
- Basit CLI akışı

## Proje Yapısı

```text
Linkedin_Agent/
├─ main.py
├─ brain.py
├─ image_generate.py
├─ outputs/
└─ README.md
```

## Nasıl Çalışır?

1. `main.py` kullanıcıdan konu alır.
2. `brain.py`, Gemini API ile:
   - LinkedIn gönderi metnini,
   - görsel üretim promptunu üretir.
3. `image_generate.py`, Hugging Face Inference API ile görsel oluşturur.
4. Metin ve görsel `outputs/` içine kaydedilir.

## Gereksinimler

- Python 3.10+
- Gemini API key
- Hugging Face API token

## Kurulum

### 1) Depoya girin ve sanal ortamı etkinleştirin

```powershell
cd "C:\Users\BERAT ÇAM\Desktop\YZT\Linkedin_Agent"
.\venv\Scripts\Activate.ps1
```

### 2) Paketleri kurun

```powershell
pip install -r requirements.txt
```

## Ortam Değişkenleri

Proje köküne `.env` dosyası ekleyin:

```env
GEMINI_API_KEY=your_gemini_api_key
HUGGİNG_FACE_API=your_huggingface_token
```

> Not: `image_generate.py` içinde değişken adı şu an `HUGGİNG_FACE_API` (Türkçe `İ` harfi) olarak kullanılıyor. `.env` dosyanızda aynı isimle tanımlanmalıdır.

## Kullanım

```powershell
python main.py
```

Ardından terminalde gelen soruya paylaşım konunuzu girin.

## Çıktılar

Başarılı çalışmada aşağıdaki dosyalar üretilir:

- `outputs/post_YYYYMMDD_HHMMSS.txt`
- `outputs/flux_YYYYMMDD_HHMMSS.png`

## Hata Giderme

- **`GEMINI_API_KEY Ayarlanmamış`**
  - `.env` dosyasında anahtarın doğru tanımlandığını doğrulayın.
- **401 / 403 Hugging Face hatası**
  - Token geçerliliğini ve model erişim izinlerini kontrol edin.
- **500 / 503 Hugging Face hatası**
  - Sunucu yoğun olabilir; kısa süre sonra tekrar deneyin.

## Güvenlik Notu

- `.env`, `venv/`, `outputs/` ve cache dosyaları `.gitignore` ile dışlanmıştır.
- API anahtarlarını repoya commit etmeyin.

## Yol Haritası (Öneri)

- `requirements.txt` eklenmesi
- CLI argüman desteği (`--topic`)
- Farklı model seçimi için config dosyası
- Loglama ve retry mekanizması

## Lisans

Bu proje için henüz lisans tanımlanmamıştır. Üretim kullanımında lisans eklenmesi önerilir.
