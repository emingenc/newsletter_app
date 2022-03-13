# newsletter_app
Full-stack  newsletter app with flask blueprint views sqlalchemy backend  vuejs quasar framework with pinia statemanagement

## quick start

```bash
git clone https://github.com/emingenc/newsletter_app.git
cd newsletter_app
docker-compose build
docker-compose up
```

## create a new newsletter

### create a admin user

After docker compose up, you can create a new user with the 'http://localhost/#/register' url.

I did not put nav button for register since it is admin only.

For test purposes everyone can create admin user with email and password.


### login as admin


after creating a new user, you can login as admin with the 'http://localhost/#/login' url.

after you logged in there will be a button to create a new newsletter. 

and when you click detail view as logged in there will be  delete and edit buttons.

