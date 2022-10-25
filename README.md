[![CircleCI](https://dl.circleci.com/status-badge/img/gh/lluc2397/InvFin/tree/master.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/lluc2397/InvFin/tree/master)

# InvFin
The main purpose of the webapp is to centralise information about investing, in spanish.

# CURRENT PARTS
* Q&A
* Screener
* Public Blog
* Roboadvisor
* SuperInvestors
* Portfolio
* Dicctionary


## Q&A
One part is the written content where users can vote, read definitions, share content, ask and answer questions (like SO), improve some definitions or create their own newsletter.
This part is very basic, users can CRUD answers, comments, etc... if they are log in, nothing really fancy.

## Screener
The second part is the screener. For now it's just companies (ETFs and Superinvestors are still in developpements, I have to recreate the database schema, and set up templates, views, etc...) 
In this part, users can look for over 30000 companies around the globe. They can see their financial statements and metrics with nice charts and tables.

## Public Blog
The third part is the "management". Users can create their own newsletter, have a subdomain and create a fan base to send them their newsletters (like substack).
In this part they can see all related to their content, views, times shared, interactions, emails opening rate, etc...

## Roboadvisor
Users will have a investor profile and based on that they can ask to analyse some company and see if it would match their profile and investement approach.

## Portfolio
Users can keep track of their finance and investments and share it with the world, set up goals and reminders.


# SIDE NOTES
## Creation
I used cookiecutter to start the project to see how to structure it "correctly".
The website is deployed on a single core CPU so multithreading is limited. For everything related to sending emails or scraping for information Celery with Redis handle that. Why Redis? Well, Django Cookiecutter came with that so I wanted to give it a try. Before I used RabbitMQ as it is focused on being a message broker I thought that it was more appropriate. Now I'm using Redis to test it and because I can use it to cache.

## TemplateTags
### UTM
A tag to create utm parameters for the urls. source and campaign are at the end as usually medium, content and term are usually changed accross the web.

#### {% utm content='', term='', medium='webapp', source='invfin', campaign='website-links' %}

- content: Identifies what specifically was clicked to bring the user to the site, such as a banner ad or a text link
- term: Identifies search terms
- medium: Identifies what type of link was used Default = webapp
- source:  	Identifies which site sent the traffic, and is a required parameter Default = invfin
- campaign: Identifies a specific product promotion or strategic campaign Default = website-links

## Socialmedias
### Facebook
When posting with images or video on facebook, around 6 (or maybe more) lines of text shows up.

## Parse Edgar
From this url f"https://data.sec.gov/submissions/CIK{cik_number}.json"
we can get all the fillings of a company. The idea would be to parse it, build the full urls to access the files
and then store the complete url with date and other info according.

# TODO
1. [ ] Improve recommendations
2. [ ] Improve roboadvisor
3. [ ] Add ETFs
4. [ ] Add other assets
5. [ ] Enable categories on portfolio
6. [ ] Add random prize
7. [ ] Improve emailing
8. [ ] Improve noitfications
9. [ ] Improve tests
