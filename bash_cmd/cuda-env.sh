sudo apt-get purge nvidia*
sudo dpkg -i cuda-repo-ubuntu*.deb
sudo apt-get update
sudo apt-get install cuda

sudo dpkg -i libcudnn*.deb

sudo apt-get install python-pycuda # for python2
sudo apt-get install python3-pycuda # for python3

sudo pip install pycuda --upgrade
sudo pip3 install pycuda --upgrade

# export PATH=/usr/local/cuda-8.0/bin${PATH:+:${PATH}}
