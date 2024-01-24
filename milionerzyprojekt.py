import random

lista_pytań = [
    {
        "Pytanie": "Druga para odnóży gębowych pajęczaków, która służy do rozdrabniania pokarmów i jako narządy dotykowe, to...",
        "Odpowiedzi": ["rękochwytki", "nogogłaszczki", "łapkomyjki", "zębołapki"],
        "Poprawna_odpowiedź": "nogogłaszczki"
    },
    {
        "Pytanie": "Jaki znak interpunkcyjny stawiany po cyfrze arabskiej sprawia, że odczytujemy ją jako liczebnik porządkowy?",
        "Odpowiedzi": ["myślnik", "przecinek", "średnik", "kropka "],
        "Poprawna_odpowiedź": "kropka "
    },
]

wyniki = []

def losuj_pytanie():
    return random.choice(lista_pytań)

def gra_milionerzy():
    stan_konta = 0
    for _ in range(5):  # Pętla wykonuje się pięć razy
        pytanie = losuj_pytanie()
        print(pytanie["Pytanie"])
        for idx, odpowiedź in enumerate(pytanie["Odpowiedzi"]):
            print(f'{idx + 1}. {odpowiedź}')

        while True:  # Pętla dla sprawdzenia poprawności odpowiedzi
            odpowiedź_użytkownika = input("Podaj numer poprawnej odpowiedzi: ")
            if odpowiedź_użytkownika.isdigit() and 1 <= int(odpowiedź_użytkownika) <= 4:
                break
            else:
                print("Podaj odpowiedź jeszcze raz. Wybierz numer od 1 do 4.")

        if pytanie["Odpowiedzi"][int(odpowiedź_użytkownika) - 1] == pytanie["Poprawna_odpowiedź"]:
            print("\nPoprawna odpowiedź! Wygrywasz!")
            stan_konta += 200000
            print(f"Twój aktualny stan konta: {stan_konta} zł")
        else:
            print("Niestety, nie wygrałeś. Poprawna odpowiedź to:", pytanie["Poprawna_odpowiedź"])
            print(f"Twój wynik: {stan_konta} zł")
            break  # Przerwij pętlę po złej odpowiedzi

    return stan_konta

def pokaz_najlepsze_wyniki():
    if not wyniki:
        print("Brak zapisanych wyników.")
    else:
        print("Najlepsze wyniki:")
        for i, wynik in enumerate(wyniki, start=1):
            print(f"{i}. Gracz: {wynik['gracz']}, Wynik: {wynik['wynik']} zł")

def menu():
    while True:
        print("\nMENU:")
        print("1. Zagraj w grę")
        print("2. Najlepsze wyniki")
        print("3. Wyjście")

        wybór = input("Wybierz opcję (1-3): ")

        if wybór == '1':
            wynik = gra_milionerzy()
            if wynik > 0:
                gracz = input("Gratulacje! Podaj swoje imię: ")
                wyniki.append({"gracz": gracz, "wynik": wynik})
        elif wybór == '2':
            pokaz_najlepsze_wyniki()
        elif wybór == '3':
            print("Dzięki za grę!")
            break
        else:
            print("Nieprawidłowy wybór. Wybierz numer od 1 do 3.")

# Uruchom menu
menu()

