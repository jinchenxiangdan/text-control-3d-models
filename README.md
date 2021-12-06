# text-control-3d-models







## 

## Chatbot File Structure:

- The outer `mysite/` root directory is a container for your project. Its name doesn’t matter to Django; you can rename it to anything you like.
- `manage.py`: A command-line utility that lets you interact with this Django project in various ways. You can read all the details about `manage.py` in [django-admin and manage.py](https://docs.djangoproject.com/en/3.2/ref/django-admin/).
- The inner `mysite/` directory is the actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it (e.g. `mysite.urls`).
- `mysite/__init__.py`: An empty file that tells Python that this directory should be considered a Python package. If you’re a Python beginner, read [more about packages](https://docs.python.org/3/tutorial/modules.html#tut-packages) in the official Python docs.
- `mysite/settings.py`: Settings/configuration for this Django project.  [Django settings](https://docs.djangoproject.com/en/3.2/topics/settings/) will tell you all about how settings work.
- `mysite/urls.py`: The URL declarations for this Django project; a “table of contents” of your Django-powered site. You can read more about URLs in [URL dispatcher](https://docs.djangoproject.com/en/3.2/topics/http/urls/).
- `mysite/asgi.py`: An entry-point for ASGI-compatible web servers to serve your project. See [How to deploy with ASGI](https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/) for more details.
- `mysite/wsgi.py`: An entry-point for WSGI-compatible web servers to serve your project. See [How to deploy with WSGI](https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/) for more details.

## Run:

*To run this project on server, run command:*

```python
python3 manage.py runserver
```



## Environment: 

```
Python 3.7.11
chatterbot 1.08
Django 3.2.9
Anoconda 4.10.1
```



``` 
# Conda package information
# Name                    Version                   Build  Channel
asgiref                   3.4.1                    pypi_0    pypi
ca-certificates           2021.10.26           hecd8cb5_2
certifi                   2021.10.8        py38hecd8cb5_0
chatterbot                1.0.4                    pypi_0    pypi
chatterbot-corpus         1.2.0                    pypi_0    pypi
click                     8.0.3                    pypi_0    pypi
django                    3.2.9                    pypi_0    pypi
flask                     2.0.2                    pypi_0    pypi
itsdangerous              2.0.1                    pypi_0    pypi
jinja2                    3.0.3                    pypi_0    pypi
joblib                    1.1.0                    pypi_0    pypi
libcxx                    12.0.0               h2f01273_0
libffi                    3.3                  hb1e8313_2
markupsafe                2.0.1                    pypi_0    pypi
mathparse                 0.1.2                    pypi_0    pypi
ncurses                   6.3                  hca72f7f_0
nltk                      3.6.5                    pypi_0    pypi
openssl                   1.1.1l               h9ed2024_0
packaging                 21.2                     pypi_0    pypi
pint                      0.18                     pypi_0    pypi
pip                       21.2.4           py38hecd8cb5_0
pymongo                   3.12.1                   pypi_0    pypi
pyparsing                 2.4.7                    pypi_0    pypi
python                    3.8.12               h88f2d9e_0
python-dateutil           2.7.5                    pypi_0    pypi
pytz                      2021.3                   pypi_0    pypi
pyyaml                    3.13                     pypi_0    pypi
readline                  8.1                  h9ed2024_0
regex                     2021.11.1                pypi_0    pypi
setuptools                58.0.4           py38hecd8cb5_0
six                       1.16.0                   pypi_0    pypi
sqlalchemy                1.2.19                   pypi_0    pypi
sqlite                    3.36.0               hce871da_0
sqlparse                  0.4.2                    pypi_0    pypi
tk                        8.6.11               h7bc2e8c_0
tqdm                      4.62.3                   pypi_0    pypi
werkzeug                  2.0.2                    pypi_0    pypi
wheel                     0.37.0             pyhd3eb1b0_1
xz                        5.2.5                h1de35cc_0
zlib                      1.2.11               h1de35cc_3
```





