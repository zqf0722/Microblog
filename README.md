# [Microblog](https://qz-microblog.herokuapp.com/)

It's a web application developed with python, flask, SQL, ElasticSearch, Azure, REACT, Redis, HTML, JSON, JavaScript, and many other tools.

You can access and play with the microblog yourself with the link above (click Microblog). I have put it online with the help of  Heroku.

Register an account and post your thoughts on the website. You can also follow others to see what they say about their lives. 

The Blog also provides l18n and L10n, searching, server-side real time translating.

There are other functionalities waiting for you to explore

## Provide L10n and l18n for Chinese and English.
If you want to add your own translation. Follow the instructions below.

First Run `flask translate init #yourlanguagecode`

Run `flask translate update`

Then translate all the sentences in `/app/translation/yourlanguagecode/LC_MESSAGES/messages.po`

Finally run `flask translate compile` to finish translating.
