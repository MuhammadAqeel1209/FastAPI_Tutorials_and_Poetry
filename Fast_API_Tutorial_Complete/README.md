# FastAPI Tutorial

## Setup
Set up your virtual environment
```bash
python -m venv fast_api_tutorial
.\fast_api_tutorial\Scripts\activate
pip install -r requirements.txt
```
If you're running Linux or MacOS you'll instead run
```bash
python -m venv env
source ./env/bin/activate
pip install -r requirements.txt
```

## Running the app
`uvicorn main:app --reload`