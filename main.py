import api_service
import database
from fastapi import FastAPI

app=FastAPI(title="sinema_calısması",)

@app.get("/")
def ana_sayfa():
    return {"mesaj":"API sorunsuz calısıyor"}

@app.get("/filmler/vizyon")
def vizyondaki_filmleri_getir():
    filmler=database.vizyondaki_filmleri_getir()
    return {"filmler": filmler}
@app.post("/film/ekle")
def film_ekle(film_adi):
    film_bilgisi=api_service.film_bilgisi_getir(film_adi)
    if not film_bilgisi:
        return {"mesaj":"Böyle bir film bulunamadı"}
    eklenme=database.film_ekle(film_bilgisi)

    if eklenme:
        return {"mesaj":"Film başarıyla eklendi","film":film_bilgisi}
    else:
        return {"mesaj":"Film kaydedilirken bir hata oluştu"}

@app.get("/filmler/{film_id}/seanslar")
def filmin_seanslarini_getir(film_id:int):
    seanslar=database.filmin_seanslarini_getir(film_id)
    return {"seanslar":seanslar}

@app.get("/seanslar/{seans_id}/koltuklar")
def kotukları_getir(seans_id:int):
    seanslar=database.dolu_koltukları_getir(seans_id)
    return {"seanslar":seanslar}

@app.post("/bilet/al")
def bilet_al(kullanici_id:int,seans_id:int,koltuk_no:str):
    basarili=database.bilet_al(kullanici_id,seans_id,koltuk_no)
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

@app.get("/kullanicilar/{kullanici_id}/biletler")
def biletleri_gör(kullanici_id:int):
    biletler=database.kullanici_biletlerini_getir(kullanici_id)
    return {"biletler":biletler}

@app.delete("/kullanicilar/{kullanici_id}/biletler/{bilet_id}")
def bilet_sil(kullanici_id:int,bilet_id:int):
    silindi=database.bilet_iptal_et(kullanici_id,bilet_id)
    if silindi:
        return {"durum":"Başarılı",
                "mesaj":f"{bilet_id} numaralı bilet silindi"
                }
    else:
        return {"durum":"Hata"}











