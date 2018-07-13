import sys
import json
from splunklib.searchcommands import dispatch, GeneratingCommand, Configuration, Option, validators
from splunklib import client


@Configuration()
class RemoteCommand(GeneratingCommand):
    query = Option(require=True)
    host = Option(require=True)
    username = Option(require=True)
    password = Option(require=True)
    port = Option(require=False, default="8089")

    def __get_data(self, query, host, username, password, port):
        service = client.connect(
            host=host,
            port=port,
            username=username,
            password=password)

        # Get the collection of jobs
        jobs = service.jobs

        # Run a blocking search--search everything, return 1st 100 events
        kwargs_blockingsearch = {"output_mode": "json", "max_count": 0}

        exportsearch_results = service.jobs.export(
            query, **kwargs_blockingsearch)
        r = exportsearch_results.read()
        r = r.split('\n')
        results = []
        try:
            for i in r[:-1]:
                a = json.loads(i)['result']
                results.append(a)
        except:
            pass
        return results

    def generate(self):
        results = self.__get_data("search " + self.query, self.host,
                                  self.username, self.password, self.port)
        return results


dispatch(RemoteCommand, sys.argv, sys.stdin, sys.stdout, __name__)
