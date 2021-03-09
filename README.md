# Period 2: Gaels

## Links
* [Study Journal](https://docs.google.com/document/d/1NFgEh_1AZGfm3fGWLUgGT7Xm9tNoPROnnH0_pO72MzM/edit?usp=sharing)
* [Collaboration video](https://youtu.be/rLajlcMSnqM)
* [Scrum Board](https://github.com/aditiakella/Period2Gaels/projects/1)
* [Project Plan](https://docs.google.com/document/d/1wBFv8xEiTdBYL12SreRxs_ixNCXaxFt93r1jJ1S14m4/edit?usp=sharing)
* [Website on Raspberry Pi Web Server](http://tweeter.gq/)

## Project Overview
## Project Components
#### Homepage (Grace): 
* Go to our [homepage](http://tweeter.gq/) by clicking on the link
* If you scroll down  on the page you will see that we feature a bird of the month and some more information about that bird
#### Navbar (Grace): 
* On each page of our website there is a navigation bar
* Clicking on those links takes you to different parts of our website
* There are drop downs included on the About Us Section
* There is a each href link on each part of the navigation bar
* On our logo if you click on it, that will take you to our logo
#### About Pages (Aditi):
* On our [homepage](http://tweeter.gq/), hover over the ["About" tab](http://tweeter.gq/aboutus/) in the navbar. Then click on each person's name to access their profile. For quick access, here is [Aditi's Profile](http://tweeter.gq/aboutus/aditi/), [Sophie's Profile](http://tweeter.gq/aboutus/sophie/), [Grace's Profile](http://tweeter.gq/aboutus/grace/), and [Luke's Profile](http://tweeter.gq/aboutus/luke/). 
* Code Review:
    * [About.html](https://github.com/aditiakella/Per2Gaels/blob/master/templates/About.html) is the Jinja template used for all about pages. It includes a [navbar](https://github.com/aditiakella/Per2Gaels/blob/f99c0e48bf4322fc750a5f29d46fa52291a568f5/templates/About.html#L92-L114), the words ["About Us:"](https://github.com/aditiakella/Per2Gaels/blob/f99c0e48bf4322fc750a5f29d46fa52291a568f5/templates/About.html#L132-L134), and a [content block](https://github.com/aditiakella/Per2Gaels/blob/f99c0e48bf4322fc750a5f29d46fa52291a568f5/templates/About.html#L138-L140). 
    * All of the information about team members can be found on [dataaboutus.py](https://github.com/aditiakella/Per2Gaels/blob/master/dataaboutus.py). 
    * Each person's information is turned into a dictionary. Here is an [example](https://github.com/aditiakella/Per2Gaels/blob/f955d7c5bd540656af979728122964ec8aeec613/dataaboutus.py#L6).
    * Then the entire team's information is turned into a [list](https://github.com/aditiakella/Per2Gaels/blob/f955d7c5bd540656af979728122964ec8aeec613/dataaboutus.py#L46).
    * This list of data is passed through the back end, [views.py](https://github.com/aditiakella/Per2Gaels/blob/f955d7c5bd540656af979728122964ec8aeec613/views.py#L67).
    * Then, Jinja variables are used on the about pages to fill in everybody's information in the content block of About.html. Here is an [example](https://github.com/aditiakella/Per2Gaels/blob/f955d7c5bd540656af979728122964ec8aeec613/templates/aditi.html#L10-L16) of the Jinja variables in use. 
* [Scrum Board Card](https://github.com/aditiakella/Per2Gaels/projects/1#card-56444144)
#### Audubon Society Twitter API (Luke):
* To access the Twitter API, click on the API link on the homepage which will rediect you to the [Twitter API](http://tweeter.gq/twitter)
* Code Review:
    * [Views.py](https://github.com/aditiakella/Per2Gaels/blob/f955d7c5bd540656af979728122964ec8aeec613/views.py#L90-L107)
        * The API keys and link are printed here in order to gain access to the API.
        * Under the keys, json.get is used to pull the data using the variables given when the API endpoint is tested on the Rapid API website.
        * Then it takes the respone [200] and prints it.
    * [Tweet.html](https://github.com/aditiakella/Per2Gaels/blob/f955d7c5bd540656af979728122964ec8aeec613/templates/tweet.html) 
        * The html code used in order to display the data the API pulls. It takes the variables from the app route and prints them onto the website.
* [Scrum Board Card](https://github.com/aditiakella/Per2Gaels/projects/1#card-56443744)
#### Easter Egg (Sophie):
* In order to run this file, go to the homepage, click the logo in the middle of the screen, and it will redirect you to the Easter Egg
* Once you have accessed the [easter egg] (https://github.com/aditiakella/Per2Gaels/blob/master/templates/easteregg.html), you will see that we have embedded the college board requirments for the project
* After the initial embedding of the College Board requirments, we used a Jinja template to organize everyones "I" abilities
* The "I" abilities highlight all of the things that we feel we have learned throughout the course of working on this project
* After you see the Jinja outline, you will see our group journal, which has also been embedded to demonstrate our completion of the college board requirments
* At the end, we used an HTML form to create a "feedback" page where you can say which aspects of the college board requirments you (the evaluator) think were not efficiently used
#### Databases Front End (Grace):
* On the navigation bar if you click on contact it will take you to an contact form
* The front end is what the user sees
* On the contact form, the user can input there name, passowrd, email, and phone number
* They add there information to a contact table and there information shows
* Users can delete there information if they don't want it there anymore \
* Here is a link to the front end of the code [link to the frontend code](https://github.com/aditiakella/Period2Gaels/blob/main/templates/index.html)
#### Database Back End (Aditi):
* In order to access our database, go to our [homepage](http://tweeter.gq/) and click on Contact in the NavBar. This will take you to the [contact database page](http://tweeter.gq/database/). 
* Code Review: 
    * First, the User class, Email class and Phone Number class are defined in [init.py](https://github.com/aditiakella/Per2Gaels/blob/a7e40d9e3dd598599e78ae0f126b3fb550ccfa75/models/__init__.py#L13-L28). 
    * The [User ID is declared as the Primary Key](https://github.com/aditiakella/Per2Gaels/blob/a7e40d9e3dd598599e78ae0f126b3fb550ccfa75/models/__init__.py#L14), which means that each person in the database will have a unique user id. 
    * Then, in [create.py](https://github.com/aditiakella/Per2Gaels/blob/a7e40d9e3dd598599e78ae0f126b3fb550ccfa75/models/crud.py#L7-L22), the model_create function is defined, which allows users to be committed into the database. 
    * Also in [create.py](https://github.com/aditiakella/Per2Gaels/blob/a7e40d9e3dd598599e78ae0f126b3fb550ccfa75/models/crud.py#L32-L42), the model_delete function is defined, which allows users to be deleted from the database. 
    * Then, [create.py](https://github.com/aditiakella/Per2Gaels/blob/a7e40d9e3dd598599e78ae0f126b3fb550ccfa75/models/crud.py#L45-L84) has a few functions that allow the names, passwords, emails, and phone numbers of users who are already in the database to be called. 
    * Next, in [views.py](https://github.com/aditiakella/Per2Gaels/blob/a7e40d9e3dd598599e78ae0f126b3fb550ccfa75/views.py#L5-L6), all of the functions from create.py are imported. 
    * In the [create procedure on views.py](https://github.com/aditiakella/Per2Gaels/blob/a7e40d9e3dd598599e78ae0f126b3fb550ccfa75/views.py#L20-L23), first, the contact form is used to gather the name, password, email and phone number of the user. 
    * Then, the [model_create procedure is called](https://github.com/aditiakella/Per2Gaels/blob/a7e40d9e3dd598599e78ae0f126b3fb550ccfa75/views.py#L25-L26) in order to commit the user's imformation to the table. The user's information is then shown in the database table. 
    * In the delete funciton on views.py, a similar method is used. 
    * First, the form is used to identify which user should be deleted from the database
    * Then the model_delete procedure is called and the user's information is no longer displayed in the table. 
    * The [functions emails and phones on views.py](https://github.com/aditiakella/Per2Gaels/blob/a7e40d9e3dd598599e78ae0f126b3fb550ccfa75/views.py#L40-L52) are used to display the users' emails and phone numbers. First the model_query_emails and model_query_phones procedures are used to call all of the emails and and phone numbers in the database. Then the emails and phone numbers are displyed on the table in index.html.
* [Scrum Board Card](https://github.com/aditiakella/Per2Gaels/projects/1#card-56443929)  
#### Phylogeny Page (Sophie):
* In order to access the phylogeny page, go to the nav bar in home and click the button on the far right side that says phylogeny
* This is a phylogenetic tree that shows the relationship between birds that we will hihglight in the bird of the month
* We were able to insert this picture by embedding an image file
* Phylogeny ([link](http://127.0.0.1:5002/Phylogenetic/))
### Databases:
   * In order to run the database, run our [website](Tweeter.gq). Then hover the cursor over Joke API and right below the drop down menu is Database. Once a user inputs data into the table a new user will appear. Here is the [link to the frontend code](https://github.com/aditiakella/Period2Gaels/blob/main/templates/index.html)
   * Scroll down to Crud Create
   * Insert your information, and it will come out, and the user can see there username password and email on a table provided above
   * All this code will be stored in the back end so that our team can see the data stores from all the users inputs
   * This back end of the code will be stored in a [file](https://github.com/aditiakella/Period2Gaels/blob/main/models/crud.py) where we can see everything that happens in our project
   * As of right now progress is still being made and learning how to fix our errors as well
   * Going to tutorial and learning from Mr.M was a great way to receive feedback as well as learning how to improve our code
   * [Scrum Board Item](https://github.com/aditiakella/Period2Gaels/projects/1#card-51445004)
### Web API:
    * Running Instructions: In order to run the API, click the link to our [website](Tweeter.gq). Then, click on word "Twitter API” in the navbar. This is the Twitter API page and it will be able to let you search on twitter.
    * First an [app route on the views.py page](https://github.com/aditiakella/Period2Gaels/blob/51c47dd73e691921b14e07146d090372afcdfe39/views.py#L42-L50) was changed from the past joke api.
    * We are still working on getting the API to succesfully run as we still need to figure out what variables to use for the backend.
    * The file [joke.html](https://github.com/aditiakella/Period2Gaels/blob/main/templates/joke.html) was the front end of the API page. 
    * [Scrum Board Item](https://github.com/aditiakella/Period2Gaels/projects/1#card-51445255)
### Easter Egg ([link](Tweeter.gq/easteregg))
    * In order to run the easter egg, click the link to our [website](Tweeter.gq). Then, click on the logo in the middle of the homepage
    * First we had to turn the logo on our homepage into a button with [this code](https://github.com/aditiakella/Period2Gaels/blob/8b3e02b436e1071a7ce265eafc1a61b28b5af40c/templates/home.html#L109).
    * Then we had to create an app route for the easter egg page with [this code](https://github.com/aditiakella/Period2Gaels/blob/8b3e02b436e1071a7ce265eafc1a61b28b5af40c/views.py#L66-L68).
    *Lastly, we had to create our easter egg page with [this code](https://github.com/aditiakella/Period2Gaels/blob/main/templates/easteregg.html)
    *[Scrum Board Item](https://github.com/aditiakella/Period2Gaels/projects/1#card-53523282)

## Scrum Team Cards
### Scrum Master Grading: 19/20 (For all team members)
* Deployment - Grace
    * Running Instructions: to run our website on the Raspberry Pi Web Server, click this [link](Tweeter.gq)
    * created a raspberry pi web server using these [instructions](http://nighthawkcoders.cf/lesson/pi-webserver/)
    * did port forwarding with our project using these [instructions](http://nighthawkcoders.cf/lesson/pi-portforward/)
    * created a domain called Tweeter.gq running our main [website](Tweeter.gq) on it
    * [Scrum Board Item](https://github.com/aditiakella/Period2Gaels/projects/1#card-52163809)
* Web API - Aditi 
    * Running Instructions: In order to run the joke API, click the link to our [website](Tweeter.gq). Then, click on word “Birds” in the navbar. This is the joke API page and every time you click on “New Joke”, a new joke will be generated. 
    * I added th joke API to the project so I could get familiar with using APIs before moving on to incproprating my own API.
    * First I added an [app route on the views.py page](https://github.com/aditiakella/Period2Gaels/blob/51c47dd73e691921b14e07146d090372afcdfe39/views.py#L42-L50) so that the joke API could have it's own page
    * Then I created a file called [joke.html](https://github.com/aditiakella/Period2Gaels/blob/main/templates/joke.html), which was the code for the joke page. 
    * Then we had to install a package called [requests](https://github.com/aditiakella/Period2Gaels/blob/51c47dd73e691921b14e07146d090372afcdfe39/views.py#L3) in views.py so that the joke page could work. 
    * [Scrum Board Item](https://github.com/aditiakella/Period2Gaels/projects/1#card-52589451)
* Feedback Page Set Up - Sophie
    * Running Instructions: In order to run the Feedback page, click the link to our [website](Tweeter.gq). Then, click “Feedback” in the NavBar of the homepage, and it should take you to a link where you answer a couple of questions. Once you are done, it will prompt you to hit “submit” and will take you to our Thank You page.
    * I added the [Responses page app route](https://github.com/aditiakella/Period2Gaels/blob/51c47dd73e691921b14e07146d090372afcdfe39/views.py#L52-L54) so that the feedback page wouldn't lead to an error once you hit submit
    * I added the colors and questions to the [Feedback page](https://github.com/aditiakella/Period2Gaels/blob/main/templates/Feedback.html)
    * I made an [app route for the Feedback page](https://github.com/aditiakella/Period2Gaels/blob/51c47dd73e691921b14e07146d090372afcdfe39/views.py#L12-L14)
    * [Scrum Board Item](https://github.com/aditiakella/Period2Gaels/projects/1#card-52906850)
 

## Scrum Team Members
* Aditi Akella
* Sophie Bulkin
* Grace Le
* Luke Manning (joined week 6)
