from _datetime import datetime, timedelta


def getOldTimeStamp(iv_number_of_days):
    # **********************************function description********************************************************#
    # This function is to get timestamp of n days before current timestamp                                          #
    # IMPORTING: iv_number_of_days   TYPE integer    REMARKS: number of days bfore current timestamp              #
    # EXPORTING: ev_timestamp        TYPE timestamp  REMARKS: required timestamp in github format                 #
    # Github stores timestamp in ISO 8601 format with "Z" at the end but python ISO 8601 format  does not have "Z"#
    # We subtract the timestamp and place "Z" at the end and return it                                            #
    # ************************************************************************************************************#

    if iv_number_of_days == 0:
        ev_timestamp = datetime.now().replace(microsecond=0).isoformat() + 'Z'
    else:
        # timedelta(n) gives timestamp difference between n days
        # replace(microsecond=0).isoformat() converts timestamp to ISO 8601 format
        ev_timestamp = (datetime.now() - timedelta(days=iv_number_of_days)).replace(microsecond=0).isoformat() + 'Z'
    return ev_timestamp


def errorMessages(iv_messageId):
    # **********************************function description********************************************************#
    # This function returns message corresponding to the number passes                                              #
    # IMPORTING: iv_messageId   TYPE integer    REMARKS: message number                                           #
    # this function has normal switch implementation of python                                                      #
    # ************************************************************************************************************#

    switcher = {
        1: 'invalid url',
        2: 'link does not contain git project',
        3: 'link does not contain git repository',
        4: 'only github links are allowed',
    }
    return switcher.get(iv_messageId, "empty")
