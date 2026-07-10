book_profile = {
"title": "Основи програмування",
"author": "Іван Петренко",
"year": 2023,
"publisher_info": {
"name": "Наукова думка",
"city": "Київ"
}
}

print(book_profile["title"])
print(book_profile["author"])


print(book_profile["publisher_info"]["name"])


print(f'Книга "{book_profile["title"]}" автора {book_profile["author"]} була видана у місті {book_profile["publisher_info"]["city"]}.')


if "year" in book_profile:
    print(book_profile["year"])
else:
    print("Рік видання невідомий")