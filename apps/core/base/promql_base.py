import os, json
from abc import abstractmethod

cwd = os.path.dirname(os.path.realpath(__file__))


class PromQLProcessor():
    @abstractmethod
    def __init__(self):
        with open(cwd + '/inputs/promql/base.json') as f:
            series_params = json.load(f)
        module = {}
        base_url = series_params['base_url']
        api_v1 = series_params['api_v1']
        module['base_url'] = base_url + api_v1
        self.module = module
