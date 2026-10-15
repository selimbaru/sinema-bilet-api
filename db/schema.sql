CREATE TABLE IF NOT EXISTS filmler (
    id SERIAL PRIMARY KEY,
    baslik VARCHAR(255) NOT NULL,
    afis_url TEXT,
    imdb_puani VARCHAR(10),
    tur VARCHAR(100),
    yil VARCHAR(10),
    sure VARCHAR(20),
    yonetmen VARCHAR(100),
    oyuncular TEXT,
    ozet TEXT
);

CREATE TABLE IF NOT EXISTS seanslar (
    id SERIAL PRIMARY KEY,
    film_id INTEGER REFERENCES filmler(id) ON DELETE CASCADE,
    salon_adi VARCHAR(50) NOT NULL,
    tarih DATE NOT NULL,
    seans_saati VARCHAR(10) NOT NULL
);

CREATE TABLE IF NOT EXISTS kullanicilar (
    id SERIAL PRIMARY KEY,
    ad_soyad VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    sifre VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS biletler (
    id SERIAL PRIMARY KEY,
    seans_id INTEGER REFERENCES seanslar(id) ON DELETE CASCADE,
    kullanici_id INTEGER REFERENCES kullanicilar(id) ON DELETE CASCADE,
    koltuk_no VARCHAR(10) NOT NULL,
    alinis_tarihi TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_koltuk_seans UNIQUE (seans_id, koltuk_no)
);