[![CircleCI](https://dl.circleci.com/status-badge/img/gh/lluc2397/InvFin/tree/master.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/lluc2397/InvFin/tree/master)

# InvFin
The main purpose of the webapp is to centralise information about investing.


# Sections:

<!-- toc -->
- [Q&A](#Q&A)
- [Dicctionary](#Dicctionary)
- [Blog](#Blog)
- [Screener](#Screener)
- [Roboadvisor](#Roboadvisor)
- [SuperInvestors](#SuperInvestors)
- [Portfolio](#Portfolio)
<!-- - [API](#API)
- [Internal](#Internal)
    - [Recsys](#Recsys)
    - [Emailing](#Emailing) -->
- [Side Notes](#Side%20Notes)
<!-- tocstop -->



## Q&A
The Q&A as the purpose of allowing users to ask questions and answer them to help their pairs.
To find the best answers users can upvote or downvote both questions and answers.
Furtheremore they can comment them if they want to add anything to it.

## Dictionnary
An extensive dictionnary fullfiled with financial, economical, accounting, investing, etc... terms where
users can learn about. They can also participate improving the definitions, examples, images and the overall explanation.

## Blog
Users can become writers and send newsletter, have their own domain (subdomain) and create a fan base to send them their newsletters through email.
In this part the writers can see all related to their content, views, times shared, interactions, emails opening rate, and so on.

## Screener
In this part, users can look for over 30000 companies around the globe. They can see their financial statements and financial metrics to make their due diligence. They can introduce their own values to analyse the future value of the company, submit FODA analysis and know which superinvestors have the given company in their portfolio.

## Roboadvisor
Users will have a investor profile and based on that they can ask to analyse some company and see if it would match their profile and investement approach.

## Portfolio
Users can keep track of their finance and investments and share it with the world, set up goals and reminders.


# SIDE NOTES
## TemplateTags
### UTM
A tag to create utm parameters for the urls. source and campaign are at the end as usually medium, content and term are usually changed accross the web.

``
{% utm content='', term='', medium='webapp', source='invfin', campaign='website-links' %}
``

- content: Identifies what specifically was clicked to bring the user to the site, such as a banner ad or a text link
- term: Identifies search terms
- medium: Identifies what type of link was used Default = webapp
- source:  	Identifies which site sent the traffic, and is a required parameter Default = invfin
- campaign: Identifies a specific product promotion or strategic campaign Default = website-links

## Socialmedias
### Facebook
When posting with images or video on facebook, around 6 (or maybe more) lines of text shows up.

### Twitter
1500 tweets per month max

## Companies Information
### Parse Edgar
From this url f"https://data.sec.gov/submissions/CIK{cik_number}.json"
we can get all the fillings of a company. The idea would be to parse it, build the full urls to access the files
and then store the complete url with date and other info according.

### CompaniesDataManagement
``
company = Company.objects.get()

UpdateCompany(company)
``
* *UpdateCompany*: 
    - Interface to call RetreiveCompanyData when updates are needed
    - Will be used by the tasks to update information async

* *RetreiveCompanyData*: 
    - Interface to call the different parsers

# TODO
1. [ ] Better data import/management/update
2. [ ] Fix and improve socialmedia posting
3. [ ] Add ETFs
4. [ ] Add other assets
5. [ ] Enable categories on portfolio
6. [ ] Add random prize
7. [ ] Improve tests
8. [ ] Switch to SPA for some parts (MPA)
9. [ ] Refactor CompaniesDataManagement to separate componenets correctly
10. [ ] Create interface for a company model to set his statements

## Possibles TODO
1. [ ] Stop using yfinance
