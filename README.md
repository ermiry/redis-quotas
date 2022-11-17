# Redis Quotas

The application is created using Python with the Flask development framework, with Redis as the primarily db hosted in the provided managed cloud solution: Redis Enterprise, which offers an easy and cost effective way to deploy an application that requires fast scaling in a reliable environment; it also supports extra functionality such as custom modules integration which enables developers to include their own commands to manage extra data structures, and clustering which is specially useful to better work with large datasets as it enables distribution across multiple instances. The JSON module can be used to model and store the data with high performance search capabilities with RediSearch through the Python Redis OM package. All the code will be provided as a GitHub repo with a configured environment using Docker to perform local tests; the application will be divided into multiple web services:

- **Tokens Service** Used to generate API Keys that can be used to authenticate when performing requests.
- **Authentication Service** Used to check token values to enable services access.
- **Quotas Service** Used to create and manage quotas.

This project was created is in collaboration with Redis through the "Write for Redis" program.

Erick Salas
