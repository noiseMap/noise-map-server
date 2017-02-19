<h1>Setup</h1>

## Setup for local development

It's recommanded to create a virtual Python environment, but not required. Therefore create and activate it.
```bash
$ virtualenv noise_map_workspace
$ cd noise_map_workspace
$ source bin/activate
```

### Setup database


#### Using Docker

Download PostGIS image from Docker Hub
```bash
$ docker pull mdillon/postgis
```

Run it. (`-p` exposed the port 5432 of the container to the port 5432 of your localhost. 5432 is the default port of PostgreSQL.)
```bash
$ docker run --name noisemap-postgres -p 127.0.0.1:5432:5432 -e POSTGRES_PASSWORD=password -d mdillon/postgis
```

Connect to the database and create a new database named "noisemap". For instance use psql, the default command line tool of PostgreSQL.
```bash
$ psql -h 127.0.0.1 -p 5432 -U postgres
postgres=# CREATE DATABASE noisemap;
```


### Setup server

Get project and install the Python dependencies
```bash
$ git clone --recursive https://github.com/noiseMap/noise-map-server
$ cd noise-map-server
$ pip install -r requirements.txt
```

Migrate the database tables and create initial data
```bash
$ ./manage.py migrate
```

Create a root user
```bash
$ ./manage.py createsuperuser
```

Finally run the build-in Django server
```bash
$ ./manage.py runserver
```

Open [http://localhost:8000](http://localhost:8000) or the admin interface [http://localhost:8000/admin/](http://localhost:8000/admin/).


### Setup client

Collect the static files
```bash
$ ./manage.py collectstatic
```

Open [http://localhost:8000/static/index.html](http://localhost:8000/static/index.html)
