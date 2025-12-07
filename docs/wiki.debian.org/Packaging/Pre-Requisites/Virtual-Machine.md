# Packaging/Pre-Requisites/Virtual-Machine - Debian Wiki

**Source:** https://wiki.debian.org/Packaging/Pre-Requisites/Virtual-Machine

---

Contents

1. [Virtual Box](#Virtual_Box)
2. [Incant](#Incant)
3. [Vagrant](#Vagrant)

We have two different options for creating Virtual Machines, Virtual Box and Incant/Vagrant. You can choose one of the two options below.

## Virtual Box

Install Virtual box and run Debian Sid in it.

```
sudo apt install virtualBox
```

For Manual installation, download Debian Testing ISO from Debian website and install it inside already installed [VirtualBox](/VirtualBox). Once you have Debian Testing, you can upgrade it to Sid/unstable.

Edit /etc/apt/sources.list and change testing to sid or unstable.

```
apt update
apt dist-upgrade
```

## Incant

Incant is a front end to Incus inspired by Vangrant, which allows provisioning VM/container using a declarative yaml file. Even though it creates a container by default, adding it in this page as a replacement for Vagrant.

Install incant and inus

```
apt install incant incus
usermod -a -G incus-admin <username>
```

Activate the new group as normal user

```
newgrp incus-admin
```

Initialize incus

```
incus admin init --auto
```

Create incant.yaml

```
instances:
  debian-sid:
    image: images:debian/14
```

If you want to create a vm instead of container, add vm: true to incant.yml

```
instances:
 debian-sid:
    image: images:debian/14
    vm: true
```

Create VM/container,

```
incant up
```

You can access the shell with,

```
incant shell debian-sid
```

Stopping and starting the container,

```
incus stop debian-sid
incus start debian-sid
```

See [Using Incus](/Packaging/Pre-Requisites/Incus#Using_the_created_container) for more options for managing the VM/container created.

## Vagrant

Vagrant versions newer than 2.3.7 are not Free Software. See [1049999](https://bugs.debian.org/1049999 "DebianBug"). We recommend you use Incant instead of Vagrant.

If you want to make your job easy just install vagrant

```
sudo apt install vagrant-libvirt libvirt-daemon-system
```

Make sure that you are having only single Hypervisor running otherwise be ready to see some error. Also, vagrant installation might ask you to install some other additional packages, allow it to do so.

Add your user to libvirt group to use vagrant without additional privillege prompts

```
sudo gpasswd -a <your user> libvirt
```

Create a new directory from where you want to start VM. vagrant will store some configuration file in that directory and then switch to that directory

```
mkdir /path/to/directory/packaging
cd /path/to/directory/packaging
```

Now we need to tell vagrant where we need to fetch Vagrant box (VM image)

You can find recent Debian Testing vagrant box on the following URL <https://app.vagrantup.com/debian/boxes/testing64>

```
vagrant init debian/testing64
vagrant up
```

Note: This can take some time depending on your internet connection speed.

Then you can connect to the VM by

```
vagrant ssh
```

Note: Current image is very old, so you will need to run apt update and apt dist-upgrade (to update debian-archive-keying) before you can upgrade to sid.

You can update to Sid by replacing testing with sid in /etc/apt/sources.list and running

```
apt update
apt dist-upgrade
```

Note: If you use nfs to share host directory with the vm, then you'll need rpc-statd service or you may get no locks available error message.

```
sudo systemctl enable rpc-statd  # Enable statd on boot
sudo systemctl start rpc-statd  # Start statd for the current session
```