from django.db import models
from django.contrib.auth.models import User

# class TodoList(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=True)
#     name = models.CharField(max_length=200)

#     def __str__(self):
#         return self.self


class List(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)


    def __str__(self):
        return self.item + ' | ' + str(self.completed)
    
    # We need to convert this funtion into database language (sql), and that can be done by making migration in the terminal.
    # After the migrations has been made(i.e converting funtion into database language) and the 0001_initial.py file has been created, 
    # then we will go ahead and push those migrations by running 'python manage.py migrate. in our terminal.
    
# Three 3 major steps in creating database stuff. First is to create the class, the 2nd step is creating a migration, and
# the 3rd step is pushing that migration into the database and making the whole thing live.