from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from app.models import UserDetailsModel


def sample(request):
    return render(request, 'sample.html')


def index_save(request):
    if request.method != 'POST':
        return HttpResponseRedirect(reverse("sample.html"))
    else:
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        mname = request.POST.get("mname")
        datepicker = request.POST.get("datepicker")
        email = request.POST.get("email")
        gender = request.POST.get("gender")
        country = request.POST.get("country")
        state = request.POST.get("state", default = None)
        file = request.POST.get("file")

    userdetailssample = UserDetailsModel(fname=fname, lname=lname, mname=mname, datepicker=datepicker, email=email,
                                             gender=gender, country=country, state=state, file=file)
    userdetailssample.save()

    return HttpResponse("Data saved successfully")
