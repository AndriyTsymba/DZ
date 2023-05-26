class TemperatureConverter:
    def celsius_to_fahrenheit(celsius):
        if celsius < -273.15:
            raise ValueError("Absolute 0 ((")
        else:
            return (celsius * 9/5) + 32

    def fahrenheit_to_celsius(fahrenheit):
        if fahrenheit < -459.67:
            raise ValueError("Absolute zero (")
        else:
            return (fahrenheit - 32) * 5/9
converter = TemperatureConverter()
try:
    celsius = 20
    fahrenheit = converter.celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C = {fahrenheit}°F")
except ValueError as e:
    print(e)
try:
    fahrenheit = 20
    celsius = converter.fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit}°F = {celsius}°C")
except ValueError as e:
    print(e)
