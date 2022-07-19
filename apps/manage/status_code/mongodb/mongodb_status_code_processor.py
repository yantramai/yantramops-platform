import json, os

from prometheus_api_client import MetricsList, MetricSnapshotDataFrame, MetricRangeDataFrame
from prometheus_api_client.utils import parse_datetime, parse_timedelta

from apps.core.base.base_status_code_processor import StatusCodeProcessor
from apps.core.base.promql_executer import PromqlExecuter
from apps.core.base.utils import Utils

cwd = os.path.dirname(os.path.realpath(__file__))


class MongoDBStatusCodeProcessor(StatusCodeProcessor):

    def __init__(self):
        super().__init__()

    def process_status_code(self, full_file_path: str) -> dict:
        start_time = parse_datetime("3d")  # Start time is 3 days before the current timestamp.
        end_time = parse_datetime("now")  # End time is now.
        chunk_size = parse_timedelta("now", "1d")  # Chunk size is 1 day.

        metric_name = "scrape_duration_seconds"  # `scrape_duration_seconds` is the time taken by prometheus to scrape it's targets for metrics.
        metric_name = 'process_virtual_memory_bytes'
        # `scrape_duration_seconds` is the time taken by prometheus to scrape it's targets for metrics.
        metric_data = self.pc.get_metric_range_data(
            metric_name,
            start_time=start_time,
            end_time=end_time,
            chunk_size=chunk_size,
        )
        metric_df = MetricSnapshotDataFrame(metric_data)
        # self._LOGGER.debug("Dataframe: %s", Utils("hhh").print_columns_in_datasource(metric_df))
        # self._LOGGER.debug("columns: %s", metric_df.columns.unique())
        self._LOGGER.debug(metric_df[['__name__','namespace','service',"value"]])

        # print(metric_df.head())
        # metrics_object_list = MetricsList(metric_data)
        # print(len(metrics_object_list))
        # for item in metrics_object_list:
        #     self._LOGGER.debug(item)
        return {}
