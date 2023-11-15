from django.contrib import admin
from .models import List


admin.site.register(List)








# This section of code adds/registers the database/table which I created to the django web Admin page, so that 
# I can manipulate it from there(djang web admin page).


# first we import model's List and then we register it on the actual page.