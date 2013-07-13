# Create your views here.
from django.http import HttpResponse


from polls.models import Poll, Choice

from django.template import RequestContext, loader
def index(request):
    """
    use template loader and RequestContext to render template
    """
    filters = {'question__contains': 'xx'}
    filters = {}
    
    polls = Poll.objects.order_by('-pub_date')
    if filters:
        polls = polls.filter(**filters)

    #create context and let template render the context
    context = RequestContext(request, {'who': 'john', 'polls': polls})
    tpl = loader.get_template('polls/index.html')
    
    return HttpResponse(tpl.render(context))

from django.shortcuts import render, get_object_or_404
from django.http import Http404    
def detail(request, poll_id):
    """
        use shortcut : render - combine HttpResponse, RequestContext, template loading all together
    """
    
    #
    # short and short cut
    #
    context = {'poll': get_object_or_404(Poll, pk=poll_id)}
    return render(request, 'polls/detail.html', context)
    
    #
    # short cut
    #
    try:
        dtl = Poll.objects.get(pk=poll_id)
        context = {'poll': dtl}        
    except Poll.DoesNotExist:
        raise Http404
        
    return render(request, 'polls/detail.html', context)
    
def result(request, poll_id):
    context = {'poll': Poll.objects.get(pk=poll_id)}
    return render(request, 'polls/result.html', context)
   
from django.http import HttpResponseRedirect   
from django.core.urlresolvers import reverse
def vote(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    
    choice = request.POST.get('choice', None)
    if choice is None:
        return render(request, 'polls/detail.html', {'poll': poll, 'error_msg': 'Please make a selection'})
    
    #ch = Choice.objects.get(pk=choice)
    ch = poll.choice_set.get(pk=choice)
    ch.votes +=1
    ch.save()
    
    return HttpResponseRedirect(reverse('sstar:result', args=(poll_id, )))
    
    
#
# generic view - pattern for common record detail -> action -> redirect result -> list
#
# - don't see much merits, kind of silly and only good for single record or drill down thing
#
#
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'polls'
    
    def get_queryset(self):
        return Poll.objects.order_by('-pub_date')[:10]
        
class DetailView(generic.DetailView):
    model = Poll
    template_name = 'polls/detail.html'

class ResultView(generic.DetailView):
    model = Poll
    template_name = 'polls/result.html'
    
    