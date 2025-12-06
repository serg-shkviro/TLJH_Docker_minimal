# jupyterhub_config.py
import os
from jupyterhub.spawner import LocalProcessSpawner

# Отключаем DockerSpawner
c.JupyterHub.spawner_class = 'jupyterhub.spawner.LocalProcessSpawner'

# Настройки для LocalProcessSpawner
c.Spawner.default_url = '/lab'
c.Spawner.debug = True

# Рабочая директория пользователей
c.Spawner.notebook_dir = '~/work'

# Окружение для пользовательских процессов
c.Spawner.environment = {
    'JUPYTER_ENABLE_LAB': '1',
    'HOME': '/home/{username}'
}

# Use DummyAuthenticator for testing
c.JupyterHub.authenticator_class = 'dummyauthenticator.DummyAuthenticator'
c.DummyAuthenticator.password = 'password'
c.Authenticator.admin_users = {'admin'}

c.JupyterHub.admin_users = {'admin'}
c.Authenticator.allowed_users = {'admin'}

# Пользовательские директории
import subprocess
import pwd
import grp

def create_user_home(spawner):
    username = spawner.user.name
    home_dir = f'/home/{username}'
    
    # Создаем пользователя и домашнюю директорию
    if not os.path.exists(home_dir):
        subprocess.run(['useradd', '-m', '-s', '/bin/bash', username])
        subprocess.run(['mkdir', '-p', f'{home_dir}/work'])
        subprocess.run(['chown', '-R', f'{username}:{username}', home_dir])

c.Spawner.pre_spawn_hook = create_user_home
