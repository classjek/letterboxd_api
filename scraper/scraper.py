import requests
from bs4 import BeautifulSoup

class LetterboxdScraper:
    def __init__(self, base_url='https://letterboxd.com/'):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': 'Your Custom User Agent'})

    def get_user_profile(self, username):
        url = f'{self.base_url}/{username}/'
        response = self.session.get(url)
        if response.ok:
            soup = BeautifulSoup(response.text, 'html.parser')
            # Now you can parse the soup object to extract user information
            # Below is an example of how you might find a user's bio:
            # profile_bio = soup.find('div', class_='bio').get_text(strip=True)
            # Return a dictionary of the user profile information you scrape
            return {
                # 'bio': profile_bio,
                # Add other profile information fields here
            }
        else:
            print(f'Error fetching {url}: Status code {response.status_code}')
            return None
    