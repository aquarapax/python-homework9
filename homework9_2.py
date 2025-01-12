def get_info(thing: str) -> str:
    # Моделируем получение информации
    return f"Information about {thing}"

def cache(db: str, expiration: int):
    cache_data = {}

    def decorator(func):
        def wrapper(thing: str):
            nonlocal expiration
            if thing in cache_data and expiration > 0:
                # Если данные кэшированы и количество запросов не истекло
                expiration -= 1
                return f"Info about: {thing} cached in {db}, expire={expiration}"

            # Получаем актуальные данные, если кэш недоступен или истек
            result = func(thing)
            expiration_value = expiration if expiration > 0 else 0
            # Кэшируем данные
            cache_data[thing] = result
            return f"Info about: {thing} from {db}, now cached with expire={expiration_value}"

        return wrapper

    return decorator

# Применяем декоратор к функции get_info
@cache('postgresql', 5)
def get_bike_info(thing: str) -> str:
    return get_info(thing)

@cache('sqlite', 3)
def get_users_info(thing: str) -> str:
    return get_info(thing)

# Вызовы
print(get_bike_info('bike_store'))  # Первый вызов, кэшируются данные
print(get_bike_info('bike_store'))  # Повторный вызов, данные выдают из кэша
print(get_bike_info('bike_store'))  # Кэш еще активен
print(get_bike_info('bike_store'))  # Кэш еще активен
print(get_bike_info('bike_store'))  # Последний доступ к кэшу
print(get_bike_info('bike_store'))  # Кэш истек, обновляем данные

print(get_users_info('users'))  # Первый вызов, кэшируются данные
print(get_users_info('users'))  # Повторный вызов, данные выдают из кэша
print(get_users_info('users'))  # Кэш еще активен
print(get_users_info('users'))  # Последний доступ к кэшу
print(get_users_info('users'))  # Кэш истек, обновляем данные