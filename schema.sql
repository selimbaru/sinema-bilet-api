CREATE TABLE IF NOT EXISTS filmler (
    id SERIAL PRIMARY KEY,
    ad VARCHAR(255) NOT NULL,
    afis_url TEXT,
    vizyon_tarihi VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS seanslar (
    id SERIAL PRIMARY KEY,
    film_id INTEGER REFERENCES filmler(id) ON DELETE CASCADE,
    salon_adi VARCHAR(50) NOT NULL,
    tarih DATE NOT NULL,
    seans_saati VARCHAR(10) NOT NULL
);

CREATE TABLE IF NOT EXISTS biletler (
    id SERIAL PRIMARY KEY,
    seans_id INTEGER REFERENCES seanslar(id) ON DELETE CASCADE,
    kullanici_id INTEGER NOT NULL,
    koltuk_no VARCHAR(10) NOT NULL,
    alinis_tarihi TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_koltuk_seans UNIQUE (seans_id, koltuk_no)
);