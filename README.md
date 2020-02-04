# Rest API using Django, Django rest framework

## About The Project

This project contains the implementation of the Celero Challenge Back-End, using Django and Django REST Framework. The project is deployed in Heroku [safe-reef-79435](https://safe-reef-79435.herokuapp.com/api/events/list/)

### Built With

* [Python 3.7.6](https://www.python.org)
* [Django 2.2.9](https://www.djangoproject.com)
* [Django REST Framework 3.11.0](https://www.django-rest-framework.org)
* [Postgresql 12.1](https://www.postgresql.org)


## Setup

### Install the depencies

```sh
git clone https://github.com/NaderFarhat/django-rest-api.git
```

```sh
pip install -r requirements.txt
```

### Migrate the database

```sh
python manage.py makemigrations
```

```sh
python manage.py migrate
```

### Populate the database

```sh
python manage.py shell
>>> exec(open('import_data_csv.py').read())
```

### Start the server

```sh
python manage.py runserver
```

### Run the tests

```sh
python manage.py tests
```
## API endpoints

### Comitee

| Method        | Url                                                           | Description           |
| ------------- |:--------------------------------------------------------:     | ------------------:   |
| GET           | https://safe-reef-79435.herokuapp.com/api/events/com/         |   List all comitees   |
| GET           | https://safe-reef-79435.herokuapp.com/api/events/com/(:id)    |   Info of one comitee.|
| POST          | https://safe-reef-79435.herokuapp.com/api/events/com/         |   Create new comitee  |
| PATCH         | https://safe-reef-79435.herokuapp.com/api/events/com/(:id)    |   Update comitee.     |
| PUT           | https://safe-reef-79435.herokuapp.com/api/events/com/(:id)    |   Update comitee(all) |
| DELETE        | https://safe-reef-79435.herokuapp.com/api/events/com/(:id)    |   Delete comitee.     |

### Event

| Method        | Url                                                           | Description           |
| ------------- |:--------------------------------------------------------:     | ------------------:   |
| GET           | https://safe-reef-79435.herokuapp.com/api/events/evt/         |   List all Events   |
| GET           | https://safe-reef-79435.herokuapp.com/api/events/evt/(:id)    |   Info of one Event.|
| POST          | https://safe-reef-79435.herokuapp.com/api/events/evt/         |   Create new Event  |
| PATCH         | https://safe-reef-79435.herokuapp.com/api/events/evt/(:id)    |   Update Event.     |
| PUT           | https://safe-reef-79435.herokuapp.com/api/events/evt/(:id)    |   Update Event(all) |
| DELETE        | https://safe-reef-79435.herokuapp.com/api/events/evt/(:id)    |   Delete Event.     |

### Athlete

| Method        | Url                                                           | Description           |
| ------------- |:--------------------------------------------------------:     | ------------------:   |
| GET           | https://safe-reef-79435.herokuapp.com/api/events/ath/         |   List all Athlete   |
| GET           | https://safe-reef-79435.herokuapp.com/api/events/ath/(:id)    |   Info of one Athlete.|
| POST          | https://safe-reef-79435.herokuapp.com/api/events/ath/         |   Create new Athlete  |
| PATCH         | https://safe-reef-79435.herokuapp.com/api/events/ath/(:id)    |   Update Athlete.     |
| PUT           | https://safe-reef-79435.herokuapp.com/api/events/ath/(:id)    |   Update Athlete(all) |
| DELETE        | https://safe-reef-79435.herokuapp.com/api/events/ath/(:id)    |   Delete Athlete.     |

## Filtering Attributes

### Example

* safe-reef-79435.herokuapp.com/api/events/ath/?name=Arvi+Aavik
