from django.shortcuts import render
import urllib.request as url
import requests
from django.contrib import messages
import math
from .utils import Validations, Data


def home(request):
    # **********************************function description**************************************#
    # Github repositorty url will come in POST function of request                                #
    # First we will validate the url in getUrlParams function of Validations.py file              #
    # If the url is valid we find the required issues count from github API                     #
    # getIssueCount function of Search.py file returns number of issues in last n number of days  #
    # ******************************************************************************************#

    # check if request coming from template is a post request or not
    if request.method == "POST":
        # get github github url entered by user from request
        lv_link = request.POST["GithubLink"]

        # validate if the url is a github repository url
        lo_url = Validations.getUrlParams(lv_link)

        # create full url from api and url entered
        # different componets of query in url
        lv_api_main = "https://api.github.com/search/issues?q=repo:" + lo_url['ev_rep_path'] + "+is:open+type:issue"
        lv_api_pagination = "&page=1&per_page=1"
        lv_api_created_tag = "+created:>"

        # if the url is not a github repository url Validations.getUrlParams returns error message number
        if lo_url['ev_errorNumber'] != 0:
            # errorMessages function of Data.py file returns mressage corresponding to message number
            messages.error(request, Data.errorMessages(lo_url['ev_errorNumber']))
        else:
            # call github api from requests.get() function -->
            lo_issues_data = requests.get(lv_api_main + lv_api_pagination)
            if lo_issues_data.status_code == 403:
                messages.error(request,"Maximum requests within 1 hour to Github API reached. Please try after 1 hour. MORE DETAILES: https://developer.github.com/v3/#rate-limiting")
            elif lo_issues_data.status_code == 422:
                messages.error(request, "Please enter valid github repository link")
            else:
                # convert it into json -->get "total_count" value from json
                lv_total_issue_count = lo_issues_data.json()["total_count"]
                lv_last_24hrs_issues = requests.get(lv_api_main + lv_api_created_tag + Data.getOldTimeStamp(1) + lv_api_pagination).json()["total_count"]

                # subtracting number of issues occured in last 24 hours from no. of issues in last 7 days
                lv_last_24hrs_to_7days_issues = requests.get(lv_api_main + lv_api_created_tag + Data.getOldTimeStamp(7) + lv_api_pagination).json()["total_count"] - lv_last_24hrs_issues

                # # getting remaining issues
                lv_remaining_issues = lv_total_issue_count - lv_last_24hrs_to_7days_issues - lv_last_24hrs_issues

                # returning required parameters in context to template
                context = {
                    "ev_total_issues": lv_total_issue_count,
                    "ev_last_24hrs_issues": lv_last_24hrs_issues,
                    "ev_last_24hrs_to_7days_issues": lv_last_24hrs_to_7days_issues,
                    "ev_remaining_issues": lv_remaining_issues
                }
                return render(request, 'GitHub/ResultPage.html', context)

    return render(request, 'GitHub/HomePage.html')


def results(request):
    return render(request, 'GitHub/ResultPage.html')
