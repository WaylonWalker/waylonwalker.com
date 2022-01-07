---
date: 2022-01-09 23:14:05.379718
templateKey: til
title: Installing Pipx on Ubuntu
tags:
  - python
  - linux
  - cli

---

## Straight in the terminal

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

``` bash

```
