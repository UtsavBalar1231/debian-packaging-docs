# Packaging/Intro - Debian Wiki

**Source:** https://wiki.debian.org/Packaging/Intro

---

[Translation(s)](/DebianWiki/EditorGuide#translation): [English](/Packaging/Intro) - [?](/es/IntroDebianPackaging)Español - [Italiano](/it/Packaging/Intro) - [Català](/ca/IntroDebianPackaging) - [Português (Brasil)](/pt_BR/Packaging/Intro) - [Română](/ro/IntroDebianPackaging) - [Русский](/ru/IntroDebianPackaging)

Introductory tutorial for making Debian packages. It doesn't get very deep into the more intricate bits of Debian packaging, but it shows how to make Debian packages for software that is simple to package. For more tutorials, see [Packaging](/Packaging).

---

Contents

1. [What is a "package"?](#What_is_a_.22package.22.3F)
2. [Requirements](#Requirements)
3. [Three central concepts](#Three_central_concepts)
4. [The packaging workflow](#The_packaging_workflow)
   1. [Step 1: Rename the upstream tarball](#Step_1:_Rename_the_upstream_tarball)
   2. [Step 2: Unpack the upstream tarball](#Step_2:_Unpack_the_upstream_tarball)
   3. [Step 3: Add the Debian packaging files](#Step_3:_Add_the_Debian_packaging_files)
   4. [Step 4: Build the package](#Step_4:_Build_the_package)
   5. [Step 5: Install the package](#Step_5:_Install_the_package)
5. [Conclusion](#Conclusion)
6. [See also](#See_also)

---

**Written in 2010**

This tutorial describes recommended practice as of 2010. The theory hasn't changed, but the specific tools are no longer recommended for general use.

For more guides, see [Packaging](/Packaging).

## What is a "package"?

A Debian package is a collection of files that allow for applications or libraries to be distributed via the package management system. The aim of packaging is to allow the automation of installing, upgrading, configuring, and removing computer programs for Debian in a consistent manner. A package consists of one source package, and one or more binary packages. The Debian Policy specifies the standard format for a package, which all packages must follow.

Binary packages contain executables, standard configuration files, other resources required for executables to run, documentation, data, ...

Source packages contain the upstream source distribution, configuration for the package build system, list of runtime dependencies and conflicting packages, a machine-readable description of copyright and license information, initial configuration for the software, and more.

The goal of packaging is to produce these packages from the unpacked source. The source package (.dsc) and binary packages (.deb) will be built for you by tools such as dpkg-buildpackage.

You can read more about the anatomy of [binary packages](/DebianPackage) or [source packages](/SourcePackage) on their wiki pages.

Packages must comply with Debian policy to be accepted into the package archives. Manually constructed .deb binary packages that are not built from a source package will not be accepted. This is to maintain consistency and reproducibility.

## Requirements

This tutorial assumes you understand:

* installation of binary packages
* general command line use
* editing files using a text editor of your choice

That is all you need.

Needed packages:

* [build-essential](https://packages.debian.org/build-essential "DebianPkg")
* [devscripts](https://packages.debian.org/devscripts "DebianPkg")
* [debhelper](https://packages.debian.org/debhelper "DebianPkg") version 13 or higher

## Three central concepts

The three central concepts are

* **upstream tarball**:

  + A **tarball** is the *.tar.gz* or *.tgz* file upstream makes (can also be in other compression formats like *.tar.bz2*,*.tb2* or *.tar.xz*).
  + Contains the software **upstream developer** has written.
* **source package**:

  + This is the second step in the packaging process, to build the **source package** from the upstream source.
* **binary package**:

  + From this source package you then build the **binary package**, which is distributed and installed.

The simplest [source package](/SourcePackage) consists of three files:

* The upstream tarball, renamed according to the naming convention
* A debian directory containing the changes made to upstream source, plus all the files required for the creation of a binary package.
* A description file (with *.dsc* extension), which contains metadata for the above two files.

## The packaging workflow

* Step 1: Rename the upstream tarball
* Step 2: Unpack the upstream tarball
* Step 3: Add the debian.tar.gz files
* Step 4: Build the package
* Step 5: Test the package

After testing, the source and binary packages can be uploaded in the Debian archive.

For this tutorial, [this tarball](/Packaging/Intro?action=AttachFile&do=view&target=hithere-1.0.tar.gz "this tarball") is used as an example.

### Step 1: Rename the upstream tarball

The packaging tools require that the tarball complies with the naming convention.

The name is as follows: source package name, underscore, upstream version number, followed by *.orig.tar.gz*. The source package name should be all lower case, and can contain letters, digits, and dashes. Some other characters are also allowed. More detailed naming convention can be found in [debmake doc](https://www.debian.org/doc/manuals/debmake-doc/ch05.en.html#name-version).

Minimal changes should be made to the original name, to make it Debian-compliant. If the original name complies with the standard, then you should use that.

In our example case, upstream has picked a suitable name, "hithere", so there are no changes needed.

We will end up with a file called **hithere\_1.0.orig.tar.gz**.

Note that there is an underscore (*\_*), not a dash (*-*), in the name. This is important.

* $ **mv** hithere-1.0.tar.gz hithere\_1.0.orig.tar.gz

### Step 2: Unpack the upstream tarball

The source will unpack into a directory of the same name and upstream version with a hyphen in between (not an underscore), so the upstream tarball should unpack into a directory called "hithere-1.0".

In this case, the tarball already unpacks into the correct subdirectory, so no changes are required.

* $ **tar** xf hithere\_1.0.orig.tar.gz

### Step 3: Add the Debian packaging files

All of the following files will be placed into the *debian/* subdirectory inside the source directory, so we create that directory.

* $ **cd** hithere-1.0   
  $ **mkdir** debian

Let's take a look at the files we need to provide.

#### debian/changelog

First file is **debian/changelog**. This is the log of changes to the Debian package.

It does not *need* to list everything that has changed in upstream code, but a summary is helpful for others.

Since we are now making the first version, there is nothing to log. However, we still need to make a changelog entry, because the packaging tools read information from the changelog: most importantly, the package version.

*debian/changelog* has a standard format. The easiest way to create it is to use the ***dch*** tool.

* $ **dch** --create -v 1.0-1 -u low --package hithere

This will result in a file like this:

```
hithere (1.0-1) UNRELEASED; urgency=low

  * Initial release. (Closes: #XXXXXX)

 -- Lars Wirzenius <liw@liw.fi>  Thu, 18 Nov 2010 17:25:32 +0000
```

A couple of notes:

* The package name (***hithere***) MUST be the same as the source package name. ***1.0-1*** is the version. The ***1.0*** part is the upstream version. The ***-1*** part is the Debian version: the first version of the Debian package of upstream version 1.0. If the Debian package has a bug, and it gets fixed, but the upstream version remains the same, then the next version of the package will be called 1.0-2. Then 1.0-3, and so on.
* ***UNRELEASED*** is called the upload target. It tells the upload tool where the binary package should be uploaded. ***UNRELEASED*** means the package is not yet ready to be uploaded. It's a good idea to keep the ***UNRELEASED*** there so you don't upload by mistake.
* ***urgency=low*** will not be explained yet.
* The ***(Closes: #XXXXXX)*** bit is for closing bugs when the package is uploaded. This is the usual way in which bugs are closed in Debian: when the package that fixes the bug is uploaded, the bug tracker notices this and marks the bug as closed. If there are no bugs fixed, this part can be omitted.
* The final line in the changelog tells who built this version of the package, and when. The dch tool tries to guess the name and e-mail address, but you can configure it with the right details. See the dch(1) manual page for details.

#### debian/control

The control file describes the source and binary package, and gives some information about them, such as their names, who the package maintainer is, and so on. Here is an example of what it might look like:

```
Source: hithere
Maintainer: Lars Wirzenius <liw@liw.fi>
Section: misc
Priority: optional
Standards-Version: 4.7.0
Build-Depends: debhelper-compat (= 13)

Package: hithere
Architecture: any
Depends: ${shlibs:Depends}, ${misc:Depends}
Description: greet user
 hithere greets the user, or the world.
```

There are several required fields, but you can just treat them as magic, for now. So, in *debian/control*, there are two stanzas.

The first stanza describes the **source package**, with these fields:

Source
:   The source package name.

Maintainer
:   The name and e-mail address of the person responsible for the package.

Priority
:   The priority of the package (one of 'required', 'important', 'standard' or 'optional'). In general, a package is 'optional' unless it's 'essential' for a standard functioning system, i.e., booting or networking functionality. As of [Debian Policy 4.5.1](https://www.debian.org/doc/debian-policy/ch-archive.html#s-priorities) (or sooner) package priority 'extra' is deprecated.

Build-Depends
:   The list of packages that need to be installed to build the package. They might or might not be needed to actually use the package.

All stanzas after the first describe the **binary packages** built from this source. There can be many binary packages built from the same source; our example only has one. We use these fields:

The *debhelper-compat* Build-Dependency specifies the "[compatibility level](https://manpages.debian.org/stable/debhelper.7.en#COMPATIBILITY_LEVELS)" for the [debhelper](https://packages.debian.org/debhelper "DebianPackage") tool level via the version constraint. The example above specifies compat level 13. (This replaces the obsolete debian/compat file)

Package
:   The name of the binary package. The name might be different from the source package name.

Architecture
:   Specifies which computer architectures the binary package is expected to work on: i386 for 32-bit Intel CPUs, amd64 for 64-bit, armel for ARM processors, and so on. Debian works on about a dozen computer architectures in total, so this architecture support is crucial. The "Architecture" field can contain names of particular architectures, but usually it contains one of two special values. 

    any
    :   (which we see in the example) means that the package can be built for any architecture. In other words, the code has been written portably, so it does not make too many assumptions about the hardware. However, the binary package will still need to be built for each architecture separately.

    all
    :   means that the same binary package will work on all architectures, without having to be built separately for each. For example, a package consisting only of shell scripts would be "all". Shell scripts work the same everywhere and do not need to be compiled.

Depends
:   The list of packages that must be installed for the program in the binary package to work. Listing such dependencies manually is tedious, error-prone work. To make this work more automatic, the ***${shlibs:Depends}*** magic bit needs to be in there for packages that contain built shared libraries and executables. The other magic stuff is there for debhelper, which will fill in the ***${misc:Depends}*** bit. For other dependencies, you need to add them manually to Depends or Build-Depends. Note that the ${...} magic bits only work in Depends, not Build-Depends.

Description
:   The full description of the binary package. It is meant to be helpful to users. The first line is used as the short synopsis (summary) description, and the rest of the description must be an independent longer description of the package.

The command *cme edit dpkg* provides a GUI to edit most packaging files, including *debian/control*. See [Managing Debian packages with cme](https://github.com/dod38fr/config-model/wiki/Managing-Debian-packages-with-cme) page. The cme command is shipped in Debian in the [cme](https://packages.debian.org/cme "DebianPkg") package. You can also edit **only** *debian/control* with *cme edit dpkg-control* command.

#### debian/copyright

It is quite an [important file](https://www.debian.org/doc/packaging-manuals/copyright-format/1.0/), but for now we will be happy enough with an empty file.

For Debian, this file is used to keep track of the legal, copyright-related information about a package. However, it is not important from a technical point of view. For now, we'll concentrate on the technical aspects. We can get back to *debian/copyright* later, if there's interest.

#### debian/rules

It should look like this:

```
#!/usr/bin/make -f
%:
        dh $@
```

* ![<!>](/htdocs/debwiki/img/attention.png "<!>") **Note**: The last line should be indented by one TAB character, not by spaces. The file is a makefile, and TAB is what the make command wants.

*debian/rules* can actually be quite a complicated file. However, the dh command in debhelper version 7 has made it possible to keep it this simple in many cases.

#### debian/source/format

The final file we need is *debian/source/format*, and it should contain the version number for the format of the source package, which is "3.0 (quilt)".

```
3.0 (quilt)
```

### Step 4: Build the package

#### First try

Now we can build the package.

There are many commands we could use for this, but this is the one we'll use. If you run the command, you'll get an output similar to this:

* $ **debuild** -us -uc

```
make[1]: Entering directory `/home/liw/debian-packaging-tutorial/x/hithere-1.0'
install hithere /home/liw/debian-packaging-tutorial/x/hithere-1.0/debian/hithere/usr/local/bin
install: cannot create regular file `/home/liw/debian-packaging-tutorial/x/hithere-1.0/debian/hithere/usr/local/bin': No such file or directory
make[1]: *** [install] Error 1
make[1]: Leaving directory `/home/liw/debian-packaging-tutorial/x/hithere-1.0'
dh_auto_install: make -j1 install DESTDIR=/home/liw/debian-packaging-tutorial/x/hithere-1.0/debian/hithere returned exit code 2
make: *** [binary] Error 29
dpkg-buildpackage: error: fakeroot debian/rules binary gave error exit status 2
debuild: fatal error at line 1325:
dpkg-buildpackage -rfakeroot -D -us -uc failed
```

Something went wrong. This is what usually happens. You do your best creating *debian/\** files, but there's always something that you don't get right.

So, the thing that went wrong is this bit:

```
install hithere /home/liw/debian-packaging-tutorial/x/hithere-1.0/debian/hithere/usr/local/bin
```

The upstream Makefile is trying to install the compiled program into the wrong location.

There are a couple of things going on here: first is a bit about how Debian packaging works.

#### Correction

When the program has been built, and is "installed", it does not get installed into **/usr** or **/usr/local**, as usual, but somewhere under the **debian/** subdirectory.

We create a subset of the whole file system under **debian/hithere**, and then we put that into the binary package. So the **.../debian/hithere/usr/local/bin** bit is fine, except that it should not be installing it under **usr/local**, but directly under **usr**.

We need to do something to make it install into the right location (**debian/hithere/usr/bin**).

The right way to fix this is to change **debian/rules** so that it tells the Makefile where to install things.

```
#!/usr/bin/make -f
%:
        dh $@

override_dh_auto_install:
        $(MAKE) DESTDIR=$$(pwd)/debian/hithere prefix=/usr install
```

It's again a bit of magic, and to understand it you'll need to know how Makefiles work, and the various stages of a debhelper run.

For now, I'll summarize by saying that there's a command debhelper runs that takes care of installing the upstream files, and this stage is called ***dh\_auto\_install***.

We need to override this stage, and we do that with a rule in **debian/rules** called ***override\_dh\_auto\_install***.

The final line in the new **debian/rules** is a bit of 1970s technology to invoke the upstream Makefile from **debian/rules** with the right arguments.

#### Let's try again

* $ **debuild** -us -uc

It still fails!

* This time, this is the failing command:

```
install hithere /home/liw/debian-packaging-tutorial/x/hithere-1.0/debian/hithere/usr/bin
```

We are now trying to install into the right place, but it does not exist. To fix this, we need to tell the packaging tools to create the directory first.

Ideally, the upstream Makefile would create the directory itself, but in this case the upstream developer was too lazy to do so.

#### Another correction

The packaging tools (specifically, debhelper) provide a way to do that.

* Create a file called **debian/hithere.dirs**, and make it look like this:

```
usr/bin
usr/share/man/man1
```

The second line creates the directory for the manual page. We will need it later. You should be careful to maintain such \*.dirs files because it can lead to empty directories in future versions of your package if the items listed in those files aren't valid anymore.

#### Let's try once more

* $ **debuild** -us -uc

Now the build succeeds, but there are still some small problems.

*debuild* runs the *lintian* tool, which checks the package that has been built for some common errors. It reports several for this new package:

```
Now running lintian...
W: hithere source: out-of-date-standards-version 3.9.0 (current is 3.9.1)
W: hithere: copyright-without-copyright-notice
W: hithere: new-package-should-close-itp-bug
W: hithere: wrong-bug-number-in-closes l3:#XXXXXX
Finished running lintian.
```

These should eventually be fixed, but none of them look like they'll be a problem for trying the package. So let's ignore them for now.

Look in the parent directory to find the package that was built.

* $ **ls** ..

```
hithere-1.0                  hithere_1.0-1_amd64.deb  hithere_1.0.orig.tar.gz
hithere_1.0-1_amd64.build    hithere_1.0-1.debian.tar.gz
hithere_1.0-1_amd64.changes  hithere_1.0-1.dsc
```

### Step 5: Install the package

The following command will install the package that you've just built.

Do NOT run it on a computer unless you don't mind breaking it.

* In general, it is best to do package development on a computer that is well backed up, and that you don't mind re-installing if everything goes really badly wrong.

Virtual machines are a good place to do development.

* $ **sudo** dpkg -i ../hithere\_1.0-1\_amd64.deb

```
[sudo] password for liw:
Selecting previously deselected package hithere.
(Reading database ... 154793 files and directories currently installed.)
Unpacking hithere (from ../hithere_1.0-1_amd64.deb) ...
Setting up hithere (1.0-1) ...
Processing triggers for man-db ...
liw@havelock$
```

How do we test the package? We can run the command.

* $ **hithere**

It works!

But, it's not perfect. Remember, lintian had things to say, and **debian/copyright** is empty, etc.

We have a package that works, but it isn't yet of the high quality that is expected of a Debian package.

## Conclusion

Once you've built your own packages, you'll eventually want to learn how to set up your apt repository, so your package is easy to install. The best tool for that I know of is [reprepro](https://packages.debian.org/reprepro "DebianPkg").

For more testing of your package, you may want to look at the tool called [piuparts](https://packages.debian.org/piuparts "DebianPkg"). (I wrote it originally so it is perfect and never has any bugs. er...)

And, finally, if you start making changes to the upstream source, you'll want to learn about the [quilt](https://packages.debian.org/quilt "DebianPkg") tool.

Other things you might want to read are listed in the [Debian Developers' Corner](https://www.debian.org/devel/).

## See also

* the [packaging FAQ](/PackagingFAQ) answers some common questions
* [Debian Developers' Corner](https://www.debian.org/devel/)
* [Debian Policy Manual](https://www.debian.org/doc/debian-policy/)
* [Writing manual pages](https://liw.fi/manpages/) by Lars Wirzenius
* the [rebuilding tutorial](/BuildingTutorial)
* [Packaging](/Packaging) is the page that gathers everything about packaging on this wiki
* [Debian Women IRC log: making Debian packages](http://meetbot.debian.net/debian-women/2010/debian-women.2010-11-18-20.05.html)
* [Debian Women IRC log: taking an existing package, re-building it, applying changes to it, and preparing those changes so as to send them as a bug patch.](http://meetbot.debian.net/debian-women/2011/debian-women.2011-05-07-11.00.html)

---

[CategoryPackaging](/CategoryPackaging)