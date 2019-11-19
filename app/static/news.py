class Sources:
    '''
    News class to define news sources objects
    '''

    def __init__(self,id,name,author,description,url,category,language,country):
        self.id = id
        self.name = name
        self.author = author
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country


# class Articles:
class Articles:
    '''
    News class to define sources objects
    '''

    def __init__(self,id,author,title,description,url,image,publishedAt,content):
        self.id = id
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.image = image
        self.publishedAt = publishedAt
        self.content = content