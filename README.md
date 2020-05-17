# Mini-Data-Pipeline
### A data pipeline using Snowplow-Micro and Flask

Miniblog is a simple 3 page blog made using Flask and a small amount of Bootstrap for minimal styling.
Its purpose is to test the ability to track user actions (in this case page-views) by sending data to a server 
created using Snowplow-Micro. 

Each time a user clicks on a link some data containing the page url and page name is amongst other information
is sent over to the server.

Fire up a Jupyter Notebook server by running `jupyter notebook` in the command line.
Open Analytics Report.ipynb and run the code to get a bar chart visualisation of the number of visits for each page 
of the blog.
