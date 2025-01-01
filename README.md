# Mountain_Soup
This is a program to help monitor changes on the website Mountain Project. MountainProject.com is an online worldwide database of rock climbing routes. Users can submit new routes as they are created. Mountain soup is a helpful application because there is currently no functionality to receive updates when new routes are added.

# Packages 
Mountain_Soup uses the Python package Beautiful Soup to scrape data off of MountainProject.com. It creates a text file for a particular geographic area and records the number of rock climbing routes in this location. The next day, the program runs again and compares the quantities. If the integer value of routes is greater, an automated email is triggered to users of the program npotifying them of a new route. 




