[Back to Readme](../README.md)

# Brief Overview

I have successfully pushed the api portion of this project to lambda AWS. I haven't configured the database for this api to interact with the database yet, I will create docs for it when I'm able to do so.

# Setup

Since I've changed the directory structure, you will have to activate your virtual environment (whatever you decided to name it, I named mine `env`) and use zappa.

To be able to push your code to lambda, you will have to configure the AWS cli to have your credentials. I'll update the details of this later.

## AWS CLI

There are two files that need to be configured. 

```bash
# In credentials
[default]
aws_access_key_id = ******
aws_secret_access_key = ******

[zappa]
aws_access_key_id = ******
aws_secret_access_key = ******
```

```bash
[default]
region = ******
output = json

[zappa]
region = ******
output = json
```

During the init of aws cli, it will ask you for your credentials. You can either input the variables here, or manually edit the files.

You can either use your root user's access keys or create an IAM user that belongs to a group to push to lambda. AWS recommends that you use an IAM user instead of root to do this. 

You can configure this on your Identity and Access Management (IAM) dashboard.

The click path for this:

Services > IAM (Under Security, Identity, & Compliance)

Or just search IAM.

## Zappa

Once you have that setup, you'll be able to run the commands necessary for deployment.

I'm assuming you have the virtual environment active, for me to activate the virtual environment, this is what I do from the root of the project:

* `cd server`
* `. env/bin/activate`

In the `server` directory, run `zappa init`. Zappa will ask you several questions, if you're unsure, leave it as default and just press enter. It will generate a basic `zappa_settings.json` file for you. There is still some settings that need to be filed out before a successful push can happen. This is what my settings file looks like:

```json
{
    "dev": {
        "app_function": "manage.lambda_app",
        "aws_region": <region here>,
        "profile_name": "zappa",
        "project_name": <project name here>,
        "runtime": "python3.8",
        "s3_bucket": <bucket name here>,
        "slim_handler": true,
        "exclude": ["*.exe", "*.Python", "*.git", ".git*", "*.zip*", "*.tar.gz",
            "*.hg", "*.egg-info", "env", "pip", "docutils*", "setuputils*", 
            "__pycache__", "node_modules"
        ]
    }
}
```

You will have to set the region to the relevant value that is set with your account. The project name can be whatever you want. For the s3_bucket, zappa will create one for you. If you want it named differently, just change the name. If you have an existing bucket you want to push to, use the name for that bucket.

From here, you can run these commands to deploy, update, delete, or see the log:

* `zappa deploy dev`
* `zappa update dev`
* `zappa undeploy dev`
* `zappa tail`

If you need the log to be written to a file, you can run a command that's similar to below:

* `zappa tail > zappa_log`
  * `zappa tail > <file name here, ext is optional>

## Environment Variables

After you deploy for the first time, you will have to edit the environment variables. For this application, at this time of writing, the required environment variables is as follows:

* APP_SETTINGS
* DATABASE_SERVER
* DATABASE_URL
* DB_NAME

Navigate to your Lambda console in AWS. You can find this in the `Services` dropdown menu at the top. It will be under the `Compute` subcategory under `Lambda`. You can also use the search bar and just search `Lambda` to find it if you don't want to look through the services list.

From the landing page for Lambda, click on `Functions` in the side bar. From there select your function name from the page you're taken to. Once you're in your Lambda function, click on `Configuration`, then `Environment Variables`.

Select `Edit` and keep adding environment variables until the appropriate number variables exist. Then just fill out the key and value pairs. 

### A Couple Things of Note

The `DATABASE_SERVER` and `DATABASE_URL` need to have the prefix `mysql+mysqlconnector://`. So for example, your connection string should look something like this:

`DATABASE_SERVER`: 

* mysql+mysqlconnector://<user>:<password>@<server>

`DATABASE_URL`:

* mysql+mysqlconnector://<user>:<password>@<server>/<db name>

For `APP_SETTINGS`, the value needs to look something like this: 

* `config.DevelopmentConfig`

For other configs, just look at the `config.py` file in the `server` directory.

Click save after you've filled out the environment variables.

I'm pretty sure the function restarts after you change the variables, but I like to update it just to be sure:

* `zappa update dev`


[Back to Readme](../README.md)