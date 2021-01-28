# limbus-ova 21.01
Repostiory containing scripts and guides to set up Open Virtualisation Appliances
for various releases of LImBuS.

**Version:** 21.01

**Repository URL:** https://github.com/AberystwythSystemsBiology/limbus/tree/21.01a

**Contact:** Keiron O'Shea <keo7@aber.ac.uk>

**Setup Script Version:** Aberfan

## Setup Guide

### Step One: Logging in and changing your password

Once you have imported the OVA and started the VM, you should be greeted to a login prompt. The default credentials for the provided OVA are: 

- **Username:** `limbus`
- **Password:** `aber2021`

As this is a public GitHub repository, it's strongly advised that you take the time to change the password for the account. You can do this by entering:

```bash
$ passwd
```

After you have logged in. This will ask for your existing password (`aber2021`) and then prompt you to enter in your new password twice. Once you have completed this, continue onward to the next step.

### Step Two: Ensuring your setup files are up to date.

As it's likely that adjustments will be made to the setup file provided in the appliance, it is strongly recommended that you pull the most recent version of the helper files. To do this, simply navigate to the `limbus-ova` folder and pull from the versioned branch:

```bash
$ cd limbus-ova
$ git pull origin 21.01a

```

### Step Three: Setting up LImBuS

Once that is complete, you should be free to run the helper script by running the following:

```
$ python3 setup.py
```

Please ensure that all the salts that you provide are secure and sensible, and do not lose them otherwise all of the data on the machine will be unretrievable.

You'll know if the setup was successful because you will be prompted with an ASCII drawing of Kryten - our helpful little bot. 

### Step Four: Post Install


