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
API used : https://api.github.com/search/issues

Note: there might be some cases where this api returns  issues with a difference of +/-1. This maight be due to newly created/deleted/merged issues 


**Solution**
- In order to fetch the count of asked issues parameters are passed in the api to query
- https://api.github.com/search/issues?q=repo:{REPOSITORY_NAME}+is:open+type:issue+created:>{TIMESTAMP}&page=1&per_page=1
- REPOSITORY_NAME: Github url added by user is broken and name of repository is found
- TIMESTAMP      : This timestamp is Current timestamp - time difference(24 hrs or 7 days)
- &page=1&per_page=1 is added to fetch minimum number of entries to increase performance.
- This API returns a json string in which first value is "total_count" which is count of open issues in asked time period.

- App is deployed on Heroku

**What could have been improved given more time:**
- Did not explore the github API in detail. There might be ways to improve performance during API calls.
- I might have missed some error handling during api calls. It could be done in a better way covering more cases of failure.
- I could have worked more on UI part and made it more appealing.


