---
date: 2022-02-25 02:33:16.000876
templateKey: til
title: Install obs flatpak
tags:
  - linux
  - linux
  - linux

---

Big announcement recently that obs studio now builds out to a flatpak,
hopefully making it easier for all of us to install, especially us near
normies that don't regularly compile anything from source.

## install flatpak

I did not have flatpak installed so the first thing I had to do was get
the `flatpak` command installed, and add their default repo.

``` bash
sudo apt install flatpak
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
```

Once I had flatpak, I was able to get obs installed with the following
command.

``` bash
flatpak install flathub com.obsproject.Studio
```

Once Installed it fired right up for me with the next command they
suggested.

``` bash
flatpak run com.obsproject.Studio
```

## Links

* [flatpak setup for ubuntu](https://flatpak.org/setup/Ubuntu)
* [obs release notes](https://github.com/obsproject/obs-studio/releases/tag/27.2.0)
* [obs flatpak](https://flathub.org/apps/details/com.obsproject.Studio)
