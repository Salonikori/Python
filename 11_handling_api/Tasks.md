
# Python API Practice Tasks

## Level 1 – Beginner

**Start here**

Learn how to send API requests and extract data.

### Task 1: Fetch Random User Details

**API:** https://jsonplaceholder.typicode.com/users

**Requirements:**
- Send a GET request.
- Convert the response into JSON.
- Print the name, email and city of the first user.
- Print the company name of the same user.

**Expected Output:**
```text
Name: Leanne Graham
Email: Sincere@april.biz
City: Gwenborough
Company: Romaguera-Crona
```

### Task 2: Fetch All Posts

**API:** https://jsonplaceholder.typicode.com/posts

**Requirements:**
- Fetch all posts.
- Print the total number of posts.
- Display the first 5 post titles.
- Ask the user to enter a post ID.
- Display the title and body of that post.

### Task 3: Fetch Weather Information

**API:** https://api.open-meteo.com/v1/forecast?latitude=19.0760&longitude=72.8777&current=temperature_2m,relative_humidity_2m,wind_speed_10m

**Requirements:**
- Fetch the current weather.
- Display temperature.
- Display humidity.
- Display wind speed.
- Display the temperature unit.

---

## Level 2 – Intermediate

Learn how to handle API parameters, user input and errors.

### Task 4: GitHub Profile Finder

**API:** https://api.github.com/users/octocat

**Requirements:**
- Ask the user for a GitHub username.
- Fetch that user's profile.
- Display username, followers, following and public repositories.
- Handle invalid usernames.

### Task 5: Currency Converter

**API:** https://open.er-api.com/v6/latest/USD

**Requirements:**
- Ask the user for an amount in USD.
- Ask which currency they want to convert into.
- Fetch the exchange rate.
- Calculate and display the converted amount.
- Handle invalid currency codes.

### Task 6: Search Movies

**API:** https://www.omdbapi.com/

**Requirements:**
- Get an OMDb API key.
- Ask the user for a movie name.
- Fetch movie details.
- Display title, year, genre, director and IMDb rating.
- Handle movies that are not found.

---

## Level 3 – Advanced

Learn how APIs work with databases and external applications.

### Task 7: Create Your Own API using Flask

**Requirements:**
- Create a Flask application.
- Create a GET endpoint `/users`.
- Return a list of users in JSON.
- Create a GET endpoint `/users/1`.
- Return details of a particular user.
- Test your endpoints using Postman.

### Task 8: POST, PUT and DELETE Requests

**Use your Flask API from Task 7.**

**Requirements:**
- POST: Add a new user.
- GET: Retrieve users.
- PUT: Update user details.
- DELETE: Delete a user.
- Return appropriate HTTP status codes.

### Task 9: API + PostgreSQL

**Requirements:**
- Connect your Flask API to PostgreSQL.
- Store user information in the database.
- Fetch users from PostgreSQL.
- Add new users through POST.
- Update and delete records through API requests.

---

## Learning Progress Tracker

### Level 1 – Beginner
- [ ] Task 1: Fetch Random User Details
- [ ] Task 2: Fetch All Posts
- [ ] Task 3: Fetch Weather Information

### Level 2 – Intermediate
- [ ] Task 4: GitHub Profile Finder
- [ ] Task 5: Currency Converter
- [ ] Task 6: Search Movies

### Level 3 – Advanced
- [ ] Task 7: Create Your Own API using Flask
- [ ] Task 8: POST, PUT and DELETE Requests
- [ ] Task 9: API + PostgreSQL
