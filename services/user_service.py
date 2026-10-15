from sinema_projesi.db import database


def kayit_ol(ad_soyad: str, email: str, sifre: str):
    kayit = database.kullanici_ekle(ad_soyad, email, sifre)

    if kayit:
        return {"mesaj": "Başarıyla kayıt olundu"}
    else:
        return {"mesaj": "Hata"}


def giris_yap(email: str, sifre: str):
    giris = database.kullanici_giris_yap(email, sifre)

    if giris:
        return {
            "mesaj": f"Hoşgeldiniz {giris['ad_soyad']}",
            "durum": giris["ad_soyad"]
        }
    else:
        return {
            "durum": "Hata",
            "mesaj": "E-posta veya şifre hatalı!"
        }
