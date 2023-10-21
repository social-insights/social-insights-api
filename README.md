# Local Development Setup
1. Install dependencies

    From the `./functions` directory:  
    >   `pip install -g firebase-tools`  
    >   `pip intall -r requirements.txt`  

    Docker is also required. Download and run it. The Firebase emulator should do the rest.

2. Run `./functions/venv/Scripts/activate` to enter the virtual environment

3. Run `firebase emulators:start` to start the development server

# Note
This code will not work without the `credentials.py` file that is not published in this repository.

Instagram limits the number of requests that can be made to the API this API is using (around 200 requests per hour). Because of this, some requests could result in an error stating that the credentials are incorrect. The credentials are correct, but the requests are being blocked. Wait another 15 minutes or so and try again.
