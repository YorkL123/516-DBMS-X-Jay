This course project is intended as a 'standard option'.

Created by [Rickard Stureborg](http://www.rickard.stureborg.com) and [Yihao Hu](https://www.linkedin.com/in/yihaoh/) for CS316, adapted for CS516.

## SETUP
After you clone/fork this repo, if you are using Mac system, go into the repo directory and then run ```./install.sh```. 

This will install a bunch of things, set up an important file called `.flashenv`. 
It may throw errors when creating database because the shell script for DB is not for Mac. To create a PostgreSQL database named `amazon`, you may need to manually run the following commands in your terminal:

```
source ../.flaskenv
createdb amazon
```

If you are using Windows VM, delete 'install.sh' and 'db/setup.sh' mentioned above, 
and use files 'install_win.sh' and 'db/setup_win.sh'. You may change their filenames, deleting "_win" and make them back to 'install.sh' and 'db/setup.sh'. After that, run '''./install.sh''' as usual.

## DB SQL IMPORTANT!
PLEASE GO TO db/create.sql & db/load.sql TO CREATE/CHANGE YOUR DATABASE
If your existing DB tables have conflicts, you may DROP all your tables, then create new tables by:

1. In your **/db** folder , run the command line: 

**psql -af create.sql amazon**

2. In your **/db/data** folder, run the command line:

**psql -af ../load.sql amazon**

**(../ is a MUST because you need to jump outside the folder)**


## Running/Stopping the Website

To run your website, in your VM, go into the repository directory and issue the following commands:
```
source env/bin/activate
flask run
```
The first command will activate a specialized Python environment for running Flask.
While the environment is activated, you should see a `(env)` prefix in the command prompt in your VM shell.
You should only run Flask while inside this environment; otherwise it will produce an error.

If you are running a local Vagrant VM, to view the app in your browser, you simply need to visit [http://localhost:5000/](http://localhost:5000/).

To stop your website, simply press <kbd>Ctrl</kbd><kbd>C</kbd> in the VM shell where flask is running.
You can then deactivate the environment using
```
deactiviate
```


