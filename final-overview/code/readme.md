# Data Collection
The repository code subfolder within the final-overview folder contains an application used to extract and transform the data from NOAA, to better format and visualize the information system for use in Apple's IOS Weather app. <br/>

The application displays a real-time marine and coastal observation table from buoy stations operated by NOAA, other government agencies, universities, and research institutions. These observations are compiled through NOAA's National Data Buoy Center. <br/><br/>

## Application Instructions
> [!IMPORTANT]
> The following instructions are for Windows users. Be sure to change the necessary information to match your operating system.
<br/>

1. Download the noaa.py file and save into a designated file folder.
   - Example- _myproject_
2. Download the dashboard.hmtl file and save within that previous folder, but to a new folder as well.
   - _myproject\templates_
4. Open the Windows Command Prompt.
5. In the terminal enter the directory containing your project files.
   - _cd C:\Users\bmo\myproject_
6. Check if you have flask and python installed.
   - _flask --version_
   - _python --version_
   - If not, follow these steps: https://flask.palletsprojects.com/en/stable/installation/ https://wiki.python.org/moin/BeginnersGuide/Download
7. Create a virtual environment.
   - _.python -m venv .venv_
8. Activate the virtual environment.
   - _.venv\Scripts\activate_
9. Set the environment variable.
   - _set FLASK_APP=noaa.py_
10. Install dependencies.
    - _pip install flask pandas requests_
11. Run the application.
    - _flask run_
12. Navigate to the link provided in your Command Prompt. From there you can view the data and manurally refresh the page to see if any new real-time updates have occurred. 
