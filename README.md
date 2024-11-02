## This backend API test project uses Flask and SQLite

> Using a virtual environment here, to avoid conflicts with other python projects.

Use this command if on windows:

cd test_flask_api
venv\Scripts\activate

> Things to install, after being in the virtual environment:

pip install Flask

> To exit virtual environment, use command:

deactivate

> To setup the SQLite database, use the command:

cd test_flask_api
python setup_db.py

> To run, use the command:

cd test_flask_api
python app.py

>

To see 1st page of 20 users (default), go put in http://127.0.0.1:5000/users

To see 2nd page of 10 users, go put in http://127.0.0.1:5000/users?page=2&limit=10

You are free to change the page and user numbers. They will only show blank if they no data is found.
