import yaml
from google.cloud import monitoring_v3
import json
import sys
import os
from pprint import pprint

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "Path/to/service/account/credentails/file"
project_id = sys.argv[1]
project = "projects/"+project_id


def list_uptime_check_configs(project_name):

    client = monitoring_v3.UptimeCheckServiceClient()
    configs = client.list_uptime_check_configs(project_name)
    uptime_check_list = []

    if configs:
        
        for config in configs:
            uptime_check = {
                "name": config.name,
                "display_name": config.display_name,
                "monitored_resource": {
                    "type": config.monitored_resource.type,
                    "labels": {
                        "host": config.monitored_resource.labels.get('host'),
                        "project_id": config.monitored_resource.labels.get('project_id')
                    }
                },
                "http_check": {
                    "use_ssl": config.http_check.use_ssl,
                    "path": config.http_check.path,
                    "port": config.http_check.port
                },
                "period": config.period.seconds,
                "timeout": config.timeout.seconds,
                "selected_regions": ['EUROPE', 'ASIA_PACIFIC', 'USA']
            }

            uptime_check_list.append(uptime_check)
        pprint(uptime_check_list)
    
    else:
        print('No uptime checks found in project')

if __name__ == '__main__':
    list_uptime_check_configs(project)
