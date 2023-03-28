# Features

### Navbar

* Navigation bar with website logo at the top of the website allows users access different pages such as Home, About Us , Blog, Contact, Login/logout, Registration/Profile, search.
* Every page has an active navbar link so users know on what page they are.

<p align="center">
<img src="./assets/features/navbar.png">
</p>

* From the navigation bar menu user can also access all categories availible or adding new blog post

<p align="center">
<img src="./assets/features/navbar_blog.png">
</p>

* From the navigation bar manu user can also access search bar and look for specific posts or authors

<p align="center">
<img src="./assets/features/navbar_search.png">
</p>

* For smaller devices navbar is collapsible

<p align="center">
<img src="./assets/features/navbar_phone.png">
</p>

### Footer 

* Footer section at the bottom of the website include social links with glowing hover effect and contact details

<p align="center">
<img src="./assets/features/footer.png">
</p>

### Home page 

* The Home page design features carousel that welcomes user with 5 images that changes automatically every 5s. The carousel also includes a cover with a short text and an Explore button. Once clicked, the button brings the user to the bottom of the page where they can learn more about the website and its content.

* Carousel

<p align="center">
<img src="./assets/features/carousel.png">
</p>

* Bottom of the home page with welcome text

<p align="center">
<img src="./assets/features/welcome_text.png">
</p>

### About Us page

* About us page provides more information about the website and it's background.

<p align="center">
<img src="./assets/features/about_us.png">
</p>

### Contact Us page

* This page allows users to send email to the website's administrator with a contact form required fields such as message topic, first name, last name , email address and text message.

<p align="center">
<img src="./assets/features/contact_us.png">
</p>


* This email form is using EmaiJS API to send messages directly to the website owner.
* Once email has been sent succesfully, user will recieve an email with text thanking for the enquiry and also a notification from the javascript alert box with their first name input. 

<p align="center">
<img src="./assets/features/contact_us_email_sent.png">
</p>

<p align="center">
<img src="./assets/features/contact_us_email_notification.png">
</p>

### User registration and authentication pages

* This pages allow users to create an account, log in and access additional features of the website such as commenting and liking or profile view.

Sign up page 
<p align="center">
<img src="./assets/features/sign_up.png">
</p>

Login page
<p align="center">
<img src="./assets/features/login.png">
</p>

Log out page
<p align="center">
<img src="./assets/features/logout.png">
</p>

### User Profile page

* This page allow users to view their profile with additional details such username, email address, date registered and how long they are logged in.
* Users can also change their username or email adress clicking on the Edit profile, once they update their username or email address, message with text "Profile has been updated" or Error message if profile was no updated is print in the Profile view box.
* If Users created posts they are able to see them in the profile box with their published or draft posts with ability to change them or delete them.

Profile details
<p align="center">
<img src="./assets/features/profile.png">
</p>

Edit profile form
<p align="center">
<img src="./assets/features/edit_profile.png">
</p>

Edit profile success message
<p align="center">
<img src="./assets/features/edit_profile_success.png">
</p>

User posts list
<p align="center">
<img src="./assets/features/profile_posts.png">
</p>

### Blog page

* On this page users can view all latest blog posts sorted by a date.
* Every post has a featured image or a default image if author won't upload an image.
* Every post has also additional details such as Title of the post, author, date created, category, num. of likes, num. of comments, update or delete post button if user is author of the post or superuser.

<p align="center">
<img src="./assets/features/blog.png">
</p>

* After clicking on one of the post image, title or "Read More link in the excerpt text" user is redirected to a post detail page where he can read more about the post.

<p align="center">
<img src="./assets/features/blog_post.png">
</p>

* Users can also view latest posts sorted by category.

<p align="center">
<img src="./assets/features/category.png">
</p>

### Blog post managment

* If user is authenticated and has staff or superuser privilege they can add blog posts.

<p align="center">
<img src="./assets/features/create_post.png">
</p>

* If user is author or superuser they can edit their posts.

<p align="center">
<img src="./assets/features/edit_post.png">
</p>

* If user is author or superuser they can delete their posts.

<p align="center">
<img src="./assets/features/delete_post.png">
</p>

### Search page

* Search bar in the navbar enables users to find blog posts by title or their author.

<p align="center">
<img src="./assets/features/search_bar.png">
</p>

* Once searched page will redirect to the search results page and show all the relevant posts.

<p align="center">
<img src="./assets/features/searched_success.png">
</p>

* If search post is not found, relevant text is displayed.

<p align="center">
<img src="./assets/features/search_not_found.png">
</p>

## Additional features

### Pagination

* All blogs posts page and categories page has pagination feature included displaying 5 posts per page.
* This allows users to  navigate through large dataset by breaking it up into smaller, more manageable pages.
* Pages include buttons to move between pages and also number of the current page displaying.

<p align="center">
<img src="./assets/features/pagination.png">
</p>

### Like/Unlike button

* If the user is authenticated they can like or unlike the post.

<p align="center">
<img src="./assets/features/like.png">
</p>

### Comments

* Every post has a comment section, if post has not been commented yet, "No comments yet." text is displayed.

<p align="center">
<img src="./assets/features/no_comment.png">
</p>

* If commented 

<p align="center">
<img src="./assets/features/commented.png">
</p>

* Authenticated users can comment posts via comment form.

<p align="center">
<img src="./assets/features/comment_form.png">
</p>

* Once comment is succesfully sent, users will get a notification with comment awaiting approval.

<p align="center">
<img src="./assets/features/comment_approve.png">
</p>

* Displayed comment once approved.

<p align="center">
<img src="./assets/features/comment_approved.png">
</p>


[Back to README.](./README.md)