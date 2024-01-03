# test

## dev

Activate a virtual env (`.venv` is a folder name):

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
poetry install
```

Run migrations:

```bash
python manage.py migrate
```

Run server:

```bash
python manage.py runserver
```

Run swagger:

```bash
docker run -p 80:8080 -e SWAGGER_JSON=/schema.yml -v ${PWD}/schema.yml:/schema.yml swaggerapi/swagger-ui
```
