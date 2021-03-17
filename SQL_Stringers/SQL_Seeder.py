# This file is no longer needed and is outdated. Just run db migrations using manage.py to seed the db with the tables.
# May keep file around for reference or other utility

def prepender(str):
    returnString = "USE " + str + ";"
    return returnString

def SQL_Init_String(str):
    query_string = """
        CREATE TABLE IF NOT EXISTS resume_submissions(resume_submission_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, job_applied_to TINYTEXT, company_name TINYTEXT, contact_name_and_title TINYTEXT, phone TINYTEXT, email_and_other_contact TINYTEXT, mailing_address TINYTEXT, website TINYTEXT, date_resume_submitted TINYTEXT, date_cover_letter_submitted DATETIME, references_sent TEXT, method_of_discovery TEXT, job_description_and_keywords TEXT, status_of_application TEXT, comments TEXT);
        CREATE TABLE IF NOT EXISTS interviews(interview_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, interview_date DATETIME, interviewer_name_and_title TINYTEXT, phone TINYTEXT, email_and_other_contact TINYTEXT, interview_address TINYTEXT, mailing_address TINYTEXT, follow_up_date DATETIME, comments TEXT)
        CREATE TABLE IF NOT EXISTS networking(networking_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, acquaintance_name_and_title TINYTEXT, company_name TINYTEXT, contact_information TINYTEXT, comments TEXT);
        CREATE TABLE IF NOT EXISTS networking_leads(networking_lead_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, fk_networking_key INT NOT NULL, lead_number INT NOT NULL, company TINYTEXT, contact_information TINYTEXT, comments TEXT);
        CREATE TABLE IF NOT EXISTS career_websites(career_website_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, website TINYTEXT, user_name TINYTEXT, date_resume_posted DATETIME, date_cover_letter_posted DATETIME, comments TEXT);
    """
    return prepender(str) + query_string
