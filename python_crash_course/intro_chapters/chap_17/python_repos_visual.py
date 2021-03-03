import requests
from plotly.graph_objs import Bar
from plotly import offline


def call_github_api():
    """Make an API call to github for python projections and store the response.

    Returns
    -------
    r : Response
        Request response from API call
    response_dict : dictionary
        json dump of r
    """

    url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
    headers = {'Accept': 'application/vnd.github.v3+json'}

    r = requests.get(url, headers=headers)

    # Store API response in a variable
    response_dict = r.json()
    return r, response_dict

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

    # Store API response in a variable
    response_dict = r.json()

    return r, response_dict


def explore_repository(r, response_dict):
    """Output diagnostics of a dictionary retrieved from an API call.

    Parameters
    ----------
    r : Response
        Request response from API call
    response_dict : dictionary
        json dump of r

     """

    print(f'Status code: {r.status_code}')
    print(response_dict.keys())
    print(f"Total repositories: {response_dict['total_count']}")

    repo_dicts = response_dict['items']
    print(f"Repositories returned: {len(repo_dicts)}")

    # Examine 1st repository
    repo_dict = repo_dicts[0]
    print(f"Keys: {len(repo_dict)}")

    for key in sorted(repo_dict.keys()):
        print(key)

    print('\nSelected information about each repository:')
    for repo_dict in repo_dicts:
        print(f"Name: {repo_dict['name']}")
        print(f"Owner: {repo_dict['owner']['login']}")
        print(f"Stars: {repo_dict['stargazers_count']}")
        print(f"Repository: {repo_dict['html_url']}")
        print(f"Created: {repo_dict['created_at']}")
        print(f"Updated: {repo_dict['updated_at']}")
        print(f"Description: {repo_dict['description']}")


def visualize_repo_dictionary(r, response_dict):
    """Output diagnostics of a dictionary retrieved from an API call.

    Parameters
    ----------
    r : Response
        Request response from API call
    response_dict : dictionary
        json dump of r

     """
    # Store the name and star counts
    names, repo_links, stars, labels = [], [], [], []

    repo_dicts = response_dict['items']

    for repo_dict in repo_dicts:
        owner = repo_dict['owner']['login']
        description = repo_dict['description']
        label = f'{owner}<br />{description}'
        labels.append(label)

        stars.append(repo_dict['stargazers_count'])
        names.append(repo_dict['name'])

        repo_name = repo_dict['name']
        repo_url = repo_dict['html_url']
        repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
        repo_links.append(repo_link)

    data = [{
        'type': 'bar',
        'x': repo_links,
        'y': stars,
        'marker': {
            'color': 'rgb(60, 100, 150)',
            'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'},
            'opacity': 0.6,
        },
        'hovertext': labels,
        }]

    my_layout = {
        'title': 'Most-Starred Python Projects on Github',
        'titlefont': {'size': 28},
        'xaxis': {
            'title': 'Repository',
            'titlefont': {'size': 24},
            'tickfont': {'size': 14},
            'tickangle': 45,
        },
        'yaxis': {
            'title': 'Stars',
            'titlefont': {'size': 24},
            'tickfont': {'size': 14},
        },
    }

    fig = {'data': data, 'layout': my_layout}
    offline.plot(fig, filename='python_repos.html')


if __name__ == '__main__':
    r_github, response_dict_github = call_github_api()
    r_hn, response_dict_hn = call_hn_api()

    explore_repository(r_github, response_dict_github)
    # explore_repository(r_hn, response_dict_hn)

    visualize_repo_dictionary(r_github, response_dict_github)
