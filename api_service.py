import requests

API_KEY = "39d2cc01"
BASE_URL = "http://www.omdbapi.com/"

def film_bilgisi_getir(film_adi):
    parametreler={"apikey":API_KEY,"t":film_adi}
    response = requests.get(BASE_URL, params=parametreler)
    if response.status_code == 200:
        veri=response.json()
        if veri.get("Response")=="True":
            return{
                "Başlık": veri.get("Title"),
                "Afiş": veri.get("Poster"),
                "Puan": veri.get("imdbRating"),
                "Tür":veri.get("Genre"),
                "Yıl": veri.get("Year"),
                "Yaş": veri.get("Rated"),
                "Süre": veri.get("Runtime"),
                "Yönetmen": veri.get("Director"),
                "Oyuncular":veri.get("Actors"),
                "Konu":veri.get("Plot"),
            }
        else:
            return veri.get("Error")
    return "Bağlantı Hatası"



