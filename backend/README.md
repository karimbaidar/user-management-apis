# Backend


## Project setup

I have established a Docker setup for both the front-end and back-end. If you wish to make modifications to the front-end, you can adjust the settings in the Dockerfile provided.

## pyproject.toml

In this section, I've documented significant backend packages with version control for clarity.

## Settings.py

Within this file, I've made several important adjustments to ensure the smooth operation of the project:

1. Added CORS and CSRF support.
2. Included middlewares related to CORS and integrated 'corsheaders' into the installed apps.
3. The ```api.py``` file in the users app contains the necessary API endpoints.
4. Tests folder in users app contain unit and integration tests (tried to cover the best possible cases, might have missed some ...). Though, still 100% coverage might not be possible.

## Urls
1. I've set up both global and app-specific URLs for the project.

## First Iteration

During the first iteration, I dedicated my best efforts to delivering optimal features. Key highlights include:
1. Created a users app and a config folder to have the configuration like settings.py etc.
2. ``api.py`` serves as a service for the exposure of the api endpoints.
3. The backend's Dockerfile has been enhanced with additional commands via the ``.dev.yml`` compose file for local development.
4. ```Tests are automatically run as part of the docker-compose.dev.yml file.``` you can see the test coverage report in the docker console when you execute the build command.
5. create_user api endpoint serves multiple purposes, one is to create a user and also to return a response in a way that will help the frontend to add users to the user state without multiple api calls, thus optmizing the performance.
6. You can also run the Tests manually via following steps:

#### Steps:
1. Begin by listing the Docker services using the following command:
````
docker ps
````
2. Then grab the backend service Container ID or name. and run the following command:
````
docker exec -it <container_id or container_name> pytest 
`````
```OR``` You can also enter into the shell of the container witht he following command

````
docker exec -it <container_id or container_name> sh
````
and then run the ```pytest``` command

3. Finally, you will get the test coverage report. Please note, you can use above commands with pooetry too when running pytest.


### Second Iteration
In steering this project towards a professional large-scale application, focus on the following key aspects:

1. **Class-Based Views:**
    - As the project grows, transition to class-based views for better organization and scalability.

2. **Authentication and Authorization:**
    - Enhance security by introducing robust authentication mechanisms, potentially using JWT tokens.
    - Implement a comprehensive permission and authorization system to control access.

3. **Code Formatting and Linting:**
    - Integrate tools like Black for code formatting and Flake8 for linting to ensure consistent and clean code.

4. **API Documentation:**
    - Explore Swagger or drf-yasg integration to generate interactive API documentation for improved developer experience.

5. **Logging and Monitoring:**
    - Implement logging for error tracking, user actions, and critical events.
    - Integrate monitoring tools to identify performance bottlenecks and proactively address issues.

6. **Testing Strategies:**
    - Expand testing strategies with more extensive unit tests, integration tests, and potentially end-to-end tests for critical workflows.

7. **Dependency Management:**
    - Regularly update and manage dependencies using tools like Poetry for security and performance reasons.

8. **Continuous Integration (CI/CD):**
    - Set up a robust CI/CD pipeline for automated testing and deployment to ensure code quality and reliability.

9. **Scalability:**
    - Design the application with scalability in mind, considering potential performance bottlenecks and facilitating horizontal scaling.

10. **Documentation:**
    - Maintain comprehensive documentation for developers, covering API, setup guides, and key architecture decisions.

11. **Error Handling:**
    - Implement a thorough error-handling strategy with meaningful error messages and stack trace logging.

12. **Security Audits:**
    - Conduct regular security audits to identify and address vulnerabilities in the application.

13. **User Feedback and Analytics:**
    - Implement tools for collecting user feedback and analytics to gain insights into user behavior.

14. **Code Review Practices:**
    - Establish and adhere to robust code review practices for quality assurance and knowledge sharing within the team.

15. **Internationalization and Localization:**
    - Consider implementing internationalization (i18n) and localization (l10n) for a global audience.

These considerations aim to elevate the project's development practices, aligning with best practices for professional and large-scale Django applications. Ensure that each step builds upon the project's current foundation and addresses specific needs as it evolves.