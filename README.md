# Cocktail Hour
Cocktail Hour is a virtual recipe collection specifically designed for cocktail recipes. 

It is a community based experience that allows casual, one-time users to browse recipes, and allows returning users to create profiles and upload and manage recipes. 

You can find the live site [here](https://cocktail-hour-ms3.herokuapp.com/)
![Main site image](static/images/README/readme-main-img.png)

---
---
# Contents
+ [User Experience](#user-experience)
  + [User Stories](#user-stories)
  + [Design](#design)
    + [Overall Feel](#overall-feel)
    + [Colour Scheme](#colour-scheme)
    + [Typography](#typography)
    + [Imagery](#imagery)
  + [Wireframes and Initial Design](#wireframes-and-initial-design)
    + [Wireframes](#wireframes)
    + [Design Mock Up](#design-mock-up)
+ [Features](#features)
  + [Current Features](#current-features)
  + [Possible Future Features](#possible-future-features)
+ [Database](#database)
+ [Technologies Used](#technologies-used)
  + [Languages](#languages)
  + [Frameworks and Libraries](#frameworks-and-libraries)
  + [All Others](#all-others)
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
### As the site owner/admin:
+ I want to be able to add new collections to the site.
+ I want the new collection to be added to the appropriate site areas.
+ I want to be able to edit the pre-existing collections.
+ I want to be able to delete any collections.
 
## Design
### Overall Feel

For this project I wanted to have a dark feel to emulate a night-time setting. While there are some family-friendly recipes to choose from, the majority of the content will be more adult-themed so I feel that the bar-type setting was the way to go. 
In keeping with the bar theme, I decided to have a neon effect following throughout all pages. 

### Colour Scheme

Because the overall theme is dark, I wanted to go with accent colours that would pop in comparison. I found the perfect colour scheme in a [Shutterstock article](https://www.shutterstock.com/blog/neon-color-palettes) that would work with my idea, just with a couple of changes for contrast reasons.

![colour scheme](static/images/README/colour-scheme.png)

### Typography

There were two fonts that I was interested in for the site. 

[Neon Tubes](https://befonts.com/neon-tubes-neon-light-font-free.html) by [guxjohn](https://befonts.com/author/guxjohn) fit perfectly with the neon light theme but is something to be used sparingly - I want to keep this just just headings and accents. I think too much of this would become tacky very quickly. 

[Raleway](https://fonts.google.com/specimen/Raleway?preview.text_type=custom&preview.text=Collections&query=Raleway) is the chosen font for the majority of the text. In comparison to Neon Tubes, it is quite simple and offers a contrasting elegance. 

### Imagery

Imagery is an important part of the user experience. Any user that uploads recipes has to accompany it with an image. And when browsing the recipes and collections, this image is the main selling point of the recipe so it's the prominent feature of the recipe card. 

Another visual element is the banners on the recipe and collections pages. One some of them, a cocktail image was best. But for others, a visual element that evoked a feeling was more appropriate. If this site were going into full production, the site owner/admin would be in charge of this. 

Lastly is the neon effect. It ties into the nightlife theme so well and I decided to use it across all pages. I think doing this makes the site visually cohesive throughout.

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
### **Navigation menu displayed across all pages**

The navigation menu will help the user move easily across all pages. For the collections pages, there is a dropdown menu in which all of those pages are held. This stops the navigation from becoming too cluttered. 

The navigation buttons update depending on whether a user is logged in, and whether that user is the admin:

| Nav Link              |Not logged in  |Logged in as user|Logged in as admin
|:-------------         |:------------- |:------------- |:------------- |
|Logo(back to home)     |&#9989;        |&#9989;        |&#9989;
|Recipes                |&#9989;        |&#9989;        |&#9989;
|Collections            |&#9989;        |&#9989;        |&#9989;
|Manage Collections     |&#10060;       |&#10060;       |&#9989;
|Account                |&#10060;       |&#9989;        |&#9989;
|Log Out                |&#10060;       |&#9989;        |&#9989;
|Register               |&#9989;        |&#10060;       |&#10060;
|Log In                 |&#9989;        |&#10060;       |&#10060;

### **Carousel displayed on home page for browsing the various 'Collections'** 

The carousel will allow the user to browse through the different recipe collections. This adds a more visual element rather than the simple text of the collections dropdown on the nav bar. All of the carousel images will link the user to the collection page of their choosing. 

### **All recipes accessible to users who don't want to make an account**

As someone who doesn't particularly like to sign up to websites that I don't plan on adding to but like to view, I wanted to make all of the recipes accessible to a casual viewer. The user can also browse through all of the collections without having to have an account. But in order to interact with the site, they Do have to have an account. Without one, the option to upload anything isn't available. 

### **Users can search for recipes based on either key words or ingredients**

Searching by ingredient is an important feature for any recipe website so that was something that I wanted to include. But people who are familiar with cocktails in general might be looking for a specific recipe based on name so this was also included in the search criteria. 

### **Pagination on recipe pages**

At the moment, the database is relatively small. But if this were site that was going into full production, the recipes list would be much more extensive. As a result, the number of recipes displyed to the user could become overwhelming very quickly. I've limited to number of recipes to 12 per page - there's still a good amount displayed to the user without being too much. This will also help reduce loading times, especially on mobile devices. 

### **Ease of access button**

While the 12-per-page layout mentioned above is quite condensed on a laptop or computer screen, it still comes across as quite lengthy on small mobile devices. During manual testing, I found it tedious to have to keep scrolling back to the top. Because of this, I added a scroll-to-top button on any pages that display recipe. This will save endless scrolling for the user. 

Another issue that I found was once I had selected a recipe to view in full, it felt like a bit of a dead end. I decided to add a 'Back to Recipes' button at the top of the page. It just redirects back to the previous page much like the back button but from a UX POV it feels less breakable!

### **User account management**

Anyone is able to make an account through the 'Register' page. They have to choose a username and a password. Measures have been put in place so that the user cannot choose a username that is already taken and they cannot use just whitespace.

Once their account is made, they will be able to log in an out when needed. 

### **User recipe management**

A registered user is able to upload recipes to the site. Once they have recipes that they have added, all recipe management can be done from their account page. This includes editing a deleting. I decided to keep these features exclusive to the account page rather than accessible on the recipes or collections pages. I like the uniformity of this. 

  + **Uploading**: when uploading, there are form validations in place that the user needs to adhere to. The two most important are: 
    + The user cannot leave any inputs blank
    + The user cannot use just whitespace. 

  + **Editing**: the user will have to go into the edit page through the recipe, make the necessary changes and confirm them at the bottom of the page. The user also has the option to cancel all changes. These steps assure that the user cannot do any of this by mistake. 

  + **Deleting**: there is a confirmation modal in place to assure the user doesn't accidentally delete the recipe. 

### **Recipe Images**

When uploading a recipe, the user needs to add an image alongside the recipe information. This image will be used on both the recipe card and on the full recipe page. But because the image is added via a url, there are some people who wither don't was to go to the rounds of finding one, or they simply can't on their device. iOS doesn't allow the user to copy an image url in the same way most android do. Because of that I have added a placeholder image url that the user can use in place of their own. It's a stylish image that was found on [Unsplash](https://unsplash.com/) that looks good with the overall feel of the site. 

### **Adding to collections**

When uploading a recipe, the user is required to add their recipe to at least one collection. This allows the user to feel like they're adding to the community in a more thoughtful way. This also takes the responsibility of curating the collections off the owner/admin. 

### **Admin 'Collections' management**

Only the admin can manage the collections pages. This includes adding, editing and deleting. The site has been designed so that the admin only has to use the collections management page to create a new collection at this will automatically be updated on the carousel, nav bar dropdown and the actual page will be created dynamically. Any edits or deletions to collections will also apply to those elements. 

## Possible Future Features
+ A rating system that allows users to rate each others recipes. 
  + This could lead to sorting by top-rated recipes.
+ Ability to 'save' recipes to a users own account to refer back to.
+ Ability to upload a saved image to their recipe rather than relying on a URL.
+ Users ability to update username. 
+ Users ability to delete their account. 
  + This could allow the user to either leave their recipes on the site or delete them along with the account 
+ Admin controlled 'featured' recipes

---
---

# Database
Below is the schema for my database:

![database schema](static/images/README/db-schema.PNG)

## Categories

| Key                   |Value type     |Desc           |
|:-------------         |:------------- |:------------- |
|_id                    |ObjectId       |
|category_name          |string         |used in *recipes* array
|carousel_img           |string         |url for the carousel image
|banner_img             |string         |url for the banner image

While the ```category_name``` key was planned ahead of time, I added the ```carousel_img``` and ```page_url``` keys later when I was experimenting with the carousel on the home page. The ```page_url``` has since been removed but I've documented this in the Bugs and Fixes section of the [testing.md](https://github.com/AmyOShea/MS3-Cocktail-Hour/blob/master/TESTING.md) file. The ```banner_img``` was also a later addition. 

## Recipes

| Key                   |Value type     |Desc           |
|:-------------         |:------------- |:------------- |
|_id                    |ObjectId       |
|category_name          |array          |each collection chosen by user from *categories*
|cocktail_name          |string         |
|main_ingredient        |string         |
|ingredients            |array          |individual ingredients input by user
|method                 |array          |individual steps input by user
|image_url              |string         |
|created_by             |ObjectId       |object id taken from *users*

## Users

| User                  |Value type     |Desc           |
|:-------------         |:------------- |:------------- |
|_id                    |ObjectId       |used in *recipes*
|username               |string         |
|password               |string         |hashed password for user security

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
+ [Am I Responsive](http://ami.responsivedesign.is/) used to generate README intro image.
+ [Autoprefixer](https://autoprefixer.github.io/) used to make CSS cross-browser compatible.
+ [favicon.io](https://favicon.io/) used to create a site favicon.
+ [Imgur](https://imgur.com/) used to host images.

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
+ In the GitPod terminal, type ```echo web: python run.py > Procfile``` to create your Procfile.
+ The Procfile needs to contain the following line: ```web: python app.py``` and make sure there is no additional blank line after it. 
+ Push these files to your repository.

### Environmentals File

Create and env.py file using the following information:

```
import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", " *unique secret key* ")
os.environ.setdefault("MONGO_URI", " *unique uri from mongo.db * ")
os.environ.setdefault("MONGO_DB", " *database name* ")
```

Because this contains sensitive information, this needs to be added to the '.gitignore' file. 

### Creating Heroku App
+ Log into Heroku
+ Select 'Create New App' from your dashboard
+ Choose an app name (if there has been an app made with that name, you will be informed and will need to choose an alternative)
+ Select the appropriate region based on your location
+ Click 'Create App'
### Connecting to GitHub
+ From the dashboard, click the 'Deploy' tab towards the top of the screen
+ From here, locate 'Deployment Method' and choose 'GitHub'
+ From the search bar newly appeared, locate your repository by name
+ When you have located the correct repository, click 'Connect'
+ DO NOT CLICK 'ENABLE AUTOMATIC DEPLOYMENT': This can cause unexpected errors before configuration. We'll come back to this
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
+ Once the app is built (it may take a few minutes), click 'Open App' from the top of the page

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

**NB:** In order to work with a clone of this project, you will need to create the env.py file using your own variables and create a MongoDB database matching the one documented in the [Database section](#database) of this doc. 

You will also need to install all of the packages listed in the requirements file you can use the following command in the terminal ```pip install -r requirements.txt``` which will do it for you. 

---
---
# Credits
## Code

+ REGEX pattern for form input validation taken from this [Stack Overflow post](https://stackoverflow.com/questions/13766015/is-it-possible-to-configure-a-required-field-to-ignore-white-space).

+ The HTML back button was taken from this [W3Schools page](https://www.w3schools.com/jsref/met_his_back.asp).

+ I used [this Stack Overflow post](https://stackoverflow.com/questions/50394358/materializecss-vertically-offset-dropdown-menu-content/50395102) to adjust the placement of the nav bar dropdown.

+ This code for [materialize slider autoplay](https://stackoverflow.com/questions/36581504/materialize-carousel-slider-autoplay) was taken directly (also credited in in js file).

+ My own neon text css classes taken from [this article](https://css-tricks.com/how-to-create-neon-text-with-css/) and re-worked for my neon boxes (also credited in in css file).

+ [This demo](https://gist.github.com/mozillazg/69fb40067ae6d80386e10e105e6803c9) was used to understand how to incorperate flask pagination into my pre existing code.

+ [This Stack Overflow post](https://stackoverflow.com/questions/27992413/how-do-i-calculate-the-offsets-for-pagination/27992616) helped me gain more of an understanding of pagination offset.

+ [This Stack Overflow post](https://stackoverflow.com/questions/27980121/pylint-warning-possible-unbalanced-tuple-unpacking-with-sequence) helped with the Pylint warning that I was getting and provided the comment to override it.

+ I used the code in this [W3Schools post](https://www.w3schools.com/howto/howto_js_scroll_to_top.asp) to create the scroll-to-top button.

+ I took the JS code from this [Stack Overflow post](https://stackoverflow.com/questions/36581504/materialize-carousel-slider-autoplay) for the carousel autoplay functionality.


## Content

### Images
+ Collections: 
    + Classics Banner and Carousel [image](https://images.unsplash.com/photo-1601084638773-a25993f38fda?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=966&q=80) from [Unsplash](https://unsplash.com/photos/Fs_pf0hubTU)
    
    
    + Elegance Banner and Carousel [image](https://images.unsplash.com/photo-1524083615948-77168224375a?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=80) from [Unsplash](https://unsplash.com/photos/JdntgyV5w0Q)
    
    
    + Fruity Banner and Carousel [image](https://images.pexels.com/photos/5947121/pexels-photo-5947121.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260) from [Pexels](https://www.pexels.com/zh-tw/photo/5947121/)
    
    
    + Hot Drinks Banner and Carousel [image](https://images.unsplash.com/photo-1521022969448-49639904ed7b?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=80) from [Unsplash](https://unsplash.com/photos/Zif9OPYfwdE)
    
    
    + Mocktails Banner and Carousel [image](https://images.unsplash.com/photo-1548016193-b9381233058c?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1955&q=80) from [Unsplash](https://unsplash.com/photos/kBo2MFJz2QU)
    
    
    + Pitchers Banner and Carousel [image](https://melbournecocktails.com/wp-content/uploads/GTea_cocktails_jug-1-1075x605.jpg) from [Melbourne Cocktails](https://melbournecocktails.com/g-and-tea-gin-garden/)
    
    
    + Shots Banner and Carousel [image](https://mk0foodfornetcoviwv0.kinstacdn.com/wp-content/uploads/B53-800x550.jpg) from [Food For Net](https://foodfornet.com/fun-alcoholic-shots/)
    
    
    + Experiment Banner and Carousel [image](https://images.unsplash.com/photo-1608989408460-75014171c099?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1050&q=80) from [Unsplash](https://unsplash.com/photos/P8D0PIc2FwQ)

+ All Cocktails banner [image](https://images.unsplash.com/photo-1605270012917-bf157c5a9541?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1949&q=80) from [Unsplash](https://unsplash.com/photos/QYWYnzvPTAQ)


+ Home Page wall background [image](https://images.unsplash.com/photo-1549930160-31d20fbcac9e?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1950&q=80) from [Unsplash](https://unsplash.com/photos/FzTc9Itg_lk)


+ Default recipe URL [image](https://images.unsplash.com/photo-1570869937455-a347fba0a41b?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80) from [Unsplash](https://unsplash.com/photos/8Zmm4NtXmdE)

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
+ All the friends who tested the site, even in its earliest stages.
+ Everyone in the CI Slack that offered answers, advice and just a bit of a chat when needed!
+ My mentor Antonio Rodriguez for  for his help at the different stages of the project.