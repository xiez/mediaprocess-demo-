#!/bin/env python

import time
import datetime

org_id = '$org_id'
event_id = '$event_id'
lvp = '$lvp'
leg = '$leg'

curl_cmd_fmt = 'curl -d  "org_id=%s&event_id=%s&event_timestamp=%d&event_type=MEDIA_PROCESSING_SUCCESS&media_id=%s&upload_method=ftp&original_filename=%s" http://vmplvp1%s.%s'


latest_log = 'latest.log'
with open(latest_log) as f:
    lines = f.readlines()

log_list = [x.strip() for x in lines]

not_processed = 'NotProcessed.txt'
with open(not_processed) as f:
    lines = f.readlines()

for line in lines:
    media_id = line.strip()
    try:
        idx = log_list.index(media_id)
    except ValueError:
        continue

    filename = log_list[idx + 1].split(' ')[-1]
    curl_cmd = curl_cmd_fmt % (org_id, event_id,
                               int(time.mktime(datetime.datetime.now().timetuple())),
                               media_id, filename, leg, lvp)
    print curl_cmd
