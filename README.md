# Hire Career Path

Named this way because puns.

# Overview

This application is a job tracking service that will track job applications and job leads. The application's basic stack is listed below:

* Linux
* Python
  * Flask
* MySQL
* Vue

For a more expansive list of technologies used, any associated `requirements.txt` and `package.json` files will have a list of the main dependencies used. There's a top level `package.json` file simply because I didn't want to install Vue globally. The reason for this is I use `nvm`, Node Version Manager, to swap between versions of node quite frequently. I suppose it's not strictly necessary to do what I did, but I felt like doing it.

There is no front-end setup at the moment. Right now the app is very basic.

# Planned expansions

* User login and authentication
* Dockerization
* Interaction with an email service to send reminder emails

# Reason for Creation

Was inspired by a spreadsheet I used to use. It was fairly cumbersome, so if I want to track my applications and their status I'd rather use this in the future. Also, a good way to learn new technologies.

# Workflows and Setup

## Initial

It looks like for Ubuntu, additional apt packages are required for mysqlclient package:


* `sudo apt-get install python3-dev default-libmysqlclient-dev build-essential`

[Link to Pypi](https://pypi.org/project/mysqlclient/)

Create Venv and activate it in root of project folder:

* `python -m venv env`
* `source env/bin/activate`

Update package manager and setup tools:

* `python -m pip install --upgrade pip`
* `python -m pip install --upgrate setuptools`

Install dependencies:

* `python -m pip install -r requirements.txt`

After installing new dependencies:

* `python -m pip freeze > requirements.txt`

### Configure Environment Variables

Configure a `.env` file and load it into your work terminal. 

* `. .env`

or 

* `. .name_of_file.env`

Example `.env` file:

```r (bash)
# .dev.env
export DB_USER="user_name"
export DB_USER_PASSWORD="user_password"
export DB_HOST="localhost"
export DB_PREFIX="mysql://"
export DB_NAME="db_name"


export DATABASE_SERVER="${DB_PREFIX}${DB_USER}:${DB_USER_PASSWORD}@${DB_HOST}"
export DATABASE_URL="${DATABASE_SERVER}/${DB_NAME}"
export APP_SETTINGS="config.DevelopmentConfig"
```

This goes without saying, but replace the fields according to your desired database setup. You can simplify this to only include the `DATABASE_SERVER`, `DATABASE_URL`, and `APP_SETTINGS` varaibles. This list may be expanded later depending on what is necessary.

### Create Database and Migrate

* `python manage.py create-db`
* `python manage.py db migrate`
* `python manage.py db upgrade`

### Deployment

Will configure this later.

[This is a list of deployment options for Flask](https://flask.palletsprojects.com/en/master/deploying/)


# Layout For Tracker

* Interviews
  * Interview Date | Interviewer Name and Title
    * Phone | Email/Other Contact | Address of Interview | Mailing Address | Date Thank-you Sent | Comments

* Resume Submissions
  * Job Applied For | Company Name | Contact Name and Title
    * Phone | Fax | Email Address | Mailing Address | Website | Date Resume Submitted | Date Cover Letter Submitted | References Sent | How I Heard About This Job | Job Description and Keywords | Status of Application | Comments

* Networking
  * Acquaintance Name and Title | Company Name
    * Contact Information | Date Contacted | Comments
      * Lead (n)  
      * Lead Name and Title | Company | Contact Information | Comments

* Career Websites
  * Website | User Name | Password (Not Recommended) | Date Resume Posted | Date Cover Letter Posted | Comments

# Database and Information Flow/Design

From Resume Submission, if in singular view, have it possible to generate an Interview Entry.

Implement a view where all Interviews, Resume Submissions, and Networking is visible for a singular Company. Search DB for any possible entries that haven't been linked. If there exists entries, pull this entry as well, but color code it different. On click, there should be a query that asks the user if this is the same company. If so, the user is prompted to link to the Company. Group them according to naming conventions. This may be easiest done with a table that essentially only holds relational id's. If a merge is necessary, then edit the entry of the one the user wants to keep while deleting the old entry.

If there are multiple companies with the same name, but for some reason are stored differently, have a popup before the query is executed clarifying which one they want to search. Then use above strategies to combine information and simplify entries. Execute the search query on the relational id table generated.

## Resume Submissions Types - "resume_submissions"

### Sub-Headers in Regular View

* resume_submisssion_id - INT NOT NULL AUTO_INCREMENT PRIMARY KEY 
* job_applied_to - TINYTEXT
* company_name - TINYTEXT

### Rest of Info in Regular View

* contact_name_and_title - TINYTEXT
* phone - TINYTEXT
* email_other_contact - TINYTEXT
* mailing_address - TINYTEXT
* website - TINYTEXT
* date_resume_submitted - DATETIME
* date_cover_letter_submitted - DATETIME
* references_sent - TEXT
* method_of_job_discovery - TEXT
* job_description_and_keywords - TEXT
* status_of_application - TEXT
* comments - TEXT

## Interviews Types - "interviews"

* interview_id - INT NOT NULL AUTO_INCREMENT PRIMARY KEY
* interview_date - DATETIME
* interviewer_name_and_title - TINYTEXT
* phone - TINYTEXT
* email_and_other_contact - TINYTEXT
* interview_address - TINYTEXT
* mailing_address - TINYTEXT
* follow_up_date - DATETIME // date_thank_you_sent
* comments - TEXT

## Networking Types - "networking"

### Sub-Headers in Regular View

* networking_id - INT NOT NULL AUTO_INCREMENT PRIMARY KEY
* aquaintance_name_and_title - TINYTEXT
* company_name - TINYTEXT

### Sub-Sub Headers in Regular View

* contact_information - TINYTEXT
* comments - TEXT

### Leads (Listed under contact so you know who gave you the lead)

* lead - TINYTEXT (Lead-(n))
* lead_name_and_title - TINYTEXT
* company - TINYTEXT
* contact_information - TINYTEXT
* comments - TEXT

## Career Websites Types - "career_websites"

* career_websites_id - INT NOT NULL AUTO_INCREMENT PRIMARY KEY
* website - TINYTEXT
* user_name - TINYTEXT
* date_resume_posted - DATETIME
* date_cover_leter_posted - DATETIME
* comments - TEXT