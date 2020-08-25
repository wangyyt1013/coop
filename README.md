This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Initial Setup Guide

1. Clone this repo.
2. If you have not done so, locally install yarn, node, and python 3.7. (Recommended: using Homebrew)
3. Go to the root directory of the project, and set up the local virtual environment by the following commands: `pipenv --python 3.7 && pipenv install`.
4. Install node dependencies with yarn: `yarn install --frozen-lockfile`.
5. Within the root directory, create an `.env` file with the following configurations for our flask application:
   ```
   export FLASK_APP='api/app.py'
   export FLASK_ENV='development'
   ```

## Available Scripts

1. To start the app, run:

   ```
   $ yarn start-frontend
   $ yarn start-backend
   ```

   in two separate tabs. These commands runs the React app and the flask server
   in development mode, and will reload when you make new changes to the code.
   Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

2. To conduct frontend and backend tests, run:

   ```
   $ yarn test-frontend
   $ yarn test-backend
   ```

   These commands will respectively run the frontend and backend tests in
   `src/tests` and `api/tests`.

3. After a `git commit` is attempted, the pre-commit hooks specified in
   `.pre-commit-config.yaml` will scan the proposed changes for reformatting
   & detecting stylistic / syntactical errors. Make sure you address those
   warnings / errors before pushing.
