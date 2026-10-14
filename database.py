import psycopg2
from psycopg2.extras import RealDictCursor

DB_HOST = "localhost"
DB_NAME = "sinema_db"
DB_USER = "postgres"
DB_PASS = "KENDİ ŞİFRENİZİ YAZIN"
DB_PORT = "5432"


def baglanti_al():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            DB_PASS = DB_PASS,
            port=DB_PORT
        )
        return conn
    except Exception as hata:
        print(f"Veritabanı bağlantı hatası: {hata}")
        return None

def film_ekle(film):
    conn = baglanti_al()
    if not conn:
        return False
    cursor = conn.cursor()

    sorgu = "insert into filmler(baslik,afis_url,imdb_puani,tur,yil,sure,yonetmen,oyuncular,ozet) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);"

    cursor.execute(sorgu, (
        film.get("Başlık"),
        film.get("Afiş"),
        film.get("Puan"),
        film.get("Tür"),
        film.get("Yıl"),
        film.get("Süre"),
        film.get("Yönetmen"),
        film.get("Oyuncular"),
        film.get("Konu")
    ))
    conn.commit()
    cursor.close()
    conn.close()
    return True

def vizyondaki_filmleri_getir():
    conn = baglanti_al()
    if not conn:
        return False
    cursor = conn.cursor()

    sorgu = "SELECT DISTINCT f.* FROM filmler f JOIN seanslar s ON f.id = s.film_id;;"
    cursor.execute(sorgu)
    filmler = cursor.fetchall()

    cursor.close()
    conn.close()
    return filmler

def seans_ekle(film_id, salon_adi, tarih, seans_saati):
    conn = baglanti_al()
    if not conn:
        return False
    cursor = conn.cursor()

    sorgu = "insert into seanslar(film_id,salon_adi,tarih,seans_saati) VALUES (%s,%s,%s,%s);"
    cursor.execute(sorgu,(film_id,salon_adi,tarih,seans_saati))
    conn.commit()
    cursor.close()
    conn.close()
    return True


def filmin_seanslarini_getir(film_id):
    conn = baglanti_al()
    if not conn:
        return False
    cursor = conn.cursor()
    sorgu = "select * from seanslar where film_id=%s"
    cursor.execute(sorgu, (film_id,))
    seanslar = cursor.fetchall()
    cursor.close()
    conn.close()
    return seanslar

def dolu_koltukları_getir(seans_id):
    conn = baglanti_al()
    if not conn:
        return False
    cursor = conn.cursor()
    sorgu="select koltuk_no from biletler where seans_id = %s;"
    cursor.execute(sorgu, (seans_id,))
    koltuklar = cursor.fetchall()
    cursor.close()
    conn.close()
    return koltuklar

def bilet_al(seans_id,kullanici_id,koltuk_no):
    conn = baglanti_al()
    if not conn:
        return False
    cursor = conn.cursor()
    sorgu = "INSERT INTO biletler (seans_id, kullanici_id, koltuk_no) VALUES (%s, %s, %s);"
    cursor.execute((sorgu),(seans_id,kullanici_id,koltuk_no,))
    conn.commit()
    cursor.close()
    conn.close()
    return True

def kullanici_ekle(ad_soyad,email,sifre):
    conn = baglanti_al()
    if not conn:
        return False
    cursor = conn.cursor()
    sorgu="insert into kullanicilar (ad_soyad,email,sifre) VALUES (%s,%s,%s);"
    cursor.execute(sorgu,(ad_soyad,email,sifre,))
    conn.commit()
    cursor.close()
    conn.close()
    return True

def kullanici_biletlerini_getir(kullanici_id):
    conn = baglanti_al()
    if not conn:
        return []
    cursor = conn.cursor()
    sorgu = """
            SELECT 
                b.id AS bilet_id,
                f.baslik,
                s.salon_adi,
                s.tarih,
                s.seans_saati,
                b.koltuk_no,
                b.alinis_tarihi
            FROM biletler b
            JOIN seanslar s ON b.seans_id = s.id
            JOIN filmler f ON s.film_id = f.id
            WHERE b.kullanici_id = %s;
        """
    cursor.execute(sorgu,(kullanici_id,))
    bilet = cursor.fetchall()
    cursor.close()
    conn.close()
    return bilet


def bilet_iptal_et(kullanici_id,bilet_id):
    conn = baglanti_al()
    if not conn:
        return False
    cursor = conn.cursor()
    sorgu = "delete from biletler where id = %s and kullanici_id = %s"
    cursor.execute(sorgu,(bilet_id,kullanici_id,))
    conn.commit()
    silindi=cursor.rowcount >0
    cursor.close()
    conn.close()
    return silindi



