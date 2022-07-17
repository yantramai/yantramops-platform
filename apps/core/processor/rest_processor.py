import os, requests, json

cwd = os.path.dirname(os.path.realpath(__file__))


class RESTProcessor():
    def get(url, params):
        headers = {}
        payload = {}
        try:
            response = requests.request("GET", url,params=params, headers=headers, data=payload)
            return response.json()

        except Exception as e:
            raise Exception(format(e))

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
            print(e)
