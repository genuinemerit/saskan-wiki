# Virtual Environments

## virtualenv

Although versions of Python beyond 3.3 include the ``venv`` command, the ``virutalenv`` package is considered to be more robust and complete.

To install at the system level: ``sudo -H pip3 install --upgrade virtualenv``

It is important to modify .gitignore to ignore virtual environments. If you do want to version them, then use a separate git repo that is set up to handle large files.  This might be worth considering as an approach to installing app-level components.

Naming of virtual environments can be very generic. Prefixing with "env_" or "venv_" is popular and should probably be included in .gitignore.  Proposal is to name virtual environments aligned to the name of the git repo for the app, so like **venv_bow_orch** in my case.

Deploy them under a different account, and  maybe even under different servers than where development work happens.

The syntax for creating a venv is: ``virtualenv <path/to/env/directory>``.

The proposed pattern for the BOW apps is: ``$HOME/.virtualenvs/(venv_name)``.

For example, to create one named **venv_bow_orch**: ``virtualenv $HOME/.virtualenvs/venv_bow_orch`

And then to start it up:  ``source ~/.virtualenvs/venv_bow_orch/bin/activate``

Once in the venv, can do pip installs without using sudo. Like: ``pip install -r /path/to/requirements.txt``.
Not by installing individual packages. Not sure how to handle this via an external deployment tool.

To take down a venv, as an example:  ``source ~/.virtualenvs/venv_bow_orch/bin/deactivate``

### app directory

As far as the physical location of stuff associated with the deployed app that runs using the venv, proposal is: ``$HOME/bow/orch/app`` for my app named ``bow_orch``.  This way, it resides next to my local git repo for development and the wiki for that repo. When I deploy to another account (bow intead of pq) everything remains the same, only the account name is different.  And if want to put other "bow" apps in the same account, I just use a distinct directory.

Within the app directory, I want only software that needs to be there at runtime. For the bow_orch app, that includes some of what I previously kept in the build sub-directory.  Standard sub-dirs under app, I think, should be:

+ **static**
+ **templates**
+ **config**

Put ``requirements.txt`` in the ``config`` directory. Executing that will be my first test for deploying an app.

BUT! Before running anything, take a look at...

## virutalenvwrapper

This provides a nicer way to manage virtual environments. It is installed separately from virtualenv:
``sudo -H pip3 install --upgrade virtualenvwrapper``

Then it requires an edit to ``.bashrc`` or equivalent session start-up configuration. Here is where to define where all of our virtual environments reside, using the "WORKON_HOME" environment variable. We put both of these lines at the end of ``.bashrc``:

```bash
#!/bin/bash

export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
```

This provides a nice set of commands:

+ **mkvirtualenv** *test* -- create a venv named "test" and auto-activate it
+ **mktmpenv** *test* -- create a temporary venv named "test", auto-activate it, and destroy it when it is deactivated
+ **workon** *app* -- switch to an (existing) venv named "app"
+ **workon** -- list all available venvs
+ **deactivate** -- deactivate the currently activated venv
+ **rmvirtualenv** *app* -- remove (destroy) the venv named "app"

### Configuring vitualenvwrapper

After installing it (on bow-spt, that is my Digital Ocean dev environment), I was getting this message on both the root and pq accounts:

```bash
/usr/bin/python: No module named virtualenvwrapper
virtualenvwrapper.sh: There was a problem running the initialization hooks.

