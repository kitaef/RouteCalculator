# FastAPI application for an optimal route calculation

This application is created to calculate an optimal route based on the passed route points. The application provides a REST API to calculate a route based on points from a .csv file, and to retrieve information about a previously created route by its ID.
During the development I practiced using:
- Python
- FastAPI
- Postgres
- Pydantic
- SQL Alchemy
- Networkxx and working with graphs

## Installation and startup

1. Install Docker.
2. Clone this repository:

   ```bash
   git clone https://github.com/kitaef/RouteTestTask.git
   ```

3. Navigate to the project directory:

   ```bash
   cd <directory name>
   ```

4. Run Docker Compose:

   ````bash
   docker-compose up --build
   ```

5. After a successful launch, you will be able to access the API at [http://localhost:80](http://localhost:80).

## Endpoints

- **POST /api/routes** - route creation. In the request body put a CSV file with the route points (the coordinates of the points should be in 'lat' and 'lng' columns.
- **GET /api/routes/{id}** - get route by its identifier.

## Testing

The repository provides a simple unit test to check the optimal route calculation function.

## Possiblle improvements

- Currently, the API does not provide the ability to update or delete routes. Adding such features could be useful for managing routes in the system.
- There is no endpoint to retrieve a list of all routes. Adding this functionality could be useful to view available routes.
- Additional HTTP methods (e.g., PUT and DELETE) can be added to provide full functionality for CRUD operations (Create, Read, Update, Delete).
