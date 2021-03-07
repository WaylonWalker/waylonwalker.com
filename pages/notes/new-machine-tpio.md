---
templateKey: blog-post
related_post_label: Check out this related post
tags: []
title: New Machine for developing Tests with TestProject.io
date: 2020-07-25T05:00:00.000+00:00
status: published
description: Today I setup a new machine on Digital Ocean to use with
  TestProject.io, Here are my installation notes.
cover: /static/new-machine-tpio.png

---
Today I setup a new machine on Digital Ocean to use with TestProject.io,  Here are my installation notes.

``` bash
apt update && apt upgrade -y

apt install zsh
chsh zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
curl -fsSL https://starship.rs/install.sh | bash
echo 'eval "$(starship init zsh)"' >> ~/.zshrc

# python
sudo apt update
sudo apt install python3-pip -y
echo 'alias python=python3' >> ~/.zshrc
echo 'alias pip=pip3' >> ~/.zshrc

# pipx
apt install python3-venv
pip install pipx
pipx install black
pipx install shell-functools
pip install ipython


# docker
sudo apt update
sudo apt install apt-transport-https ca-certificates curl gnupg-agent software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt update
sudo apt install docker-ce

# docker-compose
sudo curl -L "https://github.com/docker/compose/releases/download/1.25.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# configure git
git config --global user.name "Waylon Walker"
git config --global user.email waylon@waylonwalker.com

# fzf
git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf
~/.fzf/install

# forgit
git clone https://github.com/wfxr/forgit ~/.forgit
echo ". ~/.forgit/forgit.plugin.zsh" >> ~/.zshrc

# ag
apt install silversearcher-ag

# bat
apt install bat
echo "alias cat=batcat" >> ~/.zshrc

# testproject.io tokens
echo 'export TP_AGENT_ALIAS="Digital Ocean Agent"' >>" ~/.zshrc
echo "export TP_AGENT_API_KEY=<your-key> >>" ~/.zshrc
echo "export TP_DEV_TOKEN=<your-token> >>" ~/.zshrc

```


envsubst < .github/ci/docker-compose.yml > docker-compose.yml

``` yaml
# .github/ci/docker-compose.yml
version: "3.1"
services:
  testproject-agent:
    image: testproject/agent:latest
    container_name: testproject-agent
    depends_on:
      - chrome
      - firefox
    environment:
      TP_API_KEY: "${TP_API_KEY}"
      TP_AGENT_ALIAS: "GitHub Action Agent"
      TP_AGENT_TEMP: "true"
      TP_SDK_PORT: "8686"
      CHROME: "chrome:4444"
      CHROME_EXT: "localhost:5555"
      FIREFOX: "firefox:4444"
      FIREFOX_EXT: "localhost:6666"
    ports:
    - "8585:8585"
    - "8686:8686"
  chrome:
    image: selenium/standalone-chrome
    volumes:
      - /dev/shm:/dev/shm
    ports:
    - "5555:4444"
  firefox:
    image: selenium/standalone-firefox
    volumes:
      - /dev/shm:/dev/shm
    ports:
    - "6666:4444"
```


``` bash
docker-compose -f docker-compose.yml
```
