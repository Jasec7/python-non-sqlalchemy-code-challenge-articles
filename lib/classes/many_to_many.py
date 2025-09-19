class Article:
    all = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("Not an author")
        else:
            self._author = value

    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise Exception("Not a magazine")
        else:
            self._magazine = value

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if hasattr(self, "_title"):
            raise Exception("Title is already set")
        if not isinstance(value, str):
            raise Exception("Title must be a string")
        if len(value.strip()) < 5 or len(value.strip()) > 50:
            raise Exception("Titles must be between 5 and 50 characters")
        self._title = value
        
class Author:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if hasattr(self, "_name"):
            raise Exception("Name already set")
        if not isinstance(value, str):
            raise Exception("Name must be a string")
        if len(value.strip()) <= 0:
            raise Exception("Invalid name")
        self._name = value


    def articles(self):
        return [article for article in Article.all if article.author is self]

    def magazines(self):
        matches = []
        for magazine in self.articles():
            m = magazine.magazine
            if m not in matches:
                matches.append(m)
        return matches

    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        return new_article

    def topic_areas(self):
        matches = []
        for article in self.articles():
            c = article.magazine.category
            if c not in matches:
                matches.append(c)
        if not matches:
            return None
        else:
            return matches


class Magazine:
    all = []
    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Name must be a string")
        if len(value.strip()) < 2 or len(value.strip()) > 16:
            raise Exception("Names must be between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise Exception("Not a string")
        if len(value.strip()) <= 0:
            raise Exception("Categories must be longer than 0 characters")
        self._category = value

    def articles(self):
        return [article for article in Article.all if article.magazine is self]

    def contributors(self):
        matches = []
        for author in self.articles():
            c = author.author
            if c not in matches:
                matches.append(c)
        return matches

    def article_titles(self):
        titles = []
        for t in self.articles():
            ti = t.title
            titles.append(ti)
        if titles == []:
            return None
        else:
            return titles

    def contributing_authors(self):
        result = []
        for a in self.contributors():
            count = 0
            for article in self.articles():
                if article.author is a:
                    count += 1
            if count > 2:
                result.append(a)

        if not result:
                return None
        else:
                return result
        
    @classmethod
    def top_publisher(cls):
        if Article.all == []:
            return None
        else:
            best_magazine = None
            best_count = 0

            for m in cls.all:
                count = len(m.articles())
                if count > best_count:
                    best_count = count
                    best_magazine = m
        return best_magazine
