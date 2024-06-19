To run world of games:

1. to clone the Repo:

git clone https://github.com/otzur243/WorldOfGames.git


2. Docker-Compose:

docker-compose up --build


3. to run the Game File:

docker exec -it worldofgames-web-1 sh python MainGame.py


4. to build the jenkins:

docker build -t jenkins_server1 -f Dockerfile1 .

docker run --name jenkins --detach --restart=on-failure --env JAVA_OPTS="-Dhudson.plugins.git.GitSCM.ALLOW_LOCAL_CHECKOUT=true" --publish 8080:8080 --publish 50000:50000 --volume //var/run/docker.sock:/var/run/docker.sock jenkins_server
