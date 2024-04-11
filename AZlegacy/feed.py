"""Define function view for the feed"""
from flask import (
        Blueprint, url_for, redirect, request, render_template
        )
from flask_login import login_required
import requests


@login_required
def feed():
    """Feed the postes page with data fetch from third-party API(reddit)
    """
    headers = {'User-Agent': "AZlegacy1"}
    url = "https://www.reddit.com/r/FinancialPlanning/hot.json?limit=100"
    r = requests.get(url, headers)
    hot = r.json().get('data').get('children')
    render_template("postes.html", hot=hot)
