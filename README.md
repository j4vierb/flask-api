# HW-python

This is a demo project to learn about CI/CD pipelines in github using Github Actions.

## To run it

### Install Flask in your Virtual Environment

Just follow [this tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-windows-10).

Then, run the next command to install Flask:

```py
pip install -r requirements.txt
```

### Configure some variables

Run the following commands (I used WSL):

```sh
export FLASK_APP=app
export FLASK_ENV=development
```

### Finally, run it

Just run the next command in the shell

```sh
flask run
```

