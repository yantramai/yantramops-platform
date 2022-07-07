# Copyright: (c) 2020, Jayant Kaushal <jayant@yantram.cloud>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
import json

from com.yantram.core.promql_engine.promql_exec import PromqlExec


class postgres_metrices :

    def instant_queries(self):
       # with open('inputs/promethues/instant_query_params_1.json') as f:
       with open('inputs/promethues/instant_query_params.json') as f:
           series_params = json.load(f)
           data = PromqlExec().instant_queries(series_params)
           print(data)


def main():
    data = postgres_metrices().instant_queries()

if __name__ == '__main__':
    main()
