---
date: 2022-01-09 23:14:05.379718
templateKey: til
title: Installing Pipx on Ubuntu
tags:
  - python
  - linux
  - cli

---

I recently paired up with another dev running windows with Ubuntu running in
wsl, and we had a bit of a stuggle to get our project off the ground because
they were missing com system dependencies to get going.

## Straight in the terminal

Open up a terminal and get your required system dependencies using the apt
package manager and the standard ubuntu repos.

``` bash
sudo apt update
sudo apt upgrade
sudo apt install \
      python3-dev \
      python3-pip \
      python3-venv \
      python3-virtualenv
pip install pipx
```

## Using an Ansible-Playbook

I like running things like this through an ansible-playbook as it give me some
extra control and repeatability next time I have a new machine to setup.

``` yaml
- hosts: localhost
  gather_facts: true
  become: true
  become_user: "{{ lookup('env', 'USER') }}"

  pre_tasks:
    - name: update repositories
      apt: update_cache=yes
      become_user: root
      changed_when: False
  vars:
    user: "{{ ansible_user_id }}"
  tasks:
    - name: Install System Packages 1 (terminal)
      become_user: root
      apt:
        name:
          - build-essential
          - python3-dev
          - python3-pip
          - python3-venv
          - python3-virtualenv
    - name: check is pipx installed
      shell: command -v pipx
      register: pipx_exists
      ignore_errors: yes

    - name: pipx
      when: pipx_exists is failed
      pip:
        name: pipx
      tags:
        - pipx
```

## video clip

Here is a clip of me getting pipx running on ubuntu 21.10, and running a few of
my favorite pipx commands.

![installation video](https://images.waylonwalker.com/pipx-install-ubuntu.gif)
