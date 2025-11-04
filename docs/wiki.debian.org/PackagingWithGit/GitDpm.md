# PackagingWithGit/GitDpm - Debian Wiki

**Source:** https://wiki.debian.org/PackagingWithGit/GitDpm

---

[Translator(s)](/DebianWiki/EditorGuide#translation): English - [Indonesian](/id/PackagingWithGit/GitDpm)

---

[git-dpm](https://packages.debian.org/git-dpm "DebianPkg") helps maintain packages with [git](/git). For alternatives, see [Package maintenance tools](/PackagingTools#Package_maintenance_tools).

# Maintaining Debian source packages in git with git-dpm

This page describes how to use git-dpm to maintain Debian source packages in a git repository. See also the manpage [git-dpm(1)](https://manpages.debian.org/unstable/git-dpm/git-dpm.1.en.html) for more documentation.

**Compatibility with gbp (git-buildpackage) and DEP-14**

Please note that git-dpm is not compatible with the workflow of gbp (git-buildpackage) tools as well as the recommended Debian Enhance Proposal [DEP-14: Recommended layout for Git packaging repositories](https://dep-team.pages.debian.net/deps/dep14/). If you want to use gbp family of commands rather than git-dpm to maintain Debian source packages in a git repository, please read [Packaging with Git](/PackagingWithGit) instead.

Contents

1. [Maintaining Debian source packages in git with git-dpm](#Maintaining_Debian_source_packages_in_git_with_git-dpm)
   1. [Design goals](#Design_goals)
   2. [Documentation](#Documentation)
      1. [How to start](#How_to_start)
      2. [Common operations](#Common_operations)
         1. [Build a package](#Build_a_package)
         2. [Add a patch](#Add_a_patch)
   3. [Tricks](#Tricks)
   4. [Shortcomings](#Shortcomings)

## Design goals

The main design goals are:

* Make the generated source packages dsc format [3.0 (quilt)](/Projects/DebSrc3.0). So users unpacking the source packages from their CD or one of the Debian mirrors can easily evaluate the modifications and also look at them at [patch-tracker](http://patch-tracker.debian.org/). When they unpack a package with dpkg-source they get the final source (no understanding of any patch system needed).
* Store the patches as permanent git commits. Patches are imported at most once and then live as git commits and are edited with git methods (amend, rebase, ...). No repeated translation from patch to commit back to patch back to commit. Upstream or people from other distributions can just cherry-pick patches from your repository.
* Contain all information in one branch that can pushed and pulled fast-forwardly. While git rebase -i is the better quilt, git has no easy way to collaborate on such a branch or to retain its history. That's why in a git-dpm based workflow the patched branch is not published as git branch but only as a merged part of the history.
* Look as similar as results from Debian tools as possible. The result of an git clone should be similar enough to the source package unpacked with dpkg-source -x, so one can point users not familiar with git or git-dpm to the version stored in git to be able to test unfinished versions. Allow removal of files in the debian branch relatively to the upstream branch to support the traditional way of removing files modified by the build process in debian/rules clean.

## Documentation

### How to start

You can either import [.dsc files](/dsc) or [start from scratch](/PackagingWithGit/GitDpm/Initialize).

The following command will import a .dsc file and try to import it as git-dpm project:

```
git-dpm import-dsc --branch branchname package.dsc
```

If *branchname* does already exist, it will be added as git parent commit, otherwise a new branch will be created.

Use -p argument oo include upstream's history to the parents of the imported .orig.tar file. For example if the git repository you are in contains a tag foo-1.1 the command would look like this:

```
git-dpm import-dsc --branch foo-debian -p foo-1.1 ../foo_1.1-1.dsc
```

### Common operations

#### Build a package

The following command will check if everything is ready (possibly checking out a missing .orig.tar file using pristine tar) and then build it:

```
git-dpm prepare && dpkg-buildpackage -rfakeroot -us -uc
```

Usually it should suffice to just place the .orig.tar file in the parent directory and call dpkg-buildpackage, but git-dpm prepare will make sure you are not in the middle of some change and the correct .orig.tar file is there.

#### Add a patch

To write a patch yourself:

```
git-dpm checkout-patched
vim files
git commit -a
git-dpm update-patches
```

Include a patch file:

```
git-dpm apply-patch patchfile
git-dpm update-patches
```

Cherry pick a commit from upstream:

```
git-dpm cherry-pick commit
git-dpm update-patches
```

You of course only need the update-patches command once you are done and not if you want to add more stuff or edit any of the patches afterwards.

## Tricks

* Users of git-buildpackage are used to see the new upstream committed to pristine-tar; this can be achieved by changing a configuration default of git-dpm like this:

```
git config --global dpm.pristineTarCommit true
```

* Users of git-buildpackage are also used to see branches tagged for each version ; that can be achieved by adding the following to debian/.git-dpm (hence it's a per-package setting) :

```
debianTag="debian/%e%v"
patchedTag="patched/%e%v"
upstreamTag="upstream/%e%u"
```

## Shortcomings

* As git-dpm is quite new, it usually misses many of the nice gimmicks and some of the automatisms the tools from the git-buildpackage family offer.
* Multiple upstream tarballs are implemented but could need some testing.
* Documentation is horrible (your humble author is bad at writing documentation even beyond the usual non-native speaker's inability to do so).