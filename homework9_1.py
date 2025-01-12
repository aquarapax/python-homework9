# Функция запрашивает у пользователя имя и роль
def get_user_role():
    return input("Введите роль: ")

# Декоратор, который проверяет роль пользователя
def role_required(role: str):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Получаем роль пользователя через функцию
            user_role = get_user_role()  # Получаем роль пользователя
            if user_role == role:
                return func(*args, **kwargs)  # Разрешаем доступ к функции
            else:
                return 'Permission denied'  # Отказываем в доступе
        return wrapper
    return decorator

# Функция, доступная только для администраторов
@role_required('admin')
def secret_resource() -> str:
    return 'Permission accepted'

# Вызов 
print(secret_resource())  # Запрашивает роль пользователя