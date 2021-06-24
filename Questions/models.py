#Questions - 2 Use SQL query inside the Model

from django.db import models

# Creating Author model
class Author(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name
# Creating post model with the many-to-one relation
class Post(models.Model):
    title = models.CharField(max_length=20)
    author = models.ForeignKey(Author, on_delete= models.CASCADE)

    def __str__(self):
        return self.title

# Answer - 2

# To run the SQL Queries we will use the Django ORM by typing the "pythin manage.py shell"

# >>> from Questions.models import Author
# >>> a1 = Author(name = 'Mathew', email = 'mathew@gmail.com')
# >>> a1.save()
# >>> a2 = Author(name = 'Letham', email = 'lathem@gmail.com') 
# >>> a2.save()
# >>> from Questions.model s import Post 
# >>> p1 = Post(title = 'Ghost Stories', author = a1)
# >>> p1.save()
# >>> p2 = Post(title = 'Horror Stories, author = a2)
# >>> p2.author
# <Author: Letham>
# >>> p2.title
# 'Horror Stories'

# Questions - 4 what is _set.all() in djanog

# Answer - The _set.all() will return the post objects of perticular author. For example - We have used the _set.all() to 
# get the all posts which author name is 'Mathew'.
# Coding example - 
# >>> new_post = Post.objects.create(title = "Thriller Stories", author = a1)
# >>> new_post_set.all()

#Output:
# <QuerySet [<Post: Ghost Stories>, <Post: Thriller Stories>]>

