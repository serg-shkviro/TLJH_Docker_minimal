FROM jupyterhub/jupyterhub:latest

RUN apt-get update && apt-get install -y sudo && rm -rf /var/lib/apt/lists/*

RUN useradd -m -s /bin/bash admin && \
    echo "admin:admin" | chpasswd && \
    usermod -aG sudo admin && \
    mkdir -p /home/admin/work && \
    chown -R admin:admin /home/admin

RUN mkdir -p /home/admin/.local/share/jupyter/runtime && \
    mkdir -p /home/admin/.jupyter && \
    chown -R admin:admin /home/admin/.local

RUN pip install --no-cache-dir \
    dockerspawner \
    jupyterhub-dummyauthenticator \
    jupyterlab \
    notebook

COPY jupyterhub_config_local_spawner.py /srv/jupyterhub/jupyterhub_config.py

WORKDIR /srv/jupyterhub
EXPOSE 8000

CMD ["jupyterhub", "-f", "/srv/jupyterhub/jupyterhub_config.py"]
