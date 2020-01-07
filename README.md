## News HighLights
News highlight is a news application that gives access to the users about what is happening worldwide. The application posses news from different sources.

### Author
Munene Mike

### BDD
Behaviour	        Input	                     Output
Showcasing news 	Navigate through sources	Read requested news

### Installation Requirements
python3.6
pip
flask
Get the installation guide here

### Set-up
Open your terminal and run:

git clone https://github.com/Munene19/IP8-News_Highlight.git

cd project root directory

python3.6 -m venv --without-pip virtual to create a virtual environment

source virtual/bin/activate to activate the virtual environment

curl https://bootstrap.pypa.io/get-pip.py | python

pip install flask

deactivate to exit the virtual environment

pip install -r requirements.txt to download all dependencies in the requirements.txt

Visit the NEWS API website, sign up for a free account and generate an API key.

Create a .sh (shell)file in your root directory called start.sh and in it, type;

export API_KEY="<your-api-key>"
python3 manage.py server

#### In your terminal;

chmod +x start.sh to make the shell file from executable
./start.sh to launch the application
Open http://127.0.0.1:5000/ on your preffered browser

Technologies Used
Python 3.9
Flask
Bootstrap
Flask-Script
Jinja2
Known Bugs
No known bugs

Collaborate
Incase of any questions, problems ideas concerning the app, feel free to reach out to me:

Github: Munene19 Email: Munenexv@gmail.com

License
MIT ©2019 Munene Mike

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.