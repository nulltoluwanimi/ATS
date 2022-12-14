from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.urls import reverse
from .models import Question, Choice
from django.views import generic


# from django.views import TemplateView

# Create your views here.
# def index(request):
#     question_list = Question.objects.order_by('-pub_date')[:5]
#     print(list(question_list))
#     # output = '.'.join([q.question_text for q in question_list])
#     template = loader.get_template('polls/index.html')
#     context = {'question_list': question_list}
#     # return HttpResponse(template.render(context, request))
#     return render(request, 'polls/index.html', context)


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


# <app name>/<model name>_detail.html.
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/details.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


# class IndexView(TemplateView):
# request=<HttpRequest object>
# def detail(request, question_id):
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")
#     # return render(request, 'polls/detail.html', {'question': question})
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/details.html', {'question': question})


# request=<HttpRequest object>
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "you didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})
