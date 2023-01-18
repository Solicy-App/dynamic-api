# Dynamic API

- This application handles dynamic API calls. The available APIs are listed in `modules` folder. 
The application supports custom validation. 
- There are 2 example modules. A new one can be created using them.
- Every file in the `modules` directory which does not start with `__` is considered an endpoint module.
- A module can have a `schema` variable, which defines the validation schema of the request for that endpoint. 
More about Schema [here](https://pypi.org/project/schema/).
- A module must have a process function, which receives the database object and the request arguments object.
- The module should return an 'api_response.Response' object, which will be serialized and returned to the end user.
- `404.html` template is rendered in case of `404 Not Found` errors.
- Run with `python -m flask run`
