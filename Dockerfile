FROM jupyterhub/jupyterhub:latest

RUN pip install --no-cache-dir dockerspawner
RUN pip install --no-cache-dir jupyterhub-dummyauthenticator
RUN pip install --no-cache-dir jupyterlab
