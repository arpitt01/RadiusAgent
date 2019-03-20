from _datetime import datetime, timedelta

def getTimeStamp( iv_number_of_days):
    if iv_number_of_days == 0:
        ev_timestamp = datetime.now().replace(microsecond=0).isoformat() + 'Z'
    else:
        ev_timestamp = (datetime.now() - timedelta(days=iv_number_of_days)).replace(microsecond=0).isoformat() + 'Z'
    return ev_timestamp

def errorMessages(iv_messageId):
    switcher = {
        1: 'invalid url',
        2: 'link does not contain git project',
        3: 'link does not contain git repository',
        4: 'only github links are allowed',
    }
    return switcher.get(iv_messageId, "empty")