# BUCKETLIST
Live deployment for the app here https://ci-pp5-bucketlist.herokuapp.com/

# Project Overview

The main objective of the BucketList E-Commerce website is to provide a user-friendly platform for people to search for an adventure that suits them and to be able to purchase the advenutre securely. The target end user is anyone and everyone who is interested in an adventure, and who has a desire to travel and explore new places.

The e-commerce store has functionality that allows the user to add an adventure into a checkout bag, post testimonials, add adventures to a wishlist to save for later, contact us directly for any enquiries. This access thereby permits the user to interact with the forum platform and take part in discussions. End users are able to: 

	- Add a adventure to the checkout bag.
	- Update their checkout bag.
	- Purchase a product through stripe payment.
	- Create, Read, Update and Delete testimonial posts.
    - Add or remove an adventure from their wishlist.

Additionally, users have access to their profile, which gives them there order history and the ability to save billing information to allow smooth purchases. 

When users decide to create a post, they are prompted to provide a unique title of their choosing, their post content, and an excerpt to contextualise their post.

Once the post has been created, it will published on the forum. Once the post is published, the user will be able to see them on the main post list page. From there the user will be able to edit and delete their posts.

BucketList is a Django framework app. The user's post data is stored in a database with PostgreSql, and the app is hosted on Heroku. The Django administration site was utilised to provide admin control in order to monitor forum content, as well as super user control of CRUD operations - including the ability to delete other users’ posts and comments.

Below is the link to the live website:


# Planning
## Scope
### Main Goals
The primary goals of the website admins are:
- To add, edit and delete adventures with all the relevant information, per the model.
- To be able to view orders and reviews in the admin panel.
- To be able to see and manage user reviews.

The primary goals of the website users are: 
- To register for an account on the website. 
- To sign in and sign out of the website. 
- To View a list of all adventures.
- To view adventure details.
- To purchase adventures for multiple persons.
- To post testimonials on past adventures they have been to, and be able to edit or delete it.
- To see their order history in their profile page.

## Strategy
### User Stories
The user stories were broken down into epics first which include technical, landing page, adventures, marketing, basket, checkout, testimonials and user profiles.
These were then broken down into 5 sprints where in each sprint covered 5 days and different user stories.
Each user story is broken down into their descrition and the acceptance criteria that needed to met for it to have been achieved.
The user stories for this project can be viewed [here]()

## Marketing
### Search Engine Optimization (SEO)
SEO is used as a tool for improving the quality and quantity of website traffic to the website targeting unpaid traffic rather than direct traffic or paid traffic.
WordTracker.com and Google Keyword Tracker were the tools used to help implenting this. The keywords were inputted into these tools to gather the results for which keywords returned the highest traffic and lowest competition ideally.
Throughout the website SEO tools are implented to increase the traffic to the website.
### Marketing Techniques
A facebook page was created to increase the websites exposure online and imporve traffic to the website. This would allow users to follow the website on social media and gives an unpaid solution to improve marketing.
In addition the website includes a newsletter sign up for for users to keep updated with deals, and new adventure locations.
Chimp mail was used for this popup.
A mockup facebook page can be seen here ![Facebook Page](assets/images/facebook_page.png)
### Business Model
With the BucketList project, the goal was to create a Minimum Viable Product (MVP) for a Tourism e-commerce site, operating on a Business to Consumer (B2C) business model, whereby we are selling a product directly to customers and thereby bypassing any third-party retailers and wholesalers.

#### Target Audience 

At its core, BucketList serves as a platform for anyone and everyone seeking an exotic escape, challenging adventure, or cultural tour, to find a trip that appeals to their desires and fulfils their dreams. The adventures on offer are those which would appear on any explorer’s bucket list, hence the name. 

Being a tourism e-commerce business, the target audience for BucketList is broad. However, as the idea is to specialise in once-in-a-lifetime, curated adventures to far-flung destinations, this creates a niche for those that can afford to embark on such excursions (in terms of time and money). The target audience, therefore, most likely falls into the following categories: 

People embarking on Gap Year adventures
People seeking adventures on their sabbatical
People who have retired and want to make the most of their new found freedom

