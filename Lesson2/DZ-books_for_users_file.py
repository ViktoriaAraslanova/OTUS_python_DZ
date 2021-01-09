import json
import csv


def json_reader(path):
    with open(path, "r") as f:
        return json.loads(f.read())


def csv_reader(path):
    with open(path, "r") as file_obj:
        reader = csv.reader(file_obj)
        header = next(reader)
        rows = []
        for row in reader:
            rows.append(dict(zip(header, row)))
    return rows


def json_writer(path, json_obj):
    with open(path, 'w+') as f:
        f.write(json.dumps(json_obj, indent=4))


def add_books_for_users(users, books):
    new_users = []
    for user in users:
        new_users.append({'name': user.get('name'), 'gender': user.get('gender'), 'address': user.get('address')})

    new_books = []
    for book in books:
        new_books.append({'title': book.get('Title'), 'author': book.get('Author'), 'height': book.get('Height')})

    for user in new_users:
        if new_books:
            user['book'] = [new_books.pop()]
        else:
            user['book'] = []
    return new_users


if __name__ == "__main__":
    path_json_file = "./files/users-39204-8e2f95.json"
    path_csv_file = "./files/books-39204-271043.csv"
    path_new_json_file = "./files/users-books.json"
    users_from_file = json_reader(path=path_json_file)
    books_from_file = csv_reader(path=path_csv_file)
    users_with_books = add_books_for_users(users=users_from_file, books=books_from_file)
    json_writer(path=path_new_json_file, json_obj=users_with_books)
