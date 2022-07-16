from apps.core import StatusCodeProcessor
from apps.manage.promql_engine import PromqlExec
import json,os


cwd = os.path.dirname(os.path.realpath(__file__))



class ApacheStatusCodeProcessor(StatusCodeProcessor):


    """Extract text from an email"""
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides InformalParserInterface.load_data_source()"""
        pass

    def process_status_code(self, full_file_path: str) -> dict:
        datasource = self.load_data_source("path","file")
        datasource = 'inputs/promethues/instant_query_params.json'

        self.range_queries()
        """A method defined only in EmlParser.
        Does not override InformalParserInterface.extract_text()
        """
        return {}
    def range_queries(self):
        with open(cwd + '/inputs/range_query_params.json') as f:
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