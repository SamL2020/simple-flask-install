credits = """
#########################
# Python Flask Template #
# Made by SamL2020#1767 #
#########################
"""

print(credits)
print("This program installs Flask along side an example site.")
install = input("Would you like to continue? (Y/n): ").upper()
if install == 'Y' or install == 'YES':
	pass
else:
	print("Exiting...")
	exit()

print("Installing Dependencies...")
print("Installing Flask...")
import os
cmd = 'git clone https://github.com/pallets/flask.git install'
os.system(cmd)
flaskinstall = open("install/setup.py", "w")
setupinfo = """
import re

from setuptools import setup

with open("install/src/flask/__init__.py", encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

# Metadata goes in setup.cfg. These are here for GitHub's dependency graph.
setup(
    name="Flask",
    version=version,
    install_requires=[
        "Werkzeug>=0.15",
        "Jinja2>=2.10.1",
        "itsdangerous>=0.24",
        "click>=5.1",
    ],
    extras_require={"dotenv": ["python-dotenv"]},
)
"""
flaskinstall.write(setupinfo)
flaskinstall.close()
os.system("python3 install/setup.py install")
import shutil
shutil.rmtree('build')
shutil.rmtree('dist')
shutil.rmtree('Flask.egg-info')
shutil.copytree('install/src/flask', os.path.dirname(os.path.abspath(__file__))+'/flask')
shutil.rmtree('install')
print("Done!\n")
sucess=False
if os.geteuid() == 0:
	while sucess == False:
		try:
			port = int(input("Choose a port to host the website on: "))
			if port <= 65535 and port > 0:
				sucess=True
			else:
				print("Type a valid port number (1-65535)")
		except ValueError:
			print("Type a valid port number (1-65535)")
else:
	while sucess == False:
		try:
			port = int(input("Choose a port to host the website on (1025-65535): "))
			if port <= 65535 and port > 1024:
				sucess=True
			elif port <= 1024 and port > 0:
				print("You are requesting to use a priviliged port.")
				print("Choose another port or run this program as root (sudo python3 main.py)")
				select = input("Would you like to pick another port? (Y/n): ").upper()
				if select == 'N' or select == 'NO':
					print("Exiting...")
					exit()
			else:
				print("Type a valid port number (1025-65535)")
		except ValueError:
			print("Type a valid port number (1025-65535)")

data =f"#Import Flask\nfrom flask import Flask\napp = Flask(__name__)\n\n#Setup an main path\n@app.route('/')\ndef hello_world():\n#Return Data\n    return 'Hello, World!'\n\n#Run Flask\napp.run(host='0.0.0.0',port={str(port)})"

print("Creating files...")
setupfile = open("setup.py", "w")
if port < 1025:
	setupfile.write(f'data = """{data}"""\nmainfile = open("main.py", "w")\nmainfile.write(data)\nmainfile.close()\nprint("Done!")\nprint("Cleaning up...")\nprint("Run this program with (sudo python3 main.py)")\nimport os\nos.remove("setup.py")')
else:
	setupfile.write(f'data = """{data}"""\nmainfile = open("main.py", "w")\nmainfile.write(data)\nmainfile.close()\nprint("Done!")\nprint("Cleaning up...")\nprint("Run this program with (python3 main.py)")\nimport os\nos.remove("setup.py")')
setupfile.close()
import setup
