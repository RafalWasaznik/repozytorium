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
{
        "Pytanie": "Ile kosztuje chleb, który pierwotnie kosztował 10 zł, następnie potaniał do 8 zł, a później jego cena wzrosła o 20 proc.?",
        "Odpowiedzi": ["8,20 zł", "9 zł", "9,60 zł", "10 zł"],
        "Poprawna_odpowiedź": "9,60 zł"
    },
    {
        "Pytanie": "W Polsce wchodzimy po angielsku. Po jakiemu wchodzą Anglicy?",
        "Odpowiedzi": ["po grecku", "po francusku", "po rosyjsku", "po włosku"],
        "Poprawna_odpowiedź": "po francusku"
    },
    {
        "Pytanie": "Co jest prawdą o podkarpackim mieście, które ma w nazwie urządzenie włókiennicze?",
        "Odpowiedzi": ["słynie z hut szkła", "w X w. było stolicą Polski", "ma milion mieszkańców", "ma w herbie łódź"],
        "Poprawna_odpowiedź": "słynie z hut szkła"
    },
    {
        "Pytanie": "Czyjego pędzla portrety mieli filmowiec i przedsiębiorca Jack Warner, sopranistka Claire Dux i bizneswoman Helena Rubinstein?",
        "Odpowiedzi": ["Pabla Picassa", "Salvadora Dali", "Witkacego", "Rene Magritte'a"],
        "Poprawna_odpowiedź": "Salvadora Dali"
    },
    {
        "Pytanie": "Który z legendarnych wokalistów soulowych użyczył głosu kucharzowi ze szkolnej stołówki w serialu animowanym Miasteczko South Park?",
        "Odpowiedzi": ["James BrownŹle", "Marvin Gay", "Isaac Hayes", "Smokey Robinson"],
        "Poprawna_odpowiedź": "Isaac Hayes"
    },
    {
        "Pytanie": "Kuchenny synonim przekrętu...",
        "Odpowiedzi": ["Blat", "Dzban", "Dzban", "Wałek"],
        "Poprawna_odpowiedź": "Wałek"
    },
    {
        "Pytanie": "Kojot wygląda jak coś pomiędzy...",
        "Odpowiedzi": ["kuną a łasicą", "bobrem a wiewiórką", "rysiem a żbikiem", "wilkiem a szakalem"],
        "Poprawna_odpowiedź": "wilkiem a szakalem"
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
