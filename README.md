# Running transcription locally


## Install Python

Ensure Python is installed from the [official Python website](https://www.python.org/downloads/).

## Set Up and Activate Virtual Environment

1. **Create a virtual environment:**

   ```sh
   python -m venv env
   ```

2. **Activate the virtual environment:**

   - **Windows:**

     ```sh
     .\env\Scripts\activate
     ```

   - **macOS/Linux:**

     ```sh
     source env/bin/activate
     ```

## Manage Dependencies


1. Install from `requirements.txt`:

   ```sh
   pip install -r requirements.txt
   ```

2. Install ffmpeg

    ```command
    brew install ffmpeg
    ```


## Run the script

```command
python starter.py
```