# Packaging/sbuild - Debian Wiki

**Source:** https://wiki.debian.org/Packaging/sbuild

---

More up-to-date instructions are available at [sbuild](/sbuild)

## Clean build with sbuild

* Consider setting up [AptCacherNg](/AptCacherNg) to save bandwidth and make builds faster.
* Create chroot for sbuild.

```
$ sudo apt-get install sbuild
$ sudo sbuild-adduser $LOGNAME # substitute your username for $LOGNAME
     ... *logout* and *re-login* or use `newgrp sbuild` in your current shell
```

Now you can build packages in an isolated environment using

```
$ sudo sbuild-createchroot --include=eatmydata,ccache,gnupg,auto-apt-proxy unstable /srv/chroot/unstable-amd64-sbuild http://deb.debian.org/debian
```

Or if you have an apt proxy setup, you can use auto-apt-proxy command to speed up chroot creation and build process,

```
$ sudo auto-apt-proxy sbuild-createchroot --include=eatmydata,ccache,gnupg,auto-apt-proxy unstable /srv/chroot/unstable-amd64-sbuild http://deb.debian.org/debian
```

**Option 1**:

```
$ sbuild -A -d unstable
```

Using this method requires you to install any debhelper plugins in build dependency locally to generate the dsc file. You might want to choose this option if you are going to build a lot of packages using that debhelper plugin (for example dh-sequence-nodejs or gem2deb if you regularly work on node or ruby packages)

**Option 2**: Alternatively, you can generate the dsc file using dpkg-source -b . and run

```
$ dpkg-source -b .
$ cd ..
$ sbuild -A -d unstable <package.dsc>
```

You might want to choose this option if you use the debhelper plugin rarely (for example dh-python or some other language if you don't work with this packages regularly) and don't want to clutter your local system with those additional packages.

See [sbuild](/sbuild) for more options.

---

[CategoryPackaging](/CategoryPackaging)