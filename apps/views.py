# Create your views here.
import os
import yaml
from django.http import HttpResponse, HttpResponseRedirect
import pandas as pd
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.core.base.promql_executer import PromqlExecuter
from apps.core.processor.yantram_executer import YantramExecuter
from apps.manage.connectors.mongo_db_connection import MongoDBConnection
from apps.manage.status_code.mongodb.mongodb_status_code_processor import MongoDBStatusCodeProcessor
from apps.serializers import UserSerializer
from .forms import CustomForm, NameForm


# cwd = os.path.dirname(os.path.realpath(__file__))


def project_index(request):
    client = MongoDBConnection().get_db_handle(host="localhost",port=27017,username="root",password="12345",db_name="yantram1")
    mydb = client["yantram1"]

    # results = mongo_db_metrics_data()
    # data= {}
    # data.output_file = "/home/rashmi/repo/kubernetes-app-engine/apps/core/base/inputs/base.json"
    # file_name = Utils("ddd").write_to_file(self=data,df=df5.head(5),
    #                                        custom_file_extension='.json',
    #                                        custom_output_file_name="stem",
    #                                        custom_dir=cwd,
    #                                        source_file="promql",
    #                                        sheet_name="ticket_utils")
    # # print(df5['metric'])

    # return df2

    # print(json.dumps(result))
    # df = pandas.read_json(result)
    deployments = mydb["deployments"]
    deployments = mydb["helm_chart_values"]
    deployments = mydb["terraform_configuration"]
    for x in deployments.find():
        print(x)

    # projects = Project.objects.all()
    # return HttpResponse(results)
    context = {"projects": []}
    MongoDBStatusCodeProcessor().process_status_code("dddd")
    return render(request, "project_index.html", context)




# def process_status_code(request):
#     path = "full_path"
#     status_code_response = MongoDBStatusCodeProcessor().process_status_code(full_file_path=path)
#     context = {"projects": status_code_response}
#     return render(request, "project_index.html", context)
#


# import view sets from the REST framework
from rest_framework import viewsets

# import the TodoSerializer from the serializer file
from .serializers import TodoSerializer

from .models import Project


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})


def some_view(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CustomForm()

    return render(request, 'some_html.html', {'form': form})

    # return render(request, 'name.html', {'form': CustomForm()})

