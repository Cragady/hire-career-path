[Back to Readme](../README.md)

# Possible Links

Include link to career website to any relevant entries to gauge how effective the site is.

Link Networking, Resume Submissions, and Interviews with `companies` table.

Link later, get everything set up now.

[SQLAlchemy Docs on Linking](https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html)

# Companies - "companies"

company_id - INT NOT NULL AUTO_INCREMENT PRIMARY KEY
company_name - TINYTEXT
discovery - TEXT
comments - TEXT
created_at - DATETIME
updated_at - DATETIME

# Resume Submissions Types - "resume_submissions"

## Sub-Headers in Regular View

* resume_submisssion_id - INT NOT NULL AUTO_INCREMENT PRIMARY KEY 
* job_applied_to - TINYTEXT
* company_name - TINYTEXT

## Rest of Info in Regular View

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

# Interviews Types - "interviews"

* interview_id - INT NOT NULL AUTO_INCREMENT PRIMARY KEY
* interview_date - DATETIME
* interviewer_name_and_title - TINYTEXT
* phone - TINYTEXT
* email_and_other_contact - TINYTEXT
* interview_address - TINYTEXT
* mailing_address - TINYTEXT
* follow_up_date - DATETIME // date_thank_you_sent
* comments - TEXT

# Networking Types - "networking"

## Sub-Headers in Regular View

* networking_id - INT NOT NULL AUTO_INCREMENT PRIMARY KEY
* acquaintance_name_and_title - TINYTEXT
* company_name - TINYTEXT

## Sub-Sub Headers in Regular View

* contact_information - TINYTEXT
* comments - TEXT

## Leads (Listed under contact so you know who gave you the lead)

* lead - TINYTEXT (Lead-(n))
* lead_name_and_title - TINYTEXT
* company - TINYTEXT
* contact_information - TINYTEXT
* comments - TEXT

# Career Websites Types - "career_websites"

* career_websites_id - INT NOT NULL AUTO_INCREMENT PRIMARY KEY
* website - TINYTEXT
* username - TINYTEXT
* date_resume_posted - DATETIME
* date_cover_leter_posted - DATETIME
* comments - TEXT



[Back to Readme](../README.md)