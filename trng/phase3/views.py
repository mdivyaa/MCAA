
from django.shortcuts import render
from django.http import HttpResponse
def project(request):
     a="Project work is a methodical approach to learning where individuals or teams tackle a specific task or problem,<br> applying theoretical knowledge to a practical situation and developing solutions.<br> It's a way to combine theory and practice, encouraging problem-solving, and fostering skills like independence, creativity, and teamwork.<br>In essence, project work is a valuable learning approach that bridges the gap<br> between theoretical knowledge and practical application, <br>preparing individuals for academic and professional success. "
     return HttpResponse(a)
# Create your views here.
