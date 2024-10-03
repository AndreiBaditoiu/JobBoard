from django.shortcuts import render, get_object_or_404

from job_board.models import JobPosting


# Create your views here.

def index(request):
    active_postings = JobPosting.objects.filter(is_active=True)
    context = {'job_postings': active_postings
               }
    return render(request, 'index.html', context)


# own
# def job_detail(request, job_posting_id):
#     job_posting = JobPosting.objects.get(pk=job_posting_id)
#     context = {'job_posting': job_posting_id}
#     return render(request, 'job_detail.html', context)
#
# # The one below is more explanatory
def job_detail(request, pk):
    job_posting = get_object_or_404(JobPosting, pk=pk, is_active=True)
    context = {
        'job_posting': job_posting
    }
    return render(request, 'job_detail.html', context)
