# given through environment variable
SKYNET_PASSPHRASE="DEV"
export SKYNET_HOME=/opt/cloud/skynet
export PATH=.:$PATH:$SKYNET_HOME/bin
export PYTHONPATH=$PYTHONPATH:/opt/cloud/skynet/venv/lib/python2.7/site-packages

# customize python binary for skynet
# export PYTHON=/opt/cloud/skynet/venv/bin/python
