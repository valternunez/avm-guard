# My Django project

This is a Django project that provides a RESTful API using Django Rest Framework.

## Prerequisites

- Docker
- Docker Compose

## Getting Started

To get started, simply clone this repository and run the following command:

docker build -t avm-guard .

docker run -d -p 8000:8000 avm-guard

This command will start the Django development server in a Docker container and expose it on port 8000.

You can then access the API at `http://localhost:8000/`.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