The target audience is not limited to these groups, but these are the demographics who are most likely to have the time and money to be able to seek the adventures BucketList will have on offer.

#### Business Demand 

Tourism is a global industry with year-round demand. 

With the recent global lockdowns, and the severe impact this has had on the tourism industry, now that borders are open and travel is permitted, there is a massive demand for going on once-in-a-lifetime adventures. The goal with BucketList is to create an easy-to-use, hassle-free platform for customers to find curated adventures and book them, removing the stress that is typically involved in planning holidays. With this in mind, there is a particular emphasis on considered User Experience (UX), enabling clear navigation, profile management, content layout, and stress-free payment solutions.

#### Future Features

Looking forwards, with the BucketList application, there are plenty of avenues to expand on the offerings of the MVP. In future iterations and versions, I envision implementing the following additional features:

- Wish List / Bucket List - whereby a customer can maintain a list of their favourite destinations and adventures.
- Custom Adventures - whereby a customer can customise their adventure within the parameters of pre-defined options.

#### Partnerships

BucketList, as a business, will involve partnerships with tourism professionals in the destination countries, including local guides and operators.

Furthermore, there is demand to expand into the arena of Eco-Tourism, involving partnerships with charity missions abroad - further catering to the target demographics, and offering another facet of fulfilment.

#### Monetisation

The core principle of the BucketList e-commerce site is to offer a B2C business model, through the vessel of selling tourism adventures to customers. This involves making profits on the goods and services offered.

However, given the fact that BucketList is an e-commerce site, there is also the option to venture into monetising advertisement on the website, whereby driving traffic through to the sites of its advertising partners will generate additional income for the business.

## Design 
### Wireframes
Balsamiq was used to produce the wireframes of the website after the user stories and marketing techniques had been researched.
### Fonts
### Colours


## Structure 
### Wesbite Pages
#### Index page non user/admin
This is the index page the first page users get to when the website is loaded up.
![index page](assets/images/index_page.png)
#### Index page signed in as admin
When signed in as the admin you can see an admin dropdown menu to deal with product management.
![admin index page](assets/images/admin_index.png)
#### Adventures
This shows all the adventures unfiltered.
![adventures page](assets/images/adventures.png)
This is the advenutres page with a filter on it.
![adventures filtered page](assets/images/adventures_filtered.png)
This is the adventures detail page with a link to view the specific excursion for the adventure.
![detail](assets/images/adventure_detail.png)
![excursion](assets/images/excursions.png)
#### Authorisaton
This shows the authorisation pages needed for users to register and sign in and sign out.
![sign up](assets/images/sign_up.png)
![sign in](assets/images/sign_in.png)
![log out](assets/images/sign_in.png)
After that they can access their profile page where they can prefill billing information and order history.
![profile](assets/images/profile.png)
#### Admin 
The admin can add adventures and excursion.
![add adventures](assets/images/add_adventure.png)
![add excursion](assets/images/add_excursion.png)
The admin can view contact enquiries in the front end through their admin dropdown on the navigation bar.
![enquiries](assets/images/user_enquiries.png)
#### Users
Users can submit contact forms and add testimonials that they can view on the testimonials page.]
![contact](assets/images/contact.png)
![contact success](assets/images/contact_success.png)
![add testimonial](assets/images/add_testimonial.png)
![testimonials](assets/images/testimonials.png)






### Database
### Code Structure
## Database diagrams 

## Testing
### Manual Testing
To get the most coverage for this project a 5 stage manual testing approach was used. Automated testing wasn't being used at all.
#### 1. Unit Testing
#### 2. Integration Testing
#### 3. System Testing
#### 4. UI Testing 
#### 5. Acceptance Testing




## Testing

### Automated Testing
I used Django to run automated testing however, sqlite3 was used as a local database to achieve this testing.

* I used Django TestCase to test my forms.py, urls.py and views.py within test_forms.py, test_urls.py and test_views.py.

#### test_forms.py
![testing forms.py](assets/images/test_forms.png)

#### test_urls.py
![testing urls.py](assets/images/test_urls.png)

