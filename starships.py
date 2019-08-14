import argparse
import requests

def execute(episode_number=None):
    if episode_number:
        try:
            choice = int(episode_number)
            choices = sorted_film_titles()
            try:
                episode = choices[int(choice)-1]
            except IndexError:
                print("The eposide number provided is not a valid "
                    "episode number.")
                episode = request_episode()
        except ValueError:
            print("The episode number you provided is not an interger.")
            episode = request_episode()
    else:
        episode = request_episode()

    results = []
    # Get Starships
    starships_data = []
    for starship_url in episode['starships']:
        starship_data = (requests.get(starship_url)).json()
        starships_data.append(starship_data)
    for starship_data in starships_data:
        starship_result = {'starship': starship_data['name']}
        pilots_data = []
        for pilot_url in starship_data['pilots']:
            pilot_data = (requests.get(pilot_url)).json()
            pilots_data.append(pilot_data['name'])
        starship_result.update({'pilots': pilots_data})
        results.append(starship_result)
    print(results)
    return results

def query_films():
    url = "https://swapi.co/api/films/"
    r = requests.get(url = url)
    films = (r.json())['results']
    return films

def query_startship(episode=None):
    url =""
    r = requests.get(url = url)
    starships = r['']
    return starships

def request_episode():
    message = "Which episode do you want startships listed for? "
    #answer = input(message)
    #episode = validate_episode(answer)
    #return episode
    choices = sorted_film_titles()
    print("Episode List: ")
    print("_____________")
    for index, film in enumerate(choices):
        print(f'{index+1} - {film["title"]}')
    answer = input(message)
    return choices[int(answer)-1]

def sorted_film_titles():
    film_data = {}
    films = query_films()
    for film in films:
        film_data.update({film['episode_id']: film})
    choices = []
    for i in range(1, len(film_data)+1):
        choices.append(film_data[i])
    return choices

def test(args):
    print("Running tests")
    return None

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-e', '--episode', required=False, 
        help='The episode for which film to return data')
    parser.add_argument('-t', '--test', required=False, action='store_true',
        help='Run tests for functionaility of script')

    args = parser.parse_args()

    if args.test == True:
        test(args)
    else:
        if args.episode:
            results = execute(args.episode)
        else:
            results = execute()
        return results

if __name__ == '__main__':
    main()
    