# maps_python_TokarM

This is a server side python code, which is using Falcon API and Google Maps API in order to retrieve specified information. Main purpose of this code is to find an address of closest point of interest, distance to this point, and name of the Business.

Input: Latitude, Longitude, Destination

Output: Address of Destination, Distance to the Destination, Name of the Business

Libraries: In requirements.txt you can find third party libraries, which are required to run this code.

Description: In order to run this code, first of all you need to get Google Maps API key, which you can get on google cloud website https://cloud.google.com. After you get a Google API key insert it into specified place inside the code. Next, If you are using Windows machine this code should automatically create a localhost server using Waitress library, so you can test it right away. For example, after you run a script, open your browser and go to http://localhost:8000/key?lat=42.991&lng=-87.667&destination=dunkin. It should return JSON file with an Address, Distance and name of the Business of specified location.

On Linux machine you can use Gunicorn library in order run the server. 
