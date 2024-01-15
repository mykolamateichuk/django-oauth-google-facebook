# Django OAuth with Google and Facebook

## How to set up

1) Clone git repository

   ```
   git clone https://github.com/mykolamateichuk/django-oauth-google-facebook
   ```

2) Go into the created folder

   ```
   cd django-oauth-google-facebook
   ```

3) Create and activate virtual environment
   *MacOS*
   ```
   python3 -m venv venv
   ```
   ```
   source venv/bin/activate
   ```
   
   *Windows*
   ```
   python -m venv venv
   ```
   ```
   .\venv\Scripts\activate
   ```

4) Install requirements

   ```
   pip install -r requirements.txt
   ```

5) Migrate database

   ```
   python manage.py migrate
   ```

6) Create local SSL Certificate

   *MacOS*

   ```
   brew install mkcert
   ```
   ```
   mkcert -install
   ```
   ```
   mkcert -cert-file cert.pem -key-file key.pem localhost 127.0.0.1
   ```

7) Run HTTPS server

   ```
   python manage.py runserver_plus localhost:8000 --cert-file cert.pem --key-file key.pem
   ```

8) Go to https://localhost:8000/ and try out authentication


9) To check if it's working you can go into `auth_user` table in `db.sqlite3` file and see that you have registered all of your users in it.
