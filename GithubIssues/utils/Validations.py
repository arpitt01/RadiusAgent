from urllib.parse import urlparse

def getUrlParams(url):
    lo_url_object   = urlparse(url)
    lv_project      =  ''
    lv_repository   =  ''
    if lo_url_object.netloc == "github.com" :
        if lo_url_object.path.count('/') == 2:
            lv_slash, lv_project, lv_repository = lo_url_object.path.split('/', 2)
            if lv_project == '' :
                lv_error = 2
            elif lv_repository == '' :
                lv_error = 3
            else:
                lv_error = 0
        else:
            lv_error = 1
    else:
        lv_error = 4
    return { 'ev_iserror' : lv_error ,
             'ev_rep_path': lv_project + "/" + lv_repository}