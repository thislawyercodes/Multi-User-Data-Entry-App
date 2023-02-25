# A Multi User Data Entry Application
This is a Dynamic Django API that allows users to perform basic CRUD operations, as well as create New Tables from existing models.
It is the submission to JamboPay's technical assesment role.

This README should:
1. Guide you through getting the Dockerized Django container up and running,
2. provide a little explanation as to how it's configured, and
3. provide some basic commands on how to work with it.

It might also give the impression I understand 100% how everything works; this is an illusion but, nevertheless, things do seem to work.


# Technologies used
* [Django](https://www.djangoproject.com/): The web framework for perfectionists with deadlines (Django builds better web apps with less code).
* [DRF](www.django-rest-framework.org/): A powerful and flexible toolkit for building Web APIs
* [Docker](https://www.docker.com/): A powerful tool for containerzing applications
* [Redis](https://redis.io/): A powerful and flexible toolkit for in memory caching
* [Datatb](https://pypi.org/project/django-dynamic-datatb/): A powerful and flexible toolkit for generating filterable, paginated database tables.

## Installation
* If you wish to run your own build, first ensure you have python, Docker, Redis and pip3 globally installed in your computer. 
* After doing this, confirm that you have installed virtualenv globally as well. If not, run this:
    ```bash
        $ pip install virtualenv
    ```
* Then, Git clone this repo to your PC
    ```bash
        $https://github.com/thislawyercodes/Multi-User-Data-Entry-App.git
    ```
* #### Dependencies
    1. Cd into your the cloned repo as such:
        ```bash
            $ cd Multi-User-Data-Entry-App
        ```
    2. Create and fire up your virtual environment:
        ```bash
            $ virtualenv  venv -p python3
            $ source venv/bin/activate
        ```
     3. Create a .env file with the following environment variables
------------------------------------------------------------------
``` bash
` SECRET_KEY=yoursecretkey
DATABASE_NAME=yourdb
DATABASE_USER=yourdbuser
DATABASE_PASSWORD=yourbdpassword
DATABASE_HOST=localhost
DATABASE_PORT=5432
```
4. Export your environment variables
--------------------------------------------
``` shell
source .env
```
    5. Install the dependencies needed to run the app:
        ```bash
            $ pip3 install -r requirements.txt
        ```
    6 . Run Unit Tests
        ----------------------
        ``` shell
           python3 manage.py test

    7. Make those migrations work
        ```bash
            $ python manage.py makemigrations
            $ python manage.py migrate
        ```

* #### Run It
    Fire up the server using this one simple command:
    ```bash
        $ python manage.py runserver
   
    ```
    # Running the container

    ## 1. Build and run the container

1. Install Docker, e.g. [Docker for Mac](https://docs.docker.com/docker-for-mac/install/).

2. Download this repository.

3. Optional: In `docker-compose.yml` change the two `container_name` values from `myproject_db` and `myproject_web` to something that makes sense for your project. e.g. `weblog_db` and `weblog_web` if your project is called weblog.

4. If you did that you'll also need to change `myproject_web` in the two scripts within the `/scripts/` directory.

5. Create a `.env` file at the same level as this README, containing the following. This will be used by Docker.
    ```
    # Environment settings for local development.

    POSTGRES_USER=mydatabaseuser
    POSTGRES_PASSWORD=mypassword
    POSTGRES_DB=mydatabase
    POSTGRES_HOST=myproject_db

    DJANGO_SETTINGS_MODULE=myproject.myproject.settings.development
    ```

    **Note:** If you changed `myproject_db` in the previous step, you should change the `POSTGRES_HOST` value to match it in the `.env` file. You can change the other postgres settings if you like, but it's not required.

6. On the command line, within this directory, do this to build the image and
   start the container:

        docker-compose build

7. If that's successful you can then start it up. This will start up the database and web server, and display the Django `runserver` logs:

        docker-compose up

8. Open http://0.0.0.0:8000 in your browser.
