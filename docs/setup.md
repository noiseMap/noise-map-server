<h1>Setup</h1>

## Setup for local development

It's recommanded to create a virtual Python environment, but not required. Therefore create and activate it.
```bash
$ virtualenv noise_map_workspace
$ cd noise_map_workspace
$ source bin/activate
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
