from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def index(request):
    """View function for home page of site."""

    return render(request, 'index.html')

# def setup(request):
    # """View function for game page of site."""
    
    # # POST - on submit validation happens here, then is redirected using reverse
    # if request.method == 'POST':
    #     # Fill the form out with data you got
    #     form = SetupGameForm(request.POST)

    #     if form.is_valid():
    #         # Set fields using session data
    #         players = []
    #         players.append(form.cleaned_data['player0'])

    #         # remove all of the empty player fields
    #         while '' in players : players.remove('')
    #         request.session['players'] = players

    #         # and query and get them when loading the game
    #         request.session['ace_rule'] = form.cleaned_data['ace_rule']

    #         #  Then use reverse to redirect with form data to the game url
    #         return HttpResponseRedirect(reverse('game'))
    
    # # GET - show an empty form
    # else:
    #     form = SetupGameForm(initial={
    #         'ace_rule': 'All'})

    # context = {
    #     'form': form,
    # }

    # return render(request, 'setup.html', context=context)
