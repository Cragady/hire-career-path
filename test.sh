#!/bin/bash
#    This file will set up a test env and run tests


echo "Loading the test environment"
source .test.env 
source env/bin/activate
echo "Executing tests."
exec python manage.py test
exit 0
