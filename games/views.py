from .models import *   
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView, TemplateView
from .forms import PlayerForm, SignUpForm2, SignUpForm1
from django.contrib.auth.views import LoginView as BaseLoginView, LogoutView as BaseLogoutView

class LoginView(BaseLoginView):
    template_name = 'games/login.html'

class LogoutView(BaseLogoutView):
    pass

class PlayerDetail(DetailView):
    model = Player
    fields = '__all__'
    template_name = 'games/player-detail.html'
    

    def get_object(self):
        user = self.request.user
        player = user.player
        return player

class PlayerUpdate (View):
    template_name = 'games/player-update.html'
                
    def get(self, request):
        user = request.user
        player_form = PlayerForm(request.FILES, instance=user.player)
        user_form = SignUpForm1(instance=user)
        context = {
            'player_form': player_form,
            'user_form': user_form
        }

        return render(request, self.template_name , context)

    def post(self, request):
        user = request.user
        player_form = PlayerForm(request.POST, request.FILES, instance=user.player)
        user_form = SignUpForm1(request.POST, instance=user)

        if user_form.is_valid() and player_form.is_valid():
            player = player_form.save(commit=False)
            player.user = user
            user_form.save()
            player.save()
            
            print('valide')
            return redirect('games:player-detail')
        context = {
            'player_form': player_form,
            'user_form': user_form
        }
        return render(request, self.template_name,context)


class SignUp(TemplateView):
    template_name = 'games/inscription.html'

    def get(self, request):
        form = SignUpForm2()
        return render(request, self.template_name, {'form' : form})

    def post(self, request):
        form = SignUpForm2(request.POST)
        if form.is_valid():            
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')

            if password1==password2 :
                user = User()
                user.username = form.cleaned_data.get('username')
                user.set_password(password1)
                user.save()
                return redirect("games:login")

        print( "formulaire invalide")
        return render(request, self.template_name)