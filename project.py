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
