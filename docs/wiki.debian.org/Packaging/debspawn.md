# Packaging/debspawn - Debian Wiki

**Source:** https://wiki.debian.org/Packaging/debspawn

---

[debspawn](https://packages.debian.org/debspawn "DebianPkg") is a tool to build Debian packages. For alternative tools, see [Package build tools](/PackagingTools#Package_build_tools). For more general package maintenance, see [Package maintenance tools](/PackagingTools#Package_maintenance_tools).

debspawn uses systemd-nspawn for isolation. It caches .debs by default and uses Zstd compression for base images, making it faster than the default configurations of many similar build tools. See [the upstream README.md](https://github.com/lkhq/debspawn#readme) for more details.

Install [debspawn](https://packages.debian.org/debspawn "DebianPackage"):

```
$ sudo apt install debspawn
```

Create sid image:

```
$ debspawn create sid
```

Building a package:

```
$ debspawn build sid
```