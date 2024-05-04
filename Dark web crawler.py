import requests
from stem import Signal
from stem.control import Controller
from bs4 import BeautifulSoup

# Function to make requests through Tor
def make_tor_request(url):
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password="your_tor_password")
        controller.signal(Signal.NEWNYM)
    proxies = {'http': 'socks5h://127.0.0.1:9050', 'https': 'socks5h://127.0.0.1:9050'}
    response = requests.get(url, proxies=proxies)
    return response.content

# Function to crawl a dark web page
def crawl_dark_web(url):
    try:
        html_content = make_tor_request(url)
        soup = BeautifulSoup(html_content, 'html.parser')
        # Process and analyze content here
        for link in soup.find_all('a'):
            if link.get('href').endswith('.onion'):
                # Explore this onion link recursively
                crawl_dark_web(link.get('href'))
    except Exception as e:
        print(f"Error crawling {url}: {e}")

# Main function
def main():
    # Start crawling from a known dark web directory
    starting_url = "http://directory777onion.at"
    crawl_dark_web(starting_url)

if __name__ == "__main__":
    main()
