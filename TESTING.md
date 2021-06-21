# Full Testing
## Contents
+ [Validator Testing](#validator-testing)
+ [Lighthouse Testing](#lighthouse-testing)
+ [PowerMapper Compatibility](#powermapper-compatibility)
+ [Testing From User Stories](#testing-from-user-stories)
+ [Manually Testing Functionality](#manually-testing-functionality)
+ [Responsive Testing](#responsive-testing)
+ [Bugs and Fixes](#bugs-and-fixes)
+ [Known Bugs](#known-bugs)
---
---
## Validator Testing
### **HTML**

 I checked all of the HTML pages using [W3C Markup Validation Service](https://validator.w3.org/)

 Because the code is made up of Jinja templates, I had to check from the live site by right clicking each page, selecting View Page Source and running that generated code through the validator.

 All pages passed all checks. 

### **CSS**

I checked the CSS file using [W3C CSS Markup Validation Service](https://jigsaw.w3.org/css-validator/)

Unfortunately, it returned 3 errors:

![css validator results](static/images/README/validator-css.PNG)

All the errors were in relation to the ```backdrop-filter: blur``` property that it claims doesn't exist. However, according to [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/backdrop-filter) this is a valid property. 

There are some compatbilty issues with Firefox which I've documented in the [manual testing section](#manually-testing-functionality). 

Other than that, any other warnings were related to the vendor prefixes. 

### **JavaScript**

I checked the script.js file using [JSHint](https://jshint.com/)

The only issues coming back from JS Validator were two unused functions:

![js validator results](static/images/README/validator-js.PNG)

However, both of these functions are called throughout the site:

![js validator results](static/images/README/validator-js-02.PNG)

![js validator results](static/images/README/validator-js-03.PNG)

### **Python**
I checked the app.py file using [PEP8 online](http://pep8online.com/)

The code passed all checks.

---
---
## Lighthouse Testing

After getting the bulk of the site in place, I ran it through Chrome Lighthouse. The initial scores were a bit low:

![initial lighthouse score](static/images/README/lighthouse-dscore-01.PNG)

By the feed back given , I made a few changes to the code to raise the scores:

### **Performance**

+ Convert all images to webp format

### **Accessibility**

+ Footer h4 changed to h1
+ Add alt tags to all images
+ Add title to all links
+ Place side nav header into li

### **Best Practices**
+ Add ```rel="nopener"``` to all external links

### **SEO**
+ Add meta description

All of these changes helped bring the final score up nicely. While I would have like a higher performance score(preferably in the green) but overall, I'm happy with the progress. 

![final lighthouse score](static/images/README/lighthouse-d-score-02.PNG)

---
---
## PowerMapper Compatibility

I used [PowerMapper](https://www.powermapper.com/) to test cross-browser compatbility on other browsers that I don't have access to.

![powermapper results](static/images/README/powermapper-01.PNG)

According to their site, the ```backdrop-filter``` property had some browser compatibility issues:
![powermapper results](static/images/README/powermapper-02.PNG)

I manually checked all of the browsers specified(apart from Internet Explorer) and found that, apart from Firefox, the ```backdrop-filter``` property did work:

![safari blur](static/images/README/safari-backdrop-blur.png)
![ios blur](static/images/README/ios-backdrop-blur.png)

Firefox definitely doesn't support the property so I manually tested it to make sure that, even without the blur filter, the site still looked okay and the text was legible

![firefox blur](static/images/README/firefox-blur.png)
![firefox blur](static/images/README/firefox-blur-02.png)
![firefox blur](static/images/README/firefox-blur-03.PNG)

While it would be great to have the blur included, I still think that the look of the site holds up on firefox and all text remains legible. 

---
---
## Testing From User Stories

### As a casual user: 
+ *I want to be able to view recipes without having to register and account.*

Even without being logged in, a user is able to browse through all the recipe cards, choose one and view the full recipe:

![testing from user stories](static/images/README/Testing/testing-01.png)

---

+ *I want to be able to search for specific recipes.*
+ *I want to be able to search for recipes that have a specific ingredient.*

From the recipes page, the user can use the search bar for specifics:

![testing from user stories](static/images/README/Testing/testing-02.png)

The words searched will come from the cocktail name, main ingredient and full ingredients list. 

If there were any results, the user will see just them:

![testing from user stories](static/images/README/Testing/testing-02-a.png)

If there were no matches, the user will be shown a message informing them:

![testing from user stories](static/images/README/Testing/testing-02-b.png)

The user can then use the use the clear button to revert back to seeing all recipes. 

---

+ *I want to have a varied range of cocktails.*

The recipes page gives the user the ability to browse through all of the recipes on the site, regardless of which collection it belongs to:

![testing from user stories](static/images/README/Testing/testing-03.png)

---

+ *I want to have a some cocktail suggestions when I'm not sure what to look for.*

On the home page, the carousel will give the user various collections to scroll through. Each image is a link to the appropriate collection page:

![testing from user stories](static/images/README/Testing/testing-04.png)

---

+ *I want to have the option to register an account if I want to come back at a later date.*

From the navigation bar, the user can go to the registration page. From there, they can choose a username and password:

![testing from user stories](static/images/README/Testing/testing-05.png)

 If their chosen username has already been taken, they will be informed and can choose another:

 ![testing from user stories](static/images/README/Testing/testing-05-a.png)

---

### As a returning user: 
+ *I want to be able to log into my account.*

As long as the user has been through the registration process, they can use the long in page from the navigation bar to access their account:

![testing from user stories](static/images/README/Testing/testing-06.png)

If they use the wrong username or password, they will be informed and can retry:

![testing from user stories](static/images/README/Testing/testing-06-a.png)

---

+ *I want to be able to upload a recipe.*

From their account page, the use will see the upload button towards the top of the page:

![testing from user stories](static/images/README/Testing/testing-07.png)

Once they have clicked it, they will be redirected to the upload page:

![testing from user stories](static/images/README/Testing/testing-08.png)

---

+ *I want to be able to add a recipe to the pre-determined collections.*

Once the user has been directed to the upload page, the first option is to choose which categories they would like their recipe to be added to:

![testing from user stories](static/images/README/Testing/testing-09.png)

---

+ *I want to have ease of access to any recipes that I have already uploaded.*

From their account page, the user will be able to view all recipes that they have uploaded:

![testing from user stories](static/images/README/Testing/testing-10.png)

---

+ *I want to be able to edit or delete any recipes that I have already uploaded.*

From the account page, a logged in user has access to all of their recipes. From there, the user can hover over any of the recipes and they are presented with the edit or delete options:

![testing from user stories](static/images/README/Testing/testing-11.png)

**EDIT:**
if the user presses the edit button, the page reloads to the edit page which is a visual duplication of the upload page. However, the input fields will be populated with their original input:

![testing from user stories](static/images/README/Testing/testing-12.png)

Once the user has made the necessary changes, they can save them at the bottom of the page. Alternatively, they can cancel all changes they've made. Both buttons lead back to their account page:

![testing from user stories](static/images/README/Testing/testing-13.png)

**Delete:** if the user chooses the delete button, they will be presented with a modal to either confirm or cancel the deletion: 

![testing from user stories](static/images/README/Testing/testing-14.png)

---

### As the site owner/admin:
+ *I want to be able to add new collections to the site.*

The admin will be able to log into their account as every other user does. However, they will have the 'Manage Collections' link in the nav bar:

![testing from user stories](static/images/README/Testing/testing-15.png)

Once they're on the 'Manage Collections' page, they'll have access to the 'Add Collection' button:

![testing from user stories](static/images/README/Testing/testing-16.png)

Once they click that, they'll be redirected to the upload page where they can fill in all of the collection information. The tool tips will give them information about the input elements:

![testing from user stories](static/images/README/Testing/testing-17.png)

Once all of the inputs have been filled in correctly, the user can use the 'Add Collection' button at the bottom of the page to add it to the database:

![testing from user stories](static/images/README/Testing/testing-18.png)

---

+ *I want the new collection to be added to the appropriate site areas.*

The new collection is added to the nav bar (and side nav):

![testing from user stories](static/images/README/Testing/testing-19.png)

The new collection is added to the home page carousel:

![testing from user stories](static/images/README/Testing/testing-20.png)

The new collection has its own page created:

![testing from user stories](static/images/README/Testing/testing-21.png)

---

+ *I want to be able to edit the pre-existing collections.*

From the 'Manage Collections' page, the admin can hover/click on whichever collection they wish to edit and click the 'Edit' button:

![testing from user stories](static/images/README/Testing/testing-22.png)

This will redirect them to the edit page where they can update whatever information they want. The only thing they can't update is the collection name:

![testing from user stories](static/images/README/Testing/testing-23.png)

Once the user has updated the information, they can access they buttons at the bottom of the form. If they click 'Edit Collection', the changed will be sent to the database and be updated across the site. They also have the option to 'Cancel' which will ignore any changes and redirect them to the 'Manage Collections' page:

![testing from user stories](static/images/README/Testing/testing-24.png)

---

+ *I want to be able to delete any collections.*

From the 'Manage Collections' page, the admin can hover/click on whichever collection they wish to edit and click the 'Delete' button:

![testing from user stories](static/images/README/Testing/testing-25.png)

A modal will appear asking the admin to confirm that they want to delete the collection. They also have the option to 'Cancel' which will close the modal with no changes made:

![testing from user stories](static/images/README/Testing/testing-26.png)

---
---
## Manually Testing Functionality
### **base.html**

| Element               | Action        | Expected Result| Pass/Fail  |
|:-------------         |:------------- |:-----|:-----|
| **NavBar**            |               |      |
|Logo                   |Click|Redirect to home         |Pass|
|Recipes Link           |Click|Redirect to all recipes  |Pass|
|Collections Dropdown   |Click|Open collections dropdown|Pass|
|Collection page link   |Click|Redirect to collection page|Pass|
|Manage Collections link|Click|Redirect to all_collections page|Pass|
|                       |     |(Only visible if admin in session)|Pass|
|Register Link          |Click|Redirect to register page|Pass|
|                       |     |(Not visible if user in session)  |Pass|
|Log In Link            |Click|Redirect to log in page  |Pass|
|                       |     |(Not visible if user in session)  |Pass|
|Log Out Link           |Click|Log user out of account  |Pass|
|                       |Click|Redirect to log in page  |Pass|
|                       |     |(Only visible if user in session)  |Pass|
|Account Link            |Click|Redirect to account page|Pass|
|                       |     |(Only visible if user in session)  |Pass|
|Manage Collections Link|Click|Redirect to manage collections page|Pass|
|                       |     |(Only visible if admin in session) |Pass|
| **SideNav**           |       |    |
|Hamburger Icon         |Click|Open Sidenav             |Pass|
|Recipes Link           |Click|Redirect to all recipes  |Pass|
|Collections Dropdown   |Click|Open collections dropdown|Pass|
|Collection page link   |Click|Redirect to collection page|Pass|
|Manage Collections link|Click|Redirect to all_collections page|Pass|
|                       |     |(Only visible if admin in session)|Pass|
|Register Link          |Click|Redirect to register page|Pass|
|                       |     |(Not visible if user in session)  |Pass|
|Log In Link            |Click|Redirect to log in page  |Pass|
|                       |     |(Not visible if user in session)  |Pass|
|Log Out Link           |Click|Log user out of account  |Pass|
|                       |Click|Redirect to log in page  |Pass|
|                       |     |(Only visible if user in session)  |Pass|
|Account Link            |Click|Redirect to account page|Pass|
|                       |     |(Only visible if user in session)  |Pass|
|Manage Collections Link|Click|Redirect to manage collections page|Pass|
|                       |     |(Only visible if admin in session) |Pass|
| **Footer**            |     |     |
|Facebook Link          |Click|Open on external page    |Pass|
|Instagram Link         |Click|Open on external page    |Pass|
|Twitter Link           |Click|Open on external page    |Pass|
|TikTok Link            |Click|Open on external page    |Pass|

---
### **index.html**
| Element               | Action            | Expected Result           | Pass/Fail  |
|:-------------         |:-------------     |:-----                     |:-----|
| **Carousel**          |                   |                           |    |
|Whole Carousel         |Horizontal scroll  |Scroll through collections |Pass|
|Classics Link          |Click              |Redirect to Classics page  |Pass|
|Elegance Link          |Click              |Redirect to Elegance page  |Pass|
|Fruity Link            |Click              |Redirect to Fruity page    |Pass|
|Hot Drinks Link        |Click              |Redirect to Hot Drinks page|Pass|
|Mocktails Link         |Click              |Redirect to Mocktails page |Pass|
|Pitchers Link          |Click              |Redirect to Pitchers page  |Pass|
|Shots Link             |Click              |Redirect to Shots page     |Pass|
|Register Link          |Click              |Redirect to register page  |Pass|
|Log In Link            |Click              |Redirect to log in page    |Pass|
| **Inline Links**      |                   |                           |    |
|Sign Up link           |Click              |Redirect to Register Page  |Pass|
|Sign In link           |Click              |Redirect to Login page     |Pass|
|'Join us...'           |Click              |Redirect to recipes page   |Pass|

---

### **account.html**

| Element                   | Action            | Expected Result                   | Pass/Fail  |
|:-------------             |:-------------     |:-----                             |:-----|
| **Upload Btn**            |                   |                                   |    |
|Upload Button              |Click              |Redirect to recipe upload page     |Pass|
| **Recipe Card**           |                   |                                   |    |
|Recipe Card                |Hover/click        |Reveal recipe action buttons       |Pass|
|Full recipe btn            |Click              |Redirect to full recipe            |Pass|
|Edit recipe btn            |Click              |Redirect to edit recipe page       |Pass|
|Delete recipe btn          |Click              |Open delete confirmation modal     |Pass|
|Delete modal - delete btn  |Click              |Delete selected recipe             |Pass|
|                           |                   |Redirect to account page           |Pass|
|                           |                   |'Recipe deleted' confirmation message  |Pass|
|Delete modal - cancel btn  |Click              |Close modal with no change made    |Pass|
| **Pagination**            |                   |                                   |    |
|<< btn                     |Click              |Reveal 'previous' recipes          |Pass|
|Pagination number          |Click              |Specific recipes page number       |Pass|
|>> btn                     |Click              |Reveal 'next' recipes              |Pass|
| **Scroll to top btn**     |                   |                                   |    |
|(Mobile only) btn          |Click              |Scroll to top of page              |Pass|

---
### add_recipe.html

| Element                   | Action            | Expected Result                   | Pass/Fail  |
|:-------------             |:-------------     |:-----                             |:-----|
| **Form**                  |                   |                                   |    |
|Choose Collection dropdown |Click              |Reveal collection options          |Pass|
|Text input fields          |Type into          |Text appears, line highlights green|Pass|
|Text input fields          |Leave blank        |Line highlights red                |Pass|
|Text input fields          |Just input whitespace  |Line highlights red            |Pass|
|Tooltips                   |Hover/click        |Reveal notes/instructions          |Pass|
|Add ingredient btn         |Click              |Generate new input field           |Pass|
|Delete ingredient btn      |Click              |Delete new input field             |Pass|
|Add method step btn        |Click              |Generate new method step field     |Pass|
|Delete method step btn     |Click              |Delete new method step field       |Pass|
|Add recipe btn(all fields correct)|Click       |Recipe uploads to database         |Pass|
|                           |                   |Redirect to account page           |Pass|
|                           |                   |"Recipe Uploaded!" confirmation message  |Pass|
|Add recipe btn(some incorrect fields)|Click    |Page scrolls to incorrect fields   |Pass|

---
### **edit_recipe.html**

| Element                   | Action            | Expected Result                   | Pass/Fail  |
|:-------------             |:-------------     |:-----                             |:-----|
| **Form**                  |                   |                                   |    |
|All fields                 |On page open       |Pre-populated with previous inputs |Pass|
|Choose Collection dropdown |Click              |Reveal collection options          |Pass|
|Text input fields          |Type into          |Text appears, line highlights green|Pass|
|Text input fields          |Leave blank        |Line highlights red                |Pass|
|Text input fields          |Just input whitespace  |Line highlights red            |Pass|
|Tooltips                   |Hover/click        |Reveal notes/instructions          |Pass|
|Add ingredient btn         |Click              |Generate new input field           |Pass|
|Delete ingredient btn      |Click              |Delete new input field             |Pass|
|Add method step btn        |Click              |Generate new method step field     |Pass|
|Delete method step btn     |Click              |Delete new method step field       |Pass|
|Update btn(all fields correct)|Click           |Recipe updates on database         |Pass|
|                           |                   |Redirect to account page           |Pass|
|                           |                   |"Recipe Edited!" confirmation message  |Pass|
|Update btn(some incorrect fields)|Click        |Page scrolls to incorrect fields   |Pass|
|Cancel btn                 |Click              |No changes made to recipe          |Pass|
|                           |                   |Redirect to account page           |Pass|

---
### **full_recipe.html**

| Element                   | Action            | Expected Result                   | Pass/Fail  |
|:-------------             |:-------------     |:-----                             |:-----|
|Back to recipes btn        |Click              |Redirect to previous page          |Pass|
|Recipe image               |On page open       |Recipe image displayed properly    |Pass|
|Recipe ingredients list    |On page open       |Recipe ingredients list displayed properly |Pass|
|Recipe method list         |On page open       |Recipe method list displayed properly  |Pass|

---
### **login.html**

| Element                   | Action            | Expected Result                   | Pass/Fail  |
|:-------------             |:-------------     |:-----                             |:-----|
|**Form**                   |Click              |Redirect to previous page          |Pass|
|Username                   |Text input         |Text displayed to user             |Pass|
|Password                   |Text input         |Password hidden to user            |Pass|
|Submit btn (fields correct)|Click              |Redirect to account page           |Pass|
|Submit btn (fields incorrect)|Click            |Reload log in page                 |Pass|
|**Redirect Link**          |                   |                                   |    |
|'Register here' link       |Click              |Redirect to registration page      |Pass|

---
### **recipes.html**

| Element                   | Action            | Expected Result                   | Pass/Fail  |
|:-------------             |:-------------     |:-----                             |:-----|
|**Search**                 |                   |                                   |    |
|Text input                 |Text input         |Text displayed to user             |Pass|
|Clear btn                  |Click              |Clear searches, show all recipes   |Pass|
|Search btn (with results)  |Click              |Display matched to user            |Pass|
|Search btn (no results)    |Click              |'No Results Found' message         |Pass|
|**'No Results Found' links**|                  |                                   |    |
|Account log in link        |Click              |Redirect to log in page            |Pass|
|Register account link      |Click              |redirect to registration page      |Pass|
| **Recipe Card**           |                   |                                   |    |
|Recipe Card                |Hover/click        |Reveal recipe action buttons       |Pass|
|Full recipe btn            |Click              |Redirect to full recipe            |Pass|
| **Pagination**            |                   |                                   |    |
|<< btn                     |Click              |Reveal 'previous' recipes          |Pass|
|Pagination number          |Click              |Specific recipes page number       |Pass|
|>> btn                     |Click              |Reveal 'next' recipes              |Pass|
| **Scroll to top btn**     |                   |                                   |    |
|(Mobile only) btn          |Click              |Scroll to top of page              |Pass|


---
### **register.html**

| Element                   | Action            | Expected Result                   | Pass/Fail  |
|:-------------             |:-------------     |:-----                             |:-----|
|**Form**                   |Click              |Redirect to previous page          |Pass|
|Username                   |Text input         |Text displayed to user             |Pass|
|Password                   |Text input         |Password hidden to user            |Pass|
|**Submit btn**             |                   |                                   |    |
|Fields correct             |Click              |New user added to database         |Pass|
|                           |                   |Redirect to account page           |Pass|
|Fields incorrect format    |Click              |Fields highlighted red, user prompted to change format |Pass|
|Username already in use    |Click              |Reload register page, error message to user    |Pass|
|**Redirect Link**          ||||
|'Log in here' link         |Click              |Redirect to log in page            |Pass|

---
### **Collections pages**
*All collections pages have identical functionality so all the below test apply to each collection page:*

| Element                   | Action            | Expected Result                   | Pass/Fail  |
|:-------------             |:-------------     |:-----                             |:-----|
|Recipe Card                |On page load       |Only display recipes in that category|Pass|
|Recipe Card                |Hover/click        |Reveal recipe action buttons       |Pass|
|Full recipe btn            |Click              |Redirect to full recipe            |Pass|
| **Pagination**            |                   |                                   |    |
|<< btn                     |Click              |Reveal 'previous' recipes          |Pass|
|Pagination number          |Click              |Specific recipes page number       |Pass|
|>> btn                     |Click              |Reveal 'next' recipes              |Pass|
| **Scroll to top btn**     |                   |                                   |    |
|(Mobile only) btn          |Click              |Scroll to top of page              |Pass|
|**If nothing in collection**|                  |                                   |    |
|User message               |On page load       |Message informs user that there's no recipes in collection|Pass|
|Log in link                |On page load       |Redirect to log in page            |Pass|
|Register link              |On page load       |Redirect to registration page      |Pass|

---

### **all_collections.html**

| Element                   | Action            | Expected Result                   | Pass/Fail  |
|:-------------             |:-------------     |:-----                             |:-----|
| **Upload Btn**            |                   |                                   |    |
|Upload Button              |Click              |Redirect to collection upload page |Pass|
| **Collection Card**       |                   |                                   |    |
|Collection Card            |Hover/click        |Reveal recipe action buttons       |Pass|
|Edit collection btn        |Click              |Redirect to edit collection page   |Pass|
|Delete collection btn      |Click              |Open delete confirmation modal     |Pass|
|Delete modal - delete btn  |Click              |Delete selected collection         |Pass|
|                           |                   |Redirect to all_collections page   |Pass|
|                           |                   |'Collection deleted' confirmation message|Pass|
|Delete modal - cancel btn  |Click              |Close modal with no change made    |Pass|
| **Pagination**            |                   |                                   |    |
|<< btn                     |Click              |Reveal 'previous' recipes          |Pass|
|Pagination number          |Click              |Specific recipes page number       |Pass|
|>> btn                     |Click              |Reveal 'next' recipes              |Pass|
| **Scroll to top btn**     |                   |                                   |    |
|(Mobile only) btn          |Click              |Scroll to top of page              |Pass|


### add_collection.html

| Element                   | Action            | Expected Result                   | Pass/Fail  |
|:-------------             |:-------------     |:-----                             |:-----|
| **Form**                  |                   |                                   |    |
|Text input fields          |Type into          |Text appears, line highlights green|Pass|
|Text input fields          |Leave blank        |Line highlights red                |Pass|
|Text input fields          |Just input whitespace  |Line highlights red            |Pass|
|Tooltips                   |Hover/click        |Reveal notes/instructions          |Pass|
|Add collection btn(all fields correct)|Click   |Collection uploads to database     |Pass|
|                           |                   |Redirect to all_collections page   |Pass|
|                           |                   |"New Collection Added!" confirmation message|Pass|
|Add collection btn(some incorrect fields)|Click|Page scrolls to incorrect fields   |Pass|

---
### **edit_collection.html**

| Element                   | Action            | Expected Result                   | Pass/Fail  |
|:-------------             |:-------------     |:-----                             |:-----|
| **Form**                  |                   |                                   |    |
|All fields                 |On page open       |Pre-populated with previous inputs |Pass|
|Collection name input field|On click           |User unable to edit                |Pass|
|Text input fields          |Type into          |Text appears, line highlights green|Pass|
|Text input fields          |Leave blank        |Line highlights red                |Pass|
|Text input fields          |Just input whitespace  |Line highlights red            |Pass|
|Tooltips                   |Hover/click        |Reveal notes/instructions          |Pass|
|Update btn(all fields correct)|Click           |Collection updates in database     |Pass|
|                           |                   |Redirect to all_collections page   |Pass|
|                           |                   |"Collection Updated!" confirmation message  |Pass|
|Update btn(some incorrect fields)|Click        |Page scrolls to incorrect fields   |Pass|
|Cancel btn                 |Click              |No changes made to collection      |Pass|
|                           |                   |Redirect to all_collections page   |Pass|

---
### **Error pages**

*All error pages have identical functionality so all the below test apply to each error page:*

| Element                   | Action            | Expected Result                   | Pass/Fail  |
|:-------------             |:-------------     |:-----                             |:-----|
|Home btn                   |Click              |Redirect to home page              |Pass|

---
---
## Responsive Testing
Through devices that I have at home/readily available to me, I was able to continuously test on:
### Phone:
+ Samsung Galaxy S9
  + Google Chrome
  + Samsung Internet
+ Huawei Y7
  + Google Chrome
+ iPhone 6
  + Safari
### Tablet
+ iPad Mini 7.9"
  + Safari
+ iPad 9.7"
  + Safari
### Computer
* Avita Pura 14" Laptop
  * Google Chrome
  * Microsoft Edge
  * Opera
  * Mozilla Firefox
### Responsinator
+ When there were devices/browsers that I didn't have access to, I used [Responsinator](https://www.responsinator.com/) to make sure that the site was responsive.

---
---
## Bugs and Fixes

### **Carousel Text**

I used the Materialize Carousel for the home page and wanted to have the information collection name text appear over the image. However, no matter what CSS I tried to manipulate it, the text remained below the image:

![carousel bug](static/images/README/bugs/carousel-bug.PNG)
![carousel bug](static/images/README/bugs/carousel-code.PNG)

On their site, Materialize have another type of carousel that allows for this but I prefer the look of this - the 3d style rotation, in my opinion, looked a lot better for this project. 

I had to experiment ALOT with this but found that the below code worked great for this: 

![carousel bug](static/images/README/bugs/carousel-code-fix-01.PNG)

The above HTML with some CSS tricks helped place the text nicely over the image:

![carousel bug](static/images/README/bugs/carousel-fix.PNG)

Once I had the placement figured, I wanted to experiment further and try to create the carousel dynamically for each drinks collection. While the image and text for each element was easy enough to work through, the anchor URL proved to be tricky. I tried a couple of things and ended up with varying results: 

```<a class="carousel-item" href="{{ url_for(category.category_name) }}">```
+ This threw and error because the category name was capitalized

```<a class="carousel-item" href="{{ url_for(category.category_name).lower() }}">```
+ Worked for some of the categories but a couple of them have more than one word titles so threw another error.

In the end, I created a ```key:value``` pair in MongoDB: the key was called ```page_url``` and the value matched the name of the html page to be redirected to. I was able to pull that in the HTML code:

![carousel bug](static/images/README/bugs/carousel-code-fix-02.PNG)

I have since changed how the collections pages are created - they are now dynamically created so the ```page_url``` is no longer needed.

---
### **Card Overlaying**

![card overlay bug](static/images/README/bugs/bug-01.PNG)

When initially putting together the card layout, I was having an issue where the recipe card was layering on top of the previous one rather than generating it's own card

![card overlay bug](static/images/README/bugs/bug-01-code.PNG)

After a bit of experimenting, I moved the entire card div into the for loop and managed to sort this issue. 

![card overlay bug](static/images/README/bugs/bug-01-code-fix.PNG)

---
### **TypeError - length vs count()**

I followed the CI task manager project for the initial stages of this project. Most things translated well except the ```length``` property. When called, it would cause a TypeError.

![TypeError](static/images/README/bugs/bug-02.PNG)

![TypeError](static/images/README/bugs/bug-02-code-2.PNG)

![TypeError](static/images/README/bugs/bug-02-code.PNG)

I did a lot of research on this and while there were a few different fixes, the one that worked best for this project was to change the ```recipes``` variable from a list and use the ```count()``` function instead.

![TypeError](static/images/README/bugs/bug-02-code-fix-2.PNG)

![TypeError](static/images/README/bugs/bug-02-code-fix.PNG)

---

### **Side Nav Dropdown**

When using the Materialize navigation bar dropdown, the side nav dropdown on mobile was covering the content below, rather than pushing the content down. 

![Dropdown bug](static/images/README/bugs/bug-03.PNG)

I believe this is expected behaviour but from a UX standpoint, I wasn't happy with this on mobile.
As a result, I decided that it would be a better idea to use a Materialize collapsible on the side-nav instead. This allows the sub-menu to reposition all of the other elements rather than them being covered. 

---
### **Hover on Mobile**

I added ```hover:true``` to the dropdown menu which worked fine on desktop. But with mobile, it was causing a massive glitch - when you would click the dropdown menu, it would appear for a split second and disappear. 

![Hover bug](static/images/README/bugs/bug-04-code.PNG)

I tried removing the ```inDuration``` and ```outDuration``` but it was still happening. I decided to remove the ```hover``` option altogether and this fixed the issue. 

---
### **Deleting from Modal**

For defensive programming, I added a modal to the delete button for user confirmation. However, regardless of which recipe was selected to delete, it was always the first recipe on screen that would be deleted. 

After talking to someone on slack who had experienced the same issue, I was informed that there needed to be a direct link between the modal and the element to be deleted. 

I updated the recipe-side modal href and the actual modal ID to target the specific recipe card to be deleted. 

![Deleting bug](static/images/README/bugs/bug-05-code-fix.jpg) 

---
### **Selecting option on mobile**

On mobile, the 'Choose Collection' option in both add and edit recipe wasn't working as it should. There was an issue with selecting the options - you would select 'Fruity', but 'Mocktails' would highlight, as if there had been an upwards shift in the selection area. 

![Selecting bug](static/images/README/bugs/bug-06-code.PNG) 

Originally the ```formSelect()```m function was placed above the ```dropdown()``` function, both of which were triggered by the 'Choose Collection' dropdown. I know that the order of code matters so I tried to reorder them.

![Selecting bug](static/images/README/bugs/bug-06-code-fix.PNG)  

This fixed the issue.

---

### **Pagination in Categories Pages**

When visiting a specific collection of recipes, the correct recipes for that category were displaying. However, the pagination information was displaying the total number of recipes in the database. 

![Pagination bug](static/images/README/bugs/bug-09.jpg)

![Pagination bug](static/images/README/bugs/bug-09-code.PNG)

Because I hadn't specified the ```category_name``` in the ```find()``` function for the ```total``` variable, it was counting all recipes and then displaying this number as the total. 

![Pagination bug](static/images/README/bugs/bug-09-code-fix.PNG)

Adding the ```category_name``` key and the correct value in the ```total``` variable fixed the issue.

Since then, the code has been refactored but the theory remains the same:

``` 
recipes = mongo.db.recipes.find({"category_name": category["category_name"]})

total = recipes.count()
```
---

### **Input Field Dynamic ID**

When dynamically adding a new input field for ingredients and method, there was an issues with clicking the input field. When the second input was clicked, the focus would jump back up to the original input. 

![Input Field Dynamic ID bug](static/images/README/bugs/bug-10.PNG)

This was because I had not been dynamically adding a new ID to the newly created input fields. Adding an incrementing variable to the ID fixed this issue. 

![Input Field Dynamic ID bug](static/images/README/bugs/bug-10-code-fix.jpg)

---

### **Unbalanced Tuple Unpacking**

A pylint warning appeared when I added the pagination functionality:

![Unbalanced Tuple Unpacking bug](static/images/README/bugs/bug-12.PNG)

This was a non-issue as everything was working as it should, and the code worked fine.

After a bit of research I learned that this is referred to as a 'false positive' and by adding the below comment, the warning would go away: 

![Unbalanced Tuple Unpacking bug](static/images/README/bugs/bug-12-code-fix.PNG)

---

### **Scroll-To-Top TypeError**

I added a button to redirect the user back to the top of the page when they had scrolled for a certain amount of pixels. But because the button isn't present on all pages, the JS script was looking for it, not finding it and then throwing the error:

![Scroll-To-Top TypeError bug](static/images/README/bugs/bug-13.PNG)

Wrapping the whole button functionality inside an if statement allowed the script to check if the button was on that page and either run the functions if it was, and ignore them if it wasn't.

![Scroll-To-Top TypeError bug](static/images/README/bugs/bug-13-code-fix.PNG)

---

### **Heading Text Mobile Display**
 On mobile display, a particularly long or multiple word heading 

![Heading Text Mobile Display bug](static/images/README/bugs/bug-14.PNG)
![Heading Text Mobile Display bug](static/images/README/bugs/bug-14-02.PNG)


Making the font responsive to the view width allowed for longer text to display properly without overflowing off the screen. I used a media query targeted specifically at smaller screens so the desktop display didn't look oversized. 

![Heading Text Mobile Display bug](static/images/README/bugs/bug-14-code-fix.PNG)

![Heading Text Mobile Display bug](static/images/README/bugs/bug-14-fix-01.PNG)

---

### **Dynamic Input Pattern Attribute**

When I added the ```pattern=".*\S+.*"``` attribute to the dynamically created input fields, they weren't rendering through to HTML correctly. It was rendering as ```pattern=".*S+.*"```, omitting the backslash. 

To counter this, I added an extra backslash: ```pattern=".*\\S+.*"``` and this solved the issue. 

---

### **Ingredients list issue**

Not so much of a bug but an issues that needed to be addressed. I had friends upload recipes to test. One of the issues that came from this was them not adding to the fields following the instructions in the tool tips. 

There's an input for the main ingredient which is displayed on the recipe card but this also needs to be input under the ingredients list (preferably with measurements). It says this in the tooltips but I get that people don't always read them. 

The issue was that while the main ingredient was seen on the recipe card, once you viewed the full recipe, that was omitted:

![Ingredients list issue](static/images/README/bugs/bug-16.png)

![Ingredients list issue](static/images/README/bugs/bug-16-02.PNG)

To fix this, I added the ```main_ingredient``` to the recipe list. This worked well for recipes that had omitted it from the main ingredients list:

![Ingredients list issue](static/images/README/bugs/bug-16-fix-01.PNG)

But on a recipe that had all of the ingredients listed as per the instructions, it looked a bit strange for it to be listed twice: 

![Ingredients list issue](static/images/README/bugs/bug-16-fix-02.PNG)

To try to remedy the issues, I decided to meet somewhere in the middle - I enlarged the ```main_ingredient``` font and made it a little bolder: 

![Ingredients list issue](static/images/README/bugs/bug-16-correct-01.PNG)

![Ingredients list issue](static/images/README/bugs/bug-16-correct-02.PNG)

This way it's included on the ingredients list but looks more like a featured ingredient that can be overlooked if that ingredient is listed elsewhere.

---
---
## Known Bugs

### **URL & Username bug**

When testing error pages, I was adding addition characters to the end of the URL in the account page, anything that was changed/edited was updating the username header on the page:

![URL & Username bug](static/images/README/bugs/bug-11.PNG)

I defined username as a variable in the account section of the app.py file:

![URL & Username bug](static/images/README/bugs/bug-11-code-fix.PNG)

I retested and, while it solved that issue, adding the extra characters didn't break the code. This is an issue that hasn't been resolved. 

![URL & Username bug](static/images/README/bugs/bug-11-not-resolved.PNG)

---

### **Passive Event Handler**

From the Chrome console there are issues being reported: 

![URL & Username bug](static/images/README/bugs/bug-15.PNG)

These are coming from the ```.side-nav``` and ```.carousel``` triggers. Based on the message itself, the issue seems to be coming from Materialize rather than the script.js file.

![URL & Username bug](static/images/README/bugs/bug-15-02.PNG)

However, I spent a lot of time looking into this and trying to add the ```passive: true``` that the helper documentation pointed to but to no avail. 