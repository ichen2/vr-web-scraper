## about

I developed this web scraper while working for VRPreservation.org, a local non-profit. VRPresevation was founded out of a need for people to explore historical sites despite being unable to travel during the covid-19 pandemic. It provides virtual reality tours of historical sites in Louisiana, and gives local organizations/businesses the tools to create their own VR tours.

The site wanted to expand its services to provide tours outside of Louisiana. We found a free online resource that provided virtual tours from around the globe. I built this web scraper to parse this resource for links to the VR tours, so that we could link to them on our site. It also needed to find the name of the tour, and the location's coordinates (so that we could provide a google maps widget showing the site of each tour).

## implementation

I wrote the scraper using Python, and utilized the Selenium and BeautifulSoup libraries to help retrieve and parse the webpage. It first retrieves the url of each VR tour and stores these urls in a list. It then iterates through this list, loading each url and parsing the webpage for link to the VR tour. Once all the tour links have been retrieved, it outputs them to a csv file. A historical writing intern at VRPreservation then writes a description for each tour and uploads it to the website.

## outcome

This web scraper saved VRPreservation and estimated 50 hours of work. Without it, someone would have had to manually look through the online tour resource, and find a link to each individual tour. 

## future plans

I plan to continue to continue to expand this scraper to further fit VRPreservation's business needs. In the near future I will be adding functionality for finding the aforementioned GPS coordinates, so that we can embed a google maps widget showing the location of each tour. I also plan to adapt this program to automatically upload data for each tour onto VRPreservation.org.
