"""from functools import wraps

def log_call(func):
    @wraps(func)
    def wrappers(*args, **kwargs):
        print(f"Вызывается функция {func.__name__} с аргументами {args}")
        res = func(*args, **kwargs)
        print(f"Функция {func.__name__} успешно выполнилась")
        return res 
    return wrappers

@log_call
def wrapper_func(name, arg):
    return name, arg

res_func = wrapper_func("Данил", "хоккеист")
print(res_func)"""

#----------------------------------------------------------------------------
"""import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrappers(*args, **kwargs):

        start_time = time.perf_counter()
        res = func(*args, **kwargs)
        end_time = time.perf_counter()

        execution_time = end_time - start_time

        print(f"Функция {func.__name__} выполнилась за {execution_time:.4f} сек")
        return res
    return wrappers

@timer
def heavy_calculation():
    time.sleep(1.5)
    return "Готово"

result = heavy_calculation()
print(result)"""

#----------------------------------------------------------------------------
"""import json
from functools import wraps

def to_json(func):
    @wraps(func)
    def wrappers(*args, **kwargs):
        res = func(*args, **kwargs)
        json_res = json.dumps(res, ensure_ascii=False)
        return json_res
    return wrappers

@to_json
def get_user_profile():
    return {
        "name": "Данил",
        "role": "Хоккеист",
        "active": True,
        "skills": ["скорость", "точный бросок"]
    }

json_result = get_user_profile()
print(json_result)
print(type(json_result))"""

#----------------------------------------------------------------------------
"""from functools import wraps

def safe_execute(func):
    @wraps(func)
    def warppers(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
            return res
        except Exception as e:
            print("Ошибка")
            return None
    return warppers

@safe_execute
def divide(a, b):
    return a/b

@safe_execute
def add(a, b):
    return a + b

print("--- Тест 1 (ошибка) ---")
res_1 = divide(10, 0)
print(f"Результат {res_1}")

print("--- Тест 2 (нормально) ---")
res_2 = add(10, 5)
print(f"Результат {res_2}")"""

#----------------------------------------------------------------------------
"""from functools import wraps

def validate_ints(func):
    @wraps(func)
    def wrappers(*args, **kwargs):
        for arg in args:
            vetify_args = isinstance(arg, int)
            if vetify_args == False:
                raise TypeError("Аргументы должны быть целыми числами!")
            
        res = func(*args, **kwargs)
        return res
    return wrappers

@validate_ints
def sum_ints(a, b, c):
    return a + b + c

print("--- Тест 1 (правильные данные) ---")
print(sum_ints(1, 2, 3))

print("--- Тест 2 (Неправильные данные) ---")
print(sum_ints(1, "два", 3))"""

"""from functools import wraps

def repeat(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                res = func(*args, **kwargs)
            return res
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Привет, {name}!")

greet("Алексей")"""

#----------------------------------------------------------------------------
"""from functools import wraps

def call_limit(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if wrapper.count >= n:
                raise RuntimeError("Лимит вызовов исчерпан!")
            else:
                wrapper.count += 1
            res = func(*args, **kwargs)
            return res
        
        wrapper.count = 0
        return wrapper
    return decorator
@call_limit(2)
def get_data():
    return "Данные получены"

print(get_data())
print(get_data())
print(get_data())"""

#----------------------------------------------------------------------------
"""import time
from functools import wraps

def memoize(func):
    cache = {}
    @wraps(func)
    def wrappers(*args, **kwargs):
        key = args
        if key in cache:
            print("Взято из кэша")
            return cache[key]
        
        else:
            res = func(*args, **kwargs)
            cache[key] = res
            return res
    return wrappers

@memoize
def heavy_multiplier(n):
    time.sleep(2)
    return n*2

print("--- 1-й вызов (должен длиться 2 секунды) ---")
print(heavy_multiplier(5))

print("\n--- 2-й вызов с ТЕМ ЖЕ аргументом (должен сработать мгновенно) ---")
print(heavy_multiplier(5))

print("\n--- 3-й вызов c НОВЫМ аргументом (должен длиться 2 секунды) ---")
print(heavy_multiplier(10))"""

#----------------------------------------------------------------------------
"""from functools import wraps

ROUTES = []

def register(func):
    ROUTES.append(func)
    return func

@register
def index_page():
    return "Главная страница"

@register
def about_page():
    return "О нас"

def secret_page():
    return "Скрытая страница без декоратора"

print("--- Проверяем список зарегистривоннах функций ---")
print([f.__name__ for f in ROUTES])

print("\n --- Проверяем, что функции работают как обычно ---")
print(index_page())"""