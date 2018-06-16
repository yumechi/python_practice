#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

URL = "https://supporterzcolab.com/api/v1/event/"

def get_week_date(**kward):
    from datetime import datetime as dt, timedelta
    import time

    params = dict()
    params['order'] = kward.get('order', 1)
    start_date = dt.now()
    if kward.get('start_date'):
        sd = kward.get('start_date')
        if isinstance(str, sd):
            try:
                start_date = dt.strptime(sd, '%Y/%m/%d')
            except Exception as e:
                print('日付形式がおかしいです', sd)
                raise e
        elif isinstance(datetime, sd):
            start_date = sd
        else:
            print('start_dateはstring, datetimeのどちらかでお願いします。')
            raise TypeError
    
    for i in range(7):
        date_delta = timedelta(days=i)
        d = start_date + date_delta
        params['ymd'] = dt.strftime(start_date, '%Y%m%d')
        
        params_format = '&'.join([('{0}={1}').format(k, v) for k, v in params.items()])
        if not params_format:
            print('skip')
            continue
        access_point = '{0}?{1}'.format(URL, params_format)

        if kward.get('debug'):
            print(access_point)
            print('####################################################')
            print('####################################################')
            print()
        
        responce = requests.get(access_point).json()
        for elem in responce['events']:
            elem['description'] = ''
            print('\n'.join(['{0}={1}'.format(k, v) for k, v in elem.items()]))
        
        print()
        time.sleep(1)

if __name__=="__main__":
    get_week_date(debug=True)
