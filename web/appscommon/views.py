from django.shortcuts import render
from django.conf import settings
from appscommon.apps import AppscommonConfig


def setup_context(request):
    return {'app_name': AppscommonConfig.verbose_name,
            'app_short_name': AppscommonConfig.short_name,
            }


def home(request):
    """ Show the default page """
    context = setup_context(request)
    return render(request, 'appscommon/base.html', context)
