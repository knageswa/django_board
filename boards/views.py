from django.shortcuts import render, get_object_or_404,redirect
from django.http import Http404
from .models import Board,Topic,Post
from django.contrib.auth.models import User
from .forms import NewTopicForm



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
	user= User.objects.first()
	
	if request.method=='POST':

		form=NewTopicForm(request.POST)
		if form.is_valid():
			topic=form.save(commit=False)
			topic.board=board
			topic.starter=user
			topic.save()


			post=Post.objects.create(
				message=form.cleaned_data.get('message'),
				topic=topic,
				created_by=user
			)
			return redirect('board_topics', pk=board.pk)
	else:
		form=NewTopicForm()

	return render(request,'new_topic.html',{'board':board, 'form':form})
