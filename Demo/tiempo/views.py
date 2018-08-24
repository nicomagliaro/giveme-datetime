from django.http import HttpResponse
import datetime

# Create your views here.


def index_view(request):
    """
    Home page view
    :param request:
    :return: Html object with current date and time
    """
    now = datetime.datetime.now()
    date = "{}-{}-{}".format(now.day, now.month, now.year)
    hour = "{}:{}".format(now.hour, now.minute)
    html = "<html><body><H1>Son las {} del {}.</H1></body></html>".format(hour,date)
    return HttpResponse(html)