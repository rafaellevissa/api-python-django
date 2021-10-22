Task:
Create a simple CRUD for users using  as an example.
Support money transactions between thouse users. This should be just one endpoint where one user sends money to another.


## running with docker

`docker build -t api .`
`docker run -it --rm -p 8000:8000 api`

## running with docker-compose

change DB credentials on `db/settings.py`

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '3306',
    }
}
```

`docker-compose up -d`

## running without docker in localhost

`pip3 install -r requirements.txt`
`python3 manage.py makemigrations`
`python3 manage.py migrate`
`python3 manage.py runserver --settings=app.settings.development 0.0.0.0:8000`

## On server (CI/CD)

The `.gitlab-ci.yml` file is being used to configure the pipeline.

The test job is to run the automated tests, the Build job is to package the docker image and the deploy job for AWS is to connect via ssh to any server (which in my case is AWS) and deliver the docker package.

- **environment variables**:

$SERVER_IP : Public IP of server

$PORT : Port of service for app

$SSH_KNOWN_HOSTS_AWS : command `ssh-keyscan $SERVER_IP` using public IP on change $SERVER_IP

$SSH_PRIVATE_KEY_AWS : .pem key for AWS EC2 VM

these environment variables I put in the gitlab repository settings > CI/CD > variables

## Tests

Enter the following command to run the tests:

```
python3 manage.py test crud --settings=app.settings.test
```

## Documentation

You can find the endpoint collection looking either under the folder `docs/postman/app.postman_collection.json` or the swagger documentation which can be found at the endpoint `/api/v1/doc/`

## AWS

For the server purpose we used an ec2 instance with linux and docker as well as rds with mysql. You can look at the application up-and-running at the public address `http://100.26.131.238:8000/`.