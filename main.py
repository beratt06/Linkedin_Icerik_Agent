from brain import get_content_strategy
from image_generate import generate_image 
import os
from datetime import datetime

os.makedirs("outputs", exist_ok=True)

def main():
    print("=========================================")
    print("   LINKEDIN İÇERİK VE GÖRSEL OLUŞTURMA")
    print("=========================================")
    
    konu = input("\n📢 Bugün ne hakkında paylaşım yapalım?: ")
    
    post_metni, resim_promptu = get_content_strategy(konu)
    
    if post_metni and resim_promptu:
        print("\n-----------------------------------------")
        print("📝 OLUŞTURULAN METİN TASLAĞI:")
        print(post_metni[:50] + "...")  
        print("-----------------------------------------")
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        text_filename = f"outputs/post_{timestamp}.txt"
        
        with open(text_filename, "w", encoding="utf-8") as f:
            f.write(post_metni)
            
        print("🖼️  Görsel üretimine geçiliyor")
        image_path = generate_image(resim_promptu)
        
        print("\n İŞLEM TAMAMLANDI!")
        if text_filename:
            print(f" Metin Dosyası: {text_filename}")
        else:
            print("⚠️ Metin dosyası oluşturulamadı.")
        if image_path:
            print(f"  Görsel Dosyası: {image_path}")
        else:
            print("⚠️ Görsel üretilemedi.")

    else:
        print("❌ Bir hata oluştu, işlem iptal edildi.")

if __name__ == "__main__":
    main()
