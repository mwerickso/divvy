docker pull
docker run -d -p 1337:80 -ti divvy
http://localhost:1337/starships_by_episode/1

docker exec -it <container-name> /bin/ash
python3 starships.py (-e <int>)