# PackagingWithDarcsAndTailor - Debian Wiki

**Source:** https://wiki.debian.org/PackagingWithDarcsAndTailor

---

## Packaging Debian Packages using Darcs and Tailor

This page is intended to collect howto and tips related to Debian packaging using darcs and tailor.

For more general information, please see [PackagingWithDarcs](/PackagingWithDarcs).

### What

[darcs](http://www.darcs.net/) is a revision control system that does not need a central repository or network connectivity. Also branching is pretty cheap in time and space requirements.

[tailor](http://progetti.arstecnica.it/tailor) is a utility to convert between revision control systems. We use it to convert the upstream format to darcs format.

## Issues

darcs can have problems with ["doppleganger patches"](http://darcs.net/DarcsWiki/FrequentlyAskedQuestions#head-76fb029ff6e9c20468eacf3ff00d791e2cf03ecb), and if you read the [ConflictMisery](http://darcs.net/DarcsWiki/ConflictMisery) page in their wiki it describes a typical debian way of working: have 2 repositories (upstream and debian) where a change in the debian related is redone in the upstream respository without using darcs. A typical example is that you find a problem, fix it and report it to upstream who include the fix in their next release. This can cause darcs to spin out of control and you'll be unable to merge the new upstream with the debian repository.

This makes darcs unusable for larger packages.

([?](/JohnGoerzen)JohnGoerzen adds: In practice, this is extremely rare. I use darcs for some fairly large packages (Bacula, for instance), and despite having patches flowing back and forth, have only seen this problem once across the entire history of all the packages I maintain in it. See my Debian darcs repos at <http://darcs.complete.org> for more.)

### How

We will have 2 repositories for package foo: foo and foo-upstream. The work will be done in another repository in order to minimize rollbacks and accidental repository corruption. So you have a ~/packaging/repository/foo, ~/packaging/repository/foo-upstream, ~/packaging/work/foo and ~/packaging/work/foo-upstream structure for example.

You do your merging of upstream, preparing of packages etc in ~/packaging/work and only do darcs push if you want to record the changes. For team cooperation I would then rsync the ~/packaging/repository tree to some webserver.

#### Starting the repository

This is important: if you are using tailor \*do not\* create an initial repository.

#### Converting upstream with tailor

The best way is to use a local copy of the upstream repository. In our example we're going to use the clisp package. Sourceforge makes the CVS repositories available via rsync, so we create a copy with:

mkdir ~/tmp/clisp-cvs ; rsync://clisp.cvs.sourceforge.net/cvsroot/clisp/ ~/tmp/clisp-cvs/

Then we create a simple tailor configfile:

{{{cat <<EOF > tailorconfigfile [DEFAULT] verbose = True

[clisp] target = darcs:clisp start-revision = clisp\_2\_33\_84-2005-07-07 root-directory = ~/packaging/repository/clisp-upstream state-file = tailor.state source = cvs:clisp subdir = .

[darcs:clisp] repository = ~/packaging/repository/clisp-upstream encoding = UTF8

[cvs:clisp] repository = ~/tmp/clisp-cvs module = clisp encoding = ISO-8859-1 EOF }}}

In this case we want to start syncing the upstream cvs not from the beginning of time, but from the 2.33.84 release, because tailor barfs on some older cvs records. Please note also the convertion of character encoding, but is important for clisp because some of the source is in 8 bit latin-1 german. Then we start the import with HCRTS="-M640M -K64M" LC\_ALL=C LANG=C tailor --configfile=tailor-configfile clisp and go to sleep.

In the morning you'll have a nice darcs repository of the clisp upstream archive.

Open issues:

* we should be able to only update until a certain revision, but this does not work
* sometimes tailor produces broken darcs repositories, you need to check the repository

#### Making the first debian package

After you have a upstream repository create a new debian one with darcs get --repo-name=clisp clisp-upstream.

#### Keeping up to date

#### Team operations

### Tip and tricks

The most important tip for using darcs is that sometimes the build-in conflict management fails. So

* if a darcs command fails, retry it with more memory using GHCRTS="-M640M -K64M" darcs ...
* if the conflict is too complex, use an external merge command: GHCRTS="-M640M -K64M" darcs apply --interactive --verbose --external-merge 'kdiff3 --output %o %a %1 %2' foo.dpatch
* do a darcs check to check your repository now and again
* likewise do darcs optimize now and again.