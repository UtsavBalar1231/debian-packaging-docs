# Packaging/Pre-Requisites/LXC - Debian Wiki

**Source:** https://wiki.debian.org/Packaging/Pre-Requisites/LXC

---

Contents

1. [Install required packages](#Install_required_packages)
2. [Networking setup](#Networking_setup)
3. [Create sid container](#Create_sid_container)
4. [Using the created container](#Using_the_created_container)
5. [Create normal user](#Create_normal_user)

If you already have a GNU/Linux system, lxc would be the easiest to setup.

# Install required packages

Install lxc using this command.

```
sudo apt-get install lxc
```

If you have Ubuntu 14.04/trusty then install lxc from backports

```
sudo apt-get -t trusty-backports install lxc
```

Arch/Manjaro users see <https://wiki.archlinux.org/index.php/Linux_Containers> If you are unable to start the container, see <https://github.com/lxc/lxc/issues/4138>

Now install some necessary packages for networking support for the container.

```
sudo apt-get install -qy libvirt-clients libvirt-daemon-system iptables ebtables dnsmasq-base # if libvirt-client is not available, try libvirt-bin
```

# Networking setup

Check status of libvirt daemon (service)

```
systemctl status libvirtd
```

and start if not running

```
systemctl start libvirtd
```

Now start the networking service using

```
sudo virsh net-start default
sudo virsh net-autostart default
```

Check [LXC#Network\_setup\_in\_buster](/LXC#Network_setup_in_buster) for buster specific changes.

# Create sid container

Now create the container named debian-sid

```
sudo lxc-create -n debian-sid -t download -- --dist debian --release trixie --arch amd64
```

Note: Only trixie image is available, see [DebianUnstable](/DebianUnstable) to upgrade to sid

For Fedora/Arch users, if you are unable to start the sid container,use 'sudo systemctl start lxc.service', 'sudo systemctl start lxc-net.service', 'sudo systemctl enable lxc.service', 'sudo systemctl enable lxc-net.service'

You might have to use lxc-attach instead of lxc-console to connect to the container. After attaching yourself you could set your root password using passwd.

# Using the created container

Before connecting to the container, you might want to start the container

```
sudo lxc-start -n debian-sid
```

To connect to the container

```
sudo lxc-attach -n debian-sid
```

This is assuming that you have named your container 'debian-sid' as per the previous instructions.

* lxc-attach would not setup the tty session for other users and ask pass, what that means is, no sudo, if you switch using su - <username> (see next step). Use lxc-console if you want to use sudo.

See <http://blog.scottlowe.org/2013/11/25/a-brief-introduction-to-linux-containers-with-lxc/> for more info on using lxc.

# Create normal user

Create a new user with adduser and switch to that user with su - <username>. See <https://www.digitalocean.com/community/tutorials/how-to-add-and-delete-users-on-debian-8>. Easiest way to create a user with permission to run sudo would be:

```
useradd -m -g sudo <username>
```

It is worth noting that you need to install sudo as it does not come default. Also the -m tag creates a home folder for the user, this is not trivial and can be skipped.

Note: You can install sbuild inside the lxc container for clean builds.