import requests
from plotly.graph_objs import Bar
from plotly import offline

def call_hn_api():
    """Make an API call to Hacker News and store the response.

    Returns
    -------
    r : Response
        Request response from API call
    response_dict : dictionary
        json dump of r
    """

    # Make an API call and store the response
    url = 'https://hacker-news.firebaseio.com/v0/itme/19155826.json'
    r = requests.get(url)
    print(f'Status code: {r.status_code}')

    # Store API response in a variable
    response_dict = r.json()
    print(response_dict.keys())

print(f"Total repositories: {response_dict['total_count']}")

# Explore information about the repositories.
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

# Examine 1st repository
repo_dict = repo_dicts[0]
print(f"Keys: {len(repo_dict)}")

if __name__ == '__main__':
    my_r, my_response_dict = call_hn_api()
