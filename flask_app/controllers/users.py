from flask_app.models.user import User
from flask_app import app
from flask import render_template, jsonify, redirect, request
import os
import requests

@app.route('/')
def home():
    r = requests.get(f'https://api.github.com/users/xtina-lt/repos')
    output=r.json()
    # list of dictionaries in JSON
    # [{'id': 435033175, 'node_id': 'R_kgDOGe4UVw', 'name': 'bank_first_national_north_pole', 'full_name': 'xtina-lt/bank_first_national_north_pole', 'private': False, 'owner': {'login': 'xtina-lt', 'id': 92126039, 'node_id': 'U_kgDOBX27Vw', 'avatar_url': 'https://avatars.githubusercontent.com/u/92126039?v=4', 'gravatar_id': '', 'url': 'https://api.github.com/users/xtina-lt', 'html_url': 'https://github.com/xtina-lt', 'followers_url': 'https://api.github.com/users/xtina-lt/followers', 'following_url': 'https://api.github.com/users/xtina-lt/following{/other_user}', 'gists_url': 'https://api.github.com/users/xtina-lt/gists{/gist_id}', 'starred_url': 'https://api.github.com/users/xtina-lt/starred{/owner}{/repo}', 'subscriptions_url': 'https://api.github.com/users/xtina-lt/subscriptions', 'organizations_url': 'https://api.github.com/users/xtina-lt/orgs', 'repos_url': 'https://api.github.com/users/xtina-lt/repos', 'events_url':
    count = 0 # to count dictionaries
    lst=[]
    print(lst)
    if output == 'message':
        # empty list to add dictionaries of output
        for i in output:
            print(i)
            count += 1;
            data={
            # for every i in json request
                "name" : i['name'],
                "language": i['language'],
                "description": i['description'],
                "url": i['html_url']
            }
            lst.append(data)
    return render_template('index.html', output = lst)

@app.route('/test')
def users():
    results = User.select_all()
    print(results)
    return render_template('test.html', output = results)
