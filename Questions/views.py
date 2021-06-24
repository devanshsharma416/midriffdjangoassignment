# Question - 1 : What is the difference between the id and pk

from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def index(request, id):
    post1 = get_object_or_404(Post, id = 1) # will return same result
    post2 = get_object_or_404(Post, pk = 1) 


# pk is a special parameter in django. If we enter the index/1 the post1 and post2 will return the same values. 
# the primary difference is that id is default parameter to represent the primary key of models where pk is used when 
# define a primary key manually. In simple words, id is defaulr primary key representation and pk is used to define custom primary key.




# # Question - 3: ValueError at/akolaprofile/ The view akola.views.alokaprofile didnt return Httpresponce object. It return None. What might be wrong.
# # Answer - It can happen because of two reason - 

# 1. There are IndentationError. If the value is return inside the condition instead of funtion. It may cause of ValueError.
# 2. Return a response in cases when request.method is not post