# PackagingWithDarcs - Debian Wiki

**Source:** https://wiki.debian.org/PackagingWithDarcs

---

This page describes how to use the Darcs version control system to create Debian packages. To do the same thing with [git](/git), see [PackagingWithGit](/PackagingWithGit). For tools to use other version control systems, see [Package maintenance tools](/PackagingTools#Package_maintenance_tools).

![/!\](/htdocs/debwiki/img/alert.png "/!\") darcs-buildpackage was removed in [Debian Wheezy](/DebianWheezy).

## Packaging with Darcs

### About Darcs

David Roundy's [Darcs](http://www.darcs.net/) is a distributed version control system that can work very nicely for Debian package maintenance. It is the only DVCS that has full-fledged support for cherrypicking of patches, which is a nice feature for this sort of work. Darcs does not need a central repo or network connectivity, though it can certainly work in that model of you so desire. Every repository in Darcs is a branch, branching is cheap, and commits to a central repo are a merge.

### The Model

The basic idea of Debian package maintenance with Darcs is that you maintain two branches (repositories): one for the unmodified upstream source, and another for your Debian packages. You import new upstream versions into the upstream repository, then merge from the upstream repo into the Debian repo to update your Debian packages.

### The Tools

You'll want to apt-get install darcs darcs-buildpackage. The darcs package, of course, provides the Darcs installation. If you're not already familiar with Darcs, go over and read the [tutorial](http://www.darcs.net/manual/node4.html) and the [GettingStarted](http://wiki.darcs.net/GettingStarted) page on the Darcs [wiki](http://wiki.darcs.net).

darcs-buildpackage is a set of tools by [?](/JohnGoerzen)JohnGoerzen to automate the use of Darcs for maintaining Debian packages. The tools are:

* dbp-importdsc, which will import Debian source packages into the upstream and Debian repositories as appropriate, automatically.
* dbp-importorig, which will import an upstream tarball or directory into the upstream repository
* dbp-markdeb, which is a small wrapper around darcs tag that will automatically generate tags based on the current working version in your directory (debian/changelog version)
* dbp-get, which is a tool to check out specific Debian versions of a tree
* darcs-buildpackage, which is a wrapper around debuild to make sure that the \_darcs directory is excluded from diffs. If you don't have an orig.tar.gz, darcs-buildpackage can also build one from the upstream Darcs repo.

## Getting Started

First, you'll want to edit ~/.darcs-buildpackage and tell it where you intend to keep your Debian and upstream repositories. Mine looks like:

```
debianrepo = /home/jgoerzen/repo/debian/%(package)s
upstreamrepo = /home/jgoerzen/repo/debian/%(package)s.upstream
```

Next, you'll want to decide if you want to import existing history or start from scratch.

### Importing the upstream code

#### From an upstream Darcs repo

You can use Darcs to track a Darcs-based upstream with **darcs get** and **darcs pull**, for example

```
darcs get "http://www.slavepianos.org/rd/sw/jack.*" /home/arnouten/dev/debian/jack-tools.upstream
```

#### From source packages (keeps track of history)

To import existing history, you'll need a set of source packages (diff.gz, dsc, and orig.tar.gz). Run dbp-importdsc on each .dsc file, in order from oldest to newest. It will automatically Do The Right Thing and import into your Debian and upstream repos as appropriately, merging between them as well.

#### Starting Fresh

If you have no history you want to import, you'll want to start with an upstream tarball or directory. Use dbp-importorig /path/to/file.tar.gz packagename 1.2.3 where 1.2.3 is the upstream version you're importing. dbp-importorig will import the specified file into the upstream repo for the specified package (creating this repo if necessary), and tag it with the specified version.

### Creating the Debian repo

Then, you will do something like:

```
cd ~/repo/debian
darcs get packagename.upstream packagename
```

to initialize your Debian repo. Now in your Debian repo, you can use dh\_make to start hacking away (don't forget to darcs add the debian/ dir and all the files you create). Use darcs record early and often to commit changes.

## Building

When it's time to build, just use darcs-buildpackage in place of debuild. It will pass arguments on to debuild. If darcs-buildpackage detects that you need an orig.tar.gz (or a tar.gz for Debian-native packages), it will build one for you using the Darcs repo. (If you already have one, it won't replace it.) It will also pass on the required arguments to exclude \_darcs from the tar.gz and diff.gz files as per Debian policy.

Once you've built and uploaded, it's a good idea to run dbp-markdeb to tag this version in your repository. Then you can check it out directly later. You may also want to darcs push your package to a public repository somewhere, for other users to see.

## New Upstream

When a new upstream version comes out, use dbp-importorig again to import it into your upstream repo. Then, from your Debian repo, run:

```
darcs pull ../packagename.upstream
```

to import the upstream changes into the Debian repo. Hack away, resolve any conflicts, and darcs record early and often.

## More Info

See also:

* /usr/share/doc/darcs-buildpackage
* [PackagingWithDarcsAndTailor](/PackagingWithDarcsAndTailor)
* Darcs [homepage](http://www.darcs.net/)
* Darcs [wiki](http://darcs.net/DarcsWiki)
* Darcs [manual](http://www.darcs.net/manual/)
* [The vcs-pkg project](http://vcs-pkg.org)

---

[CategoryDeveloper](/CategoryDeveloper) [CategoryPackaging](/CategoryPackaging) [CategoryProposedDeletion](/CategoryProposedDeletion) associated package deleted in Wheezy