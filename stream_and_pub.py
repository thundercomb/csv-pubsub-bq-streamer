import requests as rq
from contextlib import closing

from google.cloud import pubsub

project_id = "my_project"
topic_name = "csv_test"
url = "https://data.kingcounty.gov/api/views/yaai-7frk/rows.csv?accessType=DOWNLOAD"
publisher = pubsub.PublisherClient(batch_settings=pubsub.types.BatchSettings(max_latency=5))
topic_path = publisher.topic_path(project_id, topic_name)

with closing(rq.get(url, stream=True)) as r:
    f = (line.decode('utf-8') for line in r.iter_lines())
    flag = 0
    for row in f:
        if flag == 0:
            flag = 1
            pass # skip header row
        else:
            publisher.publish(topic_path, data=row.encode('utf-8'))
