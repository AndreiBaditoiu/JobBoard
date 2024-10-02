from django.shortcuts import HttpResponse, render

from job_board.models import JobPosting


# Create your views here.

def index(request):
    active_postings = JobPosting.objects.filter(is_active=True)
    context = {'job_postings': active_postings
               }
    return render(request, 'index.html', context)
