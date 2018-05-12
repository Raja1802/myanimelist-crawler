'''
This script can be used to create user list from [**Myanimelist**](https://myanimelist.net/) using any forum post.
The idea is to extract user fro the post.

Output file contains list of username, one at each line.
'''
import time
from bs4 import BeautifulSoup
import requests
import sys


def get_club_page(clubID, i):
    parameter = {"action": "view", "t": "members", "id": clubID,
                 "show": i}  # # Set up the parameters we want to pass

    url = 'https://myanimelist.net/clubs.php'  # base url

    page = requests.get(url, params=parameter)  # getting page

    while page.status_code == 429:  # too many requests
        time.sleep(1)
        page = requests.get(url, params=parameter)  # getting page
    return page


def create_user_list_from_club(clubID, outputFile):
    f = open(outputFile, 'w')  # opening output file in write mode

    i = 0  # initial user counter
    count = 0  # storing number of users

    while True:
        print('\nFetching username from users number', i + 1, 'through user number', i + 36,
              '...')  # console message indicating number of comments

        page = get_club_page(clubID, i)

        if page.status_code == 200:
            c = page.content
            soup = BeautifulSoup(c, 'html.parser')  # parsing page

            # checking availability. No access still returns 200 :(
            no_access_div = soup.find('div', 'badresult')
            if no_access_div is not None and no_access_div.text == 'No access':
                # no access to this club
                print('no access here')
                break

            # print('Getting username:')
            print('Getting usernames from URL {}'.format(page.url))
            # getting username in the page
            users = soup.find_all('td', 'borderClass')
            for j in range(0, len(users)):
                count = count + 1
                # print(users[j].div.a.text)
                f.write(users[j].div.a.text + '\n')  # Writing unique username in the output file

            i = i + 36  # increamenting user count
        else:
            print('Got status code {}. No more page left in the forum. Done fetching...\n'.format(page.status_code))
            break

    print('Got', count, 'unique user.')

    f.close()  # closing file

    print('Done writing username to output file.\nOutput:', outputFile)


if __name__ == '__main__':
    # getting topic ID
    # topic ID get be seen in the url of any forum post
    # Example: this url 'https://myanimelist.net/forum/?topicid=1582476' have a topic ID = 1582476
    clubID = None
    try:
        clubID = int(sys.argv[1])
    except IndexError:
        print('Please provide all arguments.\nSyntax:\npython creteUserListFromPost.py topicID [UserList.txt]')
        sys.exit()
    except:
        print('Unexpected error.')

    # setting name of output file
    if len(sys.argv) == 3:
        outputFile = str(sys.argv[2])
    else:
        outputFile = 'UserList.txt'

    create_user_list_from_club(clubID, outputFile)
