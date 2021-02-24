import json
import streamlit as st

st.title("Bookshelf")

bookadd_expander = st.beta_expander("New Book")
booknuggets_expander = st.beta_expander("Add Nugget")


with open("/Users/arpitbhayani/myw/articles/books.json", "r") as fp:
    books = json.loads(fp.read())


bookadd_book_id = bookadd_expander.text_input("ID")
bookadd_name = bookadd_expander.text_input("Name")
bookadd_image = bookadd_expander.text_input("Image")
bookadd_description = bookadd_expander.text_area("Description")
bookadd_link = bookadd_expander.text_input("Purchase Link")
bookadd_total_pages = bookadd_expander.number_input("Total Pages")
bookadd_message = bookadd_expander.empty()
bookadd_button = bookadd_expander.button("Add this book")

booknuggets_book_id = booknuggets_expander.selectbox(
    'Pick a book',
    [book["_id"] for book in books],
)
booknuggets_nugget = booknuggets_expander.text_area("Nugget")
booknuggets_message = booknuggets_expander.empty()
booknuggets_button = booknuggets_expander.button("Add this nugget")


def do_add_book():
    global books

    if not bookadd_book_id or not bookadd_name or not bookadd_image or not bookadd_description or not bookadd_link or not bookadd_total_pages:
        bookadd_message.error("All fields are mandatory")
        return

    new_book = {
        "_id": bookadd_book_id,
        "n": bookadd_name,
        "i": bookadd_image,
        "d": bookadd_description,
        "plnk": bookadd_link,
        "total": int(bookadd_total_pages),
    }

    for book in books:
        if book["_id"] == book_id:
            bookadd_message.error("Book already exists")
            return

    books.insert(0, new_book)
    with open("/Users/arpitbhayani/myw/articles/books.json", "w") as fp:
        fp.write(json.dumps(books, indent=4))
    with open(f"/Users/arpitbhayani/myw/articles/books/{bookadd_book_id}.json", "w") as fp:
        fp.write(json.dumps([], indent=4))
    bookadd_expander.json(json.dumps(new_book))
    bookadd_message.success(f"Book added. Total Books {len(books)}")


def do_add_nugget():
    if not booknuggets_book_id or not booknuggets_nugget:
        message.error("All fields are mandatory")
        return
    
    with open(f"/Users/arpitbhayani/myw/articles/books/{booknuggets_book_id}.json", "r") as fp:
        nuggets = json.loads(fp.read())

    new_nugget = {
        "n": booknuggets_nugget,
    }

    for nugget in nuggets:
        if nugget["n"] == booknuggets_nugget:
            booknuggets_message.error("Nugget already added")
            return

    nuggets.append(new_nugget)
    with open(f"/Users/arpitbhayani/myw/articles/books/{booknuggets_book_id}.json", "w") as fp:
        fp.write(json.dumps(nuggets, indent=4))

    booknuggets_expander.json(json.dumps(new_nugget))
    booknuggets_message.success(f"Nugget added. Total Nuggets {len(nuggets)}")



if bookadd_button:
    do_add_book()

if booknuggets_button:
    do_add_nugget()
