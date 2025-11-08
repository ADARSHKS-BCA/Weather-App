# Setup Instructions

## Setting up the API Key

You need to set the `WEATHER_API_KEY` environment variable before running the app.

### Option 1: Using .env file (Recommended)

1. Install python-dotenv:
```bash
pip install python-dotenv
```

2. Create a `.env` file in the project root:
```
WEATHER_API_KEY=your_actual_api_key_here
```

3. Update `weatherapp/views.py` to load from .env (add at the top):
```python
from dotenv import load_dotenv
load_dotenv()
```

### Option 2: Set environment variable directly

**Windows (PowerShell):**
```powershell
$env:WEATHER_API_KEY="your_api_key_here"
python manage.py runserver
```

**Windows (Command Prompt):**
```cmd
set WEATHER_API_KEY=your_api_key_here
python manage.py runserver
```

**Linux/Mac:**
```bash
export WEATHER_API_KEY=your_api_key_here
python manage.py runserver
```

### Option 3: Set permanently (Windows)

1. Search for "Environment Variables" in Windows
2. Click "Edit the system environment variables"
3. Click "Environment Variables"
4. Under "User variables", click "New"
5. Variable name: `WEATHER_API_KEY`
6. Variable value: your API key
7. Click OK and restart your terminal

