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

~~Create Venv and activate it in root of project folder:~~

Create and activate the Venv in the `server` directory of the project folder:

* `python -m venv env`
* `source env/bin/activate`

Update package manager and setup tools:

* `python -m pip install --upgrade pip`
* `python -m pip install --upgrade setuptools`

Install dependencies:

* `python -m pip install -r requirements.txt`

After installing new dependencies:

* `python -m pip freeze > requirements.txt`

### Configure Environment Variables

Note: I have since moved all of my `.env` files into their own directory. For whatever setup you have, just source it appropriately. Change the `test.sh` script for your appropriate test variables, or follow the same directory setup I do.

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
export DB_PREFIX="mysql+mysqlconnector://"
export DB_NAME="db_name"


export DATABASE_SERVER="${DB_PREFIX}${DB_USER}:${DB_USER_PASSWORD}@${DB_HOST}"
export DATABASE_URL="${DATABASE_SERVER}/${DB_NAME}"
export APP_SETTINGS="config.DevelopmentConfig"
```

Note: If you are deploying with AWS, then you'll have to config the environment variables differently.

This goes without saying, but replace the fields according to your desired database setup. You can simplify this to only include the `DATABASE_SERVER`, `DATABASE_URL`, and `APP_SETTINGS` varaibles. This list may be expanded later depending on what is necessary.

### Create Database and Migrate

* `python manage.py create_db`
* `python manage.py db migrate`
* `python manage.py db upgrade`

#### AWS Database

I'm taking the quick and easy route on this. I'll update this portion when I find a better solution, as for now however, I just want to get something up and running.

Create a `.env` file, I'm probably going to name mine `.aws.env`. Put this env file in a directory named `secret.env/` for ease of access, or wherever you want the env file to go.

Source the `.env` file, then run the manage.py commands for migration and updating. 

Don't forget to source your env for your development or testing environments!

I honestly don't like running the database migrations like this, if I find a better way, I will update this section. If it gets a bit too long, I'll move this section to it's own `.md` file under the `docs/` directory.



### Deployment Backend

[This is a list of deployment options for Flask](https://flask.palletsprojects.com/en/master/deploying/)

#### AWS

Whooo, so this one was a doozy to set up for me initially. I don't know why I had to fight like this, for this repository, I've had other test repos pushed much more easily than this one. I have it working at this point though. You'll be able to find the AWS deployment method [in the AWS.md file here.](docs/AWS-deployment.md)

I will add more deployment methods later if I'm feeling inspired.

### Deployment Frontend

I'm keeping the front and back separate from each other.

# Database and Information Flow/Design

In the future, there *may* be a ***massive*** database redesign. Right now I just want to get a basic application up and running. Eventually I want to get the Interviews, Resume Submissions, and Networking all linked together to a company and the user.

From Resume Submission, if in singular view, have it possible to generate an Interview Entry.

Implement a view where all Interviews, Resume Submissions, and Networking is visible for a singular Company. Search DB for any possible entries that haven't been linked. If there exists entries, pull this entry as well, but color code it different. On click, there should be a query that asks the user if this is the same company. If so, the user is prompted to link to the Company. Group them according to naming conventions. This may be easiest done with a table that essentially only holds relational id's. If a merge is necessary, then edit the entry of the one the user wants to keep while deleting the old entry.

If there are multiple companies with the same name, but for some reason are stored differently, have a popup before the query is executed clarifying which one they want to search. Then use above strategies to combine information and simplify entries. Execute the search query on the relational id table generated.

[Further on the Database](./docs/DATABASE.md)



## Layout For Tracker

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



# Potential Problems and Possible Improvements

* Using the name `Network` and `network`. Keep an eye out for any unexpected behavior from using these names. I plan on having a better naming convention for this in the future.

* Right now I'm updating all columns when updating an entry on a table. This may cause unnecessary overhead. Will fix later.

* Maybe make a test class that contains boiler data to throw into the database. This will make writing test cases easier when creating a migration that include table links.

# Bugs/Problems/Other

This is where I'll be tracking problems. I'll remove items that I feel are sufficiently addressed. If an issue is noteworthy or may cause problems later will be listed [here.](#Fixed,%20but%20Noteworthy)

* There is one test case that will pass even if there is no endpoints set up for the dataset. Need to rewrite all test cases with the string `test_failed_update_of_` in its name.

* Need to set id to be non-editable.

* Do not allow an id of `0` to be written to database

# Fixed, but Noteworthy

Issues that have been fixed, but are noteworthy will go here. Issues that may appear to be fixed but can cause problems later will also go here.