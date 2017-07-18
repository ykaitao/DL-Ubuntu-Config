cp .theanorc ~
sudo echo 'PATH=/usr/local/cuda/bin${PATH:+:${PATH}}' >> ~/.bashrc
sudo echo 'LD_LIBRARY_PATH=/usr/local/cuda/lib64:/usr/lib/x86_64-linux-gnu${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}' >> ~/.bashrc
source ~/.bashrc
