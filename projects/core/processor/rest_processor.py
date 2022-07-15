import os, requests, json

cwd = os.path.dirname(os.path.realpath(__file__))


class RESTProcessor():
    def get(url, params):
        try:
            x = requests.get(
                url=url,
                params=params)
            return x.json()

        except Exception as e:
            raise Exception(format(e))
