# Twitch Watch Party

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

### Running the dev servers

- Open the iTerm window configurations
- Start the virtual environment in the server: `source ../env/bin/activate`
- Start the server: `python3 manage.py runserver`
- Start the client side: `npm start`
  
The server is running on port 8000, and the client on port 3000

### Migrations after Model Change

- `python3 manage.py makemigrations`
- `python3 manage.py migrate`