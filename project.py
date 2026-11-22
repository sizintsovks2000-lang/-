def calculate_discount(price: float, discount: float) -> dict:
    if not isinstance(price, (int, float)):
        raise ValueError("Цена должна быть числом.")
    if not isinstance(discount, (int, float)):
        raise ValueError("Скидка должна быть числом.")
    if price <= 0:
        raise ValueError("Цена должна быть больше нуля.")
    if discount < 0 or discount > 100:
        raise ValueError("Скидка должна быть в диапазоне от 0 до 100.")

    saved = price * discount / 100
    final = price - saved

    return {
        "price": round(float(price), 2),
        "discount": round(float(discount), 2),
        "saved": round(float(saved), 2),
        "final": round(float(final), 2),
    }

def print_result(result: dict) -> None:
    """Красивый вывод результата."""
    print("\n" + "=" * 40)
    print(f"  Цена без скидки : {result['price']:.2f} ₽")
    print(f"  Скидка          : {result['discount']:.2f} %")
    print(f"  Экономия        : {result['saved']:.2f} ₽")
    print(f"  Итоговая цена   : {result['final']:.2f} ₽")
    print("=" * 40 + "\n")

def read_float(prompt: str) -> float:
    """Безопасный ввод числа с повторной попыткой."""
    while True:
        raw = input(prompt).strip().replace(",", ".")
        try:
            return float(raw)
        except ValueError:
            print(" Ошибка: введите число (например, 199.99).")

def main() -> None:
    print("=" * 40)
    print("   КАЛЬКУЛЯТОР СКИДОК")
    print("  Команды: calc — рассчитать, exit — выход")
    print("=" * 40)

    while True:
        command = input("\nВведите команду (calc/exit): ").strip().lower()

        if command == "exit":
            print(" До свидания!")
            break

        if command != "calc":
            print("  Неизвестная команда. Используйте 'calc' или 'exit'.")
            continue

        try:
            price = read_float("Цена товара: ")
            discount = read_float("Скидка (%): ")

            result = calculate_discount(price, discount)
            print_result(result)

        except ValueError as e:
            print(f" Ошибка: {e}")
        except Exception as e:
            print(f"Непредвиденная ошибка: {e}")

