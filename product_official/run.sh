pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic << EOF
yes
EOF
uwsgi --ini product_official_uwsgi.ini