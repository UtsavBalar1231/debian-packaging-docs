# PackagingWithDocker - Debian Wiki

**Source:** https://wiki.debian.org/PackagingWithDocker

---

**Proposed page deletion**

Redundant. Contents merged with [Docker](/Docker).

[CategoryProposedDeletion](/CategoryProposedDeletion)

This page intends to git hints on how to use [Docker](/Docker) for packaging.

See <http://sfxpt.wordpress.com/2013/11/17/debianubuntu-package-developing-with-docker-continued/> for a more classical approach to the problem by sharing directories between the host and packaging containers.

```
#Install the docker service

 $apt-get install docker.io

#Create Debian Sid docker container

 $docker run -it --rm --name deb-sid debian:sid /bin/bash

#Note: Give different name in --name option for creating new containers

#Install the required packages in the container

 $apt-get install dh-make gem2deb npm2deb

#Press Ctl + p + q to exit from the container without stopping it.

# For accessing back the container

 $ docker ps

#Find the container ID and attach it to the current bash terminal using the following commands

 $docker attach <Container ID>

#Eg:
-------------
$ sudo docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
0cf9a333ad8b        debian:sid          "/bin/bash"         28 minutes ago      Up 2 minutes                            jolly

$docker attach 0cf9a333ad8b

root@0cf9a333ad8b:/#
```

---

[CategoryVirtualization](/CategoryVirtualization) | [CategoryPackaging](/CategoryPackaging)