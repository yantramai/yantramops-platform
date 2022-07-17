# Copyright: (c) 2020, Jayant Kaushal <jayant@yantram.cloud>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
import json
import os
import pandas as pd

from apps.core.processor.rest_processor import RESTProcessor

from apps.core.base.promql_base import PromQLProcessor

cwd = os.path.dirname(os.path.realpath(__file__))


class PromqlExecuter(PromQLProcessor):
    def __init__(self,url):
        # self.module = super.__init__(self)
        self.url = "http://localhost:9090/api/v1/query"

    def instant_queries(self, query_params):
        return RESTProcessor.get(self.url, query_params)

    def instant_queries_mongo(self,query_params):
        results = RESTProcessor.get(self.url, query_params)
        print("fetch instant_queries with instant_query_params \n" + json.dumps(results))

        # print(dict['data']['result'].keys())
        df2 = pd.DataFrame.from_dict(results['data']['result'])
        print(df2.head())
        return df2

    def range_queries(self, query_ranger_params):
        url = self.module.get('base_url', None) + '/query_range'
        return RESTProcessor.get(url, query_ranger_params)

    def targets(self, targets_metadata_params):
        url = self.module.get('base_url', None) + '/targets/metadata'
        return RESTProcessor.get(url, targets_metadata_params)

    def targets_metadata(self, targets_metadata_params):
        url = self.module.get('base_url', None) + '/targets/metadata'
        return RESTProcessor.get(url, targets_metadata_params)

    def series(self, series_params):
        url = self.module.get('base_url', None) + '/series'
        return RESTProcessor.get(url, series_params)

    def labels(self, label_params):
        url = self.module.get('base_url', None) + '/labels'
        return RESTProcessor.get(url, label_params)

    def label_info(self, label_name):
        url = self.module.get('base_url', None) + '/label/' + label_name + '/values'
        return RESTProcessor.get(url, {})

    def rules(self, rule_params):
        url = self.module.get('base_url', None) + '/rules'
        return RESTProcessor.get(url, rule_params)

    def tsdb(self, rule_params):
        url = self.module.get('base_url', None) + '/status/tsdb'
        return RESTProcessor.get(url, rule_params)

    def metadata(self, rule_params):
        url = self.module.get('base_url', None) + '/metadata'
        return RESTProcessor.get(url, rule_params)

