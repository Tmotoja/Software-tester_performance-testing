# performance_testing

To repozytorium zawiera przykłady oraz narzędzia do testowania wydajności aplikacji i API w języku Python. Znajdziesz tutaj proste skrypty do mierzenia czasu działania funkcji, testowania wydajności zapytań HTTP oraz wykorzystania narzędzi takich jak pytest-benchmark i Locust.

## Zawartość

- `basic_timer.py` – przykład mierzenia czasu wykonania funkcji w Pythonie.
- `test_benchmark.py` – test wydajnościowy funkcji z użyciem pytest-benchmark.
- `api_requests_get_test.py` – prosty test wysyłający zapytanie GET do API i sprawdzający odpowiedź.
- `api_load_test.py` – skrypt do wysyłania wielu zapytań do API i mierzenia całkowitego czasu odpowiedzi.
- `locustfile.py` – plik konfiguracyjny do testów wydajnościowych z użyciem narzędzia Locust.

## Do czego służy?

Repozytorium służy do nauki i demonstracji podstawowych technik testowania wydajności:
- Pomiar czasu działania funkcji.
- Testowanie wydajności API (czas odpowiedzi, obciążenie).
- Automatyzacja testów wydajnościowych.

## Jak może się przydać?

- Do nauki podstaw testowania wydajności w Pythonie.
- Jako baza do własnych eksperymentów z testami wydajnościowymi.
- Do szybkiego sprawdzenia, jak różne techniki testowania wydajności można zaimplementować w praktyce.

## Jak uruchomić?

1. Zainstaluj wymagane biblioteki:
   ```
   pip install requests pytest pytest-benchmark locust
   ```
2. Uruchom wybrany skrypt, np.:
   ```
   python basic_timer.py
   ```
3. Aby uruchomić testy benchmarkowe:
   ```
   pytest test_benchmark.py
   ```
4. Aby uruchomić testy obciążeniowe Locust:
   ```
   locust -f locustfile.py
   ```
