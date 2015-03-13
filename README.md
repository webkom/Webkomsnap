# Webkomsnap

Currently just runs on my Droplet and adds whoever adds it.

If `USE_AUTH` is set to `True` in `config.py`, it'll only add users who have been added to a sqlite database. To add yourself just send a `POST` request to `http://188.166.9.128:9090/create` with a `JSON` content header and a payload with `{"username": $your_snapchat_username, "token": $super_secret_token}`.

Alternatively just run the `identify.sh` script with your Snapchat username as the only argument (e.g. `./identify.sh abroby`).
