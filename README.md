# Period 2: Gaels

## Links
* [Study Journal](https://docs.google.com/document/d/1NFgEh_1AZGfm3fGWLUgGT7Xm9tNoPROnnH0_pO72MzM/edit?usp=sharing)
* [One Minute Commercial](https://youtu.be/UtrLlKdQrYk)
* [Scrum Board](https://github.com/aditiakella/Per2Gaels/projects/1)
* [Project Plan](https://docs.google.com/document/d/1wBFv8xEiTdBYL12SreRxs_ixNCXaxFt93r1jJ1S14m4/edit?usp=sharing)
* [Website on Raspberry Pi Web Server](http://tweeter.gq/)

## Project Overview
Our website, [tweeter.gq](http://tweeter.gq/), is a website that features information about birds and their evolution. Our project showcases our team's learning throughout the year. Our project utilizes a Python Back End and an HTML Front End, as well as Jinja templates, SQLAlchemy databases, and CSS. 
## Project Components
#### Homepage (Grace): 
* Go to our [homepage](http://tweeter.gq/) by clicking on the link
* Our homepage features a bird of the month
* Code Review:
    * On home.html, there [first section of code](https://github.com/aditiakella/Per2Gaels/blob/6d67a8bf972a9591f42cd2cc511073da9c8e96f5/templates/home.html#L8-L86) sets up the style for the rest of the page. 
    * Next, there is [code for a navbar](https://github.com/aditiakella/Per2Gaels/blob/6d67a8bf972a9591f42cd2cc511073da9c8e96f5/templates/home.html#L88-L123) so that users can navigate our website. 
    * Then there is the [code for the heading](https://github.com/aditiakella/Per2Gaels/blob/6d67a8bf972a9591f42cd2cc511073da9c8e96f5/templates/home.html#L125-L136) of the homepage and picture of flying birds.
    * Lastly, there is the [code for the bird of the month section](https://github.com/aditiakella/Per2Gaels/blob/6d67a8bf972a9591f42cd2cc511073da9c8e96f5/templates/home.html#L137-L143), which includes a title, picture, and some text. 
* [Scrum Board Card](https://github.com/aditiakella/Per2Gaels/projects/1#card-56444175)
#### Navbar (Grace): 
* On each page of our website there is a [navigation bar](http://tweeter.gq/)
* Clicking on those links takes you to different parts of our website
* If you click on our logo, which is in the middle of the navbar, you will be redirected to our [easter egg](http://tweeter.gq/easteregg)
* Code Review:
    * On home.html, [here](https://github.com/aditiakella/Per2Gaels/blob/07fd2649f40002722840140ed11eb69c20ca136d/templates/home.html#L8-L111) is the code that sets up the style for the navbar
    * [Here](https://github.com/aditiakella/Per2Gaels/blob/07fd2649f40002722840140ed11eb69c20ca136d/templates/home.html#L95wd) is the code that links the homepage of our website.
    * [Here](https://github.com/aditiakella/Per2Gaels/blob/07fd2649f40002722840140ed11eb69c20ca136d/templates/home.html#L96-L103) is the code that creates the dropdown menu for the About Us pages
    * [Here](https://github.com/aditiakella/Per2Gaels/blob/07fd2649f40002722840140ed11eb69c20ca136d/templates/home.html#L105) is the code that links the Twitter API
    * [Here](https://github.com/aditiakella/Per2Gaels/blob/07fd2649f40002722840140ed11eb69c20ca136d/templates/home.html#L91) is the code that turns our logo into the easter egg
    * [Here](https://github.com/aditiakella/Per2Gaels/blob/07fd2649f40002722840140ed11eb69c20ca136d/templates/home.html#L106-L108) is the code the links the contact page, phylogeny page, and our study journal
* [Scrum Board Card]()
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
* In order to run this file, go to the [homepage](http://tweeter.gq/), click the logo in the middle of the screen, and it will redirect you to the [Easter Egg](http://tweeter.gq/easteregg)
* Code Review: 
    * First, on easteregg.html, there is a section that sets up the [style of the easter egg](https://github.com/aditiakella/Per2Gaels/blob/414fd3fdfd85b082770f5f78b5b22d70885b6648/templates/easteregg.html#L7-L85).
    * Then, there is code for our [navbar](https://github.com/aditiakella/Per2Gaels/blob/414fd3fdfd85b082770f5f78b5b22d70885b6648/templates/easteregg.html#L88-L110)
    * Next, we [embedded the college board requirements](https://github.com/aditiakella/Per2Gaels/blob/ef16b1403cd5117da145032694bde968daec338d/templates/easteregg.html#L19-L21).
    * Then we wrote the code for the ["Who am I in Computer Science?"](https://github.com/aditiakella/Per2Gaels/blob/ef16b1403cd5117da145032694bde968daec338d/templates/easteregg.html#L113-L147), which highlights all of the things that we have learned throughout the course of working on this project.
    * We have also embedded our [group journal](https://github.com/aditiakella/Per2Gaels/blob/ef16b1403cd5117da145032694bde968daec338d/templates/easteregg.html#L149-L150), which has also been embedded to demonstrate our completion of the college board requirements
    * At the end, we used an HTML form to create a "feedback" [page](https://github.com/aditiakella/Per2Gaels/blob/ef16b1403cd5117da145032694bde968daec338d/templates/easteregg.html#L197-L218) where you can say which aspects of the college board requirements you (the evaluator) think were not efficiently used
* [Scrum Board Card](https://github.com/aditiakella/Per2Gaels/projects/1#card-56444072)
#### Databases Front End (Grace):
* On the navigation bar if you click on contact it will take you to an [contact page](http://tweeter.gq/database/)
* Code Review:
    * First, our contact page was created using [index.html](https://github.com/aditiakella/Per2Gaels/blob/master/templates/index.html), which is based on a Jinja template using [base.html](https://github.com/aditiakella/Per2Gaels/blob/master/templates/base.html). Base.html includes the style for index.htmal as well as a navbar. 
    * On the contact page, there is a contact form on which the user can input there [name, password, email, and phone number](https://github.com/aditiakella/Per2Gaels/blob/2ed96fb04bf3a90e09a31c72c25183952f99d145/templates/index.html#L119-L137)
    * Using the contact form, the user can add their information to a [contact table](https://github.com/aditiakella/Per2Gaels/blob/2ed96fb04bf3a90e09a31c72c25183952f99d145/templates/index.html#L141-L188).
    * Users can [delete](https://github.com/aditiakella/Per2Gaels/blob/2ed96fb04bf3a90e09a31c72c25183952f99d145/templates/index.html#L194-L215) there information if they don't want it there anymore
* [Scrum Board Card](https://github.com/aditiakella/Per2Gaels/projects/1#card-56444109)
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
    * In the [delete function on views.py](https://github.com/aditiakella/Per2Gaels/blob/bba4c21a37b217ac5a4171b877cb07dae3da9c3e/views.py#L30-L36), a similar method is used. 
    * First, the form is used to identify which user should be deleted from the database
    * Then the model_delete procedure is called and the user's information is no longer displayed in the table. 
    * The [functions emails and phones on views.py](https://github.com/aditiakella/Per2Gaels/blob/a7e40d9e3dd598599e78ae0f126b3fb550ccfa75/views.py#L40-L52) are used to display the users' emails and phone numbers. First the model_query_emails and model_query_phones procedures are used to call all of the emails and and phone numbers in the database. Then the emails and phone numbers are displyed on the table in index.html.
* [Scrum Board Card](https://github.com/aditiakella/Per2Gaels/projects/1#card-56443929)  
#### Phylogeny Page (Sophie):
* To access the phylogeny page, go to our [homepage](http://tweeter.gq/) and click on phylogeny in the navbar. You will be redirected to the [bird phylogeny page](http://tweeter.gq/Phylogenetic/).
* Code Review:
    * First, on phylogenetic.html, there is a section that sets up the [style of the phylogeny page](https://github.com/aditiakella/Per2Gaels/blob/2ed96fb04bf3a90e09a31c72c25183952f99d145/templates/Phylogenetic.html#L8-L77).
    * Then, there is code for our [navbar](https://github.com/aditiakella/Per2Gaels/blob/2ed96fb04bf3a90e09a31c72c25183952f99d145/templates/Phylogenetic.html#L88-L110)
    * Next there is code for a [embedded picture of a phylogenetic tree](https://github.com/aditiakella/Per2Gaels/blob/2ed96fb04bf3a90e09a31c72c25183952f99d145/templates/Phylogenetic.html#L120) that shows the relationship between orders of birds
* [Scrum Board Card](https://github.com/aditiakella/Per2Gaels/projects/1#card-56537642)

## Scrum Team Members
* Aditi Akella
* Sophie Bulkin
* Grace Le
* Luke Manning (joined week 6)
