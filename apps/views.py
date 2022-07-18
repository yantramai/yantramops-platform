# Create your views here.
import json
import os
import yaml
from django.http import HttpResponse
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

cwd = os.path.dirname(os.path.realpath(__file__))


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


def mongo_db_metrics_data():
    go_gc_duration_seconds_query = {}
    # go_gc_duration_seconds_query['query'] = 'go_gc_duration_seconds'
    # go_gc_duration_seconds_query['query'] = 'go_goroutines'
    # go_gc_duration_seconds_query['query'] = 'mongodb_exporter_build_info{branch="",goversion="go1.11.13",revision="",version=""}'
    go_gc_duration_seconds_query['query'] = 'mongodb_exporter_last_scrape_duration_seconds'
    go_gc_duration_seconds_query['query'] = 'promhttp_metric_handler_requests_total{code="200"}'
    go_gc_duration_seconds_query['query'] = 'promhttp_metric_handler_requests_total{code="503"}'
    go_gc_duration_seconds_query[
        'query'] = 'promhttp_metric_handler_requests_total{code!~"2..",container="alertmanager"}'
    go_gc_duration_seconds_query[
        'query'] = 'promhttp_metric_handler_requests_total{code!~"2..",container="alertmanager"}[5m]'
    go_gc_duration_seconds_query['query'] = 'mongodb_exporter_scrapes_total'
    go_gc_duration_seconds_query['query'] = 'mongodb_exporter_build_info'
    go_gc_duration_seconds_query['query'] = 'rate(promhttp_metric_handler_requests_total{code!~"2.."}[5m])[30m:1m]'
    print("#########################################################\n\n")
    print("fetch instant_queries with instant_query_params \n" + json.dumps(go_gc_duration_seconds_query))
    # result = PromqlExecuter().instant_queries_mongo(instant_query_params_1)
    results = PromqlExecuter("http://localhost:9090/api/v1/query").instant_queries_mongo(go_gc_duration_seconds_query)
    df2 = pd.DataFrame.from_dict(results['data']['result'])
    # print(df2['metric'])
    df3 = pd.DataFrame.from_dict(df2['metric'])
    df4 = df3['metric']
    df5 = pd.DataFrame.from_dict(df4)
    print(df5)
    return results


def process_mongo_db_prom_ql(request):
    auth = {}
    client = MongoDBConnection().connect(auth)
    mydb = client["yantram1"]
    deployments = mydb["deployments"]
    # result  = persist_deployment_configurations(client)
    # print(result)
    return HttpResponse("Hello, world. Slap a UI whenever.")
    # context = {"projects": []}
    # return render(request, "project_index.html", context)


def persist_deployments(client):
    print("*******************************************************")
    mydb = client["yantram1"]
    deployments = mydb["deployments"]
    with open('/home/rashmi/repo/kubernetes-app-engine/app-box/deployments_1.yaml') as inputDeploymentFile:
        deployment_file = yaml.load(inputDeploymentFile, Loader=yaml.FullLoader)
        x = deployments.insert_many(deployment_file)
        print(x.inserted_ids)
    print("*******************************************************")


def persist_deployment_configurations(client):
    mydb = client["yantram1"]

    server_info = client.server_info()
    print(server_info)
    print("\nserver info keys:", server_info.keys())

    # get the MongoDB server version string
    print("\nserver version:", server_info["version"])

    # get the database_names from the MongoClient()
    database_names = client.list_database_names()
    print("\ndatabases:", database_names)

    deployment_collection = mydb["deployment"]
    terraform_configuration_collection = mydb["terraform_configuration"]
    helm_chart_values_collection = mydb["helm_chart_values"]

    with open('/home/rashmi/repo/kubernetes-app-engine/app-box/deployments_1.yaml') as yantraminputDeploymentFile:
        deployment_file = yaml.load(yantraminputDeploymentFile, Loader=yaml.FullLoader)

    with open(
            '/home/rashmi/repo/kubernetes-app-engine/app-box/deployment_configurations/mongo.json') as input_terraform_configurations:
        # deployment_file1 = yaml.load(inputDeploymentonfigFile, Loader=yaml.FullLoader)
        mongo_terraform_configurations_file = json.load(input_terraform_configurations)
        mongo_helm_chart_value_orig = mongo_terraform_configurations_file['chart_configurations']['yantram_mongodb'][
            'chart_values']
        # apache_chart_values = mongo_file['chart_configurations']['yantram-apache']['chart_values']

        # print(deployment_file.keys())
        # print(deployment_file['namespace'])
        # print(deployment_file['chart_configurations'])
        # terraform_configuration = mongo_file['deployment_configurations']['yantram-mongodb']
        # print(terraform_configuration)
        with open(
                '/home/rashmi/repo/kubernetes-app-engine/apps/app-box/inputs/helm_chart_values/app/yantram-mongodb.yaml') as inputDeploymentFile:
            mongo_helm_chart_values = yaml.load(inputDeploymentFile, Loader=yaml.FullLoader)
            print("*************************************************************")
            print("deployment")
            # print(deployment_file)
            # x0 = deployment_collection.insert_many(deployment_file)
            # print(x0.inserted_ids)
            for x in deployment_collection.find():
                print(x)

            print("\n\n")

            print("mongo_terraform_configurations")
            # print(mongo_terraform_configurations_file)
            # x = terraform_configuration_collection.insert_one(mongo_terraform_configurations_file)
            # print(x.inserted_id)
            for x in terraform_configuration_collection.find():
                print(x)

            print("\n\n")

            print("mongo_helm_chart_values")
            print(mongo_helm_chart_values)
            # x1 = helm_chart_values_collection.insert_one(mongo_helm_chart_values)
            # print(x1.inserted_id)
            for x in helm_chart_values_collection.find():
                print(x)

            print("\n\n")

            print("*************************************************************")
            print("\n\n")
            print(cwd)
            print("*************************************************************")


def project_detail(request, pk):
    auth = {}
    auth['host'] = 'host'
    auth['port'] = 'port'
    auth['username'] = 'username'
    auth['username'] = 'username'
    auth['password'] = 'password'
    auth['db_name'] = 'db_name'
    connect = MongoDBConnection().connect(auth)
    print(connect)
    # project = Project.objects.get(pk=pk)
    context = {"project": []}
    return render(request, "project_detail.html", context)


def process_status_code(request):
    path = "full_path"
    status_code_response = MongoDBStatusCodeProcessor().process_status_code(full_file_path=path)
    context = {"projects": status_code_response}
    return render(request, "project_index.html", context)



# import view sets from the REST framework
from rest_framework import viewsets

# import the TodoSerializer from the serializer file
from .serializers import TodoSerializer

from .models import Project


class TodoView(viewsets.ModelViewSet):
    # create a serializer class and
    # assign it to the TodoSerializer class
    serializer_class = TodoSerializer

    # define a variable and populate it
    queryset = Project.objects.all()


class UserCreate(APIView):
    """
    Creates the user.
    """
    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response('hello')

