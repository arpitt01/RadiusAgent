This app is made as a part of the coding assignment given by Radius (formerly Agentdesks).

**Problem Statement:** 
Create a repository on GitHub and write a program in any programming language that will do the following: 

**Input**: User can input a link to any public GitHub repository

**Output** : UI should display a table with the following information -

- Total number of open issues
- Number of open issues that were opened in the last 24 hours
- Number of open issues that were opened more than 24 hours ago but less than 7 days ago
- Number of open issues that were opened more than 7 days ago 

**Implementation**:

Solution has been implemented using Django framework.

Application URL: https://radiusagent.herokuapp.com/FindGitHubIssues/

How it has been implemented:

To diaplay the number of issues api provided by Github has been used:
API used: https://api.github.com/repos/issues
    
 - this API returns all issues sorted in ascending order of 'created_on' timestamp
 - maximum 100 issues per call

Challenges in using this API:

**Problem Analysis**
- This API cannot return more than 100 issues in one call. So to analyse all the issues and give count for different intervals
this API needs to be called multiple times in loop by passing page number each time.
API call looks like this: https://api.github.com/repos/{project}/{repository}/issues?page={page number}&per_page=100 
- In order to find number of in last 24hrs, we need to traverse all the issues and compare timestamp with timestamp of 24hrs earlier
- Restriction of 100 issues per call to API, makes this a problem of searching an element in a sorted 2D array 

**Solution**
- In order to improve performance during search, Binary search Algorithm is used in this project to bring complexity down to O(log(n)).
- Main App logic is in Views.py file of folder GithubIssues
- Serach logic is in file Search.py file of GithubIssues/utils
- App is deployed on Heroku

**What could have been improved given more time:**
- Did not explore the github API in detail. There might be ways to improve performance during API calls.
- In the solution I have calculated issues occured in last 24 hrs and issues occured in last 7 days separately.
I think there might be a way where both the calculations could be done simultaneously.
- I might have missed some error handling during api calls. It could be done in a better way covering more cases of failure.
- I could have worked more on UI part and made it more appealing.


