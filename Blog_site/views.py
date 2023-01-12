from django.shortcuts import redirect
from django.urls import reverse


def IPREDIRECT(request):
    return redirect(reverse('News_Feed:main'))