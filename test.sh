#!/bin/bash
#    This file will set up a test env and run tests


echo "Loading the test environment"
if [ "$1" ]
then
    source .aws.test.env
else
    source .test.env 
fi
source env/bin/activate
echo "Executing tests."
exec python manage.py test
exit 0
