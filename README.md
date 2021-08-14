# Colorado 14er Checklist
#### Video Demo:  <https://youtu.be/mjYEH5iKdHw>
#### Description: Users are able to keep track of which of Colorado's 14ers they have climbed. Users can also view which users have climbed a specific mountain or which climbs another user has completed.


## Instructions on how to run program

  1. Create a virtual env
  2. `pip install -r requirements.txt`
  3. `python manage.py migrate`
  4. `python manage.py runserver`

## Project Description

My project is a way for users to add any number of Colorado's 14ers to their own personal profile. Each user has the ability to add ascents, view each mountains specific page, and view other users climbs. 

Under the cs50_final app you will find the settings.py used for the entire project. Within you will find that I added the main app as well as the register app. I also used settings.py to prepare my project for the static files I was going to use.

### Register App:
    Each user must first register for an account prior to logging into the website. These two componants are handeled by the register app. Within the register app you will find the html templates used for each page. 

    In views.py you will find the python code used to render the registration page and to register and create a user profile using the POST request method to complete after the form is submitted. 

    In forms.py you will see the fields and their parameters I used for the registration page. I chose to make all the fields required fields in order to get all pertinent information necessary to help create a user to a climber profile.

### Main App:
    Within the main app you will find a majority of the code used for my project. Templates folder contains all of the html code for the various webpages as well as code for my nav bar and footer. These html files are mainly styled via a css file that can be found under the static folder.

    Views.py again contains all of my python code used for the various pages and handles GET/POST request methods. 

    urls.py handles all of the pathways for the various pages set up in the views.py and html files. A majority of these pathways were created to dynamically show specific users or mountains throughout the project depending on which links are clicked and by whom.

    Models.py and migrations handle all of my data that I collect and store, which is currently using SQLite. Within my models.py I defined three classes, Climber, Mountain, and Ascents. Climber and Mountain each have different fields to store specific data while the Ascents model is used to connect Climber and Mountain via foreign keys. The data for the 14ers can be found under the migrations 0006 file where upon migrating will be inserted into the mountains model.