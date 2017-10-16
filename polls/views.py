from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .models import Question, Choice, Voter

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request):
        if request.method == "POST":
            try:
                selected_choice = Choice.objects.get(id=request.POST['choice'])
            except (KeyError, Choice.DoesNotExist):
                latest_question_list = Question.objects.order_by('-pub_date')[:5]
                return render(request, 'polls/index.html', {
                    'error_message': "You didn't select anyhting",
                    'latest_question_list': latest_question_list
                })
            if Voter.objects.filter(question_id=selected_choice.question.id,user_id=request.user.id).exists():
                latest_question_list = Question.objects.order_by('-pub_date')[:5]
                return render(request, 'polls/index.html', {
                    'error_message': "You can only vote once per poll",
                    'latest_question_list': latest_question_list
                })
            selected_choice.votes += 1
            selected_choice.save()
            v = Voter(user=request.user, question=selected_choice.question)
            v.save()
        latest_question_list = Question.objects.order_by('-pub_date')[:5]
        latest_question = Question.objects.latest('pub_date')
        context = {'latest_question_list': latest_question_list, 'latest_question': latest_question }
        return render(request, 'polls/index.html', context)
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        # return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))