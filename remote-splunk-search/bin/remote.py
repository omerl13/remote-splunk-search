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
        if sys.version_info[0] < 3:
            r = r.split('\n')
        else:
            r = r.split(bytes('\n', 'utf-8'))
        results = []
        try:
            for i in r[:-1]:
                a = json.loads(i)['result']
                results.append(a)
        except:
            pass
        return results

    def formatQuery(self, query):
        """
        Format query to fit the Splunk UI syntax 
        (default to `search`, other commands require a leading pipeline)
        """
        searchableQuery = query.lstrip()
        if searchableQuery[0] != "|":
            # In case of a regular `search` query
            return 'search ' + searchableQuery
        else:
            # In case of a different generating command - remove the leading `|`
            return searchableQuery[1:]

    def generate(self):
        results = self.__get_data(self.formatQuery(self.query), self.host,
                                  self.username, self.password, self.port)
        return results


dispatch(RemoteCommand, sys.argv, sys.stdin, sys.stdout, __name__)
