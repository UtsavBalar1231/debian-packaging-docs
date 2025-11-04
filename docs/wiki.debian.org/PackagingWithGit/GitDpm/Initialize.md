# PackagingWithGit/GitDpm/Initialize - Debian Wiki

**Source:** https://wiki.debian.org/PackagingWithGit/GitDpm/Initialize

---

Contents

1. [Introduction](#Introduction)
2. [Branch names](#Branch_names)
3. [The tarfile (required)](#The_tarfile_.28required.29)
4. [The upstream branch (required)](#The_upstream_branch_.28required.29)
5. [An already existing debian branch](#An_already_existing_debian_branch)
   1. [Preapplied patches](#Preapplied_patches)
   2. [Importing patches](#Importing_patches)
   3. [Your own patched branch](#Your_own_patched_branch)

# Introduction

This page describes how to initialize a [git-dpm](/PackagingWithGit/GitDpm) project, or a git repository that uses git-dpm to maintain a Debian source package, using git-dpm init. Alternatively, you can also initialize a git-dpm project by import [.dsc files](/dsc) using git-dpm import-dsc.

To create a new git-dpm project using git-dpm init you need some of the following things:

1. A .orig.tar file.
2. A git commit containing something [similar enough](/PackagingWithGit/GitDpm/SimilarEnough) to your .orig.tar file.
3. A git commit that is descendant of the above that contains patches already in your debian branch (optional).
4. A git commit that is descandant of this with other patches (optional).
5. A git commit containing the current state of your project (optional).

The syntax of git-dpm init is:

git-dpm [*global options>*] init [*local options*] *tarfile* [*upstream-commit* [*preapplied-commit* [*patched-commit*]]]

# Branch names

As with most other subcommands, init looks at the current HEAD to determine which branches your project will use. If it is called master, upstream or patched, your debian branch will be called master, your upstream branch upstream and your patched branch patches. Otherwise your debian branch will be called *something*, your upstream branch upstream-something and your patched branch patched-*something* in a way that your current HEAD is one of those three names.

# The tarfile (required)

The *tarfile* is only needed for two things. It's basename and its sha1sum are recorded (so git-dpm can later make sure you have the correct file around). Otherwise it is not looked at (future versions might check more).

# The upstream branch (required)

If there is no second argument, your upstream branch must already exist. Otherwise it will be set to this commit. This is the only thing beside the tarball that is not optional. An easy way to create it is just importing the .orig.tar filename. It must not contain the exact same contents, but it must be [similar enough](/PackagingWithGit/GitDpm/SimilarEnough). So the easiest example, if you want to create a project with debian branch foo and containing foo\_0.0.0.orig.tar.gz, is:

```
git branch -D foo  # make sure there is no branch foo
git-dpm import-tar ../foo_0.0.0.orig.tar.gz
git checkout -b upstream-foo
git-dpm init ../foo_0.0.0.orig.tar.gz
```

The so created project will just contain the upstream source and a debian/.git-dpm file recording it. You need to add the rest of debian/ yourself, but all the git-dpm stuff should already work[1](#fnref-6d9c54c3f7a7578c00f7114be0080064e57145b9).

# An already existing debian branch

If your debian branch already exists, git-dpm will create a new commit on top of that with the new debian/.git-dpm file and with debian/ direcory taken from that branch, while the rest of the tree is the patched upstream source. How this is generated is controlled by the other arguments of the init command. There are a few different scenarios, described in the sections below.

## Preapplied patches

If you have a debian branch (called master or something else, see above), git-dpm assumes that its tree is the one from your upstream branch (except debian/, files like .gitignore or .gitattributes and possible file deletions). If that is not the case, you must give init a third argument pointing to a branch with those changes applied. This should be a commit/branch based on your upstream branch and not containing any changes in debian/.

If there are no such changes and you want to give this argument (because you want to specifiy more arguments), you can just repeat the second argument (the *upstream*).

## Importing patches

If there is no fourth argument (after *tarfile*, *upstream* and *preapplied*), git-dpm will look into your debian branch (if it already exists) for possible patches in a quilt series or a dpatch list it can apply. If it finds some, it will try to apply them.

## Your own patched branch

If the options above give a result you do not like, or you want different patches, you can just create a commit/branch on top of the preapplied commit and give that as fourth argument.

---

1. Well, git-dpm tag will fail because there is no debian/changelog to get the name or version from ![;-)](/htdocs/debwiki/img/smile4.png ";-)") ([1](#fndef-6d9c54c3f7a7578c00f7114be0080064e57145b9-0))