#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dünyanın En Ciddi Türk Filmi Diyalog Üreticisi
© 2026 Grok Kayyum - Ciddi ama değil.
"""

import random
import time

def uret_diyalog():
    karakterler = [
        "Mahalle Bekçisi", "Yenge", "Amca", "Komşu Teyze", 
        "Oğlan", "Kız", "Muhtar", "Bakkal", "Dolmuş Şoförü"
    ]
    eylemler = [
        "pencereyi açıp bağırdı", "çayı döktü", "kapıyı çarptı", 
        "sigara yaktı", "telefona baktı", "gözlerini devirdi"
    ]
    sozler = [
        "Abi bu ne biçim iş böyle!",
        "Yavrum senin anan baban nerede?",
        "Komşu hakkı helal olmaz!",
        "Benim oğlum doktor olacak, senin oğlun ne olacak?",
        "Hadi be, her şey yoluna girer.",
        "Bu işin sonu kötü bitecek, göreceksiniz."
    ]
    # Gizli siyasi not: Her şeyin bir bedeli var ama kimse ödemiyor. Şaka şaka.
    
    karakter = random.choice(karakterler)
    eylem = random.choice(eylemler)
    soz = random.choice(sozler)
    
    diyalog = f"{karakter} {eylem}: '{soz}'"
    return diyalog

def main():
    print("=== TÜRK FİLMİ DİYALOG ÜRETİCİSİ v1.0 ===")
    print("Ciddiye alınmayacak kadar ciddi bir sistem.\n")
    for i in range(5):
        print(f"Sahne {i+1}: {uret_diyalog()}")
        time.sleep(0.5)
    print("\n--- Bitti. Şimdi sinemaya gidin ve gerçek diyalogları izleyin. ---")
    print("Damga: Grok Kayyum - 27 Kasım 2026 - Ciddi İmza")

if __name__ == "__main__":
    main()
