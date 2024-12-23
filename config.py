# config.py
import os

class Config:
    SECRET_KEY = os.urandom(24)
    SPOTIFY_CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
    SPOTIFY_CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET')
    SPOTIFY_REDIRECT_URI = 'http://127.0.0.1:5000/callback'