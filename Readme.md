# Run Backend
<b>First you need to have python 3.10 installed on your system.</b>

## Create Virtual Environment
* python -m venv env
* To activate venv, run following command <br>

        source env/bin/activate

* To deactivate, run<br>
        
        deactivate

## Install Requirements.txt
* open your terminal, cd into minerals directory where you will see a requirements.txt file.<br>
        
        cd minerals
* Run below command to install dependencies<br>

        pip install -r requirements.txt

## Now you only need to run the backend and test
* To run the project stay in the same directory where you will see manage.py file also, run below command there.<br>

        python manage.py runserver


#### The server is up and listening at http://127.0.0.1:8000/