
from django.shortcuts import render
from django.http import HttpResponse
import sys
from os import PathLike
from subprocess import Popen, PIPE
import json
import time
from tempfile import NamedTemporaryFile
# sys.path.append(
#     '/Users/user/Desktop/HOME/OFFICE/django_class/patrickB/whatsapp/logic')
# print(sys.path)


def index(request):
    if request.method == "POST":
        data = (request.POST)
        data = "hello"
        stingified_data = json.dumps(data)
        process = Popen(['node', 'receivers.js',
                        stingified_data], stdout=PIPE)
        stdout = process.communicate()[0]

        # Parse the data into json
        result_data = json.loads(stdout)
        data = result_data['data']
        return HttpResponse(data)

    else:
        return render(request, "templates\whatsapp\index.html")


def home(request):
    return HttpResponse("hello world")
