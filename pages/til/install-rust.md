---
date: 2022-02-06 15:34:02.785722
templateKey: til
title: Installing Rust and Cargo on Ubuntu 21.10 using Ansible
tags:
  - linux

---

Installing rust in your own ansible playbook will make sure that you can
get consistent installs accross all the machines you may use, or
replicate your development machine if it ever goes down.

## Personal philosophy

I try to install everything that I will want to use for more than just a
trial inside of my ansible playbook.  This way I always get the same
setup across my work and home machines, and anytime I might setup a
throw away vm.

## reccommended install

This is how rust reccomends that you install it on Ubuntu.  First update
your system, then run their installer, and finally check that the
install was successful.

``` bash
# system update
sudo apt update
sudo apt upgrade

# download and run the rust installer
curl https://sh.rustup.rs -sSf | sh

# confirm your installation is successful
rustc --version
```

## Ansible Install

The first thing I do in my playbooks is to check if the tool is already
installed.  Here I chose to look for `cargo`, you could also look for
`rustc`.

``` yaml
  - name: check if cargo is installed
    shell: command -v cargo
    register: cargo_exists
    ignore_errors: yes
```

> I first check for an existing install so I can re-run my playbooks
> quickly filling in only missing tools. More on this
> [ansible install conditionally](https://waylonwalker.com/til/ansible_install_if_not_callable/)

Next we need to download the installer script and make it executable.

``` yaml
  - name: Download Installer
    when: cargo_exists is failed
    get_url:
      url: https://sh.rustup.rs
      dest: /tmp/sh.rustup.rs
      mode: '0755'
      force: 'yes'
    tags:
      - rust
```

> I chose to download the installer, because I was unable to pass in the
> `-y` flag otherwise, which is required to do unattended installs.

Last we just run the installer given to us by rust with the `-y` flag so
that it will run unattended.

``` yaml

  - name: install rust/cargo
    when: cargo_exists is failed
    shell: /tmp/sh.rustup.rs -y
    tags:
      - rust
```

## One more thing

Make sure that you source your cargo env, otherwise your shell will not
find `rustc` or `cargo`.  I chose to do this by adding the following
line to my `~/.zshrc`.  You can but it in `~/.bashrc` if that is your
thing, or just run it in your shell to just get it to work.

``` bash
[ -f ~/.cargo/env ] && source $HOME/.cargo/env
```

## Full Install Playbook

Here is a fully working install playbook to get you started or to port
into your own playbook.

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
  - name: check if cargo is installed
    shell: command -v cargo
    register: cargo_exists
    ignore_errors: yes

  - name: Download Installer
    when: cargo_exists is failed
    get_url:
      url: https://sh.rustup.rs
      dest: /tmp/sh.rustup.rs
      mode: '0755'
      force: 'yes'
    tags:
      - rust

  - name: install rust/cargo
    when: cargo_exists is failed
    shell: /tmp/sh.rustup.rs -y
    tags:
      - rust

```

You can save this as a  `local.yml` and run the following in your shell
to run the playbook on your local machine.

``` bash
ansible-playbook local.yml --ask-become-pass
```

> note: `--ask-become-pass` is required for the system update step.
> This will ask for your password as soon as ansible starts.


I also have a very similar article on hwo I [ansible install fonts](https://waylonwalker.com/til/ansible_install_fonts/)
