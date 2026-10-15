from fastapi import FastAPI
from sinema_projesi.services import ticket_service
from sinema_projesi.services import movie_service
from sinema_projesi.services import session_service
from sinema_projesi.services import user_service


app=FastAPI(title="sinema_calısması",)

@app.get("/")
def ana_sayfa():
    return {"mesaj":"API sorunsuz calısıyor"}

@app.get("/filmler/vizyon")
def vizyondaki_filmleri_getir():
    return movie_service.vizyondaki_filmleri_getir()

@app.post("/film/ekle")
def film_ekle(film_adi: str):
    return movie_service.film_ekle(film_adi)

@app.get("/filmler/{film_id}/seanslar")
def filmin_seanslarini_getir(film_id: int):
    return session_service.filmin_seanslarini_getir(film_id)

@app.get("/seanslar/{seans_id}/koltuklar")
def koltuklari_getir(seans_id: int):
    return session_service.koltuklari_getir(seans_id)

@app.post("/bilet/al")
def bilet_al(kullanici_id: int, seans_id: int, koltuk_no: str):
    return ticket_service.bilet_al(kullanici_id, seans_id, koltuk_no)

@app.get("/kullanicilar/{kullanici_id}/biletler")
def biletleri_gor(kullanici_id: int):
    return ticket_service.biletleri_gor(kullanici_id)


@app.delete("/kullanicilar/{kullanici_id}/biletler/{bilet_id}")
def bilet_sil(kullanici_id: int, bilet_id: int):
    return ticket_service.bilet_sil(kullanici_id, bilet_id)

@app.post("/giris_yap")
def giris_yap(email: str, sifre: str):
    return user_service.giris_yap(email, sifre)


@app.post("/seans/ekle")
def seans_ekle(film_id: int, salon_adi: str, tarih: str, seans_saati: str):
    return session_service.seans_ekle(
        film_id, salon_adi, tarih, seans_saati
    )


@app.post("/kayit_ol")
def kayit_ol(ad_soyad: str, email: str, sifre: str):
    return user_service.kayit_ol(ad_soyad, email, sifre)














