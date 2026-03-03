from huggingface_hub import InferenceClient
import os
from datetime import datetime
import random


HF_TOKEN = os.getenv("HUGGİNG_FACE_API") # Hugging Face API token'ınızı .env dosyasından alır.

if not HF_TOKEN:
    raise RuntimeError("Hugging Face API token'ı ayarlanmamış.")

MODEL_ID = "black-forest-labs/FLUX.1-schnell"

client = InferenceClient(model=MODEL_ID, token=HF_TOKEN)

LINKEDIN_STYLE = """
clean corporate style, professional environment, natural lighting,
modern office, minimal composition, business photography
"""

def enhance_prompt(user_prompt):
    if len(user_prompt) > 100:
        return user_prompt

    return f"{user_prompt}, {LINKEDIN_STYLE}, ultra realistic, 8k, cinematic lighting"

def generate_image(prompt_text):
    print("\n" + "="*40)
    print(f" GÖRSEL ÜRETİMİ BAŞLIYOR")
    print(f"  Model: {MODEL_ID}")
    print("="*40)
    
    final_prompt = enhance_prompt(prompt_text)
    print(f" İşlenen Prompt: {final_prompt[:50]}...")

    try:
        seed = random.randint(0, 2**32 - 1)
        print(f" Seed: {seed}")

        print(" Hugging Face sunucularına bağlanılıyor...")
        
        image = client.text_to_image(
            prompt=final_prompt,
            width=1024,
            height=1024,
            guidance_scale=3.5, # metine ne kadar bağlı kalınacağı
            seed=seed
        )
        
        os.makedirs("outputs", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"outputs/flux_{timestamp}.png"
        
        image.save(filename)
        
        print(f" BAŞARILI! Görsel kaydedildi: {filename}")
        print("="*40 + "\n")
        
        return filename

    except Exception as e:
        print("\n HATA OLUŞTU! (Lütfen bu hatayı okuyun)")
        print(f"Hata Detayı: {e}")
        
        error_str = str(e)
        if "401" in error_str:
            print(" SEBEP: Token geçersiz veya hatalı kopyalanmış.")
        elif "403" in error_str:
            print(" SEBEP: Bu modele erişim izniniz yok (Lisans kabul edilmemiş).")
        elif "503" in error_str or "500" in error_str:
            print(" SEBEP: Hugging Face sunucuları şu an çok yoğun. Birkaç saniye sonra tekrar deneyin.")
            
        print("="*40 + "\n")
        return None