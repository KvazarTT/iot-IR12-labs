def can_fit(size, n, w, h):
    """
    Перевіряє чи можна розмістити n прямокутників w*h у квадраті зі стороною size
    """
    cols = size // w
    rows = size // h
    return (cols * rows) >= n

def get_min_square_size(n, w, h):
    """
    Бінарний пошук мінімального розміру квадрата
    """
    left = max(w, h)
    right = max(w, h) * n
    result = right
    count = 0

    while left <= right:
        count += 1
        mid = (left + right) // 2

        if can_fit(mid, n, w, h):
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return result, count

def main():
    print("Введіть через пробіл: N W H (кількість, ширина, висота)")
    print("Для виходу введіть exit")

    while True:
        try:
            user_input = input(">>> ").strip()
            if user_input.lower() == "exit":
                print("Роботу завершено")
                break
            if not user_input:
                continue
            args = list(map(int, user_input.split()))
            if len(args) != 3:
                print("Помилка: Очікується 3 цілих числа (n w h)")
                continue
            n, w, h = args
            ans, count = get_min_square_size(n, w, h)
            print(f"Результат: {ans} Ітерацій: {count}")
        except ValueError:
            print("Помилка введення: Вводьте тільки цілі числа через пробіл")
        except KeyboardInterrupt:
            print("\nВи завершили програму некоректно!")
            break

if __name__ == "__main__":
    main()