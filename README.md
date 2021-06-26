# Projekt zaliczeniowy - Selenium
## O projekcie

Projekt został wykonany w ramach pracy zaliczeniowej studiów podyplomowych na kierunku Tester Oprogramowania w Wyższej Szkole Bankowej w Chorzowie.
Testowaną aplikacją webową jest [Nozbe.com](https://nozbe.com/pl/).

Projekt napisany jest w języku Python 3.6.9 i wykorzystuje następujące biblioteki:
- selenium 3.141.0
- flake8 3.9.1
- pytest 6.2.3
- python-dotenv 0.17.1

## Przed uruchomieniem
### Przygotowanie środowiska
Repozytorium można sklonować na komputer wpisując w wybranej lokalizacji komendę:  
`$ git clone https://github.com/szymonsli/wsb-selenium-projekt.git`

Wejdź w lokalizację projektu   
`$ cd wsb-selenium-projekt`,

Następnie utwórz wirtualne środowisko Pythona  
`$ python3 -m venv .venv`

Aktywuj utworzone środowisko  
`$ source ./.venv/bin/activate`

Zainstaluj potrzebne biblioteki  
`$ make deps`

### Przygotowanie zmiennych środowiskowych
Projekt zawiera testy logowania się do aplikacji, a co za tym idzie konieczne są dane do logowania.
Załóż darmowe konto na [odpowiedniej stronie Nozbe](https://nozbe.com/pl/signup).

Utwórz plik `.env`  
`$ touch .env`  

Edytuj plik zamieszczając w nim sformatowany poniższy tekst
```txt
EMAIL=twoj_adres@email.com
PASSWORD=twoje_haslo
```

Projekt wykorzystuje bibliotekę *python-dotenv* czytającą dane z pliku `.env` i gwarantującą tajność wykorzystanych danych.

## Uruchomienie testów
Testy można uruchomić poprzez otwarcie terminala w lokalizacji projektu i wpisanie komendy  
`$ make test`

W celu sprawdzenia kodu pod kątem zgodności z PEP można wykonać komendę  
`$ make lint`


