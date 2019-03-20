import requests


def getIssueCount(iv_api_path, iv_total_rows, iv_TargetTimestamp):
    # **********************************function description********************************************************#
    # This function is to count issues created on or after "iv_TargetTimestamp"                                     #
    # IMPORTING: iv_api_path        TYPE string    REMARKS: github api with requested repository path             #
    #            iv_total_rows      TYPE integer   REMARKS: number of rows considering data as 2D matrix          #
    #            iv_TargetTimestamp TYPE timestamp REMARKS: timestamp to be compared                              #
    # EXPORTING: ev_total_issues    TYPE integer   REMARKS: required number of issues                             #
    # We consider the whole data as a sorted 2D array of size rows X 100                                          #
    # In this 2D array will find postion of iv_TargetTimestamp and return number of issues before that point      #
    # We use Binary search function in this case                                                                    #
    # ************************************************************************************************************#

    # getting the row number of the smallest timestamp greater than equal to 'iv_TargetTimestamp' in our 2D array
    lv_row_no = binarySearchOnRow(iv_api_path, 0, iv_total_rows - 1, iv_TargetTimestamp)

    # if no such row exists we return number of issues as 0
    if lv_row_no == -1:
        ev_total_issues = 0
    else:
        # getting the column number of the smallest timestamp larger or equal to 'iv_TargetTimestamp' in our 2D array
        lv_col_no = binarySearchOnCol(iv_api_path, 0, iv_TargetTimestamp, lv_row_no)

        # calculating required number of elements
        ev_total_issues = ((lv_row_no) * 100) + (lv_col_no + 1)  # each row contains 100 issues

    return ev_total_issues


def binarySearchOnRow(iv_githubApi, iv_start, iv_end, iv_TimeStamp):
    # **********************************function description********************************************************#
    # This function is to count issues created on or after "iv_TargetTimestamp"                                     #
    # IMPORTING: iv_githubApi   TYPE string     REMARKS: github api with requested repository path                  #
    #            iv_start       TYPE integer    REMARKS: first row number of 2d aray                                #
    #            iv_end         TYPE integer    REMARKS: last row number of 2d array                                #
    #            iv_TimeStamp   TYPE timestamp  REMARKS: timestamp to be compared                                   #
    # EXPORTING: iv_end         TYPE integer    REMARKS: required row number                                        #
    # We find  the row number no of smallest element(issue) larger than or equal iv_TimeStamp in our 2D arrary      #
    # If there is no such element, -1 will be returned                                                              #
    # **************************************************************************************************************#
    while iv_start <= iv_end:
        # doing this to reduce number of iterations
        # reducing scope of our search area in each iteration
        lv_mid = (iv_start + iv_end) // 2

        # calling github api to get issues
        # traversing different rows of whole data set by passing page number in api
        lo_response = requests.get(iv_githubApi + '/issues?page=' + str(lv_mid + 1) + '&per_page=100')

        # parsing json object to get "created_at" value
        if lo_response.json()[0]['created_at'] >= iv_TimeStamp:
            iv_start = lv_mid + 1
        else:
            iv_end = lv_mid - 1
    return iv_end


def binarySearchOnCol(iv_githubApi, iv_start, iv_TimeStamp, iv_row):
    # **********************************function description********************************************************#
    # This function is to count issues created on or after "iv_TargetTimestamp"                                     #
    # IMPORTING: iv_githubApi   TYPE string     REMARKS: github api with requested repository path                  #
    #            iv_start       TYPE integer    REMARKS: first element of iv_row                                    #
    #            iv_TimeStamp   TYPE timestamp  REMARKS: timestamp to be compared                                   #
    #            iv_row         TYPE timestamp  REMARKS: row number to be searched in                               #
    # EXPORTING: iv_end         TYPE integer    REMARKS: required position of issue in iv_row                       #
    # We find the coloumn number no of smallest element(issue) larger than or equal iv_TimeStamp in our 2D arrary   #
    # **************************************************************************************************************#

    # get data of iv_row in object
    # passing page number in api to get list of issues in that row
    lt_full_data = requests.get(iv_githubApi + '/issues?page=' + str(iv_row + 1) + '&per_page=100').json()

    # getting list of just timestamps to reduce calculations in further loop
    lt_timestamps = [ls_timestamps['created_at'] for ls_timestamps in lt_full_data]

    # setting end point as total elements in that row
    iv_end = len(lt_timestamps)
    while iv_start <= iv_end:
        lv_mid = (iv_start + iv_end) // 2
        if lt_timestamps[lv_mid] >= iv_TimeStamp:
            iv_start = lv_mid + 1
        else:
            iv_end = lv_mid - 1
    return iv_end
