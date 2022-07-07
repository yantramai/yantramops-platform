# Copyright: (c) 2020, Jayant Kaushal <jayant@yantram.cloud>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
import json,os
import requests
cwd = os.path.dirname(os.path.realpath(__file__))
print(cwd)

def get(url, params):
    try:
        x = requests.get(
            url=url,
            params=params)
        return x.json()

    except Exception as e:
        raise Exception(format(e))


class PromqlExec :

    def instant_queries(self,query_params):
        url = self.module.get('base_url', None) + '/query'
        return get(url,query_params)

    def range_queries(self,query_ranger_params):
        url = self.module.get('base_url', None) + '/query_range'
        return get(url, query_ranger_params)

    def targets(self,targets_metadata_params):
        url = self.module.get('base_url', None) + '/targets/metadata'
        return get(url, targets_metadata_params)

    def targets_metadata(self,targets_metadata_params):
        url = self.module.get('base_url', None) + '/targets/metadata'
        return get(url, targets_metadata_params)

    def series(self,series_params):
        url = self.module.get('base_url', None) + '/series'
        return get(url,series_params)

    def labels(self,label_params):
        url = self.module.get('base_url', None) + '/labels'
        return get(url,label_params)

    def label_info(self,label_name):
        url = self.module.get('base_url', None) + '/label/'+label_name+'/values'
        return get(url, {})

    def rules(self,rule_params):
        url = self.module.get('base_url', None) + '/rules'
        return get(url,rule_params)
    def tsdb(self,rule_params):
        url = self.module.get('base_url', None) + '/status/tsdb'
        return get(url,rule_params)
    def metadata(self,rule_params):
        url = self.module.get('base_url', None) + '/metadata'
        return get(url,rule_params)

    def __init__(self):
        with open('inputs/base.json') as f:
            series_params = json.load(f)
        module = {}
        base_url = series_params['base_url']
        api_v1 = series_params['api_v1']
        module['base_url'] = base_url + api_v1
        self.module = module


def main():
    with open(cwd+'/inputs/series_params.json') as f:
        series_params = json.load(f)
    with open(cwd+'/inputs/targets_params.json') as f:
        targets_params = json.load(f)
    with open(cwd+'/inputs/label_params.json') as f:
        labels_params = json.load(f)
    with open(cwd+'/inputs/rules_param.json') as f:
        rules_param = json.load(f)
    with open(cwd+'/inputs/targets_metadata_params.json') as f:
        targets_metadata_params = json.load(f)
    with open(cwd+'/inputs/metadata.json') as f:
        metadata_params = json.load(f)

    labels_name = "job"
    data = instanceQuery()


    result = data['data']['result']

    print(result)
    for song in result:
        print(song['metric'])
        # print(song)
        # print(song)
        print(song['value'])
    #range_data = range_queries()
    #print(range_data)

    # range_result = range_data['data']['result']
    # print(range_result)
    # for song in range_result:
    #     print(song['metric'])
    #     # print(song)
    #     # print(song)
    #     print(song['value'])
    # print("#########################################################\n\n")
    # print("fetch series with series_params \n"+json.dumps(series_params))
    # print("#########################################################")
    # PromqlExec().series(series_params)
    # print("#########################################################\n\n")
    # print("#########################################################")
    # print("list labels with labels_params \n"+json.dumps(labels_params))
    # PromqlExec().labels(labels_params)
    # print("list labels without labels_params \n"+json.dumps({}))
    # PromqlExec().labels({})
    # print("#########################################################\n\n")
    # print("#########################################################")
    # print("fetch label info for label label \n"+labels_name)
    # PromqlExec().label_info(labels_name)
    # print("#########################################################\n\n")
    # print("#########################################################")
    # print("fetch rules with rules_param \n"+json.dumps(rules_param))
    # PromqlExec().rules(rules_param)
    # print("#########################################################\n\n")
    # print("#########################################################")
    # target(targets_params)

    # print("#########################################################\n\n")
    # print("#########################################################")
    # print("fetch targets_metadata with targets_metadata_params \n"+json.dumps(targets_metadata_params))
    # PromqlExec().targets_metadata(targets_metadata_params)
    # trext = PromqlExec().tsdb({})
    # trext = PromqlExec().metadata(metadata_params)
    # print("#########################################################\n\n")
    # print("#########################################################")


def range_queries():
    with open('inputs/range_query_params.json') as f:
        range_query_params = json.load(f)
    print("#########################################################\n\n")
    print("fetch instant_queries with instant_query_params \n" + json.dumps(range_query_params))
    return PromqlExec().range_queries(range_query_params)


def target(targets_params):
    print("fetch targets with targets_params \n" + json.dumps(targets_params))
    # PromqlExec().targets({})
    # data = PromqlExec().targets({})
    data = PromqlExec().targets(targets_params)
    # json_object = json.loads(data)
    for song in data['data']:
        print(song['target']['service'])
        print(song['metric'])


def instanceQuery():
    with open('inputs/instant_query_params.json') as f:
        instant_query_params = json.load(f)
    # print("#########################################################")
    # print("fetch instant_queries with instant_query_params \n" + json.dumps(instant_query_params))
    return PromqlExec().instant_queries(instant_query_params)
    print("#########################################################")


if __name__ == '__main__':
    main()


    def get1(self):
        base_url = 'http://localhost:9090'
        try:
            x = requests.get('https://w3schools.com/python/demopage.htm')
            query_range = '/api/v1/query_range'
            alertmanagers = '/api/v1/alertmanagers'
            query = base_url + '/api/v1/query?query=up&start=2015-07-01T20:10:30.781Z&end=2015-07-01T20:11:00.781Z&step=15s'
            # query_ranger= base_url+'/api/v1/query_range?query=up&start=2015-07-01T20:10:30.781Z&end=2015-07-01T20:11:00.781Z&step=15s'

            query = base_url + '/api/v1/query'
            query_params = {
                # 'query': 'up'
                # 'query': 'http_requests_total'
                'query': 'http_requests_total{job="apiserver", handler="/api/comments"}',
                # 'time': '1502809554'
            }
            query_ranger = base_url + '/api/v1/query_range'
            query_ranger_params = {
                'query': 'sum({__name__=~".+"}) by (__name__,instance)',
                'start': '1502809554',
                'end': '1502809554',
                'step': '1'
            }

            series = base_url + '/api/v1/series'
            series_params = {
                'match[]': 'up',
                'start': '1502809554',
                'end': '1502809554',
                'step': '1'
            }
            labels = base_url + '/api/v1/labels'
            label_name = 'job'
            label_info = base_url + '/api/v1/label/' + label_name + '/values'
            labels_input = {
                'match[]': 'up',
                # 'match[]': 'process_start_time_seconds{job="prometheus"}'
                # 'query': 'up'
            }
            targets = base_url + '/api/v1/targets'
            target_input = {
                'state': 'active',
                # 'match[]': 'process_start_time_seconds{job="prometheus"}'
                # 'query': 'up'
            }
            rules = base_url + '/api/v1/rules'

            query_series_input = {
                'match[]': 'up',
                # 'match[]': 'process_start_time_seconds{job="prometheus"}'
                # 'query': 'up'
            }
            # myobj = {'query': 'somevalue'}

            # x = requests.post(url, data=myobj)
            # print(x)
        except Exception as e:
            print(x.text)
