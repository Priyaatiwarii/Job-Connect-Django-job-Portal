from django.shortcuts import render, get_object_or_404
from .models import Job, Application

# This matches your index.html location in jobs/templates/jobs/
def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/index.html', {'jobs': jobs})

# This handles applying for a job
def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        resume = request.POST.get('resume')
        
        Application.objects.create(
            job=job, 
            full_name=full_name, 
            email=email, 
            resume_link=resume
        )
        return render(request, 'jobs/success.html', {'job': job})
        
    return render(request, 'jobs/job_detail.html', {'job': job})