import simplejson
import urllib.request as url

def binarySearchOnRow( iv_githubApi, iv_start, iv_end, iv_TimeStamp):
    while iv_start <= iv_end:
        lv_mid = (iv_start + iv_end)// 2
        if simplejson.load(url.urlopen(iv_githubApi + '/issues?page=' + str(lv_mid+1) + '&per_page=100'))[0]['created_at'] >= iv_TimeStamp:
            iv_start = lv_mid + 1
        else:
            iv_end = lv_mid - 1
    return iv_end


def binarySearchOnCol(iv_githubApi, iv_start, iv_TimeStamp, iv_row):
    ls_mid_data = simplejson.load(url.urlopen(iv_githubApi + '/issues?page=' + str(iv_row+1) + '&per_page=100'))
    iv_end = len(ls_mid_data)
    while iv_start <= iv_end:
        lv_mid = (iv_start + iv_end) // 2
        if ls_mid_data[lv_mid]['created_at'] >= iv_TimeStamp:
            iv_start = lv_mid + 1
        else:
            iv_end = lv_mid - 1
    return iv_end

def getIssueCount(iv_api_path, iv_total_rows,iv_TargetTimestamp):
    lv_row_no = binarySearchOnRow(iv_api_path, 0, iv_total_rows - 1, iv_TargetTimestamp)
    if lv_row_no == -1:
        ev_total_issues = 0
    else:
        lv_col_no = binarySearchOnCol(iv_api_path, 0, iv_TargetTimestamp, lv_row_no)
        ev_total_issues = ((lv_row_no) * 100) + (lv_col_no + 1)
    return ev_total_issues