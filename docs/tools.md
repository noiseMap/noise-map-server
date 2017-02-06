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
