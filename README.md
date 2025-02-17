# djsim_song_importer
Song importer source code for DJ SIMULATOR
## install
### linux
#### python
We need python 3.8, which is an older version.
we can use an external PPA to install it, but be aware of the risks of external sources.

https://launchpad.net/%7Edeadsnakes/+archive/ubuntu/ppa

```
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.9
```

#### venv
the external PPA provides the VENV for those versions too

```
sudo apt-get install python3.9-venv
```

#### virtualenv
virtualenv has support for specific python binaries, which we have to change 

```
python -m virtualenv -p $(which python3.9) ./lib
source ./lib/bin/activate
```

#### packages
now that we have a virtualenv with the exact python3 version, we can install the requirements

```
pip install -r requirements.txt
```

## run
### linux
run the djsim_song_importer.py script with python3 in the venv

```
python3 djsim_song_importer.py
```

