# Divvy

This is a mini project designed by Divvy to test basic coding and container knowledge. The objective of this project is to list all Star Wars starships for any given episode, including the names of the pilots for each starship.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

If running the script locally:
* python3
* pip3
* requests

```
$ pip3 install requests
```

If running container in Docker:
* Docker

If running using the Helm Chart:
* VirtualBox
* Kubectl
* MiniKube
* Helm


### Running script locally

Run the script - not providing an episode:

```
$ python3 starships.py 

Episode List: 
_____________
1 - The Phantom Menace
2 - Attack of the Clones
3 - Revenge of the Sith
4 - A New Hope
5 - The Empire Strikes Back
6 - Return of the Jedi
7 - The Force Awakens
Which episode do you want startships listed for? 
```

Run the script - providing the episode via an argument:

```
$ python3 starships.py -e 1
```

Example output:

```
[
  {
    "pilots": [
      "Ric Olié"
    ],
    "starship": "Naboo Royal Starship"
  },
  {
    "pilots": [
      "Darth Maul"
    ],
    "starship": "Scimitar"
  },
  {
    "pilots": [],
    "starship": "Republic Cruiser"
  },
  {
    "pilots": [],
    "starship": "Droid control ship"
  },
  {
    "pilots": [
      "Anakin Skywalker",
      "Gregar Typho",
      "Padmé Amidala"
    ],
    "starship": "Naboo fighter"
  }
]
```

### Running container via Docker

A step by step series of examples that tell you how to get a running container in Docker.

Create the container using the provided `mwerickso/divvy` build. _Optional: Map a local port to container port 80 as provided in the example._

```
$ docker run -d -p 1337:80 -ti mwerickso/divvy
```

Test the API via browser [here](http://localhost:1337/starships_by_episode/1), or via command line:

```
$ curl http://localhost:1337/starships_by_episode/1
```

Substitute the ending `id` with the number of the episode to query.

```
$ curl http://localhost:1337/starships_by_episode/2
```

To access the container and run the script - prompting for user input of which episode to query.

```
$ docker exec -it <container-name> /bin/ash
$ python3 starships.py
```

To access the container and run the script - passing in the episode to query as an argument.

```
$ docker exec -it <container-name> /bin/ash
$ python3 starships.py -e 1
```

### Running via Helm Chart and MiniKube

A step by step series of examples that tell you how to get a running container onto MiniKube by using a Helm Chart.

Ensure MiniKube is running and your kubectl context is configured for MiniKube. Also ensure that Helm has initialized for your MiniKube Kubernetes cluster:

```
$ helm init
```

Using Helm, install the chart from the project dirctory:

```
$ cd path/to/project
$ helm install --name endpoints endpoints/
```

Create local port-forwarding to the container:

```
$ export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=endpoints,app.kubernetes.io/instance=endpoints" -o jsonpath="{.items[0].metadata.name}")
$ kubectl port-forward $POD_NAME 8080:80
```

Test the API via a browser [here](http://localhost:8080/starships_by_episode/1) or via the command line:

```
$ curl http://localhost:8080/starships_by_episode/1
```

To access the pod and run the script:

```
$ kubectl exec -it $POD_NAME -- /bin/ash
/app # python3 starships.py
```

## Authors

* **Matthew Erickson** - *All work* - [mwerickso](https://github.com/mwerickso)

## Acknowledgments

* Thanks to the authors and contributors of [Star Wars API](http://swapi.co) in which this project depends on.
