# Технічний опис завдання

Розробіть систему для керування адресною книгою.

### Сутності:

1. `Field`: Базовий клас для полів запису.
2. `Name`: Клас для зберігання імені контакту. Обов'язкове поле.
3. `Phone`: Клас для зберігання номера телефону. Має валідацію формату (10 цифр).
4. `Record`: Клас для зберігання інформації про контакт, включно з іменем та списком телефонів.
5. `AddressBook`: Клас для зберігання записів та керування ними.

### Функціональність:

1. `AddressBook`:
   - Додавання записів.
   - Пошук записів за іменем.
   - Видалення записів за іменем.
2. `Record`:
   - Додавання телефонів.
   - Видалення телефонів.
   - Редагування телефонів.
   - Пошук телефону.

### Рекомендації для виконання:

Для старту ви можете взяти наступний базовий код для реалізації цього домашнього завдання:

```python
from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація класу
    pass

class Phone(Field):
    # реалізація класу
    pass

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    # реалізація класу

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    # реалізація класу
    pass
```

Після реалізації ваш код має виконуватися таким чином:

```python
# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону в записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")
```

> ☝ У наступному домашньому завданні ми додамо цю логіку до нашого бота.

### Критерії оцінювання:

#### Клас `AddressBook`:

1. Реалізовано метод `add_record`, який додає запис до `self.data`.
2. Реалізовано метод `find`, який знаходить запис за ім'ям.
3. Реалізовано метод `delete`, який видаляє запис за ім'ям.

#### Клас `Record`:

1. Реалізовано зберігання об'єкта `Name` в окремому атрибуті.
2. Реалізовано зберігання списку об'єктів `Phone` в окремому атрибуті.
3. Реалізовано методи для додавання — `add_phone` / видалення — `remove_phone` / редагування — `edit_phone` / пошуку
   об'єктів `Phone` — `find_phone`.

#### Клас `Phone`:

1. Реалізовано валідацію номера телефону (має бути перевірка на 10 цифр).
