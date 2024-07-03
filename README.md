Blog
====

A blog site for personally curated contents and ease of use (_hopefully_). 

Implemented with [wagtail](https://github.com/wagtail/wagtail).

Usage
-----

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- Docker Compose

### Running

Build and deploy the development container with

```bash
docker compose up -d -f compose-dev.yml
```

View to the website with `localhost:8000`

Login to the admin panel `localhost:8000/admin` with the credentials in `default.env`
