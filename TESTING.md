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

---
---
## Lighthouse Testing

---
---
## PowerMapper Compatibility

---
---
## Testing From User Stories

---
---
## Manually Testing Functionality

---
---
## Responsive Testing

---
---
## Bugs and Fixes
### **Card Overlaying**

![card overlay bug](static/images/README/bugs/bug-01.PNG)

When initially putting together the card layout, I was having an isse where the reicpe card was layering on top of the previous one rather than generating it's own card

![card overlay bug](static/images/README/bugs/bug-01-code.PNG)

After a bit of experimenting, I moved the entire card div into the for loop and managed to sort this issue. 

![card overlay bug](static/images/README/bugs/bug-01-code-fix.PNG)

---
### **TypeError - length vs count()**

I followed the CI task manager project for the initial stages of this project. Most things translated well except the ```length``` property. When called, it would cause a TypeError.

![TypeError](static/images/README/bugs/bug-02.PNG)

![TypeError](static/images/README/bugs/bug-02-code-2.PNG)

![TypeError](static/images/README/bugs/bug-02-code.PNG)

I did a lot of research on this and while there were a few different fixes, the one that worked best for this project was to change the ```recipes``` variable from a list and use the ```count()``` fuction instead.

![TypeError](static/images/README/bugs/bug-02-code-fix-2.PNG)

![TypeError](static/images/README/bugs/bug-02-code-fix.PNG)

---

### **Side Nav Dropdown**

When using the Materialize navigaiton bar dropdown, the side nav dropdown on mobile was covering the content below, rather than pushing the content down. 

![Dropdown bug](static/images/README/bugs/bug-03.PNG)

I believe this is expected behaviour but from a UX standpoint, I wasn't happy with this on mobile.
As a result, I decided that it would be a better idea to use a Materialize collapsible on the side-nav instead. This allows the sub-menu to repositiono all of the other elements rathen than them being covered. 

---
### **Hover on Mobile**

I added ```hover:true``` to the dropdown menu which worked fine on desktop. But with mobile, it was causing a massive glitch - when you would click the dropdown menu, it would appear for a split second and disappear. 

![Hover bug](static/images/README/bugs/bug-04-code.PNG)

I tried removing the ```inDuration``` and ```outDuration``` but it was still happening. I decided to remove the ```hover``` option altogether and this fixed the issue. 

---
### **Deleting from Modal**

For defensive programming, I added a modla to the delete button for user confirmation. However, regardless of which recipe was selected to delete, it was always the first recipe on screen that would be deleted. 

After talking to someone on slack who had experienced the same issue, I was informed that there needed to be a direct link between the modal and the element to be deleted. 

I updated the recipe-side modal href and the actual modal ID to target the specific recipe card to be deleted. 

![Deleting bug](static/images/README/bugs/bug-05-code-fix.jpg) 

---
### **Selecting option on mobile**

On mobile, the 'Choose Collection' option in both add and edit recipe wasn't working as it should. There was an issue with selecting the options - you would select 'Fruity', but 'Mocktails' would highlight, as if there had been an upwas shift in the selection area. 

![Selecting bug](static/images/README/bugs/bug-06-code.PNG) 

Oringially the ```formSelect()```m function was placed above the ```dropdown()``` function, both of which were triggered by the 'Choose Collection' dropdown. I know that the order of code matters so I tried to reorder them.

![Selecting bug](static/images/README/bugs/bug-06-code-fix.PNG)  

This fixed the issue.

---

### **Pagination in Catagories Pages**

When visitn a specific collection of recipes, the correct recipes for that category were displating. Hoever, the pagination information was displaying the total number of recipes in the database. 

![Pagination bug](static/images/README/bugs/bug-09.jpg)

![Pagination bug](static/images/README/bugs/bug-09-code.PNG)

Becuse I hadn't specified the ```category_name``` in the ```find()``` function for the ```total``` variable, it was counting all recipes and then displaying this number as the total. 

![Pagination bug](static/images/README/bugs/bug-09-code-fix.PNG)

Adding the ```category_name``` key and the correct value in the ```total``` variable fixed the issue.

---

### **Input Field Dynamic ID**

When dynamically adding a new input field for ingredients and method, there was an issues with clicking the input field. When the second input was clicked, the focus would jump back up to the original input. 

![Input Field Dynamic ID bug](static/images/README/bugs/bug-10.PNG)

This was because I had not been dynamically adding a new ID to the newly created input fields. Adding an incrementing variable to the ID fixed this issue. 

![Input Field Dynamic ID bug](static/images/README/bugs/bug-10-code-fix.jpg)

---
---
## Known Bugs