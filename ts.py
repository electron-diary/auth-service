from datetime import datetime

# Предположим, что дата регистрации пользователя
registration_date = datetime.now() # Замените на вашу дату регистрации

# Текущая дата
current_date = datetime.now()

# Вычисляем разницу между текущей датой и датой регистрации
difference = current_date - registration_date

# Получаем количество дней
days_passed = difference.days

print(f"С момента регистрации прошло {days_passed} дней.")