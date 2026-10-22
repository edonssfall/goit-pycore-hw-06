import re
from collections import UserDict


class Field:
    """
    base class for record fields; value must not be empty
    """

    def __init__(self, value):
        if not value:
            raise ValueError('Value must be provided.')
        self.value = value

    def __str__(self) -> str:
        return str(self.value)

    def __eq__(self, value: object, /) -> bool:
        """
        compare by value, so a field equals its plain string (e.g. Name('John') == 'John')
        """
        return self.value == value

    def __hash__(self) -> int:
        return hash(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        """
        validate the phone: exactly 10 digits, otherwise raise ValueError
        """
        if not re.fullmatch(r'^\d{10}', value):
            raise ValueError('Phone must be correct: 10 numbers.')
        super().__init__(value)


class Record:
    """
    contact: a Name and a list of Phone objects
    """

    def __init__(self, name: str):
        self.name: Name = Name(name)
        self.phones: list[Phone] = list()

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, phone: str) -> None:
        """
        add a phone to the contact
        :param phone: phone number: str (validated by Phone)
        """
        self.phones.append(Phone(phone))

    def edit_phone(self, old: str, new: str) -> str:
        """
        replace the old phone with a new one at the same position, if the old one exists
        :param old: phone number to replace: str
        :param new: new phone number: str
        :return: new phone or an error message: str
        """
        index = self.find_index(old)
        if index is not None:
            self.phones[index] = Phone(new)
            return new
        return f'No phone {old} found in contact {self.name}'

    def find_index(self, phone: str) -> int | None:
        """
        find the index of a phone in the phones list
        :param phone: phone number: str
        :return: index: int, or None if not found
        """
        try:
            return self.phones.index(phone)
        except Exception:
            return None

    def find_phone(self, phone: str) -> str | Phone:
        """
        find a phone in the contact
        :param phone: phone number: str
        :return: Phone object or an error message: str
        """
        index = self.find_index(phone)
        return self.phones[index] if index is not None else f'No Phone {phone} found in contact {self.name}'

    def remove_phone(self, phone: str) -> str | Phone:
        """
        remove a phone from the contact
        :param phone: phone number: str
        :return: removed Phone object or an error message: str
        """
        index = self.find_index(phone)
        return self.phones.pop(index) if index is not None else f'No Phone {phone} found in contact {self.name}'


class AddressBook(UserDict):
    """
    address book: records stored in self.data by contact name
    """
    data: dict[Name, Record]

    def add_record(self, rec: Record) -> None:
        """
        add a record to the address book (overwrites a record with the same name)
        :param rec: Record
        """
        self.data[rec.name] = rec

    def find(self, name: str) -> Record | str:
        """
        find a record by name
        :param name: contact name: str
        :return: Record or an error message: str
        """
        if rec := self.data.get(name):
            return rec
        return f"Can't find {name} in Address Book"

    def delete(self, name: str) -> str:
        """
        delete a record by name
        :param name: contact name: str
        :return: result message: str
        """
        if self.data.get(name):
            self.data.pop(name)
            return f"Deleted record: {name}"
        return f"Can't find {name} in Address Book"


def main():
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


if __name__ == '__main__':
    main()
