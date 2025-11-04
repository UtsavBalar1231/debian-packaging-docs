# PackagingFAQ - Debian Wiki

**Source:** https://wiki.debian.org/PackagingFAQ

---

Frequently asked questions about creating packages. For general information, see [Packaging](/Packaging).

Contents

1. [General questions](#General_questions)
   1. [What do people mean by "the package" vs. "the source package" or "the binary package"?](#What_do_people_mean_by_.22the_package.22_vs._.22the_source_package.22_or_.22the_binary_package.22.3F)
   2. [What is a good packaging workflow?](#What_is_a_good_packaging_workflow.3F)
      1. [How do I keep track of my packaging changes?](#How_do_I_keep_track_of_my_packaging_changes.3F)
   3. [Can I make a package that just configures other packages?](#Can_I_make_a_package_that_just_configures_other_packages.3F)
   4. [Can I make a package that updates files in /home?](#Can_I_make_a_package_that_updates_files_in_.2Fhome.3F)
   5. [How do I make a package if upstream includes a /debian subdirectory?](#How_do_I_make_a_package_if_upstream_includes_a_.2Fdebian_subdirectory.3F)
   6. [How do I make a package if upstream only provides binaries (e.g. Nvidia blobs)?](#How_do_I_make_a_package_if_upstream_only_provides_binaries_.28e.g._Nvidia_blobs.29.3F)
   7. [What is a non-maintainer upload?](#What_is_a_non-maintainer_upload.3F)
      1. [If I do a non-maintainer upload, which debian/control field should I put my name in?](#If_I_do_a_non-maintainer_upload.2C_which_debian.2Fcontrol_field_should_I_put_my_name_in.3F)
   8. [What is the Debian equivalent of Ubuntu PPAs?](#What_is_the_Debian_equivalent_of_Ubuntu_PPAs.3F)
   9. [What's the difference between a "native" and "quilt" patch system?](#What.27s_the_difference_between_a_.22native.22_and_.22quilt.22_patch_system.3F)
   10. [What does “dfsg” or “ds” in the version string mean?](#What_does_.2BIBw-dfsg.2BIB0_or_.2BIBw-ds.2BIB0_in_the_version_string_mean.3F)
2. [Manipulating package files](#Manipulating_package_files)
   1. [How do I access the contents of a package?](#How_do_I_access_the_contents_of_a_package.3F)
   2. [How do I find out who uploaded a package?](#How_do_I_find_out_who_uploaded_a_package.3F)
   3. [How do I find the .dsc files etc. for packages in /var/cache/apt/archives?](#How_do_I_find_the_.dsc_files_etc._for_packages_in_.2Fvar.2Fcache.2Fapt.2Farchives.3F)
      1. [How do I get the changelog for packages in /var/cache/apt/archives?](#How_do_I_get_the_changelog_for_packages_in_.2Fvar.2Fcache.2Fapt.2Farchives.3F)
3. [Building packages](#Building_packages)
   1. [What format should orig tarball filenames have?](#What_format_should_orig_tarball_filenames_have.3F)
   2. [Should I repack the original tarball if it doesn't have a /<packagename>-<version> folder?](#Should_I_repack_the_original_tarball_if_it_doesn.27t_have_a_.2F.3Cpackagename.3E-.3Cversion.3E_folder.3F)
   3. [What does the --pristine-tar option for gbp commands do?](#What_does_the_--pristine-tar_option_for_gbp_commands_do.3F)
   4. [How do I check the upstream source for DFSG-compliance?](#How_do_I_check_the_upstream_source_for_DFSG-compliance.3F)
   5. [Where should I run build commands from?](#Where_should_I_run_build_commands_from.3F)
   6. [My upstream uses a strange build system, how do I support it?](#My_upstream_uses_a_strange_build_system.2C_how_do_I_support_it.3F)
      1. [Should I use --with $ADDON?](#Should_I_use_--with_.24ADDON.3F)
   7. [Where is the documentation for debian/rules targets like dh\_auto\_install?](#Where_is_the_documentation_for_debian.2Frules_targets_like_dh_auto_install.3F)
   8. [How do I sign packages with an OpenPGP signature?](#How_do_I_sign_packages_with_an_OpenPGP_signature.3F)
   9. [What's the difference between Depends: and Build-Depends: in debian/control?](#What.27s_the_difference_between_Depends:_and_Build-Depends:_in_debian.2Fcontrol.3F)
      1. [Can I have a Build-Depends without a corresponding Depends?](#Can_I_have_a_Build-Depends_without_a_corresponding_Depends.3F)
   10. [How do I know which packages to (build-)depend on?](#How_do_I_know_which_packages_to_.28build-.29depend_on.3F)
   11. [How do I build a package for e.g. arm64 on my PC?](#How_do_I_build_a_package_for_e.g._arm64_on_my_PC.3F)
   12. [Should Architecture: all builds mention the architecture in the output?](#Should_Architecture:_all_builds_mention_the_architecture_in_the_output.3F)
   13. [Does Architecture: foo affect the build process or the binary package?](#Does_Architecture:_foo_affect_the_build_process_or_the_binary_package.3F)
   14. [How do I track upstream changes?](#How_do_I_track_upstream_changes.3F)
   15. [Is it OK to edit old changelog entries?](#Is_it_OK_to_edit_old_changelog_entries.3F)
   16. [What does "dpkg-source: info: local changes detected" mean?](#What_does_.22dpkg-source:_info:_local_changes_detected.22_mean.3F)
4. [See also](#See_also)

# General questions

## What do people mean by "the package" vs. "the source package" or "the binary package"?

Saying "the package" can refer to any of:

1. a source .dsc package, which you use to build one or more binary packages
2. a binary .deb package, which you install on your computer
3. the source .dsc package and the complete set of .deb packages generated by it
4. the most interesting .deb package in the current conversation

   * e.g. if foo depends on foo-doc, you might talk about "the package" and "the doc package"

You can usually work out which one people are referring to from the context. For example, newbies often talk about "the package" but mean "the binary package" because they don't know source packages exist; whereas packaging guides often talk about "the package" but mean "the source package" because they haven't told you to build any binary packages yet. If in doubt, ask which package someone is referring to.

## What is a good packaging workflow?

It depends on your personal preference, and the specific package you're working on. Every packaging guide will give you a different recommendation, and most of them will insist theirs is the only correct choice. Just try stuff and find out what works for you.

The guides in [Packaging](/Packaging) might give you some inspiration, and the [debian-mentors' packaging questions](/DebianMentorsFaq#Packaging) might point you in a good direction.

### How do I keep track of my packaging changes?

Most people do their [packaging with git](/PackagingWithGit) or some other version control system. If you've adopted a package that's been around since before git, <https://snapshot.debian.org/> lets you download packages from older versions of Debian, which you can compare using debdiff and interdiff (in [devscripts](https://packages.debian.org/devscripts "DebianPkg") and [patchutils](https://packages.debian.org/patchutils "DebianPkg")).

## Can I make a package that just configures other packages?

It's technically possible, but such a package will only be accepted in Debian if it uses a documented interface of the other package.

Editing configuration files creates a lot of weird problems. For example, say the packages foo and bar both add the same message to /etc/motd. If you install both packages, should the message be added twice? If not, what happens when you uninstall one package but not the other?

Safely editing other packages' configuration files can only be done on a case-by-case basis, so it's against [Debian policy](https://www.debian.org/doc/debian-policy/) unless the package in question specifically supports it. For example, [logrotate](https://packages.debian.org/logrotate "DebianPkg") lets other packages put files in /etc/logrotate.d/, which it then uses to configure log rotations.

If you're doing [infrastructure as code](https://en.wikipedia.org/wiki/Infrastructure_as_code "WikiPedia"), you probably want a [continuous configuration automation tool](https://en.wikipedia.org/wiki/Infrastructure_as_code#Continuous_configuration_automation "WikiPedia") like [Ansible](https://www.ansible.com/) instead.

## Can I make a package that updates files in /home?

No. Files in /home aren't yours to update - see [debian-mentors thread](https://lists.debian.org/debian-mentors/2012/07/msg00429.html) and [Debian Policy entry](https://www.debian.org/doc/debian-policy/ch-files.html#s10.7.5).

Work with your upstream to find another solution. These include:

* if a user has a deprecated setting, have your program display a warning or refuse to run until it's fixed
* read from more than one file 
  + e.g. read from both ~/.config/foo.conf and /etc/foo/foo.conf
* provide a mechanism for users to include other files 
  + e.g. let ~/.config/foo.conf have a line like include /etc/foo/foo.conf

If you're writing a private package and are really convinced this is the right solution, you're probably using packages to do [infrastructure as code](https://en.wikipedia.org/wiki/Infrastructure_as_code "WikiPedia"). Consider using a [continuous configuration automation tool](https://en.wikipedia.org/wiki/Infrastructure_as_code#Continuous_configuration_automation "WikiPedia") like [Ansible](https://www.ansible.com/) instead.

## How do I make a package if upstream includes a /debian subdirectory?

Debian packaging information goes in the debian/ subdirectory of the package's top-level directory. Upstreams are [asked not to include a /debian directory](/UpstreamGuide#Do_not_include_a_.2Fdebian_directory), but some do anyway.

Modern packaging tools will delete this directory automatically, or you'll need to delete it manually if you're just git pulling an upstream repository. For details, see [If upstream has a /debian directory or file](/ManageUpstreamDifferences#If_upstream_has_a_.2Fdebian_directory_or_file).

Historically, this used to be a bigger problem. You may need to do some extra work if you're adopting a really old package that still uses the 1.0 format.

## How do I make a package if upstream only provides binaries (e.g. Nvidia blobs)?

Treat the tarball with the blobs as the source package, avoid compiling them from source.

You'll have difficulty getting your package accepted into Debian, for a mixture of practical reasons (how do you do a security review on a binary blob?) and philosophical ones ([Debian is about software freedom](https://www.debian.org/intro/philosophy)).

For information about Nvidia, see [NvidiaGraphicsDrivers](/NvidiaGraphicsDrivers).

## What is a non-maintainer upload?

It's when a package is uploaded to the Debian archive by someone other than its maintainer.

For more information, see [NonMaintainerUpload](/NonMaintainerUpload).

### If I do a non-maintainer upload, which debian/control field should I put my name in?

None of them, but please make the first line of the changelog "Non-maintainer upload".

debian/control has a [Maintainer field](https://www.debian.org/doc/debian-policy/ch-controlfields.html#maintainer) for the primary maintainer, and an [Uploaders field](https://www.debian.org/doc/debian-policy/ch-controlfields.html#uploaders) for co-maintainers. Despite the name, these are not required for [non-maintainer uploads](/NonMaintainerUpload).

The [changelog](https://www.debian.org/doc/debian-policy/ch-source.html#s-dpkgchangelog) should explain what changes you've made. Putting "Non-maintainer upload" here clarifies that you made the change without implying you're involved in ongoing maintenance.

## What is the Debian equivalent of Ubuntu PPAs?

Debian does not run a PPA service like Ubuntu, but it's easy enough to [create your own repository](/DebianRepository/Setup) and upload it to any static hosting service.

One guide to creating a repo is [DebianRepository/SetupWithReprepro](/DebianRepository/SetupWithReprepro).

## What's the difference between a "native" and "quilt" patch system?

Prefer quilt unless you're certain the package will *never* be useful outside of Debian. For example, [dpkg](https://packages.debian.org/dpkg "DebianPkg") is a native package, [libc6](https://packages.debian.org/libc6 "DebianPkg") is non-native.

Putting 3.0 (native) in debian/source/format disallows any differences between upstream and Debian outside of the debian/ directory, 3.0 (quilt) manages such changes using the "quilt" patch system, which was pioneered by [the program of the same name](https://packages.debian.org/quilt "DebianPkg") and is now used by all common tools. If in doubt, prefer 3.0 (quilt).

Most packages have versions like 1.2.3-4, where -4 is the Debian revision. Native packages versions just look like 1.2.3, because native format doesn't support separate Debian revisions. Native format is only useful for Debian-specific packages like [dpkg](https://packages.debian.org/dpkg "DebianPkg"), where the flexibility of the quilt format would just add needless complexity.

For more information, see [Projects/DebSrc3.0](/Projects/DebSrc3.0) and [If upstream content needs patching](/ManageUpstreamDifferences#If_upstream_content_needs_patching).

## What does “dfsg” or “ds” in the version string mean?

+dfsg.N and +ds.N are a conventional way of extending a version string, when the Debian package's upstream source tarball is actually different from the source released upstream.

+dfsg in a version string stands for [Debian Free Software Guildelines](/DebianFreeSoftwareGuidelines), and means upstream's source release contains elements that must not be hosted by Debian.

+ds in a version string stands for “Debian Source”, and means upstream's source release was modified for non-DFSG reasons (e.g. it contains huge optional files that would waste space on Debian's servers).

.N is the number of times you've repacked since changing the part of the version number before the +.

The changes should be documented in README.source.

# Manipulating package files

## How do I access the contents of a package?

Show the contents of an installed package:

```
 dpkg -L <package-name>
```

Access the contents of a package you have downloaded but not installed:

```
# List the contents of a binary package:
dpkg-deb -c <package-name>.deb
# Extract the contents of a binary package:
dpkg-deb -x <package-name>.deb /tmp/package-name
# Extract the contents of a source package:
dpkg-source -x <source-package-name>.dsc /tmp/source-package-name
```

Download a package without installing it:

```
sudo apt-get download <package-name>
```

List the contents of a package in Debian without downloading it (using [apt-file](https://packages.debian.org/apt-file "DebianPkg")):

```
sudo apt-get install apt-file
sudo apt-file update
apt-file list <package-name>
```

.debs are [binary packages](/DebianPackage), .dscs are [source packages](/SourcePackage). See also [dpkg-deb](https://manpages.debian.org/man/dpkg-deb "DebianMan") and [dpkg-source](https://manpages.debian.org/man/dpkg-source "DebianMan").

## How do I find out who uploaded a package?

```
who-uploads <package-name>
```

(who-uploads is in [devscripts](https://packages.debian.org/devscripts "DebianPkg"))

## How do I find the .dsc files etc. for packages in /var/cache/apt/archives?

Go to https://packages.debian.org/<distro>/<packagename> (e.g. <https://packages.debian.org/sid/hello>) and search for "Download Source Package". The files are linked from a section on the right of the page.

.debs are [binary packages](/DebianPackage). To save bandwidth, the associated [source packages](/SourcePackage) aren't downloaded by default.

For alternative solutions, see [Get the source package](/BuildingTutorial#Get_the_source_package).

### How do I get the changelog for packages in /var/cache/apt/archives?

If you have installed the package, it should be in /usr/share/doc/<package-name>/changelog.gz. Otherwise, do:

```
dpkg-deb -x /var/cache/apt/archives/<package-name> /tmp/package-name
ls /tmp/package-name/usr/share/doc/*/
```

# Building packages

## What format should orig tarball filenames have?

<packagename>\_<version>.orig.tar.gz (or .bz2 etc.).

For a list of valid compression schemes, see [dpkg-source --compression](https://manpages.debian.org/man/dpkg-source#Z "DebianMan"). For upstream guidance about source tarballs, see [Provide a well-named source tarball](/UpstreamGuide#Provide_a_well-named_source_tarball).

## Should I repack the original tarball if it doesn't have a /<packagename>-<version> folder?

No. Upstream developers often have their tarball's root directory contain a single subdirectory named after the project and version, but modern tools can work around this.

For more upstream developer recommendations, see [Provide a well-named source tarball](/UpstreamGuide#Provide_a_well-named_source_tarball).

## What does the --pristine-tar option for gbp commands do?

These manage a "pristine" tarball - one that is byte-for-byte identical every time (files stored in the same order etc.).

For details, see [DebianPackaging--pristine-tar-option-explained](/DebianPackaging--pristine-tar-option-explained).

## How do I check the upstream source for DFSG-compliance?

One solution is to install [devscripts](https://packages.debian.org/devscripts "DebianPkg"), then do:

```
licensecheck -r /path/to/upstream/source/
```

For more solutions, see [CopyrightReviewTools](/CopyrightReviewTools).

## Where should I run build commands from?

Wherever upstream wants you to run them from. For git projects, it's usually the directory with the .git subdirectory. For raw tarballs, it's usually the <project>-<version>/ directory created by the tarball.

Upstream maintainers are encouraged to [support out-of-tree builds](/UpstreamGuide#Support_out-of-tree_builds), but not all of them do.

## My upstream uses a strange build system, how do I support it?

At the time of writing, Debian's build system has modules to deal with ant, autoconf, cmake, make, meson, ninja, Perl (Module::Build and ExtUtils::MakeMaker), Python (distutils) and qmake (normal and qt4). These should all work without you needing to configure anything. You can edit debian/rules if you need to add something special, but that's rare nowadays.

Some build systems have proven difficult for packaging. See [Avoid Scons](/UpstreamGuide#Avoid_SCons) and [Avoid waf](/UpstreamGuide#Avoid_waf).

For upstream guidance about build systems, see [Document your build system](/UpstreamGuide#Document_your_build_system). For a list of build system modules, see [/usr/share/perl5/Debian/Debhelper/Buildsystem/\*.pm](https://packages.debian.org/stable/all/libdebhelper-perl/filelist#:~:text=/usr/share/perl5/Debian/Debhelper/Buildsystem/).

### Should I use --with $ADDON?

That works, but it's better to put Build-Depends: dh-sequence-$ADDON in debian/control instead.

Older guides often recommend putting e.g. dh $@ --with python3 in debian/rules. Specifying addons this way was a big advance when it was introduced, but people gradually found edge cases where it caused problems. Adding e.g. Build-Depends: dh-sequence-python3 does the same thing while solving those edge cases.

For details, see [dh-sequence-\* dependencies](/Multiarch/Implementation#dh-sequence-.2A_dependencies).

## Where is the documentation for debian/rules targets like dh\_auto\_install?

Find the rules your package uses with grep dh\_ /path/to/your/package.build, then look for documentation with man dh\_something or zgrep 'dh\_something' /usr/share/man/man?/\*. For example, [man dh\_auto\_install](https://manpages.debian.org/man/dh_auto_install "DebianMan").

dh uses a sequence of targets to build a package; each is called dh\_something and can be overridden by a target in debian/rules called override\_dh\_something. There's no central list, but many targets have man pages.

For information about dh itself, see [dh](https://manpages.debian.org/man/dh "DebianMan").

## How do I sign packages with an OpenPGP signature?

To sign *a whole package* yourself, you'll need to [create a key](/Keysigning) and get it [signed by an existing Debian Developer](/Keysigning/Coordination). Consider [finding a sponsor](https://mentors.debian.net/sponsors/) instead.

Debian uses OpenPGP signatures to *authenticate* you are who you say you are, but uses the [Debian keyring](/DebianKeyring) to *authorise* you to upload packages. Getting on the keyring is a difficult process, and often not necessary.

To sign *git repo tags*, see [Configure git-buildpackage](/PackagingWithGit#Configure_git-buildpackage). To sign *upstream releases*, see [Sign releases](/UpstreamGuide#Sign_releases).

## What's the difference between Depends: and Build-Depends: in debian/control?

Depends: foo means "install foo before installing the package". Build-Depends: foo means "install foo before building the package from source". Packages can be both build-dependencies and normal dependencies, but are usually only one or the other.

Consider an upstream tarball with a PHP script in it. If the script is copied into the binary package and used when the program is running, that's Depends: php. Or if the script is used by the build system to run some tests, that's Build-Depends: php. If it's used in both places, add both lines.

### Can I have a Build-Depends without a corresponding Depends?

Yes. Build-Depends and Depends are entirely separate. It's common to have dependencies in one but not the other.

## How do I know which packages to (build-)depend on?

With difficulty! Solutions include:

* check the README file 
  + [we ask upstream to put dependencies there](/UpstreamGuide#Specify_dependencies_and_versions)
* build the package in a build environment using [pbuilder](/pbuilder) or [sbuild](/sbuild)

  + missing build-dependencies will now cause build failures
  + you can [tell git-buildpackage to do this automatically](/PackagingWithGit#Configure_git-buildpackage)
* run [autopkgtest](/autopkgtest)s in a test environment

  + missing runtime-dependencies will now cause test failures
* install [devscripts](https://packages.debian.org/devscripts "DebianPkg") and run the program with [dpkg-depcheck](https://manpages.debian.org/man/dpkg-depcheck "DebianMan")
* read the program's source code
* send upstream a patch with everything you think should be in the README 
  + helps people packaging for other distributions
  + often said to be [the best way to get the right answer](https://meta.wikimedia.org/wiki/Cunningham%27s_Law)
* wait for bug reports to come in 
  + this feels bad, but it happens to all of us

## How do I build a package for e.g. arm64 on my PC?

If you're using [git-buildpackage](/PackagingWithGit):

```
gbp buildpackage --git-dist=<dist> --git-arch=<arch>
```

For more information, see [CrossCompiling](/CrossCompiling).

## Should Architecture: all builds mention the architecture in the output?

Yes, this is fine.

Architecture: all means your package can be *installed* on all architectures, but it still needs to be *built* on a specific architecture. Your .build, .buildinfo and .changes files log that architecture in case you need to e.g. debug a problem that only happens when someone builds your package on a Raspberry Pi.

## Does Architecture: foo affect the build process or the binary package?

Both. The build process only builds Architecture: all packages once, other packages need to be rebuilt for each supported architecture. The install process allows Architecture: all packages to be installed on any system, other architectures are only allowed if they're supported by the current system.

For information about allowing more than one architecture on the same system, see [Multiarch/HOWTO](/Multiarch/HOWTO).

## How do I track upstream changes?

See [debian/watch](/debian/watch) for ways to configure Debian's upstream-tracking system. Examples for common [forges](/CategoryForge) like GitHub are on that page and in the [uscan manual](https://manpages.debian.org/man/uscan#WATCH_FILE_EXAMPLES "DebianMan").

## Is it OK to edit old changelog entries?

You should refrain from doing so, but it's allowed if you have a good reason.

See [debian-mentors discussion](https://lists.debian.org/debian-mentors/2012/04/msg00387.html).

## What does "dpkg-source: info: local changes detected" mean?

If your build system finds differences between your project directory and your upstream orig.tar.gz file, it will print something like this:

```
dpkg-source: info: building your-package using existing ./your-package_1.0.orig.tar.gz
dpkg-source: info: local changes detected, the modified files are:
 your-package/your-file
dpkg-source: error: aborting due to unexpected upstream changes, see /tmp/your-package_1.0-1.diff.9bUrC7
dpkg-source: hint: make sure the version in debian/changelog matches the unpacked source tree
dpkg-source: hint: you can integrate the local changes with dpkg-source --commit
```

Changes outside debian/ need to be tracked specially, for legal and security reasons. Check the file(s) mentioned in the message - it might just be a temporary file you forgot to delete, or you might need to [manage differences with upstream](/ManageUpstreamDifferences).

# See also

* [the debian-mentors FAQ](/DebianMentorsFaq) has [a packaging section](/DebianMentorsFaq#Packaging)
* Many of these are based on questions from two Debian Women IRC logs: 
  + [making Debian packages](http://meetbot.debian.net/debian-women/2010/debian-women.2010-11-18-20.05.html)
  + [taking an existing package, re-building it, applying changes to it, and preparing those changes so as to send them as a bug patch](http://meetbot.debian.net/debian-women/2011/debian-women.2011-05-07-11.00.html)

---

[CategoryPackaging](/CategoryPackaging)