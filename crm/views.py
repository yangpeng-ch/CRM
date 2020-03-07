from django.shortcuts import render
from crm.models import Clerk, Customer
# Create your views here.


def index(request):

    return render(request, "index.html")
