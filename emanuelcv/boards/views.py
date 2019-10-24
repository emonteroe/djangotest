from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from .models import Board

def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})


def about(request):
    
    return render(request, 'about.html')
    

def board_topics(request, pk):
	# #one way to do it:
	# try:
	# 	board = Board.objects.get(pk=pk)
	# except Board.DoesNotExist:
	# 	raise Http404
	# return render(request, 'topics.html', {'board':board})

	#best way to do it, shorter:
	board = get_object_or_404(Board, pk=pk)
	return render(request, 'topics.html', {'board':board})

