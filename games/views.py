from .models import *   
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView , UpdateView , FormView
from .forms import PlayerForm, SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth import authenticate, login, logout

def test(request):
    return render(request, 'games/test.html' )


class LoginView(BaseLoginView):
    template_name = 'games/login.html'

class SignUp(CreateView):
    template_name = 'games/test.html'
    form_class = SignUpForm
    success_url = reverse_lazy('games:player-create')

    # def post(self, request):
    #     form = SignUpForm(request.POST)
    #     if form.is_valid():
    #         username = form.cleaned_data.get('username')
    #         password = form.cleaned_data.get('password')
    #         form.save()
    #         user = form.save()
    #         return HttpResponse("Success")




# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password')
#             form.save()
#             user = form.save()
#             login(request, user, backend='django.contrib.auth.backends.ModelBackend')
#             return HttpResponse("Success")
#     else:
#         form = UserCreationForm()
#     return render(request, 'games/signup.html', {'form': form})


#-------------- CRUD Player --------------------

class PlayerCreate (CreateView):
    model = Player
    form_class = PlayerForm
    success_url = reverse_lazy('games:players')
    template_name = 'games/player-create.html'

class PlayerUpdate (UpdateView):
    model = Player
    fields = "__all__"
    template_name = 'games/player-update.html'
    success_url = reverse_lazy('games:players')

class PlayerDelete (DeleteView):
    model = Player
    fields = ['pseudo']
    success_url = reverse_lazy('games:players')
    template_name = 'games/player-delete.html'

class PlayerList(ListView):
    model = Player
    template_name = 'games/players.html'

class PlayerDetail(DetailView):
    model = Player
    fields = '__all__'
    template_name = 'games/player-detail.html'

    def get_object(self):
        user = self.request.user
        return user

    # def get_context_data(self, **kwargs):
    #     context = super(PlayerDetail, self).get_context_data(**kwargs)
    #     context['user'] = Player.objects.get(pk=self.kwargs['pk'])
    #     return context