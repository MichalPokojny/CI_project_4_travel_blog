# Testing

## Code Validation

Python

* Python code was tested using PEP8 Code Institute [Python Linter Validator](https://pep8ci.herokuapp.com/)

**Blog app**

views.py
<p align="center">
<img src="./assets/test/pep_blog_views.png">
</p>

urls.py
<p align="center">
<img src="./assets/test/pep_blog_url.png">
</p>

models.py
<p align="center">
<img src="./assets/test/pep_blog_models.png">
</p>

forms.py
<p align="center">
<img src="./assets/test/pep_blog_forms.png">
</p>

context_processors.py
<p align="center">
<img src="./assets/test/pep_blog_context.png">
</p>

admin.py
<p align="center">
<img src="./assets/test/pep_blog_admin.png">
</p>

**Info app**

views.py
<p align="center">
<img src="./assets/test/pep_info_views.png">
</p>

urls.py
<p align="center">
<img src="./assets/test/pep_info_urls.png">
</p>

HTML

* HTML code was tested using [W3 Validator](https://validator.w3.org/)

Every page has passed the W3 validator

<p align="center">
<img src="./assets/test/html_validator.png">
</p>

CSS

* CSS code was tested using [Jigsaw W3 Validator](https://jigsaw.w3.org/)

<p align="center">
<img src="./assets/test/css_validator.png">
</p>

JavaScript

* Javascript code was tested using [JSHint](https://jshint.com/)

<p align="center">
<img src="./assets/test/javascript_validator.png">
</p>

## Browser Testing

The website has been tested thoroughly on several different browsers.

* Google Chrome
* Mozilla Firefox
* Microsoft Edge
* Safari
* Opera

### Google Chrome Lighthouse

Lighthouse was used to test performance, Accesibility, Best Practices and SEO of the website.

<details>

<summary>Desktop</summary>

Home page 

<p align="center">
<img src="./assets/test/home_desktop.png">
</p>

About us page 

<p align="center">
<img src="./assets/test/about_desktop.png">
</p>

Blog page 

<p align="center">
<img src="./assets/test/blog_desktop.png">
</p>

Contact Us page 

<p align="center">
<img src="./assets/test/contact_desktop.png">
</p>

Search page 

<p align="center">
<img src="./assets/test/search_desktop.png">
</p>

Profile page 

<p align="center">
<img src="./assets/test/profile_desktop.png">
</p>

Logout page 

<p align="center">
<img src="./assets/test/logout_desktop.png">
</p>

</details>

<details>

<summary>Mobile</summary>

Home page 

<p align="center">
<img src="./assets/test/home_phone.png">
</p>

About us page 

<p align="center">
<img src="./assets/test/about_phone.png">
</p>

Blog page 

<p align="center">
<img src="./assets/test/blog_phone.png">
</p>

Contact Us page 

<p align="center">
<img src="./assets/test/contact_phone.png">
</p>

Search page 

<p align="center">
<img src="./assets/test/search_phone.png">
</p>

Profile page 

<p align="center">
<img src="./assets/test/profile_phone.png">
</p>

Logout page 

<p align="center">
<img src="./assets/test/logout_phone.png">
</p>

</details>


## Black box manual testing

<details>

<summary>TEST PLAN</summary>

<p align="center">
<img src="./assets/test/test_plan_1.png">
</p>

<p align="center">
<img src="./assets/test/test_plan_2.png">
</p>

<p align="center">
<img src="./assets/test/test_plan_3.png">
</p>

<p align="center">
<img src="./assets/test/test_plan_4.png">
</p>

</details>

<details>

<summary>TEST DATA</summary>

<p align="center">
<img src="./assets/test/test_data_1.png">
</p>

<p align="center">
<img src="./assets/test/test_data_2.png">
</p>

<p align="center">
<img src="./assets/test/test_data_3.png">
</p>

<p align="center">
<img src="./assets/test/test_data_4.png">
</p>

<p align="center">
<img src="./assets/test/test_data_5.png">
</p>

<p align="center">
<img src="./assets/test/test_data_6.png">
</p>

</details>

<details>

<summary>TEST LOG</summary>

<p align="center">
<img src="./assets/test/test_log_1.png">
</p>

<p align="center">
<img src="./assets/test/test_log_2.png">
</p>

<p align="center">
<img src="./assets/test/test_log_3.png">
</p>

</details>


## Unsolved Bugs

*  Updating post can update all fields except featured image: This means that users can make changes to all parts of a post, including the title, body text, and other fields, but they cannot update the featured image. If they want to change the image, they will need to upload a new one.

* Clicking on page numbers sometimes won't react: This is a user experience issue where users may click on a page number in the pagination, but the page does not load or react. This can be frustrating for users who are trying to navigate the website. This issue needs to be addressed to ensure a smooth user experience.

* In search results comment count is not showing: This means that when users search for posts, the comment count is not displayed in the search results. This information is important for users who want to quickly see how many comments a post has received. The comment count should be added to the search results to improve user experience.


[Back to README.](./README.md)