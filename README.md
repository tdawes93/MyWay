# myway
myway is travel company specialising in personalised and tailored tour packages for individuals and small groups. It is similar to Contiki with the addition of allowing tours to be adapted using add-ons and consulting the customer team. The business idea was borne from a 'couple' of world travellers with a desire to share hidden gems and locals secrets whilst retaining the culture and serenity that comes with such places.

This app was made as the fulfilment of the Portfolio Project 5 for the Full-Stack Software Development Course (ECommerce Specialisation) provided by Code Institute. It is a Full Stack project and deployed on Heroku.

The live website can be found [here](https://myway-tours.herokuapp.com/)

![Responsive Website](/media/readme/am-i-responsive-mockups.png)

****

## Goals

RatemyRoom App is designed to help improve the quality of rentals as well as reducing the number of tenancy agreements that end badly! With that in mind, the website was designed to provide an unbiased platform for everyone to have their say. The app is split into two main user permission groups, tenant and Landlord/Estate Agent. Their features are as below:

## Structure

### Tenant

- Create a user profile, edit user details and delete the profile
- Search for properties either using the search bar or by scrolling through the carousel
- View each property's details, e.g. address, number of rooms, overall rating 
- Read other people's reviews and like individual properties
- Write a review on properties, leaving a 5-star rating on five individual categories
- Edit and delete any reviews they have written
- See a list of review titles they have written and when they were posted

### Landlord/Estate Agent

In addition to all the features found in the Tenant User Profile the Landlord/Estate Agent User Profile has access to:
- Create a property post, indicating key information e.g. if it is for rent. 
- Edit and delete any properties they have posted
- See a list of property names they have posted

Users who have not created a profile and are therefore are not authenticated can still:
- See a list of properties in the carousel
- View individual property information
- Read reviews on each property
- Search for properties using address information

It encourages all users to create a profile, even those just viewing the site as additional features that may be of interest to them could be added in further releases.

***

## UX

### Agile Developement

This project was built following an Agile design approach. As there is no client following an agile approach had to be adjusted slightly, with the principles focussing on simplicity, promoting sustainable development, delivering working software and reflecting on continuous improvement prioritised. The agile values of 'Working Software' and 'Responding to Change' were at the forefront of the design. Due to the size of the project, five epics were created in which all the user stories fall under. They are as follows 

- Registration and Sign-in
- Products
- Sorting and Searching
- Purchasing and Checkout
- Administration and Store Management

As the website progressed user stories were compeleted and new ones added as new work was identified.

#### User Stories

- Registration and Sign-in:
    - As a site user I can register for an account so I can have a personal account and be able to view my profile
    - As a customer I can login and register using my pre-exsiting facebook/gmail/apple accounts so I can link my emails and accounts into one for a more streamlined service
    - As a site user I can personalise my profile so I can view my personal order history/order confirmations and save my payment information
    - As a site user I can receive an email confirmation after registering so I can verify my account registration was successful
    - As a site user I can recover my password so I can regain access to my account
    - As a site user I can login and logout so I can access my personal/private account information

- Products
  - As a customer I can view a list of products so I can select some to purchase
  - As a customer I can view individual products so I can identify price, description, location and timeframe
  - As a customer I can see a quick view so I can see the details of each tour without navigating away from the page I'm on
  - As a customer I can compare tours side by side so I can compare the details of different tours and decide which is best for me
  - As a customer I can add products to a wish list so I can return to it later and complete my purchase
  - As a customer I can tailor and personalise the trips so I can experience the trip of a life time suited towards me
  - As a customer I can identify packages/deals/group rates so I can take advantages of special savings

- Sorting and Searching
  - As a customer I can sort products by location so I can find the products near where I want to visit
  - As a customer I can sort products by price so I can find the products within my budget
  - As a customer I can sort products by date so I can see trips available during my time off
  - As a customer I can easily see what I've searched for and the number of results so I can quickly decide whether the trip I want is available
  - As a customer I can sort products by multiple categories at once so I can find the best product for me

- Purchasing and Checkout
  - As a customer I can pay online by card so I can order my products easily without having to contact a sales representative
  - As a customer I can receive an email confirmation so I can have a record of my purchases
  - As a customer I can see an order confirmation so I can check I haven't made any mistakes when completing a purchase
  - As a customer I can easily enter my payment information so I can checkout quickly and with no hassle/issues
  - As a customer I can have my personal and payment information safe and secure so I can confidently provide the information needed to make a purchase
  - As a customer I can adjust the dates and number of guests for a trip in the bag so I can make changes just before checkout
  - As a customer I can view the items in my bag so I can identify the total cost of my purchase and details of every trip I am buying
  - As a customer I can easily select the dates and number of guests attending a trip so I can ensure I don't accidentally select the wrong trip or booking information
  - As a customer I can view the total of my purchases at any time so I can avoid spending too much

- Administration and Store Management
  - As a site user I can see messages/notifications when I perform a task so I can be confident that the task has been completed correctly
  - As a site user I can see a clear and interesting homepage so I can understand the meaning of the site and how to make a purchase
  - As a store owner I can create a product so I can keep my e-commerce store up to date
  - As a owner I can edit products so I can change products and keep my store up to date
  - As a owner I can delete products so I can remove products no longer in stock and keep my store up to date
  - As a customer I can view a Facebook page so I can be kept up to date with events and interact with the company

As part of my agile development, all user stories were assigned acceptance criteria and tasks. I then added my user stories to a backlog, before bringing some across to my first iteration. These issues were then assigned MoSoCoW prioritization with 61% of the user stories being Must-Haves. A list of the user stories, and their MoSoCoW prioritization, in the first iteration can be viewed below. ![1st iteration stories - pt1](/media/readme/iteration-1-user-stories-pt1.png)

![1st iteration stories - pt2](/media/readme/iteration-1-user-stories-pt2.png)

The user stories that were not completed in iteration 1 were put back into the backlog and reprioritized in preparation for iteration 2. You can view a screenshot of the completed project board for iteration 1 below

![Iteration 1 Project Board Snap](/media/readme/iteration1-completed-user-stories.png)

### Design

#### Colour Scheme

- As the focus of the tours is on exploring nature, local culture and new experiences the colours were chosen based upon the hero image used on the homepage. The image contains 4 girls standing on a bridge in the middle of the forest. The girls are wearing a variety of coloured jackets and backpacks leading to a vibrant and bright site. 

- As most pages contain images it was decided that a light background would frame the products without distraction. White #fff and White Smoke #f1f1f1 were chosen as the backgrounds across the site. 

- Using the hero image as a base the three other main colours used are Free Speech Red #da0000, Pakistan Green #3a6700 and Sonic Silver #6c757d. The green evokes a feeling of being outside in nature as well as ecouraging the customer to contiue forward. The red provides some needed contrast in the header, drawing the users attention to the key navigation buttons. It is also used as the back/cancel button throughout the site. The silver is used as the footer background, providing a more professional view to the important pages located in the footer.

- For contrast and ease of viewing the majority of text is in Black #000 or white depending on the background colour. 

![Colour Scheme](/media/readme/myway-colour-palette.png)

#### Typography

- Montserrat is used throughout the site. It creates a simple and clean-looking web design. Based on old 50's style street signs it's high readability yet classic design makes it perfect for customers to clearly read the product descriptions whilst gaining an insight into history.

- The site uses sentence-case throughout, with the exception of the logo being all in lowercase. This creates a laid back feeling synonymous with travellers.

- The font has a sans-serif backup.

#### Imagery

- The images used throughout invoke the feeling of freedom, wanderlust and adventure. They are full of friends, laughter and fun. They were chosen specifically to promote excitement amongst the customers in hope they will be more inclined to make a purchase.

- All photos are fully responsive across the entire range of devices and screen widths. 

### Skeleton

The final site consists of the following main pages. Every page was written in HTML using Django Template Tags (written in Python).
Pages:
 - Homepage
 - Tour List
 - Tour Detail Page
 - Bag
 - Checkout
 - Checkout Success
 - Profile
 - Site Management (Admin Users only)
 - Django All Auth pages (e.g. Login/Logout)


#### Database Schema

![Relational Database Tables](/media/readme/database_schema.png)

#### Wireframes

##### Home Page
![Home Page Wireframe](/media/readme/wireframe-homepage.png)

##### Tour Page
![Tour Page Wireframe](/media/readme/wireframe-tourpage.png)

##### Tour Detail Page
![Tour Detail Page Wireframe](/media/readme/wireframe-tourdetail.png)

##### Date Selector - Tour Detail Page
![Date Selector Wireframe](/media/readme/wireframe-tourdetail-date-selector.png)

##### Shopping Bag Page
![Shopping Baf Wireframe](/media/readme/wireframe-shoppingbag.png)

##### Property Detail
![Property Detail Wireframe](media/images/wireframes/wireframe-propertydetail.png)


## Features

### Existing Features

#### Navbar/Footer
- Located at the top and bottom over every page on the site are the Navbar and Footer.
- The navbar provides a quick-link area for users to Sign-in/Sign-up, view selected tours, a link and preview to the users bag, and site management if the user is an admin.
- It is designed responsively using Bootstrap's Breakpoints.
- At smaller screen sizes the  half Navbar will collapse into a hamburger menu icon.
- The nav will follow the same layout as small screens at medium sized screens. 
- At larger screen sizes there will be a combination of icons, text and buttons. 
- The navbar will change depending on your logged-in status and role selected upon registration, this is one of the methods used to restrict unauthorised users from accessing pages they do not have permissions for.
![Small navbar hamburgericon open](/media/readme/small-navbar.png)


![Large navbar](/media/readme/large-navbar.png)

#### Hompage
- The Homepage was designed to be eye-catching and simple. It draws people in with an adventurous photo and a easy to find button.
- First the hero image:
    - The hero image shows a group of girls having fun whilst exploring in nature. This sets the tone for the site, showing how fun and engaging the tours will be.  
    - It is also the image the colour scheme was based off so fits in effortly with the rest of the page.
    - The hero image is responsive, adapting to screen size changes so the girls always remain the subject and in the centre.
- Secondly the slogan and button
    - The slogan is a play on words using the name of the company and a famous phrase. The slight injection of humour again draws the customer in a sets the tone for the site.
    - The button (either above or below depending on screen size) is easy to find and understand. It encourages customers to click it which then takes them directly to a list of tours available. 

    ![Homepage](/media/readme/homepage.png)

#### Property Detail
- The property detail page is one of the main pages of the site. It is accessible by all users including those that have not registered. 

- The first section shows a breakdown of the key property information including:
    - Property Title
    - Number of bedrooms
    - Number of bathrooms
    - Address
    - Main image
- If the property is for rent a button indicating 'For Rent' will also pop up in this section. 
- One of the main drawing points to the property information is the average rating stars. This is calculated by taking the overall rating for each review made for the property and averaging it using the aggregate(Avg()) method built into Django. The result is then converted into an integer and the decimal places are removed using floatformat:0. The result is then transferred into a visual star form. 1 = One star filled in, 2 = Two stars etc.

- To the right of this details section is a series of buttons/links. The types and styles will change depending on if and who is logged in as. 
- Two icons visible to all are the review icon (pencil) and the like icon (heart)
- Selecting the review icon will take you to the write a review form for this particular property, or if not logged in it will prompt you to login/register
- The heart will 'like' the property increasing the count by 1. If not logged in you will not be able to press this button.
- The other two buttons will only be visible if you are logged in as the owner of the property. These buttons are the edit and delete buttons.
- The edit button will take you to the same form as the 'add-property' form but with the information already filled in.
- The delete button will take you to a confirmation page. This provides an aspect of defensive programming which can be found across the entire site. Upon confirming deletion the property and any associated reviews will be removed from the database and website.

- Below the property image is the ratings a reviews section.
- On medium and large screen sizes the ratings card can be found directly below and to the left of the property info section, on smaller screen sizes this card is omitted. 
- The ratings section provides a breakdown of how the average rating used above is calculated. It shows the average score of 5 categories in which users can rate the property when submitting their reviews. 
- The reviews card is broken up into individual reviews, which follow the same format for all screen sizes. 
- Each review displays the username of the user that left the review, the overall score given in the review, the content of the review and the dates the reviewer lived there. 
- In addition, there are two CRUD functionality buttons, similar to those in the property info above. Only the user who wrote the review can see these buttons. 
- The edit review button, brings the user back to the add-review page with the info already filled in.
- The delete review button takes you to a confirmation page as before. 

- Finally medium and large screen sizes have a location card on the property detail page. This card is currently blank as the user story was given a MoSoCoW ranking of 'Could Have' and was not completed in this iteration. This story will be placed back into the backlog and re-prioritised in subsequent releases. It was decided the location card was going to be created to avoid design and layout issues in future. 

![Layout for large screens](media/images/layout-for-lg-screens.png)
![Layout for small sreens](media/images/layout-for-sm-screens.png)

#### Add Property Page

- If the user is logged in as a Landlord or Estate Agent they will have access to the add property page. This can be accessed by the plus icon found in their navbar.
- This page brings up a form asking for the property details along with requesting an image. The user will also have an option to set the property as not published which will hide it from view.
- Once submitted the form will create a new entry in the Property table in the database and will then render a new page that can be accessed by all users.
- Logged in users can then leave reviews and like the property. 
- The edit property page renders the same form with the fields automatically populated. 

![Add property form](media/images/add-property-form.png)

#### Add Review Page

- The add review page can be accessed by all users logged in.
- There are two ways to access the page. Users can either navigate to the property detail page of the property they wish to review and press the review (pencil) icon, or they can click the small review icon in the navbar where they will be prompted to search for the property using the address information. 
- Both routes render the same page, which is a form requesting information about your review. The property information you are reviewing is displayed on the form to avoid confusion with rentals. 
- Upon submission, the form will create a new entry in the Review table in the database and the review will be shown on the property detail page, in the reviews section. 
- Again there are edit and delete buttons that work in the same way as for the edit/delete the property. 

![Add review form](media/images/add-review-form.png)


#### Register and login Page

- The register user and login pages render simple forms which can be accessed from the navbar for users that are not logged in.
- The pages can easily be navigated between the two in case the user presses the wrong link.
- Upon completion of the form the user will have successfully created/logged in to provide access to permission required pages, such as add-review and add-property.
- The registration form is the same for both Tenants and Landlords/Estate Agents, with the role being selected on the form. 

![Registration form](media/images/registration-form.png)


#### User Profile Page

- Once registered/logged in the user will have access to a profile page
- This page shows the user's personal information followed by any properties or reviews they have posted
- In addition, there is an edit profile form, where the user can change any personal information. 
- If they wish to change their password they are taken to the secure built-in Change Password Form Django provides. 
- There is a delete user button on the right of this page. Again this takes you to a confirmation page as a form of defensive programming.
- Should the user delete their profile any properties or reviews they have left will also be deleted. In the event of properties, this will also delete any associated reviews left by over users.
- It is hence advised that Landlords/Estate Agents who no longer wish to use the site contact the administrator and their account can be made inactive. 

![User profile](media/images/user-profile.png)

#### Search Page

- If users wish to use the search function on the homepage they can do so by inputting address information and clicking the search icon or pressing Enter
- Additionally users who click to leave a review using the icon in the nav bar are brought to the search bar which works in the same way.
- Both search bars bring you to two separate identical pages.
- The pages list all the properties, with useful information, that matched your search criteria. 
- Each property card is a link which will take you to either the property detail page of the add review form. 
- Although the search bar says 'Postcode' it will accept any or all of the address fields, however, it is character sensitive so a rogue space at the end will throw the function off. 

![Search results](media/images/search-results.png)


### Future Features to Implement

- In addition to the features not brought across from the backlog to this iteration and those not completed in this iteration some additional features/fixes were identified that could be implemented in the future.

- Key features still in the backlog that could be allocated as Must-Haves in the next iteration are as follows:
    - The ability to like a review
    - Improve the profile page including adding a picture. This could then be shown as part of the review in addition to the username.
    - As part of improving the profile page the property and review lists could be linked to bringing the user to the relevant item. There could also be an edit and delete button available so the user has a central location where they can perform admin tasks for their profile. 
    - The integration of the map feature should be at the forefront of the next iteration. It could be a static map indicating the location of the property or it could be an interactive map highlighting all property locations stored on RatemyRoom
    - An additional card could be added on the property detail page highlighting properties with similar details or locations.
- Some less important user stories that could be integrated if the time allowed are:
    -  Approve reviews/comments
    - Direct messaging between users
    - Followers and the ability to follow other users
    - A recent activity section/ability to save a property of interest.


***

## Technologies

### Languages
- The project was written using the Django Framework in Python 3.8.11
- The Database used was PostgreSQL hosted on Heroku
- The Front End Design was written in HTML5 and styled mainly using the Bootstrap 5 framework.
- CSS3 and Javascript (containing JQuery) files were added for customisation and functionality.
- Front End page logic and rendering were completed using the Django Template tags within the HTML files

### Tools    
- Gitpod was used as an online IDE
- Github was used as the repository for the source code
- Heroku was used as the platform to run the deployed app
- Stripe was used as the online payment software
- Amazon AWS was used to host the media and static files
- The PEP8 pylint checker was used to check the Python code for errors
- W3C validator was used to check the HTML code for errors
- Jigsaw was used to check the CSS code for errors
- JSHint was used to check the Javascript code for errors


## Testing

### Overview

Testing will be performed on the functionality of the app. This is the key aspect of the application. Secondary to this are the front-end design and strong UX. Testing of Django built-in features is not needed as the framework tests these for us and provides its own validation tools.  

Testing will look for the following:

- The views, URLs and models work as expected rendering the correct pages with no broken links
- All inputs are checked and validated to ensure the user does not input invalid data types. Errors will be raised and an opportunity to try again will be allowed following invalid data entry.
- Users cannot access pages/areas of the website they do not have permissions for. If they come across a page outside of their authorisation an error message will be thrown.
- Responsive design works throughout maintaining readability and ease of use with no unexpected changes/overlaps
- All code will be passed through an acceptable validator for the language. 

### Validator Testing

- Python
    - A Pylint checker was installed onto Gitpod and all python files were opened, checked and minor issues resolved. 

- HTML
    - The official W3C online syntax checker came back with 3 errors across all pages to be fixed. They were all to do with unclosed elements, and were fixed accordingly. Other issues raised were due to the implementation of Django Template Tags clashing with the rules of the checker.

- CSS
    - The official Jigsaw online syntax checker came back with no issues.

- Javascript 
    - The official JSHint online syntax checker came back with no issues. 


### Issues/Bugs resolved during development 

- During initial setup, the django app was crashing when logging in as super user or submitting forms, throwing an error:
  - > Forbidden (403) CSRF verification failed. Request aborted. 

  This was fixed by adding the following code to settings.py:
  - > CSRF_TRUSTED_ORIGINS=['https://*.8000-tdawes93-myway-i3ih4wshlts.ws-us63.gitpod.io']

  However this was only a temporary fix as the url kept changing everytime a session ended causing the bug to return. Eventually I decided to downgrade to django to 3.2 as CSRF_TRUSTED_ORIGINS is not a required variable in that version of django.

- After adding the increment/decrement quantity buttons on my tour quantity input, using the code taken from CI, I found they didn't work as each tour has a different max quantity. I therefore could not use preset numbers. This was solved by passing through disable buttons at min/max function with an additional parameter, tour_max_num_of_guests, on click of each  button. This parameter was then used as the max number in the logic. Due to this extra parameter, the current value variable was not calculated before the buttons were pressed so the min and max num logic had to be altered slightly.

- Upon adding Bootstrap toasts they did not show up when called. As I had used Bootstrap version5 I needed to ensure all data-attributes were data-bs-attribute. Unfortunately this didn't resolve the bug. I found that the JQuery needed to be wrapped in a function:
  - > jQuery(document).ready(function($) { // jQuery code goes in here 
    }); 

- At checkout the order items weren't adding to the order as there was an invalid type operation error. This was found to be due to the max number of digits in the total price was being exceeded by the products when added together. This was fixed by increase the number of allowed digits in the model.

- Whilst adding the Stripe webhooks, the logs kept throwing a 400-error bad request. It was solved by putting STRIPE_WH_SECRET in an env.py file and calling from there as opposed to through the gitpod variables

- Static and media files called through src attribute were not loading when deployed to heroku. Using MEDIA_URL and {% static 'url' %} in the first part of the url worked perfectly. 

#### Pre-release testing

Once the site was deployed on heroku, the url was passed around amongst friends and family for user tests. The following issues were found and resolved. 


- After feedback from friends and family testing, I re-added the home button to the top of the navbar for mobile devices for good UX.

- I found that the search bar on mobile devices in landscape overlapped past the bottom of the page's hero image. This was fixed by reducing the top margin on the search bar

- I found that once the tours were filterd by Location, you could not return to the unfiltered state without using the navigation bars, or going to the page homescreen. A simplerefresh/reload link next to search criteria was added. 

- Users not logged in were able to make orders and see their order confirmation on the site, but were not receiving confirmation emails. The webhook logs were not showing any errors. It was eventually found the webhook handler had a typo in an if statement:
  - > if username != 'Anonymouse User:'
  
  This error didn't filter out guest users so therefore the code was failing when trying to find the profile in the following line. 

- Certain users were experiencing duplicate orders on the Greek Island Tour. After playing around with shipping details and postcodes within the checkout views, webhook handler and JavaScript, I managed to get the duplicate order bug to occur on every event. Print statements showed that all order fields prior to saving matched the payment intent fields. As shipping details dictionary was not working with JS, stripe billing address details were being used. The bug was solved by cleaning the billing address data in case of empty fields. 


### Testing User Stories

- Registration and Sign-in:
    - As a site user I can register for an account so I can have a personal account and be able to view my profile
    - As a customer I can login and register using my pre-exsiting facebook/gmail/apple accounts so I can link my emails and accounts into one for a more streamlined service
    - As a site user I can personalise my profile so I can view my personal order history/order confirmations and save my payment information
    - As a site user I can receive an email confirmation after registering so I can verify my account registration was successful
    - As a site user I can recover my password so I can regain access to my account
    - As a site user I can login and logout so I can access my personal/private account information

- Products
  - As a customer I can view a list of products so I can select some to purchase
  - As a customer I can view individual products so I can identify price, description, location and timeframe
  - As a customer I can see a quick view so I can see the details of each tour without navigating away from the page I'm on
  - As a customer I can compare tours side by side so I can compare the details of different tours and decide which is best for me
  - As a customer I can add products to a wish list so I can return to it later and complete my purchase
  - As a customer I can tailor and personalise the trips so I can experience the trip of a life time suited towards me
  - As a customer I can identify packages/deals/group rates so I can take advantages of special savings

- Sorting and Searching
  - As a customer I can sort products by location so I can find the products near where I want to visit
  - As a customer I can sort products by price so I can find the products within my budget
  - As a customer I can sort products by date so I can see trips available during my time off
  - As a customer I can easily see what I've searched for and the number of results so I can quickly decide whether the trip I want is available
  - As a customer I can sort products by multiple categories at once so I can find the best product for me

- Purchasing and Checkout
  - As a customer I can pay online by card so I can order my products easily without having to contact a sales representative
  - As a customer I can receive an email confirmation so I can have a record of my purchases
  - As a customer I can see an order confirmation so I can check I haven't made any mistakes when completing a purchase
  - As a customer I can easily enter my payment information so I can checkout quickly and with no hassle/issues
  - As a customer I can have my personal and payment information safe and secure so I can confidently provide the information needed to make a purchase
  - As a customer I can adjust the dates and number of guests for a trip in the bag so I can make changes just before checkout
  - As a customer I can view the items in my bag so I can identify the total cost of my purchase and details of every trip I am buying
  - As a customer I can easily select the dates and number of guests attending a trip so I can ensure I don't accidentally select the wrong trip or booking information
  - As a customer I can view the total of my purchases at any time so I can avoid spending too much

- Administration and Store Management
  - As a site user I can see messages/notifications when I perform a task so I can be confident that the task has been completed correctly
  - As a site user I can see a clear and interesting homepage so I can understand the meaning of the site and how to make a purchase
  - As a store owner I can create a product so I can keep my e-commerce store up to date
  - As a owner I can edit products so I can change products and keep my store up to date
  - As a owner I can delete products so I can remove products no longer in stock and keep my store up to date
  - As a customer I can view a Facebook page so I can be kept up to date with events and interact with the company
 

***

## Deployment 

### Deploy to Heroku

Please deploy the app to Heroku using the following steps:

1. Log into Heroku and click the 'New' button and then "Create new app" from the drop-down list
2. Name your app (it must be unique) and select the region you are based in
3. Select settings and scroll down to the config vars section
4. Add another config var of PORT (key) 8000 (value) to ensure the mock terminal works.
5. Add your environment variables, including your SECRET_KEY, Stripe keys, Webhook Keys, Email Host Keys and AWS keys.
6. Link your environment variables into a secure file like env.py and add to the gitignore file
7. In the connect to Github section, add the repository name to link the Github.
8. Press deploy to deploy the app to Heroku, you can also opt in to "Enable Automatic Deploys" which updates the Heroku every time a new change is pushed to Github.
9. Upon full deployment ensure Debug is turned to False.

### Fork the GitHub

If you wish to view or make changes without affecting the original repository you can 'fork the repository'. This creates a copy to your GitHub and can be done using the following steps:

1. Log in to Github and locate the [MyWay Repository](https://github.com/tdawes93/MyWay)
2. At the top right of the repository underneath the notification icon is the 'fork' button
3. Click this button and you should now have a copy of the repository in your Github account

### Make a local clone

1. Log in to Github and locate the [MyWay Repository](https://github.com/tdawes93/MyWay)
2. At the top of the repository next to the 'Gitpod' button click the dropdown named 'Code'
3. To clone the repository using HTTPS, make sure HTTPS is selected and copy the link
4. Open the Git Bash
5. Change the working directory to the location you wish the clone to be made
6. Type 'git clone' and paste the copied URL
7. Press 'Enter' and your local clone will be created


***

## Credits

- The Carousel code was taken and adapted from the Bootstrap 5 docs https://getbootstrap.com/docs/5.2/components/carousel/
- The review Teaser JS code was taken and adapted from Robert Mosolgo https://github.com/rmosolgo/bootstrap-teaser