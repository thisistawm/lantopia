from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Question, Choice, Voter


@login_required
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