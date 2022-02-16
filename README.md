# Milestone 4

## User Stories

### External user’s goal:

1. To join a fitness community and purchase exercise plans and
merchandise

2. Easy access to a wide range of fitness related merchandise and goods

3. Strong features with a draw to keep coming back go

4. The ability to buy subscriptions in the store


### Site owner's goal:

1. Build an active community around the product based on
subscription and individual payments models
2. Sell
3. Exercise plans
4. Nutrition Plans
5. Nutrition and exercise products

## Answers to user stories

### External user

1. Joining a community was made very possibile by the ability to join forums, comment and post

2. The shop is the most prominant part of the site arguably and very accessable to all users 

3. Very strong features that make coming back to the site, for any number of different uses very tempting to a user and creates a good sense of variety

4. Subscriptions and their skus are listed on the store where the user can find them very easily.

### Site owner

1. The community is able to be very active and discuss products readily in the forums

2. The shop makes selling a wide range of products very simple

3. The store has an entire section dedicated to exercise plans meaning they cant be missed. And with a prominant advertisement on the homepage

4. As with the exercise plans, the nutrition plans have their own section and are very much able to be accessed with ease

5. The other sections of the store dedicated to these types of fitness merchandise are available and featured prominantly

## Wireframes

### Desktop Home
![Desktop Home](media/wireframes/home-desktop.png "Desktop Home")

### Mobile Home
![Mobile Home](media/wireframes/home-mobile.png "Mobile Home")

### Login
![Login](media/wireframes/login.png "Login")

### Mobile Login
![Mobile Login](media/wireframes/login-mobile.png "Mobile Login")

### Signup
![Login](media/wireframes/signup.png "Login")

### Signup Mobile
![Mobile Signup](media/wireframes/signup-mobile.png "Mobile Signup")

### Profile
![Profile](media/wireframes/profile.png "Profile")

### Mobile Profile 
![Mobile Profile](media/wireframes/profile-mobile.png "Mobile Profile")

### Blog
![Blog](media/wireframes/blog.png "Blog")

### Mobile Blog
![Mobile Blog](media/wireframes/blog-mobile.png "Mobile Blog")

### Blog Specific Post
![Blog Post](media/wireframes/blog-post.png "Blog Post")

### Mobile Blog Specific Post
![Mobile Blog Post](media/wireframes/blog-post-mobile.png "Mobile Blog Post")

### Shop
![Shop](media/wireframes/shop.png "Shop")

### Shop Mobile
![Shop Mobile](media/wireframes/shop-mobile.png "Shop Mobile")

### Product View
![Product View](media/wireframes/product-view.png "Product View")

### Product View Mobile
![Product View Mobile](media/wireframes/product-view-mobile.png "Product View Mobile")

### Empty Bag
![Empty Bag](media/wireframes/empty-bag.png "Empty Bag")

### Empty Bag Mobile
![Empty Bag Mobile](media/wireframes/empty-bag-mobile.png "Empty Bag Mobile")

### Bag
![Bag](media/wireframes/bag.png "Bag")

### Bag Mobile
![Bag Mobile](media/wireframes/bag-mobile.png "Bag Mobile")

### Checkout
![Checkout](media/wireframes/checkout.png "Checkout")

### Checkout Mobile
![Checkout Mobile](media/wireframes/checkout-mobile.png "Checkout Mobile")

## JSON
![JSON Category Layout](media/JSON_Catagory_layout.png "JSON Category Layout")

This model is to be the very basis of the project and how it will be laid out within the shop and how the items will be categorised.

## Database Layout
### Blog Database
![Database Blog Layout](media/databaseinformation/databaseblog.PNG "Database Blog Layout")

### Checkout Database
![Database Checkout Layout](media/databaseinformation/databasecheckout.png "Database Checkout Layout")

### Profile Database
![Database Profile Layout](media/databaseinformation/databaseprofiles.PNG "Database Profile Layout")

### Shop Database
![Database Shop Layout](media/databaseinformation/databaseshop.png "Database Shop Layout")


## Design

* Roboto by google fonts was chosen due to its strong, industrial appearence, being suitable to a gym website

* Icons from fontawesome will be used to create a more user friendly and aesthetically pleasing appearence

* Colours will be blue and white predominantly, due to being in strong association with fitness and health.

* General styling will lean towards being readable and easy to navigate at all times for the user.


## Technologies used

### Gitpod
* The version control on Gitpod was used to create commits and version control the project and was used as the primary IDE for the project.

### Github
* Github was used to store all versions committed from Gitpod and to manage the Gitpod account

### Heroku
* Heroku was used to create an app and make the website live, linking to gitpod and allowing the use of automatic deployments when a commit is made from gitpod.

### Postgres
* Postgres within Heroku will be used to store the database of the project

