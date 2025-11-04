# Packaging/Pre-Requisites/Incus - Debian Wiki

**Source:** https://wiki.debian.org/Packaging/Pre-Requisites/Incus

---

Contents

1. [Install required packages](#Install_required_packages)
2. [Initialise Incus](#Initialise_Incus)
3. [Create sid container](#Create_sid_container)
4. [Using the created container](#Using_the_created_container)
5. [Create normal user](#Create_normal_user)

If you already have a GNU/Linux system, Incus would be the easiest to setup.

# Install required packages

Install Incus using this command.

```
sudo apt install incus
```

# Initialise Incus

Allow your user to use incus with the following command.

```
sudo usermod -a -G incus-admin "$USER"
```

Then set up Incus for your user with the following command. It will ask a few questions for which the defaults are fine to accept if you are unsure.

```
incus admin init
```

# Create sid container

Now create the container named debian-sid.

```
incus launch images:debian/trixie debian-sid
```

Note: Only trixie image is available, see [DebianUnstable](/DebianUnstable) to upgrade to sid

# Using the created container

To connect to the container

```
incus shell debian-sid
```

This is assuming that you have named your container 'debian-sid' as per the previous instructions.

# Create normal user

Create a new user with adduser and switch to that user with su - <username>. See <https://www.digitalocean.com/community/tutorials/how-to-add-and-delete-users-on-debian-8>. Easiest way to create a user with permission to run sudo would be:

```
useradd -m -g sudo <username>
```

It is worth noting that you need to install sudo as it does not come default. Also the -m tag creates a home folder for the user, this is not trivial and can be skipped.

Note: You can install sbuild inside the incus container for clean builds.