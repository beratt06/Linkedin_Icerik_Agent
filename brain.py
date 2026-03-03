import os
import re
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY") # Kendi aldığınız API key'i .ENV dosyasından alır.

if not api_key:
    raise RuntimeError("❌ GEMINI_API_KEY Ayarlanmamış")
genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-2.5-flash') # İstediğiniz modeli Kullanabilirsiniz.

def get_content_strategy(user_topic):
    
    print("🧠 Gemini çalışıyor...")
    """
    Promptu istediğiniz gibi optimize edebilirsiniz
    lakin splitler bölüm 1 ve bölüm 2 üzerinden yapıldığı için formatı bozmamaya dikkat edin. :) 
    """

    prompt = f"""
    Rolün: Deneyimli bir LinkedIn içerik üreticisi ve yaratıcı görsel prompt mühendisisin.

    Konu: "{user_topic}"

    Aşağıdaki iki bölümü üret. Formatı KESİNLİKLE koru, başlıkları değiştirme, ekstra açıklama ekleme.

    [BÖLÜM 1: METİN]
    - Türkçe yaz.
    - Samimi ama profesyonel ton kullan.
    - 80–150 kelime arası olsun.
    - Metni 2–4 kısa paragrafa böl.
    - En fazla 2 emoji kullan.
    - En sonda 3–5 adet alakalı hashtag ekle.
    - Satış dili, clickbait ve aşırı emoji kullanma.

    [BÖLÜM 2: PROMPT]
    - İngilizce yaz.
    - Stable Diffusion için optimize edilmiş tek satırlık prompt üret.
    - Fotogerçekçi, sinematik, yüksek detaylı olsun.
    - Işık, kamera açısı, ortam, stil ve kalite etiketleri içersin.
    - İnsan yüzü varsa: doğal oranlar, net odak, gerçekçi cilt dokusu belirt.
    - Prompt 25–40 kelime aralığında olsun.
    - Liste veya açıklama ekleme, sadece prompt yaz.
    - Prompt sonunda "Stable Diffusion" modeline uygun İNGİLİZCE bir prompt yaz. (Örn: A futuristic office, cinematic lighting, 8k...)
    """
    
    response = model.generate_content(prompt)
    text = response.text
    try:
        match = re.search(r'\[BÖLÜM 1: METİN\](.*?)\[BÖLÜM 2: PROMPT\](.*)',
                          text,
                          re.S)
        if not match:
            raise ValueError("❌ Yanıt beklenen formatta değil.")
            
        post_text = match.group(1).strip()
        image_prompt = match.group(2).strip()
        return post_text, image_prompt
        
    except Exception as e:
        print(f"Hata oluştu: {e}")
        return None, None