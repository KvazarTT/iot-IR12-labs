import sys

try:
    from sem2_lab6 import get_min_beers
except ImportError:
    print("Помилка: Не знайдено файл")
    print("Будь ласка, збережіть свій код у файл з такою назвою в цій же папці.")
    sys.exit(1)

BEER_MENU = ["Lager (Світле)", "IPA (Крафтове)", "Stout (Темне)", "Pilsner (Пільзнер)"]

def print_header():
    print("HR BAR MANAGER")
    print("Система оптимізації корпоративного бюджету на алкоголь")


def main():
    print_header()
    employees = []

    while True:
        print("\nГоловне меню:")
        print("1. Додати працівника та його вподобання")
        print("2. Показати поточний список гостей")
        print("3. Розрахувати закупівлю")
        print("4. Вийти")
        choice = input("Обери дію (1-4): ").strip()

        if choice == '1':
            name = input("\nВведи ім'я працівника: ").strip()
            print(f"Опитуємо {name} щодо меню (y - так, n - ні):")

            likes = []
            for beer in BEER_MENU:
                ans = input(f"  Чи п'є {name} {beer}? (y/n): ").strip().lower()
                likes.append('Y' if ans == 'y' else 'N')

            if 'Y' not in likes:
                print("Увага! За правилами компанії працівник має пити хоча б щось одне. Додавання скасовано.")
            else:
                employees.append({'name': name, 'likes': likes})
                print(f"Працівника {name} успішно додано до списку!")

        elif choice == '2':
            if not employees:
                print("\nСписок гостей поки що порожній.")
                continue

            print("\n--- Список гостей та їхні смаки ---")
            for i, emp in enumerate(employees, 1):
                liked_beers = [BEER_MENU[j] for j, like in enumerate(emp['likes']) if like == 'Y']
                print(f"{i}. {emp['name']} п'є: {', '.join(liked_beers)}")

        elif choice == '3':
            if not employees:
                print("\nСпочатку додай хоча б одного працівника!")
                continue

            n = len(employees)
            b = len(BEER_MENU)
            likes_str = "".join(["".join(emp['likes']) for emp in employees])

            min_types, best_beer_indices = get_min_beers(n, b, likes_str)
            beers_to_buy = [BEER_MENU[i] for i in best_beer_indices]

            print("Результати оптимізації закупівлі")
            print(f"Кількість працівників: {n}")
            print(f"Асортимент бару: {b} видів")
            print(f"Мінімальна кількість видів пива для замовлення: {min_types}")
            print(f"Що замовляти: {', '.join(beers_to_buy)}")
            print("Шеф буде задоволений зекономленим бюджетом! 😎\n")

        elif choice == '4':
            print("\nДо зустрічі на корпоративі! Не забудьте викликати таксі.")
            break

        else:
            print("\nНевідома команда. Обери цифру від 1 до 4.")


if __name__ == '__main__':
    main()