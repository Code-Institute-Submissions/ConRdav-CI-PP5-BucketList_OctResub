from django.shortcuts import render

# Create your views here.


def view_quiz(request):
    """ A view to return the shopping bag """

    return render(request, 'quiz/quiz.html')
