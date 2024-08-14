# HamiSho

**HamiSho** is a backend project developed using the Django framework, designed to manage and publish news and announcements for representatives. This project also allows users to register representatives and retrieve their information based on representative codes. The system can connect to a mobile application, enabling users to support representatives as supporters and send messages.

## Related Project

This backend project is connected and synchronized with a mobile application developed using Flutter. The mobile app allows users to interact with the backend, support representatives, and send messages. For more information about the Flutter project, please visit the [Flutter Project Repository](https://github.com/AliNajafzadeh7916/HamiSho).

## Features

- **Publishing News and Announcements:** Publish new news and announcements by representatives.
- **Registering Representatives:** Register and manage representatives using this system.
- **Retrieving Representative Information by Code:** Users can view representative information based on representative codes.
- **Connecting to Mobile Applications:** The system has the capability to connect to a mobile application for user and representative interaction.

## Prerequisites

To run this project, you need to install the following software and tools:

- [Python](https://www.python.org/downloads/) version 3.8 or higher
- [Django](https://www.djangoproject.com/) version 3.2 or higher
- [PostgreSQL](https://www.postgresql.org/) or [SQLite](https://www.sqlite.org/) (based on your choice)

## Project Dependencies

The following packages are used in this project:

- `Django==5.0.1`
- `django-cors-headers==4.3.0`
- `django-jalali==6.0.1`
- `djangorestframework==3.14.0`
- `jdatetime==5.0.0`
- `psycopg2-binary`

## Installation and Setup

Follow these steps to set up the project:

1. Clone the repository:
    ```bash
    git clone https://github.com/Bestsenator/HamiSho.git
    ```

2. Navigate to the project directory:
    ```bash
    cd HamiSho
    ```

3. Create a Python virtual environment:
    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS or Linux:
        ```bash
        source venv/bin/activate
        ```

5. Install the project's dependencies:
    ```bash
    pip install -r requirements.txt
    ```

6. Configure the `.env` file based on the `.env.example` template.

7. Apply database migrations:
    ```bash
    python manage.py migrate
    ```

8. Run the server:
    ```bash
    python manage.py runserver
    ```

9. The project is now accessible at `http://localhost:8000`.

## Project Models

This project includes several models, each with specific responsibilities:

- **Candidate:** Stores information about candidates, including name, image, slogan, resume, colors, background, number of supporters, number of messages sent, candidate audio file, app version, and other details. It also includes methods for file management and deleting old files during updates.
- **User:** Stores information about system users. Each user has a unique code and IMEI number, with registration time also recorded.
- **APIKEY:** Stores API keys. Each key is associated with a unique code and registration time.
- **Post:** Stores posts related to candidates. Each post includes an image, file, description, and registration time.
- **News:** Stores news related to candidates. Each news item includes a title, image, attached file, and content.
- **Supporter:** Stores information about supporters of candidates. Each supporter is linked to a user and a candidate, with registration time recorded.
- **Sponsor:** Stores information about sponsors of candidates. Information includes name, image, sponsor features, and registration time.
- **MessageToCandidate:** Stores messages sent by users to candidates. Each message includes user information, name, phone number, address, and message text.
- **Developer:** Stores information about system developers. Each developer has a name, specialty, image, and registration time.
- **Provider:** Stores information about providers for candidates. Each provider has a name, logo, slogan, and is associated with a candidate.
- **Social:** Stores information about social networks. Each social network has a name and related icon.
- **SocialMedia:** Stores information about candidates' social media. Each record includes a candidate, media content, and the associated social network.

## API Endpoints

List of available API endpoints:

- `GET /getCandidateInfo/` - Retrieve candidate information
- `POST /getPostCandidate/` - Retrieve post related to a candidate
- `GET /getNewsCandidate/` - Retrieve news related to a candidate
- `POST /setSupporter/` - Register a supporter for a candidate
- `POST /setMessageToCandidate/` - Send a message to a candidate
- `GET /getDeveloperInfo/` - Retrieve developer information
- `GET /getSocialCandidate/` - Retrieve social network information for a candidate

## Project Structure

```
HamiSho/
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── api/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── index/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── funcs/
│   ├── check.py
│   └── verify.py
├── media/
│   ├── appFile/
│   ├── BackgroundCondidate/
│   ├── news/
│   ├── OriginCondidate/
│   ├── post/
│   ├── social/
│   ├── Sound/
│   ├── sponser/
│   └── verify.py
├── static/
├── manage.py
├── db.sqlite3
├── README.md
├── README.fa.md
├── README.en.md
└── requirements.txt
```

## Contributing

If you wish to contribute to this project, you can:

1. Fork this repository.
2. Create a new branch for your feature or bug fix (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push your branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## Special Thanks

[Ali Najafzadeh](https://github.com/AliNajafzadeh7916)

A special thanks to the developer of the Flutter application, who with their effort and skill, has developed this app and integrated it with the backend project. Without their hard work, creating this integrated system would not have been possible.

