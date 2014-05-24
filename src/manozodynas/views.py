"""
Prideti forma, kurioje galima butu prideti nauja irasa i db ir poto ta irasa atvaizduotu,
sukurti testa, sio funkcionalumo patikrinmui
viska i github
"""
from django.shortcuts import render
from manozodynas.models import Word
from django.http import HttpResponse
from django.views.generic import CreateView



def index_view(request):
    return render(request, 'manozodynas/index.html', {})

def random_word_view(request):
	random_word = Word.get_random_word()  
	return render(request, 'manozodynas/random.html', {"random_word":random_word.word})

def random_words_view(request, count):
	random_words = Word.get_random_words(count)
	if (random_words):
		return render(request, 'manozodynas/random_words.html', 
			{"random_words":random_words, "count":count})
	else:
		return HttpResponse('<h1>There was a problem processing your request.</h1>' \
			'<h2>You might have tried to get 0 random words.</h2>')

class AddWord(CreateView):
	model = Word
	success_url = '/words'
	template_name = 'manozodynas/add_word.html'

def words_view(request):
	return render (request, 'manozodynas/words.html', {'words': Word.objects.all()})