### Amazon web services
* The amazon web services will be used to store all images related to the project

### Django
* Django was used as the basis of the project and its technologies make up the backbone of the entire project. A lot of its other technologies
* Djangos countries, crispy-forms, allauth, countries, mathfilters and others were used within the framework to create forms, add logins, add a country list and to change the appearence of numbers and dates within the site.

### dj-database-url and boto3
* Both were used in the process of initalising the deployment of the project to heroku and for the use of postgres

### gunicorn
* gunicorn was used to connect the procfile to heroku and ensure the deployment went smoothly

### Favicon.cc
* This site was used to make the favicon for the site

### Google Chrome Development Tools
* Used heavily to test site responsiveness across many different screen sizes, and to inspect any possible layout irregularities with its ability to examine code line by line, and add or remove in the environment to see how it displays.


## Features

* Very high level of functionality and aesthetics across all platforms
* A large variety within the site for a user
* The ability to create an account and log in/out at will
* Ability for an administrator to edit and delete items on the website
* A shop and ability to edit the cart before buying
* A blog, with a full comment system to use
* A search function to browse the store within the site

## Testing

### Validation

The site underwent validation in a number of steps in order to ensure that the HTML was error free and highly functional. Each page followed a number of steps outlined below as to how they were validated.

1. The first step was to place the link into the W3C validator, and seeing what errors are present. After clearing these. These errors can then be cleared and then the next step commenced.

2. The next part of the html validation was to go into google chromes developer tools, and click source. After opening the code running behind the page, it was then copy and pasted into the html validators raw input mode. This ensures that the html is being validated, even accounting for any possible variance.

3. The third step is an extension on the second. On a page like the the bag, or blog for example where the content can vary, using the dev tools source code and checking multiple combinations of variations on each page was very useful. The bag page for instance was tested with multiple different quantities of items, different sizes, and with many different varieties of bag contents to ensure the html was secure and error free.

4. After the validation of the HTML was finished, the CSS was ran through the W3C CSS validator and ran without issue.

5. The views.py contents in each django app were ran through the validator on pep8online.com to ensure that the python code was pep8 compliant and well structed.

### Usage Testing

* The website was tested across a large amount of different screen sizes to ensure functions all work, and the absence of dead links or any poor layouts.

* 4 devices were used to test the project, two windows computers and two android phones and all functions of the website were perfectly operational

* All code was checked to be of high quality and without errors.

* Usage of every theoretical combination of functions in each order was done to ensure the site has a solid experience no matter how it is used by the user and all worked very well


## Deployment

Heroku

1. Log into Heroku

2. Click New and then from there Create new app

3. Name the new app then choose the closest region to host it

4. Go to resources, then type "postgres" into the add-ons section and select "Heroku Postgres", and choose a plan

5. back in gitpod, type in pip3 install dj_database_url

6. Then install "pip3 install psycopg2-binary"

7. Add both to requirements.txt

8. After this, import dj_database_url in settings.py   

9. Set DATABASES (also in settings.py) with default as dj_database_url.parse() and get database name from heroku config vars

10. Run migrations again, as it needs to connect to the new database

11. Use loaddata on fixture files to add them to new database

12. Create superuser for app using python3 manage.py create superuser

13. Add if function in settings.py to know where the app is running and such which database to use

14. Install gunicorn to act as a webserver. Don’t forget to freeze into requirements.

15. Create the procfile in order to interact with heroku, tell it to create dynos etc

16. Login to heroku on the terminal using ‘heroku login’

17. In the terminal write “heroku config:set DISABLE_COLLECTSTATIC=1 –app” with an app name at the end, as to prevent heroku from taking static files when deployed

18. Add ALLOWED_HOST in settings.py and set as the heroku app

19. Create a heroku remote to gitpod, with “heroku git:remote -a ” with the app name after

20. Push to the remote master.

21. Set up to automatically deploy from github using herokus connect to github button in the deploy tab. Search for the repo name and then click add.

22. Set up automatic deploys to ensure the code can automatically be pushed from gitpod

23. Get a randomly generated secret key and add to the heroku config vars

24. Set the secret key to come from the environ


### Amazon AWS

1. Set up amazon aws account and create it as a personal account

2. Search for “S3” and click create bucket. Make sure to allow public access

3. Click the name of the bucket and click the properties tab, and select to use this bucket to store a static website. And set it to selected. Fill in some default values for the fields expecting html as these are already elsewhere so will not be needed.

4. Go to permissions, add in code for a CORS configuration.

5. Go to the policy tab and click policy creator to create a policy bucket.

6. Set as S3 bucket policy, all principals set as “*” and action set to getobject

7. Get the amazon resource name and place in previous forms arn form input


### Creating bucket user

1. Open up IAM and create a group

2. Select Groups and create a group with a name relevant to the site 

