---
title: '💭 learning strawberry'
date: 2024-03-20T21:43:45
templateKey: link
link: None
tags:
  - graphql
published: true

---

> ``` python
import logging
from typing import List

import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

logger = logging.getLogger(__name__)

authors = {}
books = {}
book_authors = {}
authors_books = {}


def get_author_for_book(root) -> "Author":
    return authors[book_authors[root.id]]


@strawberry.type
class Book:
    id: int
    title: str
    author: "Author" = strawberry.field(resolver=get_author_for_book)


def get_books_for_author(root) -> List[Book]:
    print(f"getting books for {root}")
    return [books[i] for i in authors_books[root.id]]


@strawberry.type
class Author:
    id: int
    name: str
    books: List[Book] = strawberry.field(resolver=get_books_for_author)


authors = {1: Author(id=1, name="Michael Crichton")}
books = {1: Book(id=1, title="Jurassic Park")}
# relationships
book_authors[1] = 1
authors_books[1] = [1]


def get_author_by_id(id: int) -> Author:
    return authors.get(id)


def get_book_by_id(id: int) -> Book:
    return books.get(id)


def get_authors(root) -> List[Author]:
    return authors.values()


def get_books(root) -> List[Book]:
    print(books)
    print(authors)
    print(book_authors)
    print(authors_books)
    return books.values()


@strawberry.type
class Query:
    author: Author = strawberry.field(resolver=get_author_by_id)
    book: Book = strawberry.field(resolver=get_book_by_id)
    authors: List[Author] = strawberry.field(resolver=get_authors)
    books: List[Book] = strawberry.field(resolver=get_books)

    @strawberry.field
    def hello(self, name: str = None) -> str:
        """this is a resolver for hello, just like authors and books have a resolver"""
        if name is None:
            return "Hello World"
        return f"Hello {name}"


@strawberry.input
class AddBookInput:
    title: str = strawberry.field(description="The title of the book")
    author: str = strawberry.field(description="The name of the author")


@strawberry.type
class Mutation:
    @strawberry.field
    # def add_book(self, title: str, author: str) -> Book:
    def add_book(self, book: AddBookInput) -> Book:
        print(f"i got a book: {book.title}")
        print(f"of type {type(book.title)}")
        name = book.author
        title = book.title
        author = [author for id, author in authors.items() if author.name == name]
        print(f"here are the names {[author.name for id, author in authors.items()]}")
        print(f"my name is { name }")
        print(f"this is the author i found {author}")
        if author:
            author = author[0]
            author_id = author.id
        else:
            author_id = max(authors.keys()) + 1
            author = Author(id=author_id, name=name)
            authors[author_id] = author

        book = [b for id, b in books.items() if b.title == title]
        if book:
            book = book[0]
        else:
            book_id = max(books.keys()) + 1
            book_authors[book_id] = author_id
            print(f"I am making book {book_id}")
            print(f"{name} has books {authors_books.get(author_id)}")

            if author_id in authors_books.keys():
                authors_books[author_id].append(book_id)
            else:
                authors_books[author_id] = [book_id]
            book = Book(id=book_id, title=title)
            books[book_id] = book

        print(f"i got books: {books}")
        print(f"i got authors: {authors}")
        return book


schema = strawberry.Schema(query=Query, mutation=Mutation)

router = GraphQLRouter(
    schema,
)

app = FastAPI()

```

[Original thought](None)
