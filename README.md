# OVERVIEW

This template was made as a guide to ensure you cover assessment criteria in your fourth portfolio write up. It is specific to the **PORTFOLIO 5: Full-Stack Toolkit** project.

## Helpful tools

### Screenshots and Videos
**Here’s a great video on how to add videos to your readme! no need to convert to gifs!!**

https://www.youtube.com/watch?v=G3Cytlicv8Y

> 1. record a video via slack
> 2. download it
> 3. in github, edit your readme via the pencil icon
> 4. type a place holder word and highlight it
> 5. drag and drop mp4 file over that text
> 6. scroll down to the commit area
> 7. update the default commit message
> 8. click the green button
> 9. ```git pull``` changes to your gitpod workspace

**You can do the steps 3-9 for the image/screenshot uploads too!**

### Cheatsheets and Auto Generation Tools

Markdown's not all that easy so sometimes you may want to use some tools to make tables.

- [Markdown Cheatsheet](https://guides.github.com/features/mastering-markdown/)
- [markdown table generator](https://www.tablesgenerator.com/markdown_tables) - used to help with documentation table formatting
- [markdown table of contents generator](https://ecotrust-canada.github.io/markdown-toc/) - used to create table of contents (be weary it does have some bugs if you have dashes or trailing spaces in your headers)
- [readme.so](https://readme.so/) - if you don't want to learn markdown, this tool might help you

# Table of Contents
Copy your readme to http://ecotrust-canada.github.io/markdown-toc/ to make a table of contents.  This will help assessors to see the structure of your readme. Just test it out ast this tool isn't perfect. It tends to mess up with special characters like dashes.

- [PROJECT_NAME](#project_name)
  - [Author](#author)
  - [Project Overview](#project-overview)
- [UX](#ux)
  - [Target Audience](#target-audience)
  - [Goals](#goals)
  - [User Stories](#user-stories)
  - [Initial Stories](#initial-stories)
  - [Feasibility vs Importance](#feasibility-vs-importance)
  - [Scope](#scope)
  - [Design Choices](#design-choices)
  - [Wireframes](#wireframes)
- [Information Architecture](#information-architecture)
  - [Entity Relationship Diagram](#entity-relationship-diagram)
  - [Database Choice](#database-choice)
  - [Data Models](#data-models)
- [Agile Process](#agile-process)
  - [GitHub User Stories](#github-user-stories)
  - [Iterations](#iterations)
  - [Progress Boards](#progress-boards)
- [Features](#features)
  - [Implemented Features](#implemented-features)
  - [Future Features](#future-features)
- [Testing](#testing)
  - [Cross Browser and Cross Device Testing](#cross-browser-and-cross-device-testing)
  - [Accessibility Testing](#accessibility-testing)
  - [Validation Testing](#validation-testing)
  - [Automated Testing](#automated-testing)
  - [Defects](#defects)
  - [Defects of Note](#defects-of-note)
- [E-commerce Business Model](#e-commerce-business-model)
  - [Facebook Business Page](#facebook-business-page)
  - [Newsletter Signup](#newsletter-signup)
  - [Links](#links)
  - [SEO Strategy](#seo-strategy)
- [Deployment](#deployment)
  - [Prerequisits](#prerequisits)
  - [Fork and Clone the Repository](#fork-and-clone-the-repository)
  - [Development Deployment](#development-deployment)
  - [Production Deployment](#production-deployment)
- [Credits](#credits)
  - [Content](#content)
  - [Media](#media)
  - [Acknowledgments](#acknowledgments)

====================================== The Sections you Fill in are below ==============================


# Test a Wheel - used cars pre-purchase inspections
![TaW Devices](https://github.com/PPindel/test-a-wheel/assets/114284732/3ed8ead6-c375-4969-b875-4e3107dffb92)


## Author
Przemyslaw Pindel


## Project Overview

- [Test a Wheel](https://test-a-wheel-8a5bbb245942.herokuapp.com/) - Link to deployed website
- [Test a Wheel GitHub repo](https://github.com/PPindel/test-a-wheel) - link to GitHub

# UX
## Target Audience & Goals
- Test a Wheel is a perfect solution for people who are looking to buy a used car, but have no idea how to approach it in the right way. Our specialists are available seven days a week to help you with the inspection of the car. There are a few packets of services to choose from. Depending on the price, we will provide you with a comprehensive report of the car and even protect your bought with the extra warranty.
- In today's world, a lot of us need a car, but not everyone can afford a brand-new car. Secondhand market is a great idea to save some money if you choose the right car to buy. Taught by the experience, I know it's not an easy thing and can be very stressful for some people (a good friend of mine is a great example here). And that's where Test a Wheel comes to help You! Don't risk buying a crap car, entrust the inspection to professionals, and sleep well. There is nothing more important than your health, and peace of mind. With Test a Wheel buying a used car was never easier!
- Test a Wheel is a site offering professional used car inspections
- Was created for people who don't really know how to approach the buying of a used car
- Also contains a blog section with interesting and educational articles
- People can share their experiences in the review section
- Simple and easy navigation! The process of buying the service is super-easy so people will come back, and recommend our site to friends!
- Never miss any promo, thanks to the subscribe option!


## Initial Stories
(MOST IMPORTANT USER STORIES SO THE SITE CAN OPERATE)

USER:
- can register
- can create a profile
- can buy services
- can view order history
- can review orders

ADMIN:
- can add a service
- can edit the service
- can delete the service
- can add blog posts
- can edit the blog posts
- can delete the blog posts


## User Stories
All CRUD functionalities have been implemented!

![image](https://github.com/PPindel/test-a-wheel/assets/114284732/b8dcead7-e3a9-4765-af97-7f9a7677865e)

![image](https://github.com/PPindel/test-a-wheel/assets/114284732/c3d5e3d9-5d9d-41ba-a899-858a62529842)

![image](https://github.com/PPindel/test-a-wheel/assets/114284732/bc885f22-a0c7-4c48-b94e-c0effc45ee08)

![image](https://github.com/PPindel/test-a-wheel/assets/114284732/6e06a5c7-fccd-4648-89e3-2ce0ca848c00)

![image](https://github.com/PPindel/test-a-wheel/assets/114284732/af69cf32-0138-4ad2-84bf-af9d638eb6e8)

![image](https://github.com/PPindel/test-a-wheel/assets/114284732/5121a811-7477-41d2-b502-5cbecf815620)

![image](https://github.com/PPindel/test-a-wheel/assets/114284732/e5afaea9-b806-404b-927e-b00a16c30668)

![image](https://github.com/PPindel/test-a-wheel/assets/114284732/329afd40-9ea5-484d-b4bb-6072c947cf08)

![image](https://github.com/PPindel/test-a-wheel/assets/114284732/ce54adf0-6787-438b-afa3-0d293bba0551)

![image](https://github.com/PPindel/test-a-wheel/assets/114284732/ef6f8383-ea95-4d66-a653-84caca9d3dce)

![image](https://github.com/PPindel/test-a-wheel/assets/114284732/05fb6871-5133-4e6a-8bb8-31a8d75d572d)

![image](https://github.com/PPindel/test-a-wheel/assets/114284732/b8456e6e-947a-468c-8cfb-38f0ad2a3183)

![image](https://github.com/PPindel/test-a-wheel/assets/114284732/6949cbaa-e0ca-43fe-94a9-88cdead51c56)

![image](https://github.com/PPindel/test-a-wheel/assets/114284732/82125e67-6b2a-461e-807f-44fa149584e0)

![image](https://github.com/PPindel/test-a-wheel/assets/114284732/3c6d622f-e31a-4cfa-add1-819031cdfadd)

![image](https://github.com/PPindel/test-a-wheel/assets/114284732/9b11766e-e702-42e2-89d0-80cf9d1dede8)

![image](https://github.com/PPindel/test-a-wheel/assets/114284732/7ca031c6-cd26-4665-b826-fb70cf12697d)

![image](https://github.com/PPindel/test-a-wheel/assets/114284732/9ce4ae4c-eaf5-499a-ae10-dc72c104cd0f)

![image](https://github.com/PPindel/test-a-wheel/assets/114284732/165b7a96-d0cd-4da4-aaff-1aef12061f98)

![image](https://github.com/PPindel/test-a-wheel/assets/114284732/ad20dd6d-5fc4-4457-b7df-c1aad8ab61a1)

![image](https://github.com/PPindel/test-a-wheel/assets/114284732/0d1de49b-bf54-4c35-bbf8-53226c9c654d)

![image](https://github.com/PPindel/test-a-wheel/assets/114284732/0b833e38-679d-4226-b322-09552ed9fa9c)


## Feasibility vs Importance
GitHub labels were used to reflect the importance of the feature, e.g.:

![image](https://github.com/PPindel/test-a-wheel/assets/114284732/5bd0073f-a728-4432-9271-70c175f8d1b2)

[Click here for the full project](https://github.com/users/PPindel/projects/5)

## Design Choices
### Colors
Easy to read, clean, and neat, high-contrast colors were picked for this project:

![image](https://github.com/PPindel/test-a-wheel/assets/114284732/a30886a8-8e99-4d80-8f7e-84304e74bc5c)

### Typography
Fonts: Montserrat & Roboto to reflect the nature of the website

### Images
All images in the index, blog, and services were chosen to match the car-themed content of the website.

### Design Elements

> - desktop navigation
> - mobile navigation
> - footer
> - containers/cards
> - buttons
> - text input
> - textarea inputs
> - dropdowns
> - checkboxes
> - pagination
> - date pickers
> - maps
> - images
> - icons
> - file pickers

### Animations and Transitions
- Simple animation for social buttons:

  ![image](https://github.com/PPindel/test-a-wheel/assets/114284732/d0a653ce-26ff-4911-90a0-9f4605997f20)
  ![image](https://github.com/PPindel/test-a-wheel/assets/114284732/f90fa772-8580-4d54-9bee-cc4fdb3fc2c0)

- Theme-matched menu icon for mobile version:

  ![image](https://github.com/PPindel/test-a-wheel/assets/114284732/8df0d970-9260-4109-ab91-a5723fb18152)

- Hyperlinks change colors when hovered
- Customized rotating cog after purchase
- Animated FAQ

### Frameworks, plugins, and tools used

- Django
- Bootstrap
- req.txt:
  - asgiref==3.7.2
  - boto3==1.27.1
  - botocore==1.30.1
  - dj-database-url==0.5.0
  - Django==3.2.19
  - django-allauth==0.41.0
  - django-braces==1.15.0
  - django-countries==7.2.1
  - django-crispy-forms==1.14.0
  - django-model-utils==4.3.1
  - django-storages==1.13.2
  - django-summernote==0.8.20.0
  - gunicorn==20.1.0
  - jmespath==1.0.1
  - oauthlib==3.2.2
  - Pillow==9.5.0
  - psycopg2==2.9.6
  - python3-openid==3.2.0
  - pytz==2023.3
  - requests-oauthlib==1.3.1
  - s3transfer==0.6.1
  - sqlparse==0.4.4
  - stripe==5.4.0
  - swapper==1.3.0
  - urllib3==1.26.16


### Custom Styles
- Lots of styles were overwritten in this project: [CSS file](https://github.com/PPindel/test-a-wheel/blob/main/static/css/base.css)
- Visual stars implemented:

  ![image](https://github.com/PPindel/test-a-wheel/assets/114284732/2bdb76f0-d3a9-456f-ad32-5fbc8dd780e9)


### Custom Javascript
Modified script for Toasts to hide messages after 5 seconds:

![image](https://github.com/PPindel/test-a-wheel/assets/114284732/7b748748-8771-424a-a1ed-77886f216486)

## Wireframes
Index:

![image](https://github.com/PPindel/test-a-wheel/assets/114284732/c45fdb91-1e9d-4495-ad9e-f08de3ce8caf)

About (the final site was changed, but I'm presenting everything I had in my mind at the beginning of the project):

![image](https://github.com/PPindel/test-a-wheel/assets/114284732/db0a8fd4-60ba-44b7-8184-751b9beb1360)

Services:

![image](https://github.com/PPindel/test-a-wheel/assets/114284732/c1dbdb2a-a0c2-4cb7-8faf-47d96c95399f)

Car Blog:

![image](https://github.com/PPindel/test-a-wheel/assets/114284732/c22cd5c8-c8f2-48f6-890b-30ec57fc4365)

Reviews:

![image](https://github.com/PPindel/test-a-wheel/assets/114284732/384e5e6e-fe9a-44a8-9ca6-9bc27bfb6642)

Contact:

![image](https://github.com/PPindel/test-a-wheel/assets/114284732/438d92a8-e46e-48bb-9fdd-11fdd505e095)

FAQ:

![image](https://github.com/PPindel/test-a-wheel/assets/114284732/1d399b64-aebf-425b-8ba5-83473f7cb6cb)

Mobile index:

![image](https://github.com/PPindel/test-a-wheel/assets/114284732/daf4260a-c9d7-463d-a443-3a3b27de660a)

Mobile services (blog and review pages are analogical):

![image](https://github.com/PPindel/test-a-wheel/assets/114284732/4d12bdd2-0c41-4926-8912-9afaf9f59cb2)


# Information Architecture

## Entity Relationship Diagram

![test-a-wheel-graph](https://github.com/PPindel/test-a-wheel/assets/114284732/ff88022d-d17f-4c27-813a-e2a81fb716e4)


## Database Choice

- Postgres as the database because the data is relational
- Heroku servers

## Data Models

Admins can create, read, edit, and delete services in the store.
Admins can create, read, edit, and delete posts in the blog section.
Registered users can interact with the blog posts by adding likes.
Registered users (customers) can create, read, edit, and delete their own Reviews of every purchase made (Order number is a unique value for each review).
Every registered user has access to a personal profile, which can be read and edited.
Every purchase made is saved and can be accessed via the profile page if the user is registered.

## Products
Products (services) are what is the main focus of the e-commerce website. Admins can add, edit, and delete the service, select the customized options, add related image, and descriptions.

### CRUD
- **Create:** If the user is an authenticated superuser, they can add a new product by clicking the profile icon in the top right corner and selecting Add product
- **Read:** All users can view the current products in the services section
- **Update:** Only admins can edit the existing product
- **Delete:** Only admins can delete the existing product

## Reviews
Registered users can review every order made. The option "Review me!" is added to the order history accessible via the profile page.

### CRUD
- **Create:** After the order is paid, the registered user can add a review
- **Read:** All users can view the current reviews in the customer ratings section
- **Update:** Only the author of the review can edit the review via frontend
- **Delete:** Only the author of the review can delete the review via frontend

## Post
Admins (superusers) can add posts in the blog sections. The reason for this is to convince potential buyers that we are reliable in what we do and that we know our stuff (all posts are related to the services we provide).

### CRUD
- **Create:** Admins can add new posts to the blog page
- **Read:** All users can read the current posts listed in the blog section
- **Update:** Admins can edit the existing posts on the blog page
- **Delete:** Admins can delete existing posts on the blog page

# Agile Process

## GitHub User Stories
All user stories are marked to show their importance.
I used MoScOw prioritization to reduce down to an MVP.
All user stories were mentioned before - [User stories](#User-Stories)

### User Story Templates

![image](https://github.com/PPindel/test-a-wheel/assets/114284732/9c6fd76a-b3df-4c8a-8cac-e3387c5481a2)


### Issues & kanban board

All the issues were stored in GitHub kanban board issues with the proper label:

![image](https://github.com/PPindel/test-a-wheel/assets/114284732/f25632c7-b0bd-4d06-8486-81975ff74e8c)

![image](https://github.com/PPindel/test-a-wheel/assets/114284732/84d0f479-245c-4df6-9ced-9e75b3a2a849)

![image](https://github.com/PPindel/test-a-wheel/assets/114284732/bca4f560-8020-452f-ba38-d5fc0808ac44)

![image](https://github.com/PPindel/test-a-wheel/assets/114284732/6abd9fca-2e07-44d8-83ce-340a0ea427b3)

![image](https://github.com/PPindel/test-a-wheel/assets/114284732/b058263c-39b0-45ba-9046-8358957e6e46)

![image](https://github.com/PPindel/test-a-wheel/assets/114284732/82d67434-0572-4f19-b154-ef4305763fc4)

![image](https://github.com/PPindel/test-a-wheel/assets/114284732/2fc63b22-5a32-47ef-a9b6-883f4488c1a3)

![image](https://github.com/PPindel/test-a-wheel/assets/114284732/2ecc69b3-f752-46eb-b181-2c5e36209b56)

![image](https://github.com/PPindel/test-a-wheel/assets/114284732/89c307ef-35f7-4b4d-9995-ee962476f79f)

![image](https://github.com/PPindel/test-a-wheel/assets/114284732/fb04df4f-f37b-49cc-97b4-58249a32199a)


# Features
## Implemented Features
- Index page with navigation, search tool, and footer:

  ![image](https://github.com/PPindel/test-a-wheel/assets/114284732/9f4050c1-4208-4184-9d8a-af78f784686c)

  ![image](https://github.com/PPindel/test-a-wheel/assets/114284732/604df710-00dc-4876-afc1-4834efafcfdc)

- Favicon:

  ![image](https://github.com/PPindel/test-a-wheel/assets/114284732/92c305b6-7f86-490f-a0b5-a865c006d6b6)

- Account registration with the authentication process, customized signup, login, and logout pages:

  ![image](https://github.com/PPindel/test-a-wheel/assets/114284732/c4604ccf-4b6d-4d7c-8090-e287bc5ed2b0)

  ![image](https://github.com/PPindel/test-a-wheel/assets/114284732/c2eed2c3-4cc0-47c0-9fa6-423edb77ecf3)

  ![image](https://github.com/PPindel/test-a-wheel/assets/114284732/05e88b42-e6b4-46c8-a6e4-424a20c7c203)

  ![image](https://github.com/PPindel/test-a-wheel/assets/114284732/b8b085d7-151a-4107-8d5e-1a3298c7f602)

  ![image](https://github.com/PPindel/test-a-wheel/assets/114284732/b887b7ba-00e3-4101-b956-44556b1f8c45)

  ![image](https://github.com/PPindel/test-a-wheel/assets/114284732/8e917ad2-4478-428c-bfbf-222c09143132)

- Contact page:

  ![image](https://github.com/PPindel/test-a-wheel/assets/114284732/ce254918-be2e-456a-b6b9-b785622fa414)

- Animated FAQ page:

  ![image](https://github.com/PPindel/test-a-wheel/assets/114284732/22473466-51d3-4364-9505-cfba398b3df1)

- Customer ratings page with stars-rating feature:

  ![image](https://github.com/PPindel/test-a-wheel/assets/114284732/06d84ec4-2845-4b07-affd-ec11009695f3)

- Services page and product detail page:

  ![image](https://github.com/PPindel/test-a-wheel/assets/114284732/52262f2b-8c8e-47a2-836e-930e42293fe6)

  ![image](https://github.com/PPindel/test-a-wheel/assets/114284732/dafb3ac8-ac8b-465a-a4ea-e156625508b5)

- Blog page with likes button:

  ![image](https://github.com/PPindel/test-a-wheel/assets/114284732/d0302866-25b0-40f2-b44a-514f7d87a241)

  ![image](https://github.com/PPindel/test-a-wheel/assets/114284732/8d706a7e-54ac-4436-946e-96b1e24aa589)

- Profile page:

  ![image](https://github.com/PPindel/test-a-wheel/assets/114284732/3d05f7aa-8805-41a6-8c10-00d2e610cda3)

- Cart page:

  ![image](https://github.com/PPindel/test-a-wheel/assets/114284732/28a6886a-b79e-4b9a-b109-85d0d315e5f0)

- Checkout page:

  ![image](https://github.com/PPindel/test-a-wheel/assets/114284732/7d4a12fc-ce49-4f77-82dd-bc0f32dcd162)

- Order confirmation page:

  ![image](https://github.com/PPindel/test-a-wheel/assets/114284732/496de7b2-1a86-4e6a-9cdc-f763af128717)

- Profile page updated with details after purchase, order history, and access to order details and add review page:

  ![image](https://github.com/PPindel/test-a-wheel/assets/114284732/77835e72-1229-4293-a0aa-1333c3ed437d)

  ![image](https://github.com/PPindel/test-a-wheel/assets/114284732/25418106-8c7c-46a2-b606-bedefe2670f1)

  ![image](https://github.com/PPindel/test-a-wheel/assets/114284732/9927c166-e00d-43e1-9755-1a61cfde6555)

  ![image](https://github.com/PPindel/test-a-wheel/assets/114284732/9bbafdeb-58bf-4e9a-8055-535684434d83)

- Reviews must be accepted first by admin, then the author can edit or delete the review:

  ![image](https://github.com/PPindel/test-a-wheel/assets/114284732/3c8f5c06-728d-4a06-837d-09bd918b9546)

  ![image](https://github.com/PPindel/test-a-wheel/assets/114284732/001a79bc-7bbe-43a5-a9d2-be5ff355f41c)

  ![image](https://github.com/PPindel/test-a-wheel/assets/114284732/a4992a96-bd82-47e8-96ec-b28eb3cd60ef)

- Add product and add posts to blog options for admins (admins also can edit or delete services and posts):

  ![image](https://github.com/PPindel/test-a-wheel/assets/114284732/108a8fa4-4a8c-4187-bd90-6a6aeba8b3fc)

  ![image](https://github.com/PPindel/test-a-wheel/assets/114284732/2cda778c-55b9-4bbb-8926-553ac95f9260)

  ![image](https://github.com/PPindel/test-a-wheel/assets/114284732/d92771df-311a-4607-896f-55ea3a55e629)

- Custom error pages (403, 404, 500 - same design, just presenting 404 below):

  ![image](https://github.com/PPindel/test-a-wheel/assets/114284732/8d60ac01-862f-4c14-b817-e91f69053c0f)

- Mailchimp newsletter signup form:

  ![image](https://github.com/PPindel/test-a-wheel/assets/114284732/3dc4abbe-0b15-4ee7-98c0-858a33bd01ee)

  ![image](https://github.com/PPindel/test-a-wheel/assets/114284732/aaf928da-1a28-4ffa-a679-d6e5e8657bce)

  ![image](https://github.com/PPindel/test-a-wheel/assets/114284732/79d281c3-0c82-40b0-a1cc-70be9ad93c1f)
  
- Facebook business page: [Test a Wheel Facebook](https://www.facebook.com/profile.php?id=61550205204443)
  Screenshots:
  
  ![Test-a-Wheel-Facebook](https://github.com/PPindel/test-a-wheel/assets/114284732/50f75605-3e9f-4bde-8288-8859cc3a4687)
  
  ![Test-a-Wheel-Facebook-2](https://github.com/PPindel/test-a-wheel/assets/114284732/9dbd19f2-ffd0-44fa-a4ab-f9f09c721b83)
  
  ![Test-a-Wheel-Facebook-3](https://github.com/PPindel/test-a-wheel/assets/114284732/93d0e5d4-2f44-4319-aea6-38d7e759daf6)

- Defensive programming implemented (all pages and functions are protected from tampering):

  ![image](https://github.com/PPindel/test-a-wheel/assets/114284732/7b439d7c-496b-4008-bc54-6dc98af9aab7)
  
- Toast messages disappearing after 5 seconds
  
  ![image](https://github.com/PPindel/test-a-wheel/assets/114284732/e1d3ea4b-db4f-417f-845c-1976cdf137a3)

- Order confirmation emails:

  ![image](https://github.com/PPindel/test-a-wheel/assets/114284732/7329c091-c604-4847-9403-3e58a6a03b15)

- Search bar and sorting feature:

  ![image](https://github.com/PPindel/test-a-wheel/assets/114284732/627d2ce1-009f-49cb-be16-bf8612c06f7e)

  ![image](https://github.com/PPindel/test-a-wheel/assets/114284732/184edd66-20c3-42d0-9dbc-1abe5b4e3a42)


## Future Features

- Add a forum for customers who successfully bought a car with Test a Wheel so they can share pictures of it and discuss
- Improve the Reviews system to connect them with actual products (for now, the product rate is set by the admin), and also restrict the product selection to actually bought services
- Add a form for the Dream service, so Customers can send all information about the wanted vehicle

# Testing
Please refer to the [TESTING.md](TESTING.md) file for all testing performed.

# E-commerce Business Model
🚨**Required**

In this section discuss your business model, how you use  SEO to get users to your site and how you hope to generate more traffic and get sponsors to back link to your site. 

## Facebook Business Page
🚨**Required**

- copy a screenshot of the FB page
- add a couple of bulletpoints about the goals of what this fills for building out followers & special content

## Newsletter Signup
🚨**Required**

- copy a screenshot of the signup 
- add a couple of bullet oints outlining the goals of what this functionality provides for building out followers

## Links
- sponsored links are flagged with rel="sponsored"
- social links and other links that go outside domain have `rel="nofollower"` to signal to search engines that those links are not associated with our specific domain

## SEO Strategy
🚨**Required**

In this section write out the process you used to come up with short tailed and long tailed results to help refine the keywords you came up with. You should call out attention to the following:

### Keywords
Describe the process you went through identifiying keywords that you want Google and other search engines to relate to your site.

### Description
Note that you have a the meat description tag and if any of the content changes based on the page.

### Title
Call out that you have this set in your base.html so it can be changed per page

### Relevant Content
Call out how you purposefully incorporated keywords into your content, H1, meta data etc. 

### Sitemap
🚨**Required**

- [sitemap.xml file]() call out files that exist so browsers can easily crawl site

### Robots.txt
🚨**Required**

- [robots.txt file]() to restrict pages that are should be searched by google, authentication and others are blocked to only allow relevant pages to be searched by google

# Deployment
🚨**Required** 

## Prerequisits
🚀 **merit & beyond**

If the user is required to have certain keys and credentials you should include this section with directions on how to get the necessary information. ex)

1. **Gmail Account:** In order to have verification and forgot password emails sent to registered users you need a
   google account. 
  - [create a gmail accoount](https://accounts.google.com/signup) 
  - [downgrade to less secure](https://myaccount.google.com/lesssecureapps?pli=1) after you are signed into the gmail account, downgrade to less secure
2. **Couldinary URL**
  - [create an account](https://cloudinary.com/)
  - go to the dashboard and copy your API environmental variable
   
    <img width="1230" alt="image" src="https://user-images.githubusercontent.com/23039742/213839829-b4f349b3-419d-4ea2-bbca-90cf3c663bba.png">     
 
## Fork and Clone the Repository
🚀 **merit & beyond**
To keep the main reposotory for this project clean, please fork the repostiory into your own account. GitHub has [forking directions](https://docs.github.com/en/get-started/quickstart/fork-a-repo#forking-a-repository) but here's what you might do:
1. login to your own gitHub account
2. navigate to [my repository](URL OF YOUR LIVE REPOSITORY)
3. In the top right corner of the page, click fork 

![image](https://user-images.githubusercontent.com/23039742/213840378-e785eaa0-712b-468c-bcda-64fde56eae44.png)

4. set yourself as the owner
5. change the name of the repo if you want
6. add a description if you want
7. choose what to copy, typicall the main branch only
8. click the snazy green button

![image](https://user-images.githubusercontent.com/23039742/213840549-5bef12ae-198e-412b-84b6-0cc718b6fa1d.png)

9. To get files to your local environment, you need to clone it: click the code button
10. Copy the url as needed (here's gitHub instructions)[https://docs.github.com/en/get-started/quickstart/fork-a-repo#cloning-your-forked-repository}



## Development Deployment 
🚨**Required** 

This section should describe the process someone would have to go through to get the local working in GitPod, or your preferred IDE. Start from installing the chrome extension then clicking the green gitpod button in THEIR FORKED repository, the enumerate the steps to walk them through the process as if they were brand new to this proccess. **Include screenshots** where applicable.

**Key points to cover** 
- Install required python packages: `pip3 install -r requirements.txt`
- Create env.py
- What to put in the env.py, don’t disclose real values
>  - EMAIL_HOST_PASSWORD=<YOUR_VALUE>
>  - DEFAULT_FROM_EMAIL=<YOUR_VALUE>
>  - EMAIL_USERNAME=<YOUR_VALUE>
>  - SECRET_KEY=<YOUR_VALUE>
>  - CLOUDINARY_URL=<YOUR_VALUE>
>  - DEV=True
- Apply Database Migrations so the database starts up `python3 manage.py migrate`
- Create a super user so you can add and inspect things via django admin  `python3 manage.py createsuperuser`
- Preload data: Sometimes you might want to include steps to create data in the admin or preload a data dump [coderwall blog](https://coderwall.com/p/mvsoyg/django-dumpdata-and-loaddata) has examples on how to dump data and load it which saves a bunch of time when deploying the application from a local database to a hosted database but you don’t  have to do this step
- Start the server `python3 manage.py runserver`


## Production Deployment
🚨**Required** 

This section should describe the process you went through to deploy the project to a server where anyone can access the url without your machine running. This is typically Heroku. **Include screenshots** if you think they would make the process easier. Start with getting an heroku account and then setting up databases and other packages.

If you have project settings required for Heroku, provide a table of the keys and values. Do not share your personal
keys but either cut them out of the screenshot or say <YOUR_VALUE> and include links on how the user would obtain such
values.

**Key points to cover** 
- cerating new app
- setting app name
- setting region
- entering dreaded billing info
- subscribing to a plan
- setting up db
- adding environmental values- have a list or table so user has less chance of typos
>  - EMAIL_HOST_PASSWORD
>  - DEFAULT_FROM_EMAIL
>  - EMAIL_USERNAME
>  - SECRET_KEY
>  - CLOUDINARY_URL
>  - COLLECT_STATIC
- adding build packages
- deploy
- gitHub connection
- auto vs manul deploy
- monotior logs


# Credits
🚨**Required**

To avoid plagiarism amd copyright infringement, you should mention any other projects, stackoverflow, videos, blogs, etc that you used to gather imagery or ideas for your code even if you used it as a starting point and modified things. Giving credit to other people's efforts and ideas that saved you time acknowledges the hard work others did.

-[Code Institute Template](https://github.com/Code-Institute-Org/python-essentials-template)
    - The Template for the GUI for this project was provided by Code Institute. This allows for the Command line to be shown and used within the browser.

## Content

Use bullet points to list out sites you copied text from and cross-reference where those show up on your site

## Media

Make a list of sites you used images from. If you used several sites try to match up each image to the correct site. This includes attribution for icons if they came from font awesome or other sites, give them credit.

## Acknowledgments

This is the section where you refer to code examples, mentors, blogs, stack overflow answers and videos that helped you accomplish your end project. Even if it's an idea that you updated you should note the site and why it was important to your completed project.

If you used a CodeInstitute Instructional project as a starting point. Make note of that here too.

