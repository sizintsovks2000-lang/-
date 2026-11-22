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
