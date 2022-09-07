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
  * [Local Deployment](#local-deployment)
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
This websites business model is Business to Consumer (B2C) as we are selling a product directly to customers and thereby bypassing any third-party retailers and wholesalers.

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





