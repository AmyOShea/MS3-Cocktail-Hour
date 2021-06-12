# Cocktail Hour
Cocktail Hour is a virtual recipe collection speifically designed for coctail recipes. 

It is a community based experience that allows casual, one-time users to browse recipes, and allows returning users to create profiles and upload and manage recipes. 

You can find the live site [here](https://cocktail-hour-ms3.herokuapp.com/)

---
---
# Contents
+ [User Experience](#user-experience)
  + [User Stories](#user-stories)
  + [Design](#design)
    + [Overall Feel](#overall-feel)
    + [Colour Scheme](#colour-scheme)
    + [Typography](#typography)
  + [Wireframes and Initial Design](#wireframes-and-initial-design)
    + [Wireframes](#wireframes)
    + [Design Mock Up](#design-mock-up)
+ [Features](#features)
  + [Current Features](#current-features)
  + [Possible Future Features](#possible-future-features)
+ [Technologies Used](#technologies-used)
  + [Languages](#languages)
  + [Frameworks and Libraries](#frameworks-and-libraries)
  + [All Others](#all-others)
  + [Programmes and Ext Resources](#programmes-and-ext-resources)
+ [Testing](#testing)
+ [Deployment](#deployment)
  + [Deployment through GitHub Pages](#deployment-through-gitHub-pages)
  + [Forking the Repository](#forking-the-repository)
  + [Cloning Project](#cloning-project)
+ [Credits](#credits)
  + [Content](#content)
  + [Media](#media)
  + [Acknowledgements](#acknowledgements)
---
---
# User Experience
## User Stories
### As a casual user: 
+ I want to be able to view recipes without having to register and account. 
+ I want to be able to search for specific recipes. 
+ I want to be able to search for recipes that have a specific ingredient.
+ I want to have a varied range of cocktails.
+ I want to have a some cocktail suggestions when I'm not sure what to look for.
+ I want to have the option to register an account if I want to come back at a later date. 
### As a returning user: 
+ I want to be able to log into my account.
+ I want to be able to upload a recipe. 
+ I want to be able to add a recipe to the pre-determined collections.
+ I want to have ease of access to any recipes that I have already uploaded.
+ I want to  be able to edit or delete any recipes that I have already uploaded.
## Design
### Overall Feel

For this poroject I wanted to have a dark feel to emulate a night-time setting. While there are some family-friendly recipes to choose from, the majority of the content will be more adult-themed so I feel that the bar-type setting was the way to go. 
In keeping with the bar theme, I dewcided to have a neon effect following throughout all pages. 

### Colour Scheme

Because the overall theme is dark, I wanted to go with accent colours that would pop in comparison. I found the perfect colour scheme in a [Shutterstock article](https://www.shutterstock.com/blog/neon-color-palettes)that would work with my idea, just with a couple of changes for contrast reasons.

![colour scheme](static/images/README/colour-scheme.png)

### Typography

There were two fonts that I was interested in for the site. 

[Neon Tubes](https://befonts.com/neon-tubes-neon-light-font-free.html) by [guxjohn](https://befonts.com/author/guxjohn) fit perfectly with the neon light theme but is something to be used sparingly - I want to keep this just just headings and accents. I think too much of this would become tacky very quickly. 

[Raleway](https://fonts.google.com/specimen/Raleway?preview.text_type=custom&preview.text=Collections&query=Raleway) is the chosen font for the majority of the text. In comparrison to Noeon Tubes, it is quite simple ansd offers a contrasting elegance. 

## Wireframes and Initial Design
### Wireframes
All Wireframes were designed for laptop/computer, iPad/tablet and phone display.
+ All wireframes [here](https://github.com/AmyOShea/MS3-Cocktail-Hour/blob/master/assets/pre-work/MS3-initial-wireframes.pdf)

### Design Mock Up
+ All designs [here](https://github.com/AmyOShea/MS3-Cocktail-Hour/blob/master/assets/pre-work/MS3-initial-design.pdf)

---
---
# Features
## Current Features
+ Navigation menu displayed across all pages.
+ Carousel displayed on home page for browsing the various 'Collections'. 
+ All recipes accessible to users who don't want to make an account.
+ Users can search for recipes based on either key words or ingredients.
+ Users can create an account.
+ Users can log into/sign out of their account.
+ Registered users can upload their own recipes.
+ Registered users add their own recipes to one or more 'Collections'.
+ Registered users can add an image their own recipes via URL.
+ Registered users who don't want to search for an image can use the default image URL.
+ Registered users can view their own added recipes.
+ Registered users can edit recipes that they have already added. 

## Possible Future Features
+ A rating system that allows users to rate each others recipes. 
  + This could lead to sorting buy top-rated recipes.
+ Ability to 'save' recipes to a users own account to refer back to.
+ Ability to upload a saved image to their recipe rather than relying on a URL.
+ Users ability to update username. 
+ Users ability to delete their account. 
  + This could allow the user to either leave their recipes on the site or delete them along with the account 

---
---

# Database
Below is the schema for my database:
![database schema](static/images/README/db-schema.PNG)
+ Categories

While the ```category_name``` key was planned ahead of time, I added the ```carousel_img``` and ```page_url``` keys later when I was experimenting with the carousel on the home page. I've documented this in the Bugs and Fixes section of the [testing.md](https://github.com/AmyOShea/MS3-Cocktail-Hour/blob/master/TESTING.md) file.
The category_name key links to the Recipies THING

+ Recipes


+ Users



---
---
# Technologies Used
## Languages
+ [HTML5](https://en.wikipedia.org/wiki/HTML5)
+ [CSS3](https://en.wikipedia.org/wiki/CSS)
+ [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
+ [Python3](https://www.python.org/)

## Frameworks and Libraries
+ [Flask](https://flask.palletsprojects.com/en/1.1.x/)
+ [Flask-PyMongo](https://pypi.org/project/Flask-PyMongo/)
+ [Pip3](https://pip.pypa.io/en/stable/)
+ [dnspython](https://www.dnspython.org/)
+ [jQuery](https://jquery.com/)
+ [Flask Paginate](https://pythonhosted.org/Flask-paginate/)
+ [Jinja](https://jinja.palletsprojects.com/en/3.0.x/)
+ [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/)
+ [Materialize](https://materializecss.com/)
+ [FontAwesome](https://fontawesome.com/)
+ [Google Fonts](https://fonts.google.com/) 

## All Others
+ [Heroku](https://www.heroku.com/) used to deploy live site
+ [MongoDB](https://www.mongodb.com/) used to host database information.
+ [GitHub](https://github.com/) used to host repository.
+ [GitPod](https://www.gitpod.io/) used to develop project and organise version 
+ [Procreate](https://procreate.art/) used to design initial mock ups, tilable background, logo and other design accents. 
+ [Adobe Photoshop](https://www.adobe.com/ie/products/photoshop.html) used to cut and re-frame site images. 
+ [Balsamiq](https://balsamiq.com/) used to create wireframes.
+ [RandomKeygen](https://randomkeygen.com/) used to create a strong password for required  `<SECRET_KEY>`.
+ [CloudConvert](https://cloudconvert.com/) to convert all images to .webp format.
+ [Autoprefixer CSS](https://autoprefixer.github.io/) used to make CSS cross-browser compatible.
+ [Transfonter](https://transfonter.org/) used to convert font from .tff to .woff and .woff2.
+ [Lighthouse](https://developers.google.com/web/tools/lighthouse) for performance review.
+ [PowerMapper](https://www.powermapper.com/) used to check compatibility with older browsers.
+ [Responsinator](https://www.responsinator.com/) used to check site was responsive on different screen sizes.
+ [Autoprefixer](https://autoprefixer.github.io/) used to make CSS cross-browser compatible.
+ [favicon.io](https://favicon.io/) used to create a site favicon.

---
---
# Testing
Due to the size of the testing section, I have created a separate document for it. You can find it [here](https://github.com/AmyOShea/MS3-Cocktail-Hour/blob/master/TESTING.md). 

---
---
# Deployment

## Heroku Deployment
This project was deployed through Heroku using the following steps:

### Requirements and Procfile
Heroku needs to know which technologies are being used and any requirements, so I created files to let it know. Before creating the Heroku app, create these files using the following steps in GitPod: 
+ In the GitPod terminal, type ```pip3 freeze --local > requirements.txt``` to create your requirements file.
+ In the GitPod terminal, type ```echo web: python run.py > Procfile``` to create your procfile.
+ Push these files to your repository.

### Creating Heroku App
+ Log into Heroku
+ Select 'Create New App' from your dashboard
+ Choose an app name (if there has been an app made with that name, you will be informed and will need to choose an alternative)
+ Select the appropiate region based on your location
+ Click 'Create App'
### Connecting to GitHub
+ From the dashboard, click the 'Deploy' tab towards the top of the screen
+ From here, locate 'Deployment Method' and choose 'GitHub'
+ From the search bar newly appeared, locate your respository by name
+ When you have located the correct repository, click 'Connect'
+ DO NOT CLICK 'ENABLE AUTOMATIC DEPLOYMENT': This can cause unexpected errors before configuation. We'll come back to this
+ Click the 'Settings' tab towards the top of the page
+ Locate the 'Config Vars' and click 'Reveal Config Vars'
+ Use the following keys and values which must match the key/value pairs in your env.py file:

| Key           | Value               |
| ------------- |:--------------------|
| IP            | 0.0.0.0             |
| PORT          | 5000                |
| SECRET_KEY    |*Secure secret key*  |
| MONGO_URI     |mongodb+srv://root:*PASSWORD*@myfirstcluster.dr4g1.mongodb.net/cocktail_hour?retryWrites=true&w=majority |
| MONGO_DBNAME  |cocktail_hour        |
|               |                     |

+ Go back to the 'Deploy' tab and you can now click 'Enable Automatic Deployment'
+ Underneath, locate 'Manual Deploy'; choose the master branch and click 'Deploy Branch'
+ Once the app is built (it may take a few mminutes), click 'Open App' from the top of the page

## Forking the Repository
+ Log in to GitHub and locate the GitHub Repository
+ At the top of the Repository above the "Settings" Button on the menu, locate the "Fork" Button.
+ You will have a copy of the original repository in your GitHub account.
+ You will now be able to make changes to the new version and keep the original safe. 
## Making a Local Clone
+ Log into GitHub.
+ Locate the repository.
+ Click the 'Code' dropdown above the file list.
+ Copy the URL for the repository.
+ Open Git Bash on your device.
+ Change the current working directory to the location where you want the cloned directory.
+ Type ```git clone``` in the CLI and then paste the URL you copied earlier. This is what it should look like:
  + ```$ git clone https://github.com/AmyOShea/MS3-Cocktail-Hour```
+ Press Enter to create your local clone.

---
---
# Credits
## Code

+ REGEX pattern for form input validation taken from this [Stack Overflow post](https://stackoverflow.com/questions/13766015/is-it-possible-to-configure-a-required-field-to-ignore-white-space).

+ The HTML back button was taken from this [W3Schools page](https://www.w3schools.com/jsref/met_his_back.asp).

+ I used [this Stack Overflow post](https://stackoverflow.com/questions/50394358/materializecss-vertically-offset-dropdown-menu-content/50395102) to adjust the placement of the nav bar dropdown.

+ This code for [materialze slider autoplay](https://stackoverflow.com/questions/36581504/materialize-carousel-slider-autoplay) was taken directly (also credited in in js file).

+ My own neon text css classes taken from [this article](https://css-tricks.com/how-to-create-neon-text-with-css/) and re-worked for my neon boxes (also credited in in css file).

+ [This demo](https://gist.github.com/mozillazg/69fb40067ae6d80386e10e105e6803c9) was used to understand how to incorperate flask pagination into my pre existing code.

+ [This Stack Overflow post](https://stackoverflow.com/questions/27992413/how-do-i-calculate-the-offsets-for-pagination/27992616) helped me gain more of an understanding of pagination offset.

+ [This Stack Overflow post](https://stackoverflow.com/questions/27980121/pylint-warning-possible-unbalanced-tuple-unpacking-with-sequence) helped with the Pylint warning that I was getting and provided the comment to override it.

+ I used the code in this [W3Schools post](https://www.w3schools.com/howto/howto_js_scroll_to_top.asp) to create the scroll-to-top button.

+ I took the JS code from this [Stack Overflow post](https://stackoverflow.com/questions/36581504/materialize-carousel-slider-autoplay) for the carousel autoplay functionality.


## Content

### Images
+ Collections: 
    + Classics Banner and Carousel [image](https://images.unsplash.com/photo-1601084638773-a25993f38fda?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=966&q=80)
    + Elegance Banner and Carousel [image](https://images.unsplash.com/photo-1524083615948-77168224375a?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=80)
    + Fruity Banner and Carousel [image](https://images.pexels.com/photos/5947121/pexels-photo-5947121.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260)
    + Hot Drinks Banner and Carousel [image](https://images.unsplash.com/photo-1521022969448-49639904ed7b?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=80)
    + Mocktails Banner and Carousel [image](https://images.unsplash.com/photo-1548016193-b9381233058c?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1955&q=80)
    + Pitchers Banner and Carousel [image](https://melbournecocktails.com/g-and-tea-gin-garden/)
    + Shots Banner and Carousel [image](https://mk0foodfornetcoviwv0.kinstacdn.com/wp-content/uploads/Three-shots-of-vodka-on-a-black-slate-800x530.jpg)

+ All Cocktails banner [image](https://images.unsplash.com/photo-1605270012917-bf157c5a9541?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1949&q=80)
+ Home Page wall background [image](https://images.unsplash.com/photo-1549930160-31d20fbcac9e?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1950&q=80)
+ Default recipe URL [image](https://images.unsplash.com/photo-1570869937455-a347fba0a41b?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80)

### Test Recipes

+ All test recipes that I added were collected from [BBC Good Food website](https://www.bbcgoodfood.com/):
   + [Mojito](https://www.bbcgoodfood.com/recipes/mojito)
   + [Espresso Martini](https://www.bbcgoodfood.com/recipes/espresso-martini)
   + [Sangria](https://www.bbcgoodfood.com/recipes/sangria)
   + [Sex on the Beach](https://www.bbcgoodfood.com/recipes/sex-beach-cocktail)
   + [Vodka Martini](https://www.bbcgoodfood.com/recipes/vodka-martini)
   + [Bloody Mary](https://www.bbcgoodfood.com/recipes/easy-bloody-mary)
   + [Cosmopolitan](https://www.bbcgoodfood.com/recipes/cosmopolitan-cocktail)
   + [Summer Punch](https://www.bbcgoodfood.com/recipes/wilhelminas-punch)
   + [Strawberry Mojito](https://www.bbcgoodfood.com/recipes/strawberry-mojito)
   + [Lemon Drizzle Shots](https://www.bbcgoodfood.com/recipes/lemon-drizzle-shots)
   + [Diablo Grenadine](https://www.bbcgoodfood.com/recipes/diabolo-grenadine)
   + [Hot Toddy](https://www.bbcgoodfood.com/recipes/hot-toddy)
+ All other recipes added by friends/family testers
## Acknowledgements
