# 🚀 LinkedIn Agent

LinkedIn Agent, kullanıcı tarafından belirlenen herhangi bir konu üzerinden yapay zeka destekli profesyonel LinkedIn gönderileri ve bu gönderilerle tam uyumlu yüksek çözünürlüklü görseller üreten otomatize bir araçtır. 

Gemini ve Hugging Face FLUX modellerini entegre çalıştırarak içerik üretim sürecini saniyelere indirger ve çıktıları düzenli bir şekilde arşivler.

## ✨ Temel Özellikler

* **Akıllı Metin Üretimi:** Gemini API altyapısı ile konuya özel, etkileşim odaklı ve profesyonel Türkçe LinkedIn gönderileri oluşturur.
* **Otomatize Prompt Mühendisliği:** Üretilen metne en uygun görseli oluşturmak için arka planda İngilizce "Stable Diffusion" uyumlu promptlar hazırlar.
* **Yüksek Kaliteli Görsel Çıktısı:** Hugging Face FLUX.1-schnell modeli kullanılarak 1024x1024 piksel çözünürlüğünde, paylaşıma hazır görseller üretir.
* **Sistematik Arşivleme:** Üretilen tüm metin ve görselleri zaman damgası (timestamp) ile isimlendirerek `outputs/` dizininde depolar.
* **Kullanıcı Dostu CLI:** Terminal üzerinden tek komutla çalışan, sade ve hızlı bir akış sunar.

## 📂 Proje Mimarisi

```text
Linkedin_Agent/
├── main.py              # Uygulamanın ana giriş noktası ve kullanıcı etkileşimi
├── brain.py             # Gemini API entegrasyonu (Metin ve Prompt üretimi)
├── image_generate.py    # Hugging Face API entegrasyonu (Görsel üretimi)
├── outputs/             # Üretilen dosyaların saklandığı dizin
├── requirements.txt     # Gerekli kütüphaneler
└── README.md            # Proje dökümantasyonu
```

## ⚙️ Nasıl Çalışır?

1. **Girdi:** `main.py` çalıştırıldığında kullanıcıdan bir LinkedIn paylaşım konusu talep edilir.
2. **İşleme (Brain):** `brain.py`, konuyu Gemini modeline ileterek hem Türkçe bir gönderi metni hem de bu metni betimleyen İngilizce bir görsel promptu üretir.
3. **Üretim (Render):** `image_generate.py`, elde edilen İngilizce promptu Hugging Face Inference API'ye göndererek FLUX modeli ile görseli çizer.
4. **Çıktı:** Üretilen içerikler eş zamanlı olarak `outputs/` klasörüne kaydedilir.

## 🚀 Kurulum & Başlangıç

### 1. Sistem Gereksinimleri
* Python 3.10 veya üzeri
* Geçerli bir **Gemini API Key**
* Geçerli bir **Hugging Face API Token**

### 2. Projeyi Hazırlama

Sanal ortamı oluşturun ve gerekli paketleri yükleyin:

```powershell
# Proje dizinine gidin
cd "C:\Users\BERAT ÇAM\Desktop\YZT\Linkedin_Agent"

# Sanal ortamı aktif edin
.\venv\Scripts\Activate.ps1

# Bağımlılıkları yükleyin
pip install -r requirements.txt
```

### 3. Ortam Değişkenleri (Environment Variables)

Projenin ana dizininde bir `.env` dosyası oluşturun ve API anahtarlarınızı aşağıdaki formatta ekleyin:

```env
GEMINI_API_KEY=sizin_gemini_api_anahtariniz
HUGGİNG_FACE_API=sizin_huggingface_tokeniniz
```

> **⚠️ ÖNEMLİ NOT:** Mevcut kod yapısında Hugging Face değişkeni Türkçe karakter içererek `HUGGİNG_FACE_API` şeklinde tanımlanmıştır. Çalışma hatası almamak için `.env` dosyasındaki isimlendirmenin birebir aynı olduğundan emin olun.

## 💻 Kullanım

Uygulamayı başlatmak için terminalde aşağıdaki komutu çalıştırın:

```powershell
python main.py
```

Sistem sizden bir konu girmenizi isteyecektir. Konuyu yazıp `Enter` tuşuna bastığınızda süreç başlar.

**Örnek Çıktılar:**
İşlem tamamlandığında `outputs/` klasöründe iki adet dosya oluşturulur:
* 📄 `post_20231025_143000.txt` (Gönderi metni ve etiketler)
* 🖼️ `flux_20231025_143000.png` (Üretilen 1024x1024 görsel)

## 🛠️ Hata Giderme (Troubleshooting)

| Hata Durumu | Çözüm Önerisi |
| :--- | :--- |
| **`GEMINI_API_KEY bulunamadı`** | `.env` dosyasının proje kök dizininde olduğunu ve değişken adının doğru yazıldığını kontrol edin. |
| **401 / 403 Hugging Face Hatası** | Hugging Face token'ınızın süresinin dolmadığından ve hesabınızın FLUX modeline erişim izni olduğundan emin olun. |
| **500 / 503 Hugging Face Hatası** | API sunucularında geçici yoğunluk olabilir. Birkaç dakika bekleyip tekrar deneyin. |

## 🔒 Güvenlik & Gizlilik

* `.env` dosyası, `venv/` klasörü, API anahtarları ve `outputs/` içerisindeki kişisel veriler `.gitignore` dosyasına eklenmeli ve GitHub (veya benzeri) uzak depolara **kesinlikle yüklenmemelidir**.

## 🗺️ Yol Haritası (Roadmap)

Gelecek sürümlerde planlanan geliştirmeler:
- [ ] Terminal üzerinden direkt parametre gönderimi (`python main.py --topic "Yapay Zeka"`)
- [ ] Farklı metin ve görsel modelleri arasında dinamik geçiş yapabilme (Config desteği)
- [ ] Hatalara karşı otomatik yeniden deneme (Retry) mekanizması ve detaylı loglama altyapısı.

## 📄 Lisans

Bu proje için henüz bir lisans tanımlanmamıştır. Açık kaynak kodlu sistemlerde veya kurumsal kullanımlarda uygun bir lisans (örn. MIT, Apache 2.0) eklenmesi tavsiye edilir.