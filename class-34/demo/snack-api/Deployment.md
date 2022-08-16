# Deployment
## Database Deployment:

1- Created an account and a database on https://api.elephantsql.com/

2- We changed the database settings to read from .env

3- We add the required information for online database connection to the .env

## Server Deployment

1- Install Heroku Cli

2- Login to Heroku on Browser

3- Login to heroku from terminal using ```heroku login```

4- Create an app on heroku using the following command ```herok apps:create app-name```

5- Check the local repo is connected with heroku's repo using the following command ```git remote -v```

6- If you did not heroku in the remote so add it using ```heroku git:remote -a app-name```

7- Run ```heroku stack:set container```

8- Run ```python manage.py collectstatic```

8- ```git add .```

9- ```git commit -m "message"```

10- ```git push heroku main```
