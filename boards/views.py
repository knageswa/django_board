from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Board

def home(request):
    boards= Board.objects.all()
    board_names=list()

    for board in boards:
    	board_names.append(board.name)

    response_html= '<br>'.join(board_names)

    return render(request,'home.html',{'boards':boards})

def board_topics(request,pk):
	try:
		board=Board.objects.get(pk=pk)
	except Board.DoesNotExist:
		raise Http404
	return render(request, 'topics.html',{'board':board})
# Create your views here.

def new_topic(request,pk):
	board= get_object_or_404(Board,pk=pk)
	return render(request,'new_topic.html',{'board':board})