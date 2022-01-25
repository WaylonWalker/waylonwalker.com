---
date: 2022-01-25 03:07:39.768774
templateKey: til
title: nix rescues modded minecraft night
tags:
  - cli
  - cli
  - cli

---

With the latest version of minecraft it requires a very new, possibly
the latest, version of java.  Lately we have been getting into modded
minecraft and I maintain the server for us.  It's been tricky to say the
least.  One hurdle I recently hit involves having the wrong version of
java.  In researching our errors, I found this on a forum.

> Pre-1.13 Forge only works with Java 8.


I don't write java, or really know how to manage different versions of
java, but I have nixpkgs installed and it has a ton of odd stuff like
this readily available, so
[searching nixpkgs](https://search.nixos.org/packages?channel=21.05&show=jdk8&from=0&size=50&sort=relevance&type=packages&query=java+8)
landed me with this.

``` bash
nix-env -iA nixpkgs.jdk8
```

once I had this installed I then just changed out java for the full path
to my new nixpkgs.jdk8 java and it worked.

``` bash
/home/walkers/.nix-profile/bin/java -server -Xms${MIN_RAM} -Xmx${MAX_RAM} ${JAVA_PARAMETERS} -jar ${SERVER_JAR} nogui
```

I don't write java or do anything other than host minecraft servers wtih
it.  There is probably a better way of maintaining java versions than
this, but this worked for me.