#### test_views.py
![testing views.py](assets/images/test_views.png)

![Test result](assets/images/test_result.png)

* I attempted to test models.py but didn't have a great understanding of what to test for so decided to continue with manual testing for the rest of my application in order to verify quality and usability from the user's perspective.

#### Django Coverage report
![Coverage report](assets/images/coverage_report.png)
* Using Django Coverage I realised that I hadn't covered enough testing with Django TestCase so manual testing was the next step to cover more testing.


* Post Model blog posts were ordered by creation date, the blog title is returned and that the like count is returned. 

* Comment model comments being ordered by creation date, and commenter name was returned along with the comment. 

* For the Author Profile model the user, the bio and location is returned.

* The paths from url.py that I didn't cover in my automated tested which were users_post, edit_post and delete_post, user_profile and user_profile edit are all working.

* If the user isn't logged in they can't create,edit or delete a post and the user can't comment or like a post. The user can view a post and signup or login.![Unregistered User](assets/images/index_page.png) ![Unregistered User](assets/images/view_post_non_user.png) ![Unregistered User](assets/images/sign_up.png) ![Unregistered User](assets/images/sign_in.png)

* Logged in users can create, edit and delete their posts. Can comment and like on posts aswell as the ability to sign out.
![Logged in user](assets/images/index_page_user.png) ![Logged in user](assets/images/user_posts.png) ![Logged in user](assets/images/create_post.png) ![Logged in user](assets/images/edit_post.png) ![Logged in user](assets/images/logout.png) 

* Django Admin user can create, edit and delete posts from the Django admin panel, and can approve posts and comments from there too. This gives the admin the ability to moderate the posts on the blog.
![Django Admin](assets/images/admin_index.png) ![Django Admin](assets/images/admin_comments.png) ![Django Admin](assets/images/admin_posts.png) ![Django Admin](assets/images/admin_add_post.png) ![Django Admin](assets/images/admin_add_comment.png) 

### Pep8 and Pylint Python Validators
* admin.py
![admin.py](assets/images/admin_py.png) 
* apps.py
![apps.py](assets/images/app_py.png) 
* forms.py 
![forms.py](assets/images/forms.png) 
* models.py 
![models.py](assets/images/models_py.png) 
* urls.py
![urls.py](assets/images/blog_url.png) 
* views.py 
![views.py](assets/images/views.png) 
* test_forms.py
![test_forms.py](assets/images/test_forms_pep8.png)
* test_urls.py 
![test_urls.py](assets/images/test_urls_pep8.png)
* test_views.py 
![test_views.py](assets/images/test_views_pep8.png)

### HTML Validation with Official W3C Validator
## base.html
* Offical W3C Validator picked up errors for using {{ }} and {% %} syntax, this are used for Django functionality
## index.html
* Offical W3C Validator picked up errors for using {{ }} and {% %} syntax, this are used for Django functionality
## about.html
* Offical W3C Validator picked up errors for using {{ }} and {% %} syntax, this are used for Django functionality
## add_adventure.html
* Offical W3C Validator picked up errors for using {{ }} and {% %} syntax, this are used for Django functionality
## add_excursion.html
* Offical W3C Validator picked up errors for using {{ }} and {% %} syntax, this are used for Django functionality
## adventure_detail.html
* Offical W3C Validator picked up errors for using {{ }} and {% %} syntax, this are used for Django functionality
## adventures.html
* Offical W3C Validator picked up errors for using {{ }} and {% %} syntax, this are used for Django functionality
## edit_adventures.html
* Offical W3C Validator picked up errors for using {{ }} and {% %} syntax, this are used for Django functionality
## excursion_detail.html
* Offical W3C Validator picked up errors for using {{ }} and {% %} syntax, this are used for Django functionality
## bag.html
* Offical W3C Validator picked up errors for using {{ }} and {% %} syntax, this are used for Django functionality
## checkout_success.html
* Offical W3C Validator picked up errors for using {{ }} and {% %} syntax, this are used for Django functionality
## checkout.html
* Offical W3C Validator picked up errors for using {{ }} and {% %} syntax, this are used for Django functionality
## contact.html
* Offical W3C Validator picked up errors for using {{ }} and {% %} syntax, this are used for Django functionality
## profile.html
* Offical W3C Validator picked up errors for using {{ }} and {% %} syntax, this are used for Django functionality
## add_testimonial.html
* Offical W3C Validator picked up errors for using {{ }} and {% %} syntax, this are used for Django functionality
## testimonials.html
* Offical W3C Validator picked up errors for using {{ }} and {% %} syntax, this are used for Django functionality
## django-all_auth's login.html edited for uniformity
* Offical W3C Validator picked up errors for using {{ }} and {% %} syntax, this are used for Django functionality
## django-all_auth's logout.html edited for uniformity
* Offical W3C Validator picked up errors for using {{ }} and {% %} syntax, this are used for Django functionality
## django-all_auth's signup.html edited for uniformity
* Offical W3C Validator picked up errors for using {{ }} and {% %} syntax, this are used for Django functionality

