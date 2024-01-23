# Pobieramy od użytkownika wysokość diamentu
height = int(input("Podaj wysokość diamentu (najlepiej liczba nieparzysta): "))

# Górna część diamentu
for i in range(1, height, 2):
    print(" " * ((height - i) // 2) + "*" * i + " " * ((height - i) // 2))

# Środkowa część diamentu
print("*" * height)

# Dolna część diamentu
for i in range(height - 2, 0, -2):
    print(" " * ((height - i) // 2) + "*" * i + " " * ((height - i) // 2))