# Milestone 4



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

### Python


### Django

1. When creating the shop model in django, the links were not functioning and the templates were not being reached when there was an attempt to go to the shop template. This was an error in usage of django, requiring the path being added to urls.py.

2. After mistakenly placing the static folder within the palestra app, it was moved outside into the main project folder after failing to be accessed by other apps and this resolved any errors.

3. When creating the filter function in views.py, an empty "categories" variable could be passed to the page when sorting is not present causing an error to occur. A solution to this was setting "categories = None" at the top of the function to prevent this error.

4. During the creation of contexts.py for the bag app, the site would crash when trying to access the bag page. This was due to a variable referenced before assignment. For the sake of simplicity and before the variable can be established elsewhere, it was set to 0 before reference to prevent the site crashing before the grand_total variable can be created elsewhere.

5. When creating the sorting bar for the mobile page, the code would not be read by the if functions as they previously were written {% if 'X' in request.get %}. However this proved to be incorrect and changing to {% if 'X' in request.get_full_path %} allowed it to function as intended.

6. When creating the bag app there was an issue using the default django template calculations. ${% widthratio item.product.price 1 item.quantity %} in the code originally rounded the subtotal, thus reducing accuracy. The solution was installing mathfilters and changing the code to ${{ item.product.price|mul:item.quantity }}, thus removing the rounding error.

7. When creating the deletion form on the shopping bag, an error occured when trying to delete items of a certain size. Adding a hidden input that would send the product_value was used to resolve the problem. Originally there was an attempt to try use the dictionary key attribute to get the size which did not work.


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
