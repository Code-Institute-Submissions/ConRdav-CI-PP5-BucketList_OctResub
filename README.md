# BUCKETLIST
Live deployment for the app here 

# Table of contents
- [Project Overview](#project-overview)
- [Planning](#planning)
    * [Scope](#scope)
        + [Primary Goals](#primary-goal)
    * [Strategy](#strategy)
        + [User Stories](#user-stories)
	* [Marketing](#smarketing)
        + [Business Model](#business-model)
		+ [SEO Implementation](#seo-implementation)
		+ [Marketing Techniques](#marketing-techniques)
    * [Design](#design)
        + [Wireframes](#wireframes)
        + [Colours](#colours)
        + [Fonts](#fonts)
	 * [Structure](#structure)
        + [Website pages](#website-pages)
        + [Code Structure](#code-structure)
        + [Database](#database)
            - [Database diagram](#database-diagram)
            - [Models](#models)
- [Features](#features)
    * [Feature 1 - Navigation Bar and Homepage](#feature-1)
    * [Feature 2 - Welcome text](#feature-2)
    * [Feature 3 - Upcoming Trips](#feature-3)
    * [Feature 4 - Footer](#feature-4)
    * [Feature 5 - Trip Details](#feature-5)
    * [Feature 6 - Trip Registration](#feature-6)
    * [Feature 7 - Past Trips](#feature-7)
    * [Feature 8 - Trip Review](#feature-8)
    * [Feature 9 - Delete Review](#feature-9)
    * [Feature 10 - Edit Review](#feature-10)
    * [Feature 11 - Register](#feature-11)
    * [Feature 12 - Login](#feature-12)
    * [Feature 13 - Logout](#feature-13)
    * [Feature 14 - Admin page](#feature-14)
- [Technologies Used](#technologies-used)
    * [Languages](#languages)
    * [Libraries and other resources](#libraries-and-other-resources)
- [Testing](#testing)
- [Deployment](#deployment)
  * [AWS S3](#aws-s3)
  * [Heroku and Postgres Database](#heroku-and-postgres-database)
- [Credits](#credits)


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

## Credits
- All the prepopulated information for excursions and adventures were copied and modified from travel sites. This were Wanderlust, Lonely Planet, Vacation Ideas, The Culture Trip, Travellers WorldWide, The Crazy Tourist and Trip Advisor.
- All the images used in the advenutre and excursion models were downloaded from google images and I take no credit over them whatsoever.





