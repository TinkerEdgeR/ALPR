#!/usr/bin/python3

from os import listdir
from datetime import datetime, timezone, timedelta
import requests, ast, csv, sys, base64


image_folder = sys.argv[1]
url = 'http://127.0.0.1/image'

tz = timezone(timedelta(hours=+8))
with open(datetime.now(tz).strftime("%Y-%m-%d_%H-%M-%S") + '.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Item', 'Filename', 'Confidence', 'Plate', 'Start Time', 'End Time', 'Take time'])
    for idx, image_name in enumerate(listdir(image_folder)):
        print('{}: handle {}'.format(idx, image_name))
        try:
            with open(image_folder + image_name, 'rb') as image_file:
                start_time = datetime.now(tz)
                response = requests.post('http://localhost:8080/data/image/recognize', data=(base64.b64encode(image_file.read())).decode())
                end_time = datetime.now(tz)
                #print(response)
                if response.status_code == 200:
                    response_content = response.content.decode('UTF-8')
                    response_content = ast.literal_eval(response_content)
                    print(repr(response_content))
                    object_len = len(response_content)
                    if object_len > 0:
                        for jdx, result in enumerate(response_content):
                            writer.writerow([str(idx + 1), (image_name + '_p' + str(jdx + 1)) if object_len > 1 else image_name, result['confidence'], result['plate'], start_time.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3], end_time.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3], (end_time - start_time).total_seconds()])
                    else:
                        writer.writerow([str(idx + 1), image_name, 'NA', 'NA', start_time.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3], end_time.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3], (end_time - start_time).total_seconds()])
                else:
                    print('get fail response with: ' + response.text)
                    writer.writerow([str(idx + 1), image_name, 'ERROR', response.text + '({})'.format(response.status_code), start_time.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3], end_time.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3], (end_time - start_time).total_seconds()])
        except Exception as e:
            print('except: ' + str(e))
            break
