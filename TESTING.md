# Test a Wheel - Testing Documentation

![TaW Devices](https://github.com/PPindel/test-a-wheel/assets/114284732/297cc3b7-e11e-4e0a-a9aa-81a7420abdf6)

Below is the documentation of my testing process.

## Table of contents
- [Test a Wheel - Testing Documentation](#test-a-wheel---testing-documentation)
  * [Table of contents](#table-of-contents)
  * [Validation Testing](#validation-testing)
    + [CSS](#css)
    + [JavaScript](#javascript)
    + [Python](#python)
  * [Visual (UI) Testing: Cross Browser and Cross Device Testing](#visual--ui--testing--cross-browser-and-cross-device-testing)
  * [Lighthouse](#lighthouse)
      - [Desktop Results](#desktop-results)
      - [Mobile Results](#mobile-results)
  * [Manual Testing](#manual-testing)
  * [Defensive programming testing](#defensive-programming-testing)
    + [Testing User Stories](#testing-user-stories)
  * [Outstanding Defects](#outstanding-defects)
  * [Defects of Note](#defects-of-note)

[Back to README.md](https://github.com/PPindel/test-a-wheel#testing)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


## Validation Testing
[W3C](https://validator.w3.org/) was used to validate the HTML on all pages of the site. It was also used to validate the CSS. As the site is created with Django and utilizes Django templating language within the HTML, I have checked the HTML by inspecting the page source and then running this through the validator.

Index page:
![index-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/5929d190-9931-44b4-821b-ce38734eecf0)

Add post page:
![add-post-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/f8291f67-2736-4dba-bd59-4c5f1c24c5ac)

Add product page:
![add-product-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/a8e8e206-5675-4309-9aa1-d4c0ee640906)

Add review page:
![add-review-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/c9ec75bb-63ea-4044-b266-bb1d3e01c71c)

Blog page:
![blog-list-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/585eed7f-3a9b-4bd1-94d1-a61d4cc51880)

Checkout page:
![checkout-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/4d814eef-1781-453e-813f-d2d724da4e4d)

Contact page:
![contact-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/d649d24d-6464-49a7-aeda-f8a5a355dbc5)

Delete review page:
![delete-review-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/c6240330-909f-464c-9c65-25fc8c7cfb77)

Edit product page:
![edit-product-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/b934e3cf-aefe-42eb-b837-c2315bce16da)

Edit review page:
![edit-review-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/c20eb7ff-8c15-4bca-8fcc-fa22c37f9a3e)

Error 404 page:
![error-404-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/308c0ceb-7f92-4d29-96a4-2cadb01b9220)

FAQ page:
![faq-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/cc910fa5-2058-4a9f-982c-9dfb5d0fa3a3)

Shopping cart:
![shopping-cart-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/5cba3ab8-5b77-40d1-8827-efb83ea99479)

Login page:
![login-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/0e7726ba-4042-410e-b04c-aa4aafa7d990)

Logout page:
![logout-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/4221b8a0-10e6-48df-adea-9517743c1d29)

Profile page:
![my-profile-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/e0e1620b-87f3-4750-b869-5af2f1b0ce75)

Order confirmation page:
![order-confirmation-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/84dd466e-8646-4d59-bfa4-b9160ca0fce8)

Order history page:
![order-history-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/6cdd4121-c2df-4535-8980-317accb05078)

Post edit page:
![post-edit-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/c8889035-de4b-478e-a593-9bb38efae55e)

Product detail page:
![product-detail-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/3a12f746-7e8a-4817-b39c-e6ad424c4df6)

Sign-up page:
![register-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/58bec6b6-d814-4443-a3a0-6e600cfb50c7)

Review list page:
![review-list-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/1f2b5246-a901-4559-a562-6baae5ccaf13)

Services page:
![services-page-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/8bea6817-9b15-431b-aed0-291ae16bb179)


### CSS

[W3C](https://validator.w3.org/) was used to validate the CSS. 

Static CSS file:
![static-css-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/92e8e480-8aa3-4cd1-9a6e-6dfd3ccbc326)

Profile CSS file:
![profile-css-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/c58cc753-8c80-4483-89bd-c69db43aea58)


### JavaScript

[JS Hint](https://jshint.com/) was used to validate the JavaScript.

JS Stripe file:
![js-hint-stripe-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/02c185be-f605-4172-b388-4dad8c3509fe)


### Python

[Code Institute Python Linter](https://pep8ci.herokuapp.com/) was used to validate the Python. The code was also checked with the Flake8 tool.

Blog admin py:
![blog-admin-python-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/1bb8ef58-3597-4739-8c92-116e58810fe1)

Blog models py:
![blog-models-python-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/39308b0b-acf5-408b-b41e-e828059c1c4b)

Blog views py:
![blog-views-python-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/45d6751c-3c22-4e74-9d09-ca6553c88254)

Cart contexts py:
![cart-contexts-python-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/531f7a09-8e04-451d-a12d-0cbef04ff6ec)

Cart views py:
![cart-views-python-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/54a10889-656c-4e3f-b4c5-dd6c1cb8dde5)

Checkout admin py:
![checkout-admin-python-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/5406d88b-e6db-4654-a848-19a585d78bff)

Checkout forms py:
![checkout-forms-python-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/51e5746d-dd82-4577-85f5-da60eb9a3e97)

Checkout models py:
![checkout-models-python-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/70620fca-f9f9-4c7f-87bd-97541c8fb3d0)

Checkout views py:
![checkout-views-python-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/daf72e0f-c292-4dfa-bacf-2dc4d52d43cf)

Checkout webhook handler py:
![checkout-webhook-handler-python-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/861dc931-5a8d-47eb-bdf2-aca6fca8a745)

Checkout webhooks py:
![checkout-webhooks-python-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/e61fc8c0-bb62-4711-acfc-a3aec730b089)

Home views py:
![home-views-python-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/fed654dd-987f-45be-95d8-b26d96930ddb)

Products admin py:
![products-admin-python-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/7d648d4e-c238-4301-b7b0-ee24fbac8bca)

Products forms py:
![products-forms-python-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/b4d42307-12c4-4892-8cd2-1cd64d6922cf)

Products views py:
![products-views-python-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/6eed62b6-cd6a-4512-9937-b7c966482ea9)

Profiles forms py:
![profiles-forms-python-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/c14a1a5a-2d29-4314-b3f7-916c6c26b9dc)

Profiles models py:
![profiles-models-python-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/1a1f2d2c-c837-4a7e-98f6-630c25f1a04f)

Profiles views py:
![profiles-views-python-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/8b63f61d-1da8-433d-8381-d17167bbe040)

Reviews admin py:
![reviews-admin-python-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/07e8dd9f-fa68-4eb5-af25-697cc3668375)

Reviews models py:
![reviews-models-python-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/cf720354-524d-41d0-b3ce-57acd7d51d25)

Reviews views py:
![reviews-views-python-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/bef79bf3-7f00-43d4-a66f-2398e3d8549a)

Test a Wheel settings py:
![test-a-wheel-settings-python-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/169e2507-d508-442e-a6f9-697b169c946e)

Test a Wheel urls py:
![test-a-wheel-urls-python-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/8f1e5575-ab4e-4307-8607-827f3147b4b2)


## Visual (UI) Testing: Cross Browser and Cross Device Testing
- The below combination of devices, browsers, and operating systems was used to test the website. A range of viewport sizes was checked to see if users would have the same experience across multiple devices and browsers. Priority was given to mobile devices and tablets. 

| **TOOL / Device**           | **BROWSER**      | **OS**   | Passed 
|-----------------------------|------------------|----------|---------
| dev tools: Galaxy Fold      | Chrome           | android  |Yes
| dev tools: iPhone SE        | Safari           | iOS      |Yes
| dev tools: Samsung S9+      | Chrome           | android  |Yes
| browserstack: Xiaomi 12 Pro | Chrome           | android  |Yes
| browserstack: Pixel 6 Pro   | Chrome           | android  |Yes
| browserstack: Ipad Pro 12   | Safari           | iOS      |Yes
| real phone: Samsung S22     | Samsung Browser  | android  |Yes
| real phone: iPhone 11       | Safari           | iOS      |Yes
| real laptop: Asus Vivo Book | Firefox & Chrome | Windows  |Yes
| real desktop: 27' & 24' scr | Firefox & Chrome | Windows  |Yes

Xiaomi Redmi Note 12 Pro:

![Xiaomi Redmi Note 12 Pro](https://github.com/PPindel/test-a-wheel/assets/114284732/f9177ba1-41d9-4172-8295-dee46975b446)

iPad Pro 12:

![Ipad Pro 12](https://github.com/PPindel/test-a-wheel/assets/114284732/2f766e42-4416-47fd-aa58-ec3369686d6c)

Pixel 6 Pro:

![image](https://github.com/PPindel/test-a-wheel/assets/114284732/e5833a46-91fd-4993-b680-d9f018a0a5ee)

As the most popular browsers in Europe are Chrome and Safari, I decided to focus on these 2 browsers.

![image](https://github.com/PPindel/test-a-wheel/assets/114284732/1f653b87-c10e-4605-a23a-7f382a1eb9be)

Source: https://gs.statcounter.com/browser-market-share/all/europe

## Lighthouse

For the performance, accessibility, best practices, and SEO of the site for mobile and desktop I used the Chrome Lighthouse tool:

#### Desktop Results

Index Page:
![image](https://github.com/PPindel/test-a-wheel/assets/114284732/6ac84fc1-a0dc-494a-9335-aafd7a031b5d)


Services Page:
![image](https://github.com/PPindel/test-a-wheel/assets/114284732/16b4f0b9-bea9-41df-9aba-8a48e237f12e)


User Profile:
![image](https://github.com/PPindel/test-a-wheel/assets/114284732/c9f45fbb-14d3-4980-b90a-07ef7f90df29)


Blog Page:
![image](https://github.com/PPindel/test-a-wheel/assets/114284732/7f87c0b6-54c5-48ab-91f0-98a0406414d7)


Blog Post Detail Page:
![image](https://github.com/PPindel/test-a-wheel/assets/114284732/5a9b7e4e-a90b-43ef-b573-f666472a9586)


Reviews Page:
![image](https://github.com/PPindel/test-a-wheel/assets/114284732/d0ed979c-84ba-4356-ab2f-a463552adf05)


Review Update Page:
![image](https://github.com/PPindel/test-a-wheel/assets/114284732/05402e33-4810-4e1b-9708-d1a6ae0f163a)


Checkout Page:
![image](https://github.com/PPindel/test-a-wheel/assets/114284732/0dacd201-2493-445f-8360-4104391854ff)


Order Confirmation Page:
![image](https://github.com/PPindel/test-a-wheel/assets/114284732/0605d86b-3568-4a26-ae55-17c0b32f37bb)


- Desktop performed well on all major pages of the site.
- The 83-point score for Best Practices is due to the scripts beyond my control (e.g. Mailchimp)

#### Mobile Results

Index Page:
![image](https://github.com/PPindel/test-a-wheel/assets/114284732/6e75fbb3-95f4-40fc-a007-a135afade965)


Services Page:
![image](https://github.com/PPindel/test-a-wheel/assets/114284732/063f0293-69d3-4cb4-8b5d-f64d44aeb1e9)


User Profile:
![image](https://github.com/PPindel/test-a-wheel/assets/114284732/a5635fbf-2b7d-41b8-bf54-52636865f78d)


Blog Page:
![image](https://github.com/PPindel/test-a-wheel/assets/114284732/515248ef-64ac-46e3-8966-afaf264e2d57)


Reviews Page:
![image](https://github.com/PPindel/test-a-wheel/assets/114284732/ed2f9137-865a-43a7-8d7e-16c485116747)


Checkout Page:
![image](https://github.com/PPindel/test-a-wheel/assets/114284732/422b7b3d-e781-40c5-97df-2fb450d678b7)


- Mobile performed well on all major pages of the site.
- The 83-point score for Best Practices is due to the scripts beyond my control (e.g. Mailchimp)

## Manual Testing
Manual testing is presented in the table below:

![image](https://github.com/PPindel/test-a-wheel/assets/114284732/5b7c6991-63c4-463a-be4c-bb1618841953)

[Link to the table HERE](https://docs.google.com/spreadsheets/d/1C3Ni6gYPPfFCggJV_hhHWbIbZ7pAhgZ7NZpm4pp-mBA/edit?usp=sharing)

## Defensive programming testing
- Defensive programming was implemented to all pages and critical user details
- When users try to hack protected flows where personal information is stored, they are greeted with a warning page as shown below:
  ![image](https://github.com/PPindel/test-a-wheel/assets/114284732/dd9ec437-88c1-4914-8402-bf889230755d)
  
Flows that have this protection are:
  - order history - only the logged-in owner of an order can view an order history page
  - profile - a logged-in user can only see their own profile
  - add review - only a logged-in user that owns a given order can add a review & they can only add one review per order
  - Update review - only a logged-in admin or the logged-in creator can update a review
  - delete review - only a logged-in admin or the logged-in creator can update a review
  - add, update, and delete pages are protected also for Blog and Services (products)

Other defensive stuff:
  - active listeners preventing manipulating with item quantity
  - boolean fields checking if the order was already reviewed or the confirmation email was sent
  - stripe mechanism for text fields (preventing injecting dangerous scripts)
  - and there could be some more not listed here, as the project is really big...


### Testing User Stories
Link to project and user stories (agile methodology and all CRUD functionalities were implemented):
[Test a Wheel - user stories](https://github.com/users/PPindel/projects/5)

Example of a user story: 
![image](https://github.com/PPindel/test-a-wheel/assets/114284732/2a102b9d-5634-4a2e-8007-c396dd7db85c)


## Outstanding Defects
Users can select any service on the Add Review page (it's not determined by the actual service purchased in the order):
![image](https://github.com/PPindel/test-a-wheel/assets/114284732/52372dd7-d172-42ae-a94f-a7d63bca02bb)

It was decided that fully integrated reviews were a bit of a stretch goal for an MVP project, thus it was determined low risk to allow users to select an inappropriate service at this point in time, especially since admins must approve reviews before they are shared on the site for all uses.
This will be fixed in the future.

## Defects of Note
1. Connecting the order number with the review and making it a unique value for each order completed gave me a few good days of intensive problem-solving
2. Achieving acceptable Lighthouse performance on all pages wasn't an easy thing, and I know it still could be better, but I am happy with the final result

[Back to README.md](https://github.com/PPindel/test-a-wheel#testing)
