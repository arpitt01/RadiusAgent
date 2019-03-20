from django.shortcuts import render
import urllib.request as url
import simplejson
from django.contrib import messages
import math
from .utils import Search, Validations, Data

def home(request):
    if request.method == "POST":
        lv_link = request.POST["GithubLink"]
        lo_url = Validations.getUrlParams(lv_link)
        if lo_url['ev_iserror'] != 0:
            print(Data.errorMessages(lo_url['ev_iserror']))
            messages.error(request, Data.errorMessages(lo_url['ev_iserror']))
        else:
            lv_api = "https://api.github.com/repos/" + lo_url['ev_rep_path']
            lv_total_issue_count = simplejson.load(url.urlopen(lv_api))["open_issues_count"]
            lv_total_rows = math.ceil(lv_total_issue_count/100)
            lv_last_24hrs_issues = Search.getIssueCount(lv_api,lv_total_rows,Data.getTimeStamp(1))
            lv_last_24hrs_to_7days_issues = Search.getIssueCount(lv_api,lv_total_rows,Data.getTimeStamp(30)) - lv_last_24hrs_issues
            lv_remaining_issues  = lv_total_issue_count - lv_last_24hrs_to_7days_issues - lv_last_24hrs_issues
            context = {
                "ev_total_issues"                 : lv_total_issue_count,
                "ev_last_24hrs_issues"            : lv_last_24hrs_issues,
                "ev_last_24hrs_to_7days_issues"   : lv_last_24hrs_to_7days_issues,
                "ev_remaining_issues"             : lv_remaining_issues
            }
            return render(request, 'GitHub/ResultPage.html' ,context )

    return render(request, 'GitHub/HomePage.html')

def results(request):
    return render(request, 'GitHub/ResultPage.html')