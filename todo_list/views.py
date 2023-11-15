from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import List
from .forms import ListForm
from django.contrib import messages
# I am using this code below so that users can only access the home page only when they are logged in.
from django.contrib.auth.decorators import login_required



# I am using this @login_required decorator so that users can only access the home page only when they are logged in.
@login_required
def home(request):
    if request.method == "POST":
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request, ('Item Has Been Added'))
            return render(request, 'todo_list/home.html', {'all_items': all_items})
        else:
            return redirect('home')

    else:
        all_items = List.objects.all
        return render(request, 'todo_list/home.html', {'all_items': all_items}) 
    
# def create(request):
#     if request.method == "POST":
#         form = ListForm(request.POST)

#         if form.is_valid():
#             n = form.cleaned_data["name"]
#             t = TodoList(name=n)
#             t.save()
#             request.user.todolist.add(t)

#         return HttpResponseRedirect("/%i" %t.id)
    
#     else:
#         form = ListForm()


 
def about(request): 

    context = {
                'first_name': 'David',
                'last_name': 'Olu'
              }
    return render(request, 'todo_list/about.html', context)

def delete(request, list_id):
    context2 = List.objects.get(pk=list_id)
    context2.delete()
    messages.success(request, ('Item Has Been Deleted!'))
    return redirect('home')

def cross_off(request, list_id):
    context2 = List.objects.get(pk=list_id)
    context2.completed = True
    context2.save()
    return redirect('home')

def uncross(request, list_id):
    context2 = List.objects.get(pk=list_id)
    context2.completed = False
    context2.save()
    return redirect('home')

def edit(request, list_id):
    if request.method == 'POST':
        item = List.objects.get(pk=list_id)

        form = ListForm(request.POST or None, instance=item) 

        if form.is_valid():
            form.save()
            messages.success(request, ('Item Has Been Edited!'))
            return redirect('home')

    # Here this 'item' object variable and key are the real object 'item' and key. 
    else:
        item = List.objects.get(pk=list_id)
        return render(request, 'todo_list/edit.html', {'item': item})
    

































# def login_user(request):
#     # we add this code after we have added the 'method' attribute in our form which is in login.html
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)
#             messages.success(request, ('You Have Successfully Logged In!'))
#             return redirect('home')
        
#         else:
#             messages.success(request, ('Error Logging In - Please Try Again. Thank You!'))
#             return redirect('login')
    
#     else:
#         return render(request, 'todo_list/login.html', {})
    
    
    

