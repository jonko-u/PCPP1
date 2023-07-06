run it, so you should expect some delay – be patient and issue the following command:

npm install -g json-server

After successful installation, your screen should look like ours:

json-server window


We need to perform a brief test to ensure that the server is operating correctly. Do the following actions:

    download the JSON file cars.json from here: Download cars.json (zip archive) and save it in your home directory or any other directory you have the right to write into;
    return to the system console and issue the following command:

    json-server --watch cars.json


Note: the file name you put after –-watch should be specified absolutely, i.e., it has to contain the path leading to the downloaded file. Due to the fact that we’ve placed the file in our home directory (C:\User\user), the same directory in which we work during the tests (see the command prompt) we don't need to use the complete path. This doesn't mean you don't need it, either!

If everything went correctly, you'll see the following screen:

cars.json is open in console window


This means that the server is working and is ready to serve incoming connections. Don't let it wait. Let's connect to it!