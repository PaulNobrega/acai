from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.forms.models import model_to_dict
from .models import Library
from .forms import UserCreationForm, LoginForm


class LibraryView(LoginRequiredMixin, TemplateView):

    def get(self, request):
        template_name = 'library/library.html'
        all_books = Library.objects.all().values()
        context = {'books': all_books}
        return render(request, template_name, context=context)

class LibraryHtmxView(LoginRequiredMixin, TemplateView):

    def get(self, request):
        template_name = 'library/library-htmx.html'
        all_books = Library.objects.all().values()
        context = {'books': all_books}
        return render(request, template_name, context=context)
    
    def post(self, request):
        template_name = 'library/partials/row.html'
        book_id = request.POST['pk']
        book = Library.objects.get(pk=book_id)
        book.isInStock = False
        book.save()
        book = Library.objects.get(pk=book_id) #dateCheckedOut is an auto_field so query for update and add to return
        result = model_to_dict(book)
        result['dateCheckedOut'] = book.dateCheckedOut
        context = {'book': result}
        return render(request, template_name, context=context)   

class UsersView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):

    def get(self, request):
        template_name = 'register/users.html'
        all_users = User.objects.all()
        context = {'users': all_users}
        return render(request, template_name, context=context)
    
    def test_func(self):
        return self.request.user.groups.filter(name='admin').exists()
    

class LibraryPopulateView(LoginRequiredMixin, View):
    
    def get(self, request):
        Library.faker_populate_library()
        return redirect('library')


class UserSignup(TemplateView):

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('library')
    
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'register/signup.html', {'form': form})


class UserLogin(TemplateView):

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('library')
    
    def get(self, request):
        form = LoginForm()
        return render(request, 'register/login.html', {'form': form})


class UserLogout(LoginRequiredMixin, TemplateView):

    def get(self, request):
        logout(request)
        return redirect('login')