3. Select Policy then create policy.

4. Go to the json tab and select import managed policy. Import s3 full access

5. Go to bucket policy in s3 and get the arn to add into the policy. Click review policy then give a name, description

6. Go to groups and attach the policy to the created group and click permissions and attach policy. Then click attach policy
Go to users, add user, and give programmatic access. After this attach the user to the group
Download the csv file supplied with access keys


### Connecting django to s3

1. Install boto3 and django-storages

2. Add settings to django to allow it to detect AWS. 

3. Go to heroku and add the keys to the config vars

4. Create a custom_settings.py file and import django settings. Add storage information into this file

5. In settings.py add all the links and relevant parts to connect the files

### Finalising
1. Go into settings and add code to allow caching within the app

2. Go to s3 and create media folder

3. Inside click upload and add files, then select all images

4. Now add the stripe secret keys to heroku


## Bug report

### HTML

1. When using the bootstrap template for the mobile header and after interacting with the 
products and accounts sub menus within the mobile navbar, this would close the main navbar.
This was resolved by changing the classes of the navbar and divs containing the nav elements to
be more similar to that of the enclosed navbars. Changed From an anchor element with a class of 
"nav-link" to a nav element with a class of "navbar". This allowed the navbar to remain open.

2. The container classes from bootstrap were applied to the third and fourth elements within the mobile navbar, creating an inbalance within the appearence of the navbar thus requiring the addition of a div with the class of container wrapping the first and second li elements. This added the required classes and fixed the imbalance.

3. The HTML file would be completely unstyled, however this was resolved by adding "{% load static %}" to the base.html to prevent any elements from being unstyled.

4. When connecting the input within the form to the search query the information entered would not be processed and all products would show despite lack of relevence. The problem turned out to be a mismatch between the name searched for by the python search code and the name attribute on the inputs. This was fixed by matching the two.

5. In the view_product.html, the image is normally meant to lead to a product.image.url, however this link was the same even with the noimage.png loaded in the absence of a product image. A fix to this was removing the anchor element around the noimage.png loader, as it is not necessary and can crash the application.

### CSS

1. After creating the mobile header element, the content from the page would collapse below the header and would prevent reading of the top elements. This was resolved by adding a margin of 40px (the height of the mobile header) to the divs and other main body elements of the page on mobile.

2. The products title had padding that when it crossed two lines ended up causing major disruption to the layout. A solution was removing the padding and modifyin the settings in the css file for its height.

### Javascript

1. When creating the sliding image mainscreen, the code to check the current "left" alignment of the divs was originally set to detect when left is -100% before being moved to 200% to set the infinite cycle. A problem that occured in testing was that if the container did not go to -100% precisely, it would cycle left indefinitely. this was resolved by setting the code to check for any elements further left than -100%, preventing moving indefinitely, and allowing the cycle to be continued without error.


### PYTHON/Django

1. When creating the shop model in django, the links were not functioning and the templates were not being reached when there was an attempt to go to the shop template. This was an error in usage of django, requiring the path being added to urls.py.

2. After mistakenly placing the static folder within the palestra app, it was moved outside into the main project folder after failing to be accessed by other apps and this resolved any errors.

3. When creating the filter function in views.py, an empty "categories" variable could be passed to the page when sorting is not present causing an error to occur. A solution to this was setting "categories = None" at the top of the function to prevent this error.

4. During the creation of contexts.py for the bag app, the site would crash when trying to access the bag page. This was due to a variable referenced before assignment. For the sake of simplicity and before the variable can be established elsewhere, it was set to 0 before reference to prevent the site crashing before the grand_total variable can be created elsewhere.

5. When creating the sorting bar for the mobile page, the code would not be read by the if functions as they previously were written {% if 'X' in request.get %}. However this proved to be incorrect and changing to {% if 'X' in request.get_full_path %} allowed it to function as intended.

6. When creating the bag app there was an issue using the default django template calculations. ${% widthratio item.product.price 1 item.quantity %} in the code originally rounded the subtotal, thus reducing accuracy. The solution was installing mathfilters and changing the code to ${{ item.product.price|mul:item.quantity }}, thus removing the rounding error.

7. When creating the deletion form on the shopping bag, an error occured when trying to delete items of a certain size. Adding a hidden input that would send the product_value was used to resolve the problem. Originally there was an attempt to try use the dictionary key attribute to get the size which did not work.

### Existing bugs

1. When using the sort items by selector on the shop, it will only sort by all items on the store, not within a subcategory.


## Credits

### content
* All code written by Stephen Galway

### Acknowlegements
* My mentor Spencer for providing many valuable insights on improving the website and the various 
testers who offered advice to make the website more user friendly. Also to the staff at the tutor support who were a fantastic help throughout the project and provided many hours of assistance and helped with many bugs and issues