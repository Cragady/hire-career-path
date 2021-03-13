# Workflows and Setup

## Initial

It looks like for Ubuntu, additional apt packages are required for mysqlclient package:


* `sudo apt-get install python3-dev default-libmysqlclient-dev build-essential`

[Link to Pypi](https://pypi.org/project/mysqlclient/)

Create Venv and activate it:

* `python -m venv env`
* `source env/bin/activate`

Update package manager and setup tools:

* `python -m pip install --upgrade pip`
* `python -m pip install --upgrate setuptools`

Install dependencies:

* `python -m pip install -r requirements.txt`

After installing new dependencies:

* `python -m pip freeze > requirements.txt`

## Create Database

* `python manage.py create-db`


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

## Resume Submissions Types

### Sub-Headers in Regular View

* resume_submisssion_id - INT NOT NULL PRIMARY KEY 
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

aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa