# Copyright: (c) 2020, Jayant Kaushal <jayant@yantram.cloud>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
import json
from abc import ABC

from apps.core.base.promql_executer import PromQLProcessor
from apps.core.base.promql_executer import PromqlExecuter
cwd = os.path.dirname(os.path.realpath(__file__))



class PromqlPostgresProcessor(PromQLProcessor, ABC) :

    def instant_queries(self):
       # with open('inputs/promethues/instant_query_params_1.json') as f:
       with open('inputs/promethues/instant_query_params.json') as f:
           series_params = json.load(f)
           data = PromqlExecuter().instant_queries(series_params)
           print(data)

    def main(self):
        with open(cwd + '/inputs/series_params.json') as f:
           series_params = json.load(f)
        with open(cwd + '/inputs/targets_params.json') as f:
           targets_params = json.load(f)
        with open(cwd + '/inputs/label_params.json') as f:
           labels_params = json.load(f)
        with open(cwd + '/inputs/rules_param.json') as f:
           rules_param = json.load(f)
        with open(cwd + '/inputs/targets_metadata_params.json') as f:
           targets_metadata_params = json.load(f)
        with open(cwd + '/inputs/metadata.json') as f:
           metadata_params = json.load(f)

        labels_name = "job"
        data = self.module.instanceQuery()

        result = data['data']['result']

        print(result)
        # for song in result:
        #     print("****************************metric:****************************")
        #     print(song['metric'])
        #     print("****************************metric:****************************")
        #     print("****************************value****************************")
        #     print(song['value'])
        #     print("****************************value****************************")
        # range_data = range_queries()
        # print(range_data)

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


