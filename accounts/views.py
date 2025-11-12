from django.shortcuts import render, redirect 
from django.contrib.auth import login 
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    if request.method != 'POST':
        form = UserCreationForm() # display blank registration form 
    else:
        form = UserCreationForm(data=request.POST) # process completed form 
        if form.is_valid():
            new_user = form.save() # save new user to database 
            login(request, new_user) # log in the new user 
            return redirect('learning_logs:index') # redirect to index page
    
    context = {'form': form}
    return render(request, 'registration/register.html', context)