def fix_text(mystr):
    # Gelen metni boşluklara göre ayırarak bir liste oluşturur.
    words = mystr.split()
    
    # Düzeltilecek kelimeleri tutacak olan liste
    fixed_words = []

    for word in words:
        # Parantezleri kontrol et
        if word.startswith("(") and word.endswith(")"):
            # Parantezleri kaldır ve düzeltilmiş kelimeyi listeye ekle
            fixed_words.append(word[1:-1])
        else:
            # Kelimeyi ters çevir ve düzeltilmiş kelimeyi listeye ekle
            fixed_words.append(word[::-1])

    # Düzeltildiği düşünülen kelimeleri birleştirerek düzeltilmiş metni oluştur
    corrected_text = " ".join(fixed_words)

    return corrected_text

if __name__ == "__main__":
    INPUT = ("nhoJ (Griffith) nodnoL saw (an) (American) ,tsilevon "
             ",tsilanruoj (and) laicos .tsivitca ((A) reenoip (of) laicremmoc "
             "noitcif (and) naciremA ,senizagam (he) saw eno (of) (the) tsrif "
             "(American) srohtua (to) emoceb (an) lanoitanretni ytirbelec "
             "(and) nrae a egral enutrof (from) ).gnitirw")

    CORRECT_ANSWER = "John Griffith London was an American novelist, journalist, and social activist. (A pioneer of commercial fiction and American magazines, he was one of the first American authors to become an international celebrity and earn a large fortune from writing.)"

    result = fix_text(INPUT)
    print("Correct!" if result == CORRECT_ANSWER else f"Sorry, it does not match with the correct answer.\nYour result: {result}")
    
    # Düzeltilmiş metni yazdır
    print(result)