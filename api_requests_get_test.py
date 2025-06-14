import requests

url = "https://myefe.com/transcription-pronunciation"

print("Wysylamy zapytanie GET do:", url)

response = requests.get(url)

print("Otrzymalismy odpowiedz o statusie:", response.status_code)

if response.status_code == 200:
    #jesli status to 200 to mozemy zobaczyc co zwraca nam sprona/API
    data = response.json()
    print("Zawartosc strony to:", data)
else:
    print("Nie udalo sie pobra danych ze strony/API")
