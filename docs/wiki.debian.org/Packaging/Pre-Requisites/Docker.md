# Packaging/Pre-Requisites/Docker - Debian Wiki

**Source:** https://wiki.debian.org/Packaging/Pre-Requisites/Docker

---

Contents

1. [Docker with Debian-based host](#Docker_with_Debian-based_host)
2. [Docker with non-Debian-based host](#Docker_with_non-Debian-based_host)
3. [Applications that support Docker build environments](#Applications_that_support_Docker_build_environments)
   1. [Dedicated User Environment (DUE)](#Dedicated_User_Environment_.28DUE.29)

Install docker either from your OS's package repositories

```
sudo apt install docker.io
```

or check out <https://docs.docker.com/engine/installation/linux/>. If you have a Debian-based host system, you could run apt-cacher-ng and sbuild on your host system, but otherwise you need to install them inside the container.

## Docker with Debian-based host

**Note:** The source for this docker image is at <https://gitlab.com/fsci/resources> and it has the password for default user.

Pull the development docker image that FSCI provides

```
# docker pull registry.gitlab.com/fsci/resources/debian-dev:latest
```

Create a container with it and run bash on it

```
# docker run --name debian-dev -it registry.gitlab.com/fsci/resources/debian-dev:latest bash
```

If needed, update and upgrade to latest versions of packages. developer itself. Password is developer.

```
sudo apt-get update && sudo apt-get dist-upgrade
```

Create a normal user for packaging. See <https://www.digitalocean.com/community/tutorials/how-to-add-and-delete-users-on-debian-8>

Exit after your work is done. If you need to connect to it later, use the following commands which will take you to the bash prompt

```
docker start debian-dev
docker attach debian-dev
```

## Docker with non-Debian-based host

If your host system is not Debian-based (for example arch), then you can follow the steps below (this will setup docker with systemd integration which allows you to run services like apt-cacher-ng easily),

```
docker pull jgoerzen/debian-base-standard:sid
docker run -td --stop-signal=SIGRTMIN+3 \
   --tmpfs /run:size=100M --tmpfs /run/lock:size=100M \
   -v /sys/fs/cgroup:/sys/fs/cgroup:ro \
   --name=debian-sid jgoerzen/debian-base-standard:sid
```

You can start the container and get an interactive shell

```
docker start debian-sid
docker exec -it debian-sid bash
```

Setup apt-cacher-ng (this will cache all the packages locally) and auto-apt-proxy (this will auto configure the installed proxy for apt).

```
apt install apt-cacher-ng auto-apt-proxy
```

auto-apt-proxy command should display http://172.17.0.1:3142 upon successful setup.

You will now get a root shell and it is better to create a normal user for packaging.

Now run this inside the container,

```
adduser <username>
su - <username>
```

## Applications that support Docker build environments

See also the [curated list of existing Debian docker builders](/PackagingTools#Package_build_tools).

Please update as needed. Given the high number of existing docker build tools, focus should be set on improving and maintaining the tooling (i.e. sbuild-schroot, due, etc.) rather than indulging into the [Not Invented Here syndrome](https://en.wikipedia.org/wiki/Not_invented_here#In_computing).

### Dedicated User Environment (DUE)

DUE is a wrapper for Docker that configures and runs containers from user selected releases. In addition to making common build and configuration tasks easier, it automatically maps the user's account and home directory to be available in the container, creating a more comfortable work environment.

To install from Debian 11 Bullseye:

```
sudo apt-get install due
```

For earlier Debian releases, source code and packaged .debs are available at the project's home page, here: <https://github.com/cumulusnetworks/DUE>