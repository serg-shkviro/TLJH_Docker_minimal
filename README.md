# TLJH_Docker

Данный репозиторий является форком!!!

Спасибо большое оригинальному автору!

`git clone https://github.com/imSrbh/TLJH_Docker.git`

---
Дистрибутив Littlest JupyterHub (TLJH) поможет вам предоставить Jupyter Notebooks от 1 до 100 пользователям на одном сервере.

Шаги запуска используя только Docker:

1. Склонировать репозиторий
`https://github.com/serg-shkviro/TLJH_Docker_minimal.git`

2. Собрать образ
```
docker build -t tljh-dev .
```

3. Запуск без docker-compose (привелигерованный режим нужен). Если не уверены, насчёт настроек, то посмотрите подходят ли Вам данные [параметры](https://docs.docker.com/reference/cli/docker/container/run/#privileged): 

```bash
docker run --privileged -d --name=tljh-dev -p 12000:80 -v $(pwd):/srv/src:rw   tljh-systemd
```

4. Get a shell inside the running docker container.
```
	docker exec -it tljh-dev /bin/bash
```

5. Run the bootstrapper from inside the container (see step above): The container image is already set up to default to a dev install, so it’ll install from your local repo rather than from github.
```python
docker exec -it tljh-dev python3 /srv/src/bootstrap/bootstrap.py --admin admin:password
```


6. You should be able to access the JupyterHub from your browser now at `http://localhost:12000`. Congratulations, you are set up to develop TLJH!

>If you want to add more user, from admin panal you can create user and when user will be signing in the password of his choice which he uses at that first time sign in, that will will be the password for that user.

Inside the container `/home` -> You can see the user as `jupyter-abc`, `jupyter-xyz`

```
root@277863f1ab7e:/home# ls
jupyter-abc  jupyter-xyz
```

#### This was the basic testing setup.  
#### **Detailed info :** https://github.com/jupyterhub/the-littlest-jupyterhub



---

# Использование docker-compose

1.   `git clone https://github.com/imSrbh/TLJH_Docker.git`
2.  Create the container for service
```
docker-compose up --build -d
```

3. Run the container

```
saurabh@srbh:~/Git/TLJH_Docker$ sudo docker run \
   --privileged \
   --detach \
   --name=tljh-dev_web \
   --publish 12000:80 \
   --mount type=bind,source=$(pwd),target=/srv/src \
   tljh_docker_web
```
4.  Run in interactive mode
```
sudo docker exec -it tljh-dev_web /bin/bash
```

5. Setup admin password

```
python3 /srv/src/bootstrap/bootstrap.py --admin admin:password
```

6. See the JupyterHub in browser goto 

   localhost:12000

---
## TODO
- [x] script file(.sh)  
  - [x] Multi admin setup bash script.  
        [admin_setup.sh](https://gist.github.com/imSrbh/0349a99b393f351061b4a9932258816b)  
    
    (This is not mounted yet with the docker-compose )
    
  - [ ]   ~~User setup bash script.~~
  
- [x] Basic Docker-Compose  file

-  We can modify it's html also inside the running container `/opt/tljh/hub/share/jupyterhub/templates# `.