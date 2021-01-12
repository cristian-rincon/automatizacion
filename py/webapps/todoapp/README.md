# Todo APP - FullStack

End to end application build with Django(Backend) and React(Frontend).

## Using with docker

> You must need to have Docker and docker-compose installed on the machine where you want to run this feature.

```bash
# Run the containers
docker-compose up
```

- Backend service will run at localhost:8000
- Frontend service will run at localhost:3000

You can perform CRUD operations like:

- Create tasks
- Read tasks
- Update tasks
- Delete Tasks

In addition, you can perform the same operations by using DRF front.

## API Endpoints

```bash
/api/tasks/ - List  all created tasks
api/ task/<str:pk>
```

| Endpoint     | HTTP Method | Description            |
| ------------ | ----------- | ---------------------- |
| /api/tasks/  | `GET`       | List all created tasks |
| /api/tasks/  | `POST`      | Create new task        |
| /api/task/id | `GET`       | Get task               |
| /api/task/id | `PUT`       | Update task            |
| /api/task/id | `DELETE`    | Delete task            |

## Stack

| Service  | Technologies       |
| -------- | ------------------ |
| Frontend | React.js/Bootstrap |
| Backend  | Python3/Django-DRF |
| Db       | Postgresql         |

## Create superuser on Django

```
docker-compose run --rm app python manage.py createsuperuser
# Fill the prompt below
```

Once you have created superuser successfully, go to `localhost:8000/admin` and test you login
To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
