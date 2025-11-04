# Packaging/HackingDependencies - Debian Wiki

**Source:** https://wiki.debian.org/Packaging/HackingDependencies

---

[Translation(s)](/DebianWiki/EditorGuide#translation): none

---

## How to create a dummy package

You can read [?](/CreateDummyPackage)how to create a dummy package with *[equivs](https://packages.debian.org/equivs "DebianPkg")*

and also how to create a [?](/Packaging/Files)package with some files with *[equivs](https://packages.debian.org/equivs "DebianPkg")*

## Hacking dependencies

Some window managers (like [GNOME](/Gnome)) comes with a lot of packages. But what do you do when you don't want a special package installed, but your system depends it?

Please note that this is a crude hack and if thoughtlessly used, it might possibly do damage to your packaging system. And please note as well that using it is not the recommended way of dealing with broken dependencies. Better file a bug report instead.

Anyway, if you still want to keep reading, the answer is to make a dummmy package. This text will give a small example on how to create a dummy package for *gnome-games*. The idea is to give the dummy a version number so high that the real package will never reach it.

For this job you need *[equivs](https://packages.debian.org/equivs "DebianPkg")*. If you haven't installed this package before, you should do so now.

Open up your favourite editor, name it something like *anti-gnome-games.equivs* and write the following lines:

```
Package: gnome-games
Version: 99:99
Maintainer: Your Name <mail@domain.com>
Architecture: all
Description: dummy gnome-games package
 A dummy package with a version number so high that the real gnome packages
 will never reach it.
```

And then in your console:

```
equivs-build anti-gnome-games.equivs
```

You will then have a *gnome-games\_99\_all.deb* which you can install with *dpkg -i*.

The *99:99* version means [epoch](https://www.debian.org/doc/debian-policy/ch-controlfields.html#version) 99, version 99 – if you don't need an intentionally-absurd version number, you should avoid the epoch and have a version like *1*.

## Documentations

* [equivs-build(1)](https://manpages.debian.org/man/1/equivs-build "DebianMan") - make a Debian package to register local software
* [equivs-control(1)](https://manpages.debian.org/man/1/equivs-control "DebianMan") - create a configuration file for equivs-build

## See Also

* [tasksel](/tasksel) - a user interface for installing tasks

---

[CategoryPackaging](/CategoryPackaging)