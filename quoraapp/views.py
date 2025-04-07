
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, QuestionForm, AnswerForm
from .models import Question, Answer

def home(request):
    questions = Question.objects.all().order_by('-created')
    return render(request, 'home.html', {'questions': questions})

def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('home')
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def post_question(request):
    form = QuestionForm(request.POST or None)
    if form.is_valid():
        question = form.save(commit=False)
        question.author = request.user
        question.save()
        return redirect('home')
    return render(request, 'post_question.html', {'form': form})

def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    answers = question.answers.all()
    form = AnswerForm(request.POST or None)
    if form.is_valid():
        answer = form.save(commit=False)
        answer.question = question
        answer.author = request.user
        answer.save()
        return redirect('question_detail', pk=pk)
    return render(request, 'question_form.html', {'question': question, 'answers': answers, 'form': form})

@login_required
def like_answer(request, pk):
    answer = get_object_or_404(Answer, pk=pk)
    answer.likes.add(request.user)
    return redirect('question_detail', pk=answer.question.pk)
