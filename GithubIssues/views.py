from django.shortcuts import render
import urllib.request as url
import requests
from django.contrib import messages
import math
from .utils import Search, Validations, Data


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

        # if the url is not a github repository url Validations.getUrlParams returns error message number
        if lo_url['ev_errorNumber'] != 0:
            # errorMessages function of Data.py file returns mressage corresponding to message number
            messages.error(request, Data.errorMessages(lo_url['ev_errorNumber']))
        else:
            # create full url from api and url entered
            lv_api = "https://api.github.com/repos/" + lo_url['ev_rep_path']
            # call github api from requests.get() function --> convert it into json --> get "open_issues_count" value drom json
            try:
                lv_total_issue_count = requests.get(lv_api).json()["open_issues_count"]

                # considering github issues as 2D array of size: lv_total_rows X 100
                # so we get total number of rows by "lv_total_issue_count/100"
                lv_total_rows = math.ceil(lv_total_issue_count / 100)

                # getOldTiimeStamp function of Data.py returns timestamp of n days before current timestamp in format which github stores
                # getting issues occured in last 24 hours from function getIssueCount by passing tmestamp of 1 day before current timestamp
                lv_last_24hrs_issues = Search.getIssueCount(lv_api, lv_total_rows, Data.getOldTimeStamp(1))

                # subtracting number of issues occured in last 24 hours from no. of issues in last 7 days
                lv_last_24hrs_to_7days_issues = Search.getIssueCount(lv_api, lv_total_rows,
                                                                     Data.getOldTimeStamp(7)) - lv_last_24hrs_issues

                # getting remaining issues
                lv_remaining_issues = lv_total_issue_count - lv_last_24hrs_to_7days_issues - lv_last_24hrs_issues

                # returning required parameters in context to template
                context = {
                    "ev_total_issues": lv_total_issue_count,
                    "ev_last_24hrs_issues": lv_last_24hrs_issues,
                    "ev_last_24hrs_to_7days_issues": lv_last_24hrs_to_7days_issues,
                    "ev_remaining_issues": lv_remaining_issues
                }
                return render(request, 'GitHub/ResultPage.html', context)
            except requests.exceptions.RequestException as e:
                messages.error(request, "API request limit reached")

    return render(request, 'GitHub/HomePage.html')


def results(request):
    return render(request, 'GitHub/ResultPage.html')