If Python could not import the module virtualenvwrapper.hook_loader,
check that virtualenvwrapper has been installed for
VIRTUALENVWRAPPER_PYTHON=/usr/bin/python and that PATH is
set properly.
```

My guess was that it is because /usr/bin/python is defaulting to python2.7.
And my guess was correct. So I did...

```bash
rm /usr/bin/python
sudo ln -s /usr/bin/python3.6 /usr/bin/python
```

... and that fixed it. I had modifid ``.bashrc`` in both root and in pq, which was probably not necessary because now I have ``.virtualenvs`` defined in both. I removed it from the root ``.bashrc`` and deleted the ``.virtualenvs`` stuff it had created in the root account.  This is something to put in the ``.bashrc`` for the bow account, once it is created.

Here is what ``.virtualenvs`` looks like initially:

```bash
pq@bow-spt:~$ ll .virtualenvs
total 56
drwxrwxr-x  2 pq pq 4096 Aug  4 20:30 ./
drwxr-xr-x 15 pq pq 4096 Aug  4 20:31 ../
-rwxr-xr-x  1 pq pq  135 Aug  4 20:30 get_env_details*
-rw-r--r--  1 pq pq   96 Aug  4 20:30 initialize
-rw-r--r--  1 pq pq   73 Aug  4 20:30 postactivate
-rw-r--r--  1 pq pq   75 Aug  4 20:30 postdeactivate
-rwxr-xr-x  1 pq pq   66 Aug  4 20:30 postmkproject*
-rw-r--r--  1 pq pq   73 Aug  4 20:30 postmkvirtualenv
-rwxr-xr-x  1 pq pq  110 Aug  4 20:30 postrmvirtualenv*
-rwxr-xr-x  1 pq pq   99 Aug  4 20:30 preactivate*
-rw-r--r--  1 pq pq   76 Aug  4 20:30 predeactivate
-rwxr-xr-x  1 pq pq   91 Aug  4 20:30 premkproject*
-rwxr-xr-x  1 pq pq  130 Aug  4 20:30 premkvirtualenv*
-rwxr-xr-x  1 pq pq  111 Aug  4 20:30 prermvirtualenv*
```

### Using virtualenvwrapper

```bash
pq@bow-spt:~/bow/orch$ mkvirtualenv env_bow_orch
Using base prefix '/usr'
New python executable in /home/pq/.virtualenvs/env_bow_orch/bin/python3
Also creating executable in /home/pq/.virtualenvs/env_bow_orch/bin/python
Installing setuptools, pip, wheel...
done.
virtualenvwrapper.user_scripts creating /home/pq/.virtualenvs/env_bow_orch/bin/predeactivate
virtualenvwrapper.user_scripts creating /home/pq/.virtualenvs/env_bow_orch/bin/postdeactivate
virtualenvwrapper.user_scripts creating /home/pq/.virtualenvs/env_bow_orch/bin/preactivate
virtualenvwrapper.user_scripts creating /home/pq/.virtualenvs/env_bow_orch/bin/postactivate
virtualenvwrapper.user_scripts creating /home/pq/.virtualenvs/env_bow_orch/bin/get_env_details
(env_bow_orch) pq@bow-spt:~/bow/orch$
```

Cool. Worked just as advertised.

At first I was little turned around regarding the file and directory structure. I can still cd all over the place.

Then I grokked that only thing that is different is my python environment. See notes above about setting up a deployed-app environment (file structure) that is distinct from the local git repo for the app.

### Proving requirements.txt

First, I can see that my usual collection of packages is not available when I am in the venv.

Then run pip install on the requirments.txt file; and show that the packages can now be imported.

```bash
(venv_bow_orch) pq@bow-spt:~/bow/orch/app/config$ python
Python 3.6.8 (default, Jan 14 2019, 11:02:34)
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import arrow
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'arrow'
>>> exit()
```

arrow is in my requirements.txt...

```bash
(venv_bow_orch) pq@bow-spt:~/bow/orch/app/config$ pip install -r ./requirements.txt
Collecting arrow (from -r ./requirements.txt (line 1))
...
```

Try importing it again...

```bash
(venv_bow_orch) pq@bow-spt:~/bow/orch/app/config$ pip freeze
arrow==0.14.4
Click==7.0
Flask==1.1.1
Flask-API==1.1
itsdangerous==1.1.0
Jinja2==2.10.1
MarkupSafe==1.1.1
param==1.9.1
pathlib==1.0.1
python-dateutil==2.8.0
six==1.12.0
tornado==6.0.3
tornado-jinja2==0.2.4
Werkzeug==0.15.5


(venv_bow_orch) pq@bow-spt:~/bow/orch/app/config$ python
Python 3.6.8 (default, Jan 14 2019, 11:02:34)
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import arrow
>>>
```

Good! I can do similar checks from a script by putting output of pip freeze into a grep and so on.

### deactive and workon

Simply typing **deactive** puts me back into "native" python mode.

```bash
(venv_bow_orch) pq@bow-spt:~/bow/orch/app/config$ deactivate
pq@bow-spt:~/bow/orch/app/config$
```

Then typing **workon env_bow_orch** gets me back into it.

```bash
pq@bow-spt:~/bow/orch/app/config$ workon env_bow_orch
(venv_bow_orch) pq@bow-spt:~/bow/orch/app/config$
```

That's all cool. What I have not succeeded at (so far) is executing command inside the venv from a remote or different account.  I can that that OK at the Linux level using ``su``, like ``"su {} -c 'pip3 install --upgrade virtualenv'".format(options.app_user)`` works fine when I am running a deployment script from a different account on the same server.  But when I tried running the commands to bring up the venv and then do stuff inside it, was not having luck.
