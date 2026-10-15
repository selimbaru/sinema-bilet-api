from sinema_projesi.db import database


def filmin_seanslarini_getir(film_id: int):
    seanslar = database.filmin_seanslarini_getir(film_id)
    return {"seanslar": seanslar}


def koltuklari_getir(seans_id: int):
    koltuklar = database.dolu_koltukları_getir(seans_id)
    return {"seanslar": koltuklar}


def seans_ekle(film_id: int, salon_adi: str, tarih: str, seans_saati: str):
    seans = database.seans_ekle(
        film_id, salon_adi, tarih, seans_saati
    )

    if seans:
        return {"mesaj": "Seans başarıyla eklendi"}
    else:
        return {"mesaj": "Bir hata oluştu"}