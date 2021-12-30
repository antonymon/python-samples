# Website whit Python using Flask and Congnitive Services to translate text

## Prerequisites
- Install Python 3.6 or later (if not already installed)
- Python virtual enviroment
- Install Flask and other liberies
- Create Translator service
- Create environment variables
### Install Python 
You can confirm wherher it's installed by executing one of the follewing comands:
| OS | Command |
| --- | --- |
| Windows | `python --vesion` |
| MacOs or Linux| `python3 --version` |

### Create a Python virtual enviroment
Is folder that contains all of the libraries we need to run applicaction, including the Python runtime itself.
```console
# Windows
# Create the environment 
python -m venv venv
# Activate the environment 
.\\venv\\scripts\\activate`

# macOS or Linux
# Create the environment 
python3 -m venv venv
# Activate the environment 
source ./venv/bin/activate
```
**Note:** If venv is not available, you need to install  in *macOS or Linux* the command `apt install python3-venv` or for install in [Windows](https://mothergeo-py.readthedocs.io/en/latest/development/how-to/venv-win.html) `pip install virtualenv`.

### Install Flask and other liberies
In console, run command `code .` to open the directory in Visual Studio Code or open other editor code.

### Create Translator service
We'll need an [Azure Account](https://azure.microsoft.com/en-us/), now get keys for the Transalator service.
    
- In [Azure Portal](https://portal.azure.com/#home) select **Create a resource** in search box, enter Translator and selected **Create**.
- Complete the **Create Translator** whit your values and don't forget to select "Pricing tier: Free F0".
- Select **Go to resource**, **Rexource Management** > **Keys and Endpoint** and copy **KEY 1**, **ENDPOINT** , **LOCATION**.

### Create environment variables
- In Visual Studio Code or other create new file and naming it **.env**
- Paste the followin text into **.env**
    ```text
    KEY=your_key
    ENDPOINT=your_endpoint
    LOCATION=your_location
    ```
- Replace the placeholders with your secrets


## Test the application
Use the integrate terminal inside Visual Studio Code to make our lives a little easier.
- Open the integrate terminal en Visual Studio Code or terminal to be used in the project path.
- Set the Flask runtime to development
   ```
    # Windows
    set FLASK_ENV=development

    # Linux/macOS
    export FLASK_ENV=development
    ```
- Run the application `flask run`
- Open the aplication in browser by navigatin to url show in terminal, example: http://127.0.0.1:5000/ 