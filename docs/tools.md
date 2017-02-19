<h1>Development tools</h1>

## Django tips

Open the shell
```bash
$ ./manage.py shell
```
Clear database
```bash
$ ./manage.py flush
```

Update your model file <app-name>/models.py. Then create the database migrations for the app and migrate you database
```
$ ./manage.py makemigrations <app-name>
$ ./manage.py migrate
```

## PostgreSQL tips

For using psql on Debian-based system install the following package
```bash
$ apt-get install postgresql-client
```

## Docker tips

Output all running container
```bash
docker ps -a
``

Stop and delete a container
```bash
docker stop <container-id>
docker rm <container-id>
```