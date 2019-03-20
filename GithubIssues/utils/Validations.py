from urllib.parse import urlparse


def getUrlParams(url):
    # **********************************function description******************************************************#
    # This function is to validate if url is a valid github repository url  and send back repository path         #
    # IMPORTING: url             TYPE string                     REMARKS: fetching url to be validated          #
    # EXPORTING: ev_errorNumber  TYPE integer  RANGE: 0,1,2,3,4  REMARKS: sending what king of error url has    #
    #            ev_rep_path     TYPE string                     REMARKS: path of guthub repository             #
    # In this function we break the url in 3 parts using urlparse() and then analyze each part                    #
    # **********************************************************************************************************#

    # local data declation
    lv_project = ''
    lv_repository = ''

    # parsing url and breaking it in 3 parts and then storing it in object
    lo_url_object = urlparse(url)

    if lo_url_object.netloc.lower() == "github.com":  # checking if netloc part is github.com

        # proceeding forward only if path after "github.com" has 2 '/'.
        if lo_url_object.path.count('/') == 2:
            # path after "github.com"  will be like "/projectName/repository"
            # splitting path in 3 parts at "/" : blank, projectName and repository
            lv_slash, lv_project, lv_repository = lo_url_object.path.split('/', 2)

            # raising message 2 if there is no project name
            if lv_project == '':
                lv_error = 2
            # raising message 3 if there is no repository name
            elif lv_repository == '':
                lv_error = 3
            # no message if all is ok
            else:
                lv_error = 0
        else:
            # raising message 1 if url is invalid
            lv_error = 1
    else:
        lv_error = 4
    return {'ev_errorNumber': lv_error,
            'ev_rep_path': lv_project + "/" + lv_repository}
