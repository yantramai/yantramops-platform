# Create your views here.
import json
import os

import yaml


from django.shortcuts import render

from apps.core.base.promql_executer import PromqlExecuter
from apps.manage.connectors.mongo_db_connection import MongoDBConnection
from apps.manage.status_code.mongodb.mongodb_status_code_processor import MongoDBStatusCodeProcessor


cwd = os.path.dirname(os.path.realpath(__file__))

def project_index(request):
    auth = {}
    client = MongoDBConnection().connect(auth)
    mydb = client["yantram1"]
    deployments = mydb["deployments"]
    # result  = persist_deployment_configurations(client)
    # print(result)

    with open(cwd + '/manage/promql_engine/inputs/instant_query_params_1.json') as f:
        instant_query_params_1 = json.load(f)
    print("#########################################################\n\n")
    print("fetch instant_queries with instant_query_params \n" + json.dumps(instant_query_params_1))
    result = PromqlExecuter().instant_queries(instant_query_params_1)
    print(result)
    # df = pandas.read_json(result)
    # for x in deployments.find():
    #     print(x)



    # projects = Project.objects.all()

    context = {"projects": []}
    return render(request, "project_index.html", context)


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


    with open('/home/rashmi/repo/kubernetes-app-engine/app-box/deployment_configurations/mongo.json') as input_terraform_configurations:
        # deployment_file1 = yaml.load(inputDeploymentonfigFile, Loader=yaml.FullLoader)
        mongo_terraform_configurations_file = json.load(input_terraform_configurations)
        mongo_helm_chart_value_orig = mongo_terraform_configurations_file['chart_configurations']['yantram_mongodb']['chart_values']
        # apache_chart_values = mongo_file['chart_configurations']['yantram-apache']['chart_values']

        # print(deployment_file.keys())
        # print(deployment_file['namespace'])
        # print(deployment_file['chart_configurations'])
        # terraform_configuration = mongo_file['deployment_configurations']['yantram-mongodb']
        # print(terraform_configuration)
        with open('/home/rashmi/repo/kubernetes-app-engine/app-box/inputs/helm_chart_values/app/yantram-mongodb.yaml') as inputDeploymentFile:
            # with open('/home/rashmi/repo/kubernetes-app-engine/app-box/inputs/helm_chart_values/app/yantram-apache.yaml') as inputDeploymentFile:
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
    auth['host'] ='host'
    auth['port'] ='port'
    auth['username'] ='username'
    auth['username'] ='username'
    auth['password'] ='password'
    auth['db_name'] ='db_name'
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