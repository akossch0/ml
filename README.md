# ML Project - Mood-based playlist generation and multinomial genre classification of Spotify tracks

## Introduction

This project aims to generate mood-based playlists and classify the genre of Spotify tracks using machine learning techniques.

## Project setup

**Pre-requisites**:
- Python >= 3.8
- Pip >= 21.0

**Create venv, and install dependencies**:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

**Make a copy of the .env-template file and rename it to .env**:
Note: For the Spotify integration to work, you need to create a Spotify Developer account and create a new app. You will then get a client ID and a client secret which you need to add to the .env file. On top of this, we used OpenAI's API, which requires an API key. The `spotify-integration.ipynb` script will not work without these keys.

## Running the project

It is possible to run the eda and modeling notebooks found in the `eda` and `modeling` folders without the Spotify and OpenAI integration, as we did a staging of the data in the `data` folder.

However, for convenience, the notebooks will already be executed, making available the output of the runs.

## Contributors

- Jóhannes Kári Sólmundarson
- Ákos Schneider