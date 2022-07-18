import json,os

from prometheus_api_client import MetricsList, MetricSnapshotDataFrame
from prometheus_api_client.utils import parse_datetime, parse_timedelta

from apps.core.base.base_status_code_processor import StatusCodeProcessor
from apps.core.base.promql_executer import PromqlExecuter


cwd = os.path.dirname(os.path.realpath(__file__))



class MongoDBStatusCodeProcessor(StatusCodeProcessor):

    def __init__(self):
        super().__init__()

    def process_status_code(self, full_file_path: str) -> dict:
        print(self.pc.all_metrics())
        start_time = parse_datetime("3d")  # Start time is 3 days before the current timestamp.
        end_time = parse_datetime("now")  # End time is now.
        chunk_size = parse_timedelta("now", "1d")  # Chunk size is 1 day.

        metric_name = "scrape_duration_seconds"  # `scrape_duration_seconds` is the time taken by prometheus to scrape it's targets for metrics.
        metric_data = self.pc.get_metric_range_data(
            metric_name,
            start_time=start_time,
            end_time=end_time,
            chunk_size=chunk_size,
        )
        metric_df = MetricSnapshotDataFrame(metric_data)
        print(metric_df.head())
        metrics_object_list = MetricsList(metric_data)
        print(len(metrics_object_list))
        for item in metrics_object_list:
            print(item.metric_name, item.label_config, "\n")
            print(item.metric_values)
        return {}


    def range_queries(self):
        with open(cwd + '/inputs/range_query_params.json') as f:
            range_query_params = json.load(f)
        print("#########################################################\n\n")
        print("fetch instant_queries with instant_query_params \n" + json.dumps(range_query_params))
        return PromqlExecuter().instant_queries_mongo(range_query_params)
