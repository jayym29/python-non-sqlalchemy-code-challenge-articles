class Article:
    all_articles = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        self.add_to_all()

    def __repr__(self):
        return f"Article('{self.author}', '{self.magazine}', '{self.title}')"

    def add_to_all(self):
        Article.all_articles.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        if isinstance(new_author, Author):
            self._author = new_author
        else:
            raise TypeError("Author must be an instance of Author")

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, new_magazine):
        if isinstance(new_magazine, Magazine):
            self._magazine = new_magazine
        else:
            raise TypeError("Magazine must be an instance of Magazine")

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        if isinstance(new_title, str) and 5 <= len(new_title) <= 50:
            self._title = new_title
        else:
            raise ValueError("Title must be a string between 5 and 50 characters")


class Author:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Author(name='{self.name}')"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and len(new_name) > 0:
            self._name = new_name
        else:
            raise ValueError("Name must be a non-empty string")

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        magazine.add_article(article)
        return article


class Magazine:
    all_magazines = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._articles = []
        Magazine.all_magazines.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 2 <= len(new_name) <= 16:
            self._name = new_name
        else:
            raise ValueError("Name must be a string with length between 2 and 16 characters.")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if isinstance(new_category, str) and len(new_category) > 0:
            self._category = new_category
        else:
            raise ValueError("Category must be a non-empty string.")

    def add_article(self, article):
        self._articles.append(article)

    def __repr__(self):
        return f"Magazine(name='{self.name}', category='{self.category}')"

