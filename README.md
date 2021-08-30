###### Leaf Jewellery
###### Milestone project 4: Full Stack Frameworks with Django– Code Institute
The project is made for business purposes, taking mostly B2C form as the shop is more interesting for 
individual shopping. This handmade jewellery site is balanced for customers to find jewellery for every day, 
to order it smoothly online and to enjoy. 
#### UX
Leaf Jewellery site is made super simple to meet the customer needs for quick online shopping purposes. 
The photographs of the jewellery were taken for customers to focus on exact piece of jewellery, 
without being distracted by surroundings. Images are used of a good quality for users to see the product 
they are buying or just admiring. 
#### User Stories
1. As a user I would love to see all the choice of products but would like to see the photo and description of individual pieces of jewellery as well.
2. I want to have an opportunity to see what products I have already chosen at any time of shopping.
3. Easy and comfortable payment system is very attractive.
4. I like the idea of having my own account and making it a bit more personalised.
5. Simple registration and log in log out system.
6. I always wondered why shop keepers do not want to hear a feedback on their shop so they can improve – 
it would be nice to have an opportunity to write them or at least to leave some kind of one product review.

#### Strategy
The goal of an online shop is to advertise the product and make customers comfortable to choose and 
buy handmade jewellery.
#### Scope
The site is structured to easily navigate through choosing, shopping, paying processes with maximum comfort.
#### Structure
The site structure is based on simplicity, keeping the customers buy hand and leading through choosing and 
purchasing process.
#### Sceleton
Using these wireframes were created to support the idea of a site.
https://drive.google.com/drive/folders/1EGLB31vevTqcGMHJhX39fmW4vqui5s_7?usp=sharing
#### Surface
The colour palette was chosen on Pinterest platform to benefit a simple design of the project.
#### Technologies
HTML – to create the foundation of a site.
CSS – to create visually pleasant web page.
JavaScript – to make it more interactive.
MongoDB – for data 
Python 
Bootstrap– to make it responsive.
Balsamiq – to create sketches of a future site.


#### Features
The customer can choose and purchase a chosen jewellery product, 
can look through the whole shop or just their bag, can contact the shop, 
can easily pay for their products, or delete a chosen product from their bag.
The project is responsive on all screen sizes.
#### Features left to implement
The future features: more payment opportunities and create and order your own design jewellery.

#### Deployment
The site was deployed to heroku using AWS. The Deployment process was
complicated so I really needed to follow all the steps from the course in an accurate manner.
The steps taken were as follows:
1. First while building the foundation of a project all the add ons and changes were commited and pushed to Github.
I had to add products and categories to my project manually.
2. Then heroku app was connected to a github. and there I had to add products manually as well.
3. AWS was chosen to store static and media files. 

#### Issues and Bugs
There were some issues with me undersstanding and implementing the new knowledge about secret key
- where it should be and how it has to look like. With a help of Tutor Team I was able to solve that quite quickly.
I also struggled to connect my database with heroku as I did not used fixtures from course project so that is why I entered everything manually.
Also Tutor team helped very much to understand models and to make my apps work and connect to my database.
There was always error 500 thrown when somebody needed to register or log in so I put the setting of DEBUG to True and with a help of my mentor and tutor team was able to solve the issue by reading and understanding the console logs and how to fix them.

#### Testing
Following user stories all the functions that users can interact with were tested.
There are many ways to check on every product the site has and to search for something specifically, I searched by colours and everything worked in an ideal way.
There was a bit of a problem to register and to log in for the users before, but now the error 500 is fixed and users can register and start being a member with a profile, as well as log in and of course see their orders that were made earlier. One can still shop without registering.
There are two ways for the user of a shop to leave some feedback for the shop owner as they can leave a comments about general things or their ideas about improving a shop or some issue that they experience or they can leave a review about a specific product. Those features were tested and are working.
The site was tested on a mobile gadgets as well as laptops with different browsers.



#### Media
Photographs, Jewellery and drawings are made by me.


#### Acknowledgements
My Mentor for support and updates. Tutor support at Code Institute for their support and endless patience.

















![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome Laura Kubiliene,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Gitpod and the extensions we use.

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidently make it public then you can create a new one with _Regenerate API Key_.

## Updates Since The Instructional Video

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

---

Happy coding!
