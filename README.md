# RAPGEN DATABASE WEB APPLICATION
![Python](https://img.shields.io/badge/Python-14354C.svg?logo=python&logoColor=white) ![CSS](https://img.shields.io/badge/CSS-1572B6.svg?logo=css3&logoColor=white) ![HTML](https://img.shields.io/badge/HTML-E34F26.svg?logo=html5&logoColor=white) ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white) ![Jinja](https://img.shields.io/badge/jinja-white.svg?style=for-the-badge&logo=jinja&logoColor=black)![Neovim](https://img.shields.io/badge/NeoVim-%2357A143.svg?&style=for-the-badge&logo=neovim&logoColor=white) ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)

[![Author](https://img.shields.io/badge/Author-Devyn-orange)](https://github.com/surbd)

This application is to simplify the management of RAPGEN's data, so easy access to get and modify data with roles for each individual, making the data organised.

###### Note: This web application is still in it's development phase and is open for contributions, you can fork it to your repo and make improvements to it.
![Login Page for RapgenDBMS](app/static/images/login-page-01.png)

## Installation

You would find the required dependencies to run RapgenDBMS on your local machine in the `requirements.txt` file.

Clone this Repo(or Fork)
```sh
git clone git@github.com:SurbD/RapgenDBMS.git
```
Create a virtual environment and activate it (use `source venv\bin\activate` for mac)
```sh
python -m venv [venv-name]
venv\Scripts\activate
```
> Make sure you create the virtual environment in the project directory

Install the dependencies and start the server.

```sh
pip install -r requirements.txt
FLASK_APP=run.py
```
```
python run.py
```
> Environments variables like the `SECRET KEY` and ` YOUR POSTGRESSQL DATABASE LOGIN DETAILS`
>  would have to be manually set, there's no production database for now.

## Technologies Used

- Flask
- Python
- PostgreSQL
- pyscopg2
- HTML
- CSS
- Javascipt
- Pandas
- SQLAlchemy

## Features

- Add data to DB as CSV or excel file
- Bulk Inserts from SQL script
- Create and Add to new Table
- Get back data in Text, CSV, Excel or PDF format
- Sort and Filter Data
- Easy Data View Dashboard
- Set user roles
- Group By Location
- Authentication for Admins Access
- Interactive UI for Updating Data (later feature)

## Later ADD ons

- Create seperate API and Frontend for better structure.
- Birthday Notification with Google Calendar.
- Bulk Message Sending Integration.
- Analytics for database growth, update timeline, region.
- Find by location with Google Maps.
