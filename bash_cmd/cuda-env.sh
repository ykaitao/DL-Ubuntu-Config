sudo dpkg -i cuda-repo-ubuntu1604-8-0-local-ga2_8.0.61-1_amd64.deb
sudo apt-get update
sudo apt-get install cuda

sudo apt install nvidia-340
sudo apt install nvidia-331

sudo apt install python-pycuda # for python2
sudo apt install python3-pycuda # for python3

sudo pip install pycuda --upgrade
sudo pip3 install pycuda --upgrade

# export PATH=/usr/local/cuda-8.0/bin${PATH:+:${PATH}}
