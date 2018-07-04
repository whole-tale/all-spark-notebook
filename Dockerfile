FROM jupyter/all-spark-notebook:e7000ca1416d

COPY ./.wt/jupyter_notebook_config.py /home/$NB_USER/.jupyter/jupyter_notebook_config.py
COPY ./.wt/custom.js /home/$NB_USER/.jupyter/custom/custom.js
