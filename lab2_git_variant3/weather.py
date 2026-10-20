"""Вариант 3: вывод температуры воздуха и скорости ветра."""


def show_weather(temperature: float, wind_speed: float) -> None:
    """Выводит температуру (°C) и скорость ветра (м/с)."""
    print("Информация о погоде")
    print(f"Температура воздуха: {temperature:g} °C")
    print(f"Скорость ветра: {wind_speed:g} м/с")


def main() -> None:
    temperature = 18
    wind_speed = 5
    show_weather(temperature, wind_speed)


if __name__ == "__main__":
    main()
print("\nДополнительная информация о погоде")

humidity = 65
print(f"Влажность воздуха: {humidity}%")