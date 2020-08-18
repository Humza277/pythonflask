This is a readme of my flask project 

This code makes a simple web app that takes a user input to display 
that input onto a webpage 


# What is MVC
The Model-View-Controller (MVC) is an architectural pattern that separates an application into three main logical components: the model, the view, and the controller. 
Each of these components are built to handle specific development aspects of an application. 

Model
The Model component corresponds to all the data-related logic that the user works with. 
This can represent either the data that is being transferred between the View and Controller components or any other business logic-related data. 
    
    For example, a Customer object will retrieve the customer information from the database, manipulate it and update it data back to the database or use it to render data.

View
The View component is used for all the UI logic of the application. 

    For example, the Customer view will include all the UI components such as text boxes, dropdowns, etc. that the final user interacts with.

Controller
Controllers act as an interface between Model and View components to process all the business logic and incoming requests, manipulate data using the Model component and interact with the Views to render the final output. 
    
    For example, the Customer controller will handle all the interactions and inputs from the Customer View and update the database using the Customer Model. The same controller will be used to view the Customer data.

# Installing relevant packages

Flask
    
Flask-Login: to handle user sessions (the presence of a user with a specific IP address)
    
    Sessions create a file in a temporary directory on the server where registered session variables and values (username, password) are stored
    Cookies are stored in client-side machine

Flask-SQLAlchemy: to represent the user model and interface with the database

23/07/2020

Log in method has been added 
Working on the user sign up functionality 