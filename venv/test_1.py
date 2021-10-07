documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def people(documnet_number):
    for var1 in documents:
        if var1['number'] == documnet_number:
            return var1['name']


# document_number = input("Введите номер документа: ")
# print(people(document_number))


def shelf(document_number):
    for var2 in directories:
        if document_number in directories[var2]:
            return var2
    return "несуществующий документ"


# document_number = input("Введите номер документа: ")
# print(shelf(document_number))


def list():
    for var3 in documents:
        type = var3['type']
        number = var3['number']
        name = var3['name']
        print('{0}"{1}" "{2}"'.format(type, number, name))


# print(list())


def add(doc_type, doc_number, doc_owner, shelf_id):
    if shelf_id not in directories:
        return "Полки не существует"

    new_doc = dict(type=doc_type, number=doc_number, name=doc_owner)

    documents.append(new_doc)
    directories[shelf_id] += [doc_number]

    return "Документ успешно добавлен"


# doc_type = input("Введите тип докемента: ")
# doc_number = input("Введите номер документа: ")
# doc_owner = input("Введите имя владельца документа: ")
# shelf_id = input("Введит номер полки {} : ".format(directories.keys()))
# print(add(doc_type, doc_number, doc_owner, shelf_id))
# print('')
# print(documents)
# print('')
# print(directories)
# print("Документ успешно добавлен")


def main(doc, direc):
    user_input = input('Введите команду: ')
    if user_input == 'p':
        document_number = input("Введите номер документа: ")
        print(people(document_number))
    elif user_input == 's':
        document_number = input("Введите номер документа: ")
        print(shelf(document_number))
    elif user_input == 'l':
        print(list())
    elif user_input == 'a':
        doc_type = input("Введите тип докемента: ")
        doc_number = input("Введите номер документа: ")
        doc_owner = input("Введите имя владельца документа: ")
        shelf_id = input("Введит номер полки {} : ".format(directories.keys()))
        print(add(doc_type, doc_number, doc_owner, shelf_id))
        print('')
        print(documents)
        print('')
        print(directories)
        print("Документ успешно добавлен")
    elif user_input == " ":
        print('До свидания!')


main(documents, directories)