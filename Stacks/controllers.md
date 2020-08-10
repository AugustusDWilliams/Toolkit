# Controllers

## Overview
Controllers are classes that are responsible for "controlling" a component in an application. Controllers hold functions and variables related to that specific component as opposed to the larger application.

## Rules
- Controllers should create a class 1st with a "connection" to the target component that is initialized as None
- Controllers can either attempt to establish a connection to the component in the __init__ function or have the main app call the connect function
- Controllers should be able to operate (exist) if the connection fails or is None
- Controllers should have a status attribute to indicate is the connection is alive or not
- Controllers should have __del__ a function that cleans up the component before exiting the application

## Example