### CSS Validation with Official W3C Validator
![CSSVALIDATION](assets/images/css_validation.png)

## LightHouse testing
![lighthouse1]()

![lighthouse2]()

![lighthouse3]()

![lighthouse4]()

![lighthouse5]()

## Responsive testing
This app has been tested on mobile and tablet devices and is responsive.
![mobile1]()

![mobile2]()

![mobile3]()

![mobile4]()

![mobile5]()




## Models
### User
- The User model contains information about each user that registers
- It is part of the Django allauth library
- The following fields are used for this project: username, email, password

#### Adventures
- The Adventure model is the main model
- Only Admins can create Adventure objects, but all users can interact with them
- The model contains the following fields: 

#### Testimonials
- Used by users to review Adventure objects, thus has a ForeignKey relationship with both Adventure and User

#### Contact 
- Used by users for any queries related to the website.
- Admins have the function to approve the request


## Deployment

Deployment procedure (using Heroku):

1. First, after logging in to the Heroku dashboard, navigate to ‘Create New App’.
2. Give your project a unique name and choose an appropriate region, before creating your app.
3. Navigate to the Resources tab. Using the Add Ons section, add ‘Heroku Postgres’ as the app’s database.
4. Create an env.py file in your root directory and import the os library within this file.
5. Within your env.py file, create environment variables for your DATABASE_URL and SECRET_KEY. They should appear as follows:

	__*os.environ[“DATABASE_URL”] = “___”__

	__*os.environ[“SECRET_KEY”] = “___”__

6. Assign a value to your DATABASE_URL and SECRET_KEY and within the Heroku settings tab, create corresponding Config Variables.
7. In your settings.py file, assign your Heroku app as a localhost in your ALLOWED_HOSTS variable, using the appropriate format:

	__app_name.herokuapp.com__

8. After updating all of the necessary environment and configuration variables in the settings.py and env.py files, create a new file at the top level directory called ‘Procfile’. 
9. Within Procfile, add the following code:


	__web: guincorn PROJECT_NAME.wsgi__

10. Using the Command Line interface: add, commit and push your files. 
11. Finally, navigate to the Deployment tab in Heroku and deploy your branch manually, observing the build logs for errors.
12. Heroku will build the app for you. If the build is successful, Heroku will provide a link to your live app.

13. To store static and media files Amazon Web Services simple cloud storage was used. After an account is created and your search for s3 cloud storage the set up is simple and involves you adding your heroku deployed url.
### Django AdminUser
For this project the built in Django admin page is where the admin approves posts and comments so that they can be viewed on the post list.



## Used Technologies
* HTML
* CSS
* Python
* JavaScript
* ChimpMail
* AWS S3

## Frameworks and Libraries used
* Django with;
    * gunicorn
    * psycopg2
    * postgresql
    * AllAuth
    * Crispy Forms
    * colorfield
* Bootstrap

## Credits
- All the prepopulated information for excursions and adventures were copied and modified from travel sites. This were Wanderlust, Lonely Planet, Vacation Ideas, The Culture Trip, Travellers WorldWide, The Crazy Tourist and Trip Advisor.
- All the images used in the advenutre and excursion models were downloaded from google images and I take no credit over them whatsoever.





