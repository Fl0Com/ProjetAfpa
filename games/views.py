from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView , UpdateView 
from .forms import PlayerForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('player-detail', )
    return render(request, 'games/login.html')

# @login_required(login_url='games/login/')
# def main(request):
#     return render(request, "games/main.html")

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            form.save()
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return HttpResponse("Success")
    else:
        form = UserCreationForm()
    return render(request, 'games/signup.html', {'form': form})

#-------------- CRUD Player --------------------

class PlayerCreate (CreateView):
    model = Player
    form_class = PlayerForm
    # template_name = 'games/player-create.html'
    success_url = reverse_lazy('games:players')
    template_name = 'games/registration.html'

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

    def get_context_data(self, **kwargs):
        context = super(PlayerDetail, self).get_context_data(**kwargs)
        context['user'] = Player.objects.get(pk=self.kwargs['pk'])
        return context