"""import time

class Timer:
    def __enter__(self):
        self.start_time = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc, tb):
        self.end_time = time.perf_counter()
        execution_time = self.end_time - self.start_time
        print(f"Время выполнения: {execution_time:.4f} сек")
        return False

with Timer():
    print("Начало вычислений")
    result = sum(i*i for i in range(10**7))
    print("Вычисления завершены")"""
#----------------------------------------------------------------------

"""from contextlib import contextmanager

@contextmanager
def html_tag(tag_name):
    print(f"<{tag_name}>")

    try:
        yield

    finally:
        print(f"<{tag_name}>")

with html_tag('div'):
    print("Привет, мир!")


with html_tag('ul'):
    with html_tag('il'):
        print('Первый элемент списка')
    with html_tag('li'):
        print('Второй элемент списка')"""
#--------------------------------------------------------

"""class IgnoreException:
    def __init__(self, exeptions_to_ignore):
        self.exeptions_to_ignore = exeptions_to_ignore

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        if exc_type is not None and issubclass(exc_type, self.exeptions_to_ignore):
            print(f"Найдена и успешно проигнорирована ошибка {exc_type.__name__}")
            return True
        return False

with IgnoreException(ZeroDivisionError):
    print("Пробуем поделить на ноль...")
    result = 1 / 0
    print("Этот код не выполнится, так как строка выше выбросит ошибку.")

print("Программа не упала! Идем дальше.\n")

try:
    with IgnoreException(ZeroDivisionError):
        print("Пробуем преобразовать текст в число...")
        int("строка")  # Это ValueError
except ValueError:
    print("Перехватили ValueError снаружи, контекстный менеджер её не тронул!")

with IgnoreException((KeyError, IndexError)):
    my_list = [1, 2, 3]
    print(my_list[99])  # IndexError — будет подавлена"""
#--------------------------------------------------------------------------

"""class TransactionCounter:
    def __init__(self, account):
        self.account = account
        self.saved_balance = None

    def __enter__(self):
        self.saved_balance = self.account.balance
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(f"Произошла ошибка: {exc_val}. Откатываем баланс к {self.saved_balance}")
            self.account.balance = self.saved_balance
            return False
        print("Транзакция успешно зафиксирована!")

class Account:
    def __init__(self, balance):
        self.balance = balance

acc = Account(100)

print(f"Исходный баланс: {acc.balance}")

with TransactionCounter(acc):
    acc.balance += 50
    print(f"Внутри контекста (начислили 50): {acc.balance}")

print(f"Баланс после успешного контекста: {acc.balance}\n")

try:
    with TransactionCounter(acc):
        acc.balance += 200
        print(f"Внутри контекста (начислили 200): {acc.balance}")
        # Имитируем внезапный сбой (например, пропал интернет или выключился свет)
        raise ValueError("Сбой связи с банком")
except ValueError:
    print("Ошибка перехвачена в главном коде.")

print(f"Итоговый баланс после сбоя: {acc.balance}")"""
#--------------------------------------------------------------------------------------

"""import sys

class RedirectStdout:
    def __init__(self, filename):
        self.filename = filename
        self.file = None
        self.original_stdout = None

    def __enter__(self):
        self.original_stdout = sys.stdout
        self.file = open(self.filename, "w", encoding="utf=8")
        sys.stdout = self.file

        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout = self.original_stdout

        if self.file:
            self.file.close()

        return False

print("1. Эта строка выведется в обычную консоль.")

with RedirectStdout("output.txt"):
    print("2. А эта строка запишется внутрь файла output.txt!")
    print("3. И эта тоже пойдет в файл.")

print("4. Мы вышли из контекста! Эта строка снова в консоли.")"""
#-------------------------------------------------------------------------

"""import os
from contextlib import contextmanager

@contextmanager
def change_dir(target_path):
    old_path = os.getcwd()
    print(f"Сохраняем исходный путь: {old_path}")

    os.chdir(target_path)
    print(f"Перелетели в папку: {target_path}")

    try:
        yield
    finally:
        os.chdir(old_path)
        print(f"Надежно вернулись обратно в: {old_path}")

if not os.path.exists("test_folder"):
    os.makedirs("test_folder")

print(f"--- Скрипт запущен в папке: {os.getcwd()} ---\n")

try:
    with change_dir("test_folder"):
        print(f"   [Внутри with] Сейчас мы работаем тут: {os.getcwd()}")
        print("   [Внутри with] Происходит какая-то ошибка...")
        raise RuntimeError("Упс! Что-то пошло не так во внешней папке.")
except RuntimeError as e:
    print(f"\n Ошибка перехвачена в основном коде: {e}")

print(f"\n--- Скрипт завершается в папке: {os.getcwd()} ---")"""
