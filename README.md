This project is a quick start guide for using Vue 3, DJango, Tailwind css and Docker. I've used Docker Compose and Dockerfiles to make it easy to kick off the project. Feel free to check it out and apply the concepts to your own work.

Please see the specific `README.md` files for backend and frontend in their corresponding directories

`frontend/README.md`
`backend/README.md`

# Project Setup:

You have two docker-compose files, one is docker-compose.yml and other is docker-compose.dev.yml (Overrided). The overrided compose file is used for lcoal development. We might also create another overrided file i.e. prod.yml for production environment.

## NySQL

1. it is setup as part of the docker. Used volumes for persistence. and used .env file to pass data around.

2. Although commiting `.env` file is not a good practice for security reasons, But for the sake of this project and simplicity, I would push it with this repo.


# Build and RUN:

- For running both the backend and frontend, please navigate or CD to the project direcotry where docker-compose and docker-compose.dev.yml files are placed and run the following command:

```
docker-compose -f docker-compose.yml -f docker-compose.dev.yml up --build
```

After running above command, following would happen:

1. Both front and backend services alongside mysql service would be readily available.
2. The docker might take some time to make the services available
3. Frontend: http://localhost:8080


# Extras
- If you want to get into the bash of the docker services or if you want to use mysql-client for the installed mysql service, you can also do so.


## How to Contribute

I welcome contributions from the community to make this project even better. Here are some guidelines to get you started:

1. Fork the repository.
2. Clone the forked repository to your local machine.

```bash
git clone https://github.com/your-username/project.git
```

3. Create a new branch for your feature or bug fix.
```bash
git checkout -b feature-or-bugfix-branch
```

4. Make your changes and commit them with a descriptive commit message.
```bash
git commit -m "Add feature or fix bug: a brief description"
```

5. Push your changes to your fork on GitHub.
```bash
git push origin feature-or-bugfix-branch
```

6. Open a pull request (PR) to the main branch of the original repository.
7. Provide a clear and concise description of your changes in the pull request.
8. Your contribution will be reviewed, and if everything looks good, it will be merged.

## Code Style
Follow the existing code style in the project. If you're introducing new features or making significant changes, consider updating or adding relevant documentation.

## Issues
Feel free to check the existing issues for tasks that need attention or open a new issue if you find a bug or have a feature request.

Thank you for contributing!

