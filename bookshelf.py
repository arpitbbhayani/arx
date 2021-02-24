import json
import streamlit as st

st.title("Bookshelf")

# New Book
newbook_expander = st.beta_expander("New Book")
book_id = newbook_expander.text_input("ID")
name = newbook_expander.text_input("Name")
image = newbook_expander.text_input("Image")
description = newbook_expander.text_area("Description")
link = newbook_expander.text_input("Purchase Link")
total_pages = newbook_expander.number_input("Total Pages")

message = newbook_expander.empty()


def do_add_book():
    with open("/Users/arpitbhayani/myw/articles/books.json", "r") as fp:
        books = json.loads(fp.read())
    
    if not book_id or not name or not image or not description or not link or not total_pages:
        message.error("All fields are mandatory")
        return

    new_book = {
        "_id": book_id,
        "n": name,
        "i": image,
        "d": description,
        "plnk": link,
        "total": int(total_pages),
    }

    for book in books:
        if book["_id"] == book_id:
            message.error("Book already exists")
            return

    books.insert(0, new_book)
    with open("/Users/arpitbhayani/myw/articles/books.json", "w") as fp:
        fp.write(json.dumps(books, indent=4))
    newbook_expander.json(json.dumps(new_book))
    message.success(f"Book added. Total Books {len(books)}")


if newbook_expander.button("Add this book"):
    do_add_book()
