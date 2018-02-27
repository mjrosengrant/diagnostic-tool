Thought Process

I decided to use a two app architecture for the project. I created an app `api` for the Symptom and Condition models, and an app called `webapp`. The webapp would be a single page Ajax application, that consumed data provided by the api.

The majority of my time was spent on the `api` app. I thought about using the Django REST framework, but decided it would be overkill. It was much easier to write functional views to return JSON.

I started with the modeling work, and then wrote the import_symptoms management command to load the provided test data into the database. then I worked on the views, and got the API urls routed and rendering. The last piece I got done was incrementing the symptom's search_count value when it's api view was hit.

After I had done all that, I moved onto the webapp. I planned on doing all of the API connections through Ajax. I set up the urls, views, and templates for the a basic one page app. I started digging into the Jquery, and quickly realized this was going to take way too long. I was already past the recommended 4 hour limit. I have left the webapp as a blank page.

If I had more time, I would definitely use it on building out the front end. Since I'm submitting the project as a pull request, I'm taking the educated guess that it will not be run locally. In my mind, it is worth the time setting up a strong API before moving on to the sites that consume it. For the equivalent of half a day's work, I think it is a solid foundation on which the client side application can be built.
