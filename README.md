# ORBITUARY WEB APPLICATION

## Description
This  web application  allows users to post obituaries of their loved ones,  to view obituaries of other people and delete their own obituaries. 


## table of contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Features](#features)
4. [Acknowledgements](#acknowledgements)
5. [License](#license)


## Installation
1. Clone the repository  
``git clone link`` 

2. Setup Virtualenvironment   
``virtualenv -p python3 directoryName``  

3. Install the required dependencies    
``pip install -r requirements.txt``  

4. To run the application, enter the root folder(directory at which your manage.py file is locatedand run the following command)    
``python manage.py runserver``  



## Usage
1. Migration  
``python manage.py migrate``

2. Create a super user account  
``python manage.py createsuperuser``  

3. Login to the admin dashboard 
``http://address:port/admin``

There are 3 views namely:
1. Home view : /
2. userview/ : for displaying deceased details
3. usercreate/  : for entering deceased details