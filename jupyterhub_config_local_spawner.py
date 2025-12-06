# jupyterhub_config.py
import os

c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.DockerSpawner.image = os.environ['DOCKER_NOTEBOOK_IMAGE']
c.DockerSpawner.network_name = os.environ['DOCKER_NETWORK_NAME']
c.JupyterHub.hub_ip = '0.0.0.0'
c.DockerSpawner.remove = True

c.DockerSpawner.volumes = {
    # Персональная рабочая директория (Docker volume)
    'jupyterhub-user-{username}': '/home/jovyan/work',
}

c.DockerSpawner.notebook_dir = '/home/jovyan/work'

# Таймауты
c.Spawner.start_timeout = 300
c.Spawner.http_timeout = 300

# Аутентификация
c.JupyterHub.authenticator_class = 'dummyauthenticator.DummyAuthenticator'
c.DummyAuthenticator.password = 'password'
c.Authenticator.admin_users = {'admin'}
c.JupyterHub.admin_users = {'admin'}
c.Authenticator.allowed_users = {'admin'}

# Логирование
c.Spawner.debug = True
c.JupyterHub.log_level = 'DEBUG'
