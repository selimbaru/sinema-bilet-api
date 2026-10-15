from sinema_projesi.db import database


def bilet_al(kullanici_id:int,seans_id:int,koltuk_no:str):
    basarili= database.bilet_al(kullanici_id, seans_id, koltuk_no)
    if basarili:
        return {"durum":"başarılı",
                "mesaj":"Bilet başarıyla kesildi",
                "detay":{
                    "kullanici_id":kullanici_id,
                    "seans_id":seans_id,
                    "koltuk_no":koltuk_no
                }
                        }
    else:
        return {
            "durum":"Hata",
            "mesaj":"Bir hata oluştu"
        }

def biletleri_gor(kullanici_id: int):
    biletler = database.kullanici_biletlerini_getir(kullanici_id)
    return {"biletler": biletler}

def bilet_sil(kullanici_id: int, bilet_id: int):
    silindi = database.bilet_iptal_et(kullanici_id, bilet_id)

    if silindi:
        return {
            "durum": "Başarılı",
            "mesaj": f"{bilet_id} numaralı bilet silindi"
        }
    else:
        return {"durum": "Hata"}