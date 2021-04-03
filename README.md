# spot-on-ify
Playlist Recommendation App based on Spotify Web API

## Setup

### Setting up the Spotify Web API
- Head to ![developer.spotify.com](developer.spotify.com) and Login with your Spotify.
- Once redirected to your Dashboard, Click on 'Create and App'.
- Register your app by giving it a name and a description and confirm.
- In your app dashboard, copy the `Client ID` and paste it in the respective field in `config.py`.
- Click on `Show Client Secret` to reveal your `Client Secret` and paste in `config.py`.

❗ Your Client ID and Client Secret are to be highly confidential. Do not make it public at any costs. ❗

### Running the app:
- Clone this repo to your system.
- Navigate to `config.py` and replace the CLIENT_ID and CLIENT_SECRET with the values in your app dashboard.
      - Copy the `Client ID` from the dashboard, paste it in place of "YOUR_CLIENT_ID" enclosed by quotes.
      - Click on `Show Client Secret` to reveal your `Client Secret` and replace "YOUR_CLIENT_SECRET" with your string.
- Run `main.py`.
