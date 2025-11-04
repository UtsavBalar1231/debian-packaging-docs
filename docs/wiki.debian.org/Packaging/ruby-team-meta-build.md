# Packaging/ruby-team-meta-build - Debian Wiki

**Source:** https://wiki.debian.org/Packaging/ruby-team-meta-build

---

Debian Ruby team maintains a set of scripts that helps testing reverse dependencies of packages when updating an existing package in addition to running clean build with sbuild and autopkgtest with lxc. It runs autopkgtest for all reverse dependencies and rebuilds all reverse build dependencies.

You can clone [this repo](https://salsa.debian.org/ruby-team/meta/) from salsa and use build script. You will need to run setup script first to create all required root file systems and install required packages.

Note: Currently you need to follow [these steps](https://lists.debian.org/debian-ruby/2019/02/msg00035.html) if you got an error when creating lxc container or your autopkgtests always fail. You will need apparmor installed to have these settings to work.

**Window Subsystem for Linux (WSL2)**

In setting up ruby-team-meta-build script which makes testing reverse dependencies easy, by default its uses LXC as its default autopkgtests backend which doesn't work in WSL2 so you can configure to use schroot by setting AUTOPKGTEST\_VIRT\_SERVER to "schroot" and exporting it (export AUTOPKGTEST\_VIRT\_SERVER="schroot") in ~/.bashrc file, autopkgtests will use schroot backend which is suitable for WSL2.

---

[CategoryPackaging](/CategoryPackaging) [CategoryRuby](/CategoryRuby)