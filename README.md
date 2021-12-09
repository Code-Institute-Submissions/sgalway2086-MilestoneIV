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