A simple Python program that extracts data from https://www.sslproxies.org/, scraping the IP Addresses and Port of a
proxy. It then saves said IP and Port into two lists, which become connected to each other to create the full proxy
address. Lastly, a random proxy is taken each time from the list, sending a request to check its availability. If it is
available, then execution of the program stops. On the contrary, if connection fails, then an error message shows up and
the specific proxy is removed from the list so the next time another is chosen, it won't be the same as before. 

Used libraries are:
- ReGex
- BeautifulSoup
- Selenium
- Random
- Requests

This can and will be used as a module for future projects that use a functioning proxy to scrape, alongside a user agent
for safety reasons.