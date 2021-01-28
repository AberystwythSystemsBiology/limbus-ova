'''
The Libre Biobank System
Version: 21.01a
Repository URL: https://github.com/AberystwythSystemsBiology/limbus/tree/21.01a
Contact: Keiron O'Shea <keo7@aber.ac.uk>
Date: 28/01/2021
==============================================================================
'''

import subprocess
import os

BRANCH_NAME = "21.01a"
REMOTE_REPO = "https://github.com/AberystwythSystemsBiology/limbus"
HOME_DIR = os.path.expanduser('~')
LIMBUS_DIR = os.path.join(HOME_DIR, "limbus")

print(__doc__)

print("Welcome to the interactive setup for the Libre Biobank System.\n")

print("First, let me grab LImBuS from GitHub.\n")

git_retrieve = subprocess.run(str("git clone --single-branch --branch %s %s %s" % (BRANCH_NAME, REMOTE_REPO, LIMBUS_DIR)).split(" "))

print("Now let's set up an environment file for you. This contains all of the credentials required to run the service.\n")

POSTGRES_USER = input("\nPOSTGRES_USER: the username for the psql instance: (default: psqluser)")

if POSTGRES_USER == "":
    POSTGRES_USER = "psqluser"

POSTGRES_PASSWORD = input("\nPOSTGRES_PASSWORD: the password for the psql instance. Please make sure this is secure: :")
SECRET_KEY = input("\nSECRET_KEY: the salt to help mitigate against cookie tampering. Please make sure this is secure: ")
WTF_CSRF_SECRET_KEY = input("\nWTF_CSRF_SECRET_KEY: the salt to help mitigate against XSS. Please make sure this is secure: ")
DOID_PATH = input("\nPath to the DOID xrdf file: (default: https://users.aber.ac.uk/keo7/doid.xrdf)")


if DOID_PATH == "":
    DOID_PATH = "https://users.aber.ac.uk/keo7/doid.xrdf"

ENV_DATA = ""
ENV_DATA += "FLASK_CONFIG=production\n"
ENV_DATA += "POSTGRES_USER=%s\n" % (POSTGRES_USER)
ENV_DATA += "POSTGRES_PASSWORD=%s\n" % (POSTGRES_PASSWORD)
ENV_DATA += "POSTGRES_DB=limbus\n"
ENV_DATA += "SECRET_KEY=%s\n" % (SECRET_KEY)
ENV_DATA += "WTF_CSRF_SECRET_KEY=%s\n" % (WTF_CSRF_SECRET_KEY)
ENV_DATA += "DEBUG=False\nDOCUMENT_DIRECTORY=/limbus/documents\nTEMPLATES_DIRECTORY=/limbus/templates\nONTOLOGY_DIRECTORY=/limbus/ontologies/\n"
ENV_DATA += "LC_ALL=C.UTF-8\nLANG=C.UTF-8\n"
ENV_DATA += "DOID_PATH=%s" % (DOID_PATH)

ENV_PATH = os.path.join(LIMBUS_DIR, ".env")

print("NOTE: Writing to file: %s" % (ENV_PATH))

with open(ENV_PATH, "w") as outfile:
    outfile.write(ENV_DATA)


print("Now I'm going to get everything built...")

DOCKER_COMPOSE_PATH = os.path.join(LIMBUS_DIR, "docker-compose.staging.yml")

post_build = subprocess.run("bash postbuild.sh".split(" "))
