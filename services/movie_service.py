from sinema_projesi import api_service
from sinema_projesi.db import database


def vizyondaki_filmleri_getir():
    filmler = database.vizyondaki_filmleri_getir()
    return {"filmler": filmler}


def film_ekle(film_adi):
    film_bilgisi = api_service.film_bilgisi_getir(film_adi)

    if not film_bilgisi:
        return {"mesaj": "Böyle bir film bulunamadı"}

    eklenme = database.film_ekle(film_bilgisi)

    if eklenme:
        return {
            "mesaj": "Film başarıyla eklendi",
            "film": film_bilgisi
        }
    else:
        return {"mesaj": "Film kaydedilirken bir hata oluştu"}