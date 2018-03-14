from django.shortcuts import render,redirect
from .models import Todo
from .forms import TodoForm
# Create your views here.
def home(request):
	queryset = Todo.objects.all()
	form = TodoForm(request.POST)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return redirect('home')
	context = {
	"queryset":queryset,
	'form':form
	}
	return render(request,'test.html',context)

def Done(request,id):
	query = Todo.objects.get(id=id)
	query.done = True
	query.save()
	return redirect('home')

def NotDone(request,id):
	query = Todo.objects.get(id=id)
	query.done = False
	query.save()
	return redirect('home')

def delete(request,id):
	query = Todo.objects.get(id=id)
	query.delete()
	return redirect('home')