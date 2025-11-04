# Packaging/Pre-Requisites/nspawn - Debian Wiki

**Source:** https://wiki.debian.org/Packaging/Pre-Requisites/nspawn

---

Contents

1. [Install required packages and enable networking service](#Install_required_packages_and_enable_networking_service)
2. [Start the container](#Start_the_container)
3. [Use the container (get a shell inside container)](#Use_the_container_.28get_a_shell_inside_container.29)
4. [Configure the container (add normal user and networking)](#Configure_the_container_.28add_normal_user_and_networking.29)

If you are not on Debian Stable, you can consider [Docker, LXC or Virtual Machine options](/Packaging/Pre-Requisites) that will use images instead of depending on the debian package archive (which may give errors due to missing signing keys etc)

See [nspawn](/nspawn) for more details of configuring systemd-nspawn containers. See [Arch Linux specific tips](https://wiki.archlinux.org/title/Systemd-nspawn#Create_a_Debian_or_Ubuntu_environment) if you have Arch Linux as host machine. For clean builds, you can install sbuild inside your container or setup sbuild on host and use the shared home option to access packaging files.

## Install required packages and enable networking service

Install systemd-container and mmdebstrap packages

```
sudo apt install systemd-container mmdebstrap
```

Setup the root filesystem using mmdebstrap

```
sudo mmdebstrap --include=systemd-container,auto-apt-proxy,sudo unstable /var/lib/machines/debian-sid
```

![/!\](/htdocs/debwiki/img/alert.png "/!\") Users of distributions that do not include apt and mmdebstrap, can install and use debootstrap instead of mmdebstrap.

Optional: If you already have apt-cacher-ng setup, then speed up the setup by running

sudo auto-apt-proxy mmdebstrap --include=systemd-container,auto-apt-proxy,sudo unstable /var/lib/machines/debian-sid

Enable systemd-networkd

```
sudo systemctl enable systemd-networkd
sudo systemctl start systemd-networkd
```

## Start the container

Create /etc/systemd/nspawn dir if it doesn't exist:

```
sudo mkdir -p /etc/systemd/nspawn
```

Create /etc/systemd/nspawn/debian-sid.nspawn and add the following lines (replace <username> with your host machines username):

```
[Exec]
Boot=yes
PrivateUsers=no

[Files]
Bind=/home/<username>
PrivateUsersOwnership=no

[Network]
VirtualEthernet=yes
```

See man 5 systemd.nspawn for more options you can add to this file.

Remove the /etc/hostname file within the container, so it doesn't conflict with the machine name:

```
sudo rm /var/lib/machines/debian-sid/etc/hostname
```

Set the setuid bit on the sudo binary in the container:

```
sudo chmod 4755 /var/lib/machines/debian-sid/usr/bin/sudo
```

## Use the container (get a shell inside container)

To start the container, run:

```
sudo machinectl start debian-sid
```

To stop the container, run:

```
sudo machinectl stop debian-sid
```

You can get a shell inside the container with the following command,

```
sudo machinectl shell <username>@debian-sid
```

See man machinectl for more options.

## Configure the container (add normal user and networking)

Create a normal user with sudo access:

Simpler case, for most users, when user on your host system, which you want to map to container, uid is 1000.

Step 1: Get a shell in the container.

```
sudo machinectl shell root@debian-sid
```

Step 2: Once inside the container,

```
root@debian-sid:~# adduser <username>
root@debian-sid:~# adduser <username> sudo
```

Advanced case, this should be run from the host system,

If you are on a multi-user system, and your UID/GID are not 1000:1000, ensure the user in the container is created with the appropriate ID's.

This will ensure that the files from the bind mount will be accessible within the container.

```
sudo useradd --create-home --groups sudo \
  --shell /bin/bash --root /var/lib/machines/debian-sid \
  -u 1000 -g 1000 \
  <username>

passwd -R /var/lib/machines/debian-sid <username>
```

Enable systemd-networkd inside the container,

```
root@debian-sid:~# systemctl enable systemd-networkd
root@debian-sid:~# systemctl start systemd-networkd
```

Optional: Edit /etc/hosts and add debian-sid to 127.0.0.1 line

```
root@debian-sid:~$ cat /etc/hosts
127.0.0.1       localhost debian-sid
::1             localhost ip6-localhost ip6-loopback
ff02::1         ip6-allnodes
ff02::2         ip6-allrouters
```

Press Control + D (or type exit to exit from container).

Now login as a normal user for packaging

```
sudo machinectl shell <username>@debian-sid
```

---

[CategoryPackaging](/CategoryPackaging)