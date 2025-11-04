# PackagingWithGit - Debian Wiki

**Source:** https://wiki.debian.org/PackagingWithGit

---

[Translations](/DebianWiki/EditorGuide#translation): [English](/PackagingWithGit) - [Deutsch](/de/PackagingWithGit) - [Italiano](/it/PackagingWithGit) - [Indonesian](/id/PackagingWithGit) - [Português (Brasil)](/pt_BR/PackagingWithGit)

---

![pbuilder software stack](/PackagingWithGit?action=AttachFile&do=get&target=packaging-process.svg "pbuilder software stack")

This page describes how to create debian packages using the git version control system. For general information about the version control system, see [git](/git). For general information about creating packages, see [Packaging](/Packaging).

The attached image shows the packaging model as described by this page. You may prefer to think about it a different way.

![{i}](/htdocs/debwiki/img/icon-info.png "{i}") The most common git packaging suite is "*git-*buildpackage". The most common command in that suite is *gbp*buildpackage.

Contents

1. [Configure git-buildpackage](#Configure_git-buildpackage)
2. [Import stage](#Import_stage)
   1. [Import from tarballs](#Import_from_tarballs)
   2. [Import from an upstream git repository](#Import_from_an_upstream_git_repository)
   3. [Import from both tarballs and git](#Import_from_both_tarballs_and_git)
   4. [If there is no upstream](#If_there_is_no_upstream)
3. [Patch stage](#Patch_stage)
   1. [Create the debian/ directory](#Create_the_debian.2F_directory)
   2. [Manage debian/changelog](#Manage_debian.2Fchangelog)
      1. [Common policy questions](#Common_policy_questions)
      2. [Helpful tools](#Helpful_tools)
   3. [Manage debian/copyright](#Manage_debian.2Fcopyright)
   4. [Manage files outside of debian/](#Manage_files_outside_of_debian.2F)
4. [Build stage](#Build_stage)
   1. [Build script](#Build_script)
5. [Publish stage](#Publish_stage)
6. [See also](#See_also)

# Configure git-buildpackage

[git-buildpackage](https://packages.debian.org/git-buildpackage "DebianPkg") is the most popular suite of tools to create Debian packages, but its default configuration should be modified before use. Edit your ~/.gbp.conf to contain at least the following:

```
[DEFAULT]

# Manage a "pristine-tar" branch:
pristine-tar = True
pristine-tar-commit = True

# Use Debian-style branch names:
upstream-branch=upstream/latest
debian-branch=debian/latest

# Build packages with pbuilder:
pbuilder = True
# Or use sbuild:
#builder = sbuild

# Sign tags (optional):
#sign-tags = True
#keyid = <fingerprint>
```

Links in this section use full URLs instead of [?](/DebianMan)DebianMan URLs because [MoinMoin](/MoinMoin)'s [InterWiki](/InterWiki) feature mangles links that contain "~"

pristine-tar and pristine-tar-commit
:   If you need to import a project from an upstream tarball, you might some day be asked to prove that a commit maps to a tarball with a specific checksum. These options keep track of e.g. the order that files appeared in the tarball (see [pristine-tar](https://manpages.debian.org/man/pristine-tar), [--git-pristine-tar](https://manpages.debian.org/man/gbp-buildpackage#git) and [--git-pristine-tar-commit](https://manpages.debian.org/bookworm/git-buildpackage/gbp-buildpackage.1.en.html#git~7)).

upstream-branch and debian-branch
:   [DEP-14](https://dep-team.pages.debian.net/deps/dep14/) recommends using upstream/latest instead of master, and using debian/latest for the Debianised version of upstream/latest. These options tell git-buildpackage to use those names (see [--git-upstream-branch](https://manpages.debian.org/bookworm/git-buildpackage/gbp-buildpackage.1.en.html#git~4) and [--git-debian-branch](https://manpages.debian.org/man/gbp-buildpackage#git~39)).

pbuilder and builder
:   Packages should be built in a clean chroot environment, so your local configuration doesn't contaminate the package. pbuilder=True uses the [pbuilder](/pbuilder) stack, and is a good default choice. Or builder=sbuild uses [sbuild](/sbuild), which provides more flexibility for complex use cases. Your stack will need to be configured before use - see the relevant page for details.

sign-tags and keyid
:   If you want to PGP-sign your git tags, set sign-tags=True and set keyid to the fingerprint for the key marked [SC] in the output of gpg --list-secret-key. This will attach a PGP signature when you do gbp buildpackage --git-tag, proving you were the one who created that tag.

/etc/git-buildpackage/gbp.conf lists many more useful options - you might like to come back and review it once you're comfortable with your workflow. For details, see [the man pages for each command](https://honk.sigxcpu.org/projects/git-buildpackage/manual-html/#:~:text=Command%20Reference).

![{i}](/htdocs/debwiki/img/icon-info.png "{i}") git-buildpackage has [several configuration files](https://manpages.debian.org/man/gbp.conf "DebianMan"). ~/.gbp.conf is for configuration that applies to all your projects. For branch- and project-specific configuration, use your project's debian/gbp.conf or .git/gbp.conf.

# Import stage

The *import* stage involves creating a git repository based on whatever upstream provides, and optionally describing how to get updates from them. That usually means downloading/scanning tarballs on an FTP server, cloning/pulling changes from a [forge](/CategoryForge), or branching/merging commits in your own repo.

## Import from tarballs

The traditional way to get upstream code is to import their latest release tarball:

```
git init --initial-branch="$(gbp config DEFAULT.debian-branch)" some-project.git
cd some-project.git
gbp import-orig https://some-project.example.com/releases/some-project_1.0.tar.gz
```

This will pull the tarball into the upstream and debian branches you specified in your [~/.gbp.conf](/PackagingWithGit#Configure_git-buildpackage), create a new upstream/1.0 tag, and update the pristine-tar branch (if you set that option).

You should also create a debian/watch file to tell git-buildpackage how to pull new tarballs. For details, see [debian/watch](/debian/watch).

git import-orig discards any top-level debian/ directory from your tarball. In the unlikely event this is a problem, see [ManageUpstreamDifferences](/ManageUpstreamDifferences).

Once you have created your debian/watch and [debian/changelog](/PackagingWithGit#Manage_debian.2Fchangelog), you can get new versions of the tarball with gbp import-orig --uscan. Or if you can't create a debian/watch file, you'll have to download a new tarball and call gbp import-orig <tarball> every time.

![{i}](/htdocs/debwiki/img/icon-info.png "{i}") you might like to add a [git alias](https://git-scm.com/book/en/v2/Git-Basics-Git-Aliases) for your import command. For example git config --local alias.get '!gbp import-orig --uscan' makes git get work in this repository

## Import from an upstream git repository

If your upstream doesn't provide tarballs but does put their source code in a git [forge](/CategoryForge) with [release tags](https://git-scm.com/book/en/v2/Git-Basics-Tagging) that have a useful pattern (like vMAJOR.MINOR.PATCH or release-MAJOR.MINOR.PATCH), adapt the following to suit your requirements:

```
# Clone the upstream repository and `cd` into it:
git clone https://forge.example.com/some-project.git
cd project.git

# Use DEP-14 branch names, but don't bother with an upstream branch:
git branch -m debian/latest

# Describe what upstream tags look like (see below for details):
mkdir -p debian
cat >> debian/gbp.conf <<EOF
[DEFAULT]
upstream-tag=v%(version)s

# No tarballs to track (upstream uses git):
pristine-tar = False
pristine-tar-commit = False
EOF
git add debian/gbp.conf
```

By default, git-buildpackage assumes upstream tags are of the form upstream/%(version)s. Set upstream-tag in debian/gbp.conf if your upstream uses a different format. For details, see [the manual](https://honk.sigxcpu.org/projects/git-buildpackage/manual-html/gbp.import.upstream-git.html#gbp.import.upstream.git.notarball).

Disabling pristine-tar and pristine-tar-commit avoids creating a redundant extra branch, and makes the project configuration clearer for anyone reviewing your work.

If your upstream doesn't create useful release tags, consider asking them to start. If they're not willing to create tags, but do provide release tarballs, you'll have to [import from tarballs](/PackagingWithGit#Import_from_tarballs) - Git and Debian both have excellent alternatives to git pull, but can't replicate the information in a release tarball.

If your upstream contains a top-level /debian directory, you will need to delete it from the upstream branch. For details, see [ManageUpstreamDifferences](/ManageUpstreamDifferences).

To get new versions from an upstream git repository, just do a normal git pull from upstream/latest.

## Import from both tarballs and git

If your upstream provides tarballs *and* a git repository, you can import both and compare them:

```
# Import the tarball first:
git init --initial-branch="$(gbp config DEFAULT.debian-branch)" some-project.git
cd some-project.git
gbp import-orig https://some-project.example.com/releases/some-project_1.0.tar.gz

# Then import the git repo:
git remote add origin https://forge.example.com/some-project.git
git fetch

# Compare the tarball and the repo (remember to use the right tags):
git diff upstream/1.0 v1.0
```

If git diff shows one source or other is definitely correct, delete some-project.git and start over with the appropriate set of instructions. Or if you need to track both, configure [debian/watch](/debian/watch) and [debian/changelog](/PackagingWithGit#Manage_debian.2Fchangelog), then get new versions with something like gbp import-orig --uscan && git fetch.

## If there is no upstream

Some projects don't have an upstream. For example, Debian-specific projects often have a single repository with upstream code in one branch and Debian packaging in another.

If possible, set your main development branch name to upstream/latest:

```
# Set branch name when creating the repo:
git init --initial-branch="$(gbp config DEFAULT.upstream-branch)" project.git
# Or rename the branch when you start to Debianise:
git branch -m master "$(gbp config DEFAULT.upstream-branch)"
```

The rest of this page assumes your project is ready to package, so you may want to pause here and come back once you finish your first version.

Once you've finished your first version, check out a new branch for Debian-specific changes:

```
git checkout -b "$(gbp config DEFAULT.debian-branch)" \
        --track "$(gbp config DEFAULT.upstream-branch)"
```

Projects without an upstream repository can usually choose their own tag pattern and ignore upstream tarballs. Consider doing:

```
mkdir -p debian
cat >> debian/gbp.conf <<EOF
[DEFAULT]
upstream-tag=v%(version)s

# No tarballs to track (no upstream repo):
pristine-tar = False
pristine-tar-commit = False
EOF
git add debian/gbp.conf
```

Because debian/latest tracks upstream/latest, you can get upstream changes with git pull just like you would with a remote repository.

![{i}](/htdocs/debwiki/img/icon-info.png "{i}") Debian-specific packages that will *never* have an upstream repository can use the native patch system instead of the default quilt model - see [Projects/DebSrc3.0](/Projects/DebSrc3.0).

# Patch stage

The *patch* stage involves creating files in your debian/ directory, and optionally changing other directories as required by Debian. For example, Debian requires programs to have a man page, which you should create if it's missing upstream.

![{i}](/htdocs/debwiki/img/icon-info.png "{i}") This section is a language-neutral guide to patching a project. Prefer [language-specific guides](/Packaging#Language-specific_guides) where available.

## Create the debian/ directory

Debian metadata is stored in debian/, which is usually initialised with [debmake](https://packages.debian.org/debmake "DebianPkg") or [dh-make](https://packages.debian.org/dh-make "DebianPkg"). Unfortunately, they only work with tarballs:

```
# Specify your project name and version:
PROJECT_ID=<project> # e.g. "myproject"
PROJECT_VERSION=<version> # e.g. "1.0"

# Remember to run this in your debian branch:
git checkout debian/latest

# Create a release tarball and associated directory:
mkdir -p tmp debian
git archive HEAD --prefix="${PROJECT_ID}-${PROJECT_VERSION}"/ \
    -o tmp/"${PROJECT_ID}_${PROJECT_VERSION}".orig.tar.gz
cd tmp
tar zxf "${PROJECT_ID}_${PROJECT_VERSION}".orig.tar.gz

# Run debmake and move debian/ into your repo:
cd "${PROJECT_ID}-${PROJECT_VERSION}"
debmake # or dh_make
mv -n debian/* ../../debian/
git add ../../debian/

# Tidy up:
cd ../..
rm -rf tmp/"${PROJECT_ID}-${PROJECT_VERSION}"
rm -rf tmp/"${PROJECT_ID}_${PROJECT_VERSION}".orig.tar.gz
rmdir tmp

# Commit auto-generated files before making manual changes (optional):
git commit debian/ -m 'Create initial debian/ directory with debmake'
```

This will create all the files you're likely to need, plus .ex examples for files you might need to create.

Read through all the files in the debian/ directory. [Debian policy](https://www.debian.org/doc/debian-policy/) explains which of these you need and what they should look like. Tests during the build stage (e.g. [lintian](/Lintian)) will tell you anything you missed. debmake and dh-make have different opinions about which defaults are best - adapt your favourite suggestions from each of them.

![{i}](/htdocs/debwiki/img/icon-info.png "{i}") [dh-make](https://packages.debian.org/dh-make "DebianPkg") (with a dash) is the name of a package, dh\_make (with an underscore) is the name of the main program in that package. See [dh\_make(1)](https://manpages.debian.org/man/dh_make "DebianMan") for information about the questions it asks.

## Manage debian/changelog

This file acts both as a human-readable history of the project, and as a machine-readable configuration file for e.g. the version number and target distribution. It will be installed to /usr/share/doc/<your-package>/changelog.Debian.gz.

You need to decide a policy about what to include in your changelog. This section discusses some policy questions to help decide your policy, and some tools to help automate your workflow.

See also [debian/changelog](/debian/changelog).

### Common policy questions

What will your version numbers look like?
:   Most projects use [semantic versioning](https://semver.org/), but some use calendar versioning, or don't have version numbers at all. You'll need a way to extract version numbers from the upstream project, and may need to reformat the numbers for Debian.

Do you want to include upstream changes in the changelog?
:   Some projects go to great lengths to tell users what changed in each version, others just keep their man pages up-to-date and expect users to re-read them now and then. It's good to Debianise upstream changes if they're available; but it's not worth trying to write new information that wasn't recorded upstream.

Do you want to generate your changelog from the git commit history?
:   If your upstream project has a neatly-maintained CHANGES file, you might prefer to write your own script to convert it to Debian format. Otherwise, adapt your workflow so you can generate a changelog from git commits.

If your changelog is based on the commit history, which commits should you include?
:   For example, your upstream might use [topic branches](https://git-scm.com/book/en/v2/Git-Branching-Branching-Workflows#_topic_branch), so only their merge commits belong in the changelog. Or if they don't have any useful information about changes, you might want to exclude upstream commits altogether.

### Helpful tools

Guidance about Debianising version numbers is available at [deb-version](https://manpages.debian.org/man/deb-version "DebianMan"), but also be aware that Debian repositories require every .deb to have a unique filename. Different architectures get different filenames automatically, but different distributions need unique [Debian revision numbers](https://manpages.debian.org/man/deb-version#debian-revision "DebianMan"). For example, you might like to use odd numbers for stable and even numbers for testing, or you could use decorated revision numbers like -ubuntu1 or -forky2.

If you want to write a changelog by hand, use [dch](https://manpages.debian.org/man/dch "DebianMan") to create and edit entries. The changelog format is quite precise and sometimes unintuitive, and dch will help find mistakes. dch --edit uses [sensible-editor](https://manpages.debian.org/man/sensible-editor "DebianMan"), so you can use [select-editor](https://manpages.debian.org/man/select-editor "DebianMan") to configure your preferred editor.

If you want to write a script that generates a changelog, read [the changelog specification](https://manpages.debian.org/man/deb-changelog "DebianMan"). You might like to use dch to actually edit the file, or just to check you've got the format right.

Links in the following paragraph use full URLs instead of [?](/DebianMan)DebianMan URLs because [MoinMoin](/MoinMoin)'s [InterWiki](/InterWiki) feature mangles links that contain "~" If you want to generate debian/changelog from your git changelog, use [gbp-dch](https://manpages.debian.org/man/gbp-dch "DebianMan"). You may be able to exclude upstream commits by calling gbp dch debian/, or you may need to use [--git-log](https://manpages.debian.org/man/gbp-dch#git~2) to specify [git log](https://manpages.debian.org/man/git-log) parameters. If the latter, consider saving them in your debian/gbp.conf:

```
[dch]
# Only include merge commits:
git-log = --merges
# Exclude merge commits:
git-log = --no-merges
# Exclude upstream commits:
git-log = --first-parent
```

gbp dch --new-version adds a new entry to the changelog, unless the current entry has distributions set to UNRELEASED, in which case it merges changes into the current entry. For example, you may want to make several [snapshot commits](https://manpages.debian.org/man/gbp-dch#SNAPSHOT_MODE "DebianMan") during development, then merge them together in the public changelog.

## Manage debian/copyright

This is a machine-readable file that specifies users' legal rights to use the package, and the files in it. debmake should have provided an initial version, but there are many [copyright review tools](/CopyrightReviewTools). You can use whichever you prefer, but [licensecheck](/CopyrightReviewTools#licensecheck) is a good default, and [cme](/CopyrightReviewTools#cme)'s interactive mode may help you learn how the file works.

Getting this right can be very time-consuming, but Debian won't host packages unless they know it's legal to do so. If you have a good relationship with upstream, consider asking them to read [the licensing section of the upstream guide](/UpstreamGuide#Choose_a_standard_open_source_license).

## Manage files outside of debian/

Changes in your debian branch but outside your debian/ directory need special handling. For example, you might need to patch the build system to install files in the right locations, and Debian will refuse to host even an upstream tarball that violates the [Debian Free Software Guidelines](/DebianFreeSoftwareGuidelines). For details, see [ManageUpstreamDifferences](/ManageUpstreamDifferences).

# Build stage

The *build* stage involves generating and testing your package files, including one or more .deb files.

To do a test-build of your package, make sure your debian/changelog has the correct version number, then do:

```
gbp buildpackage --git-dist=<dist> --git-arch=<arch>
# Or if you configured pbuilder=True and want to use pbuilder instead of cowbuilder:
BUILDER=pbuilder gbp buildpackage --git-dist=<dist> --git-arch=<arch>
```

If your build succeeds, it should produce a collection of ../<project>\_<version>\* files.

[Package checkers](/PackagingTools#Package-checking_tools) look for issues that don't cause build failures. It's particularly important to run [lintian](/Lintian), [piuparts](/piuparts) and [autopkgtest](/autopkgtest), as Debian will usually reject packages that fail these tests.

lintian looks for common issues and violations of Debian policy. For example, boilerplate text that hasn't been modified since you ran debmake. You can run it with most tests enabled by doing lintian --info --display-info --pedantic /path/to/your/package.changes, or choose your preferred options from the [lintian man page](https://manpages.debian.org/man/lintian "DebianMan").

piuparts creates a minimal chroot, then tries to install and uninstall your package in it. It needs pbuilder-style .tgz files - it can't use cowbuilder's .cow directories. It's often run as sudo piuparts --log-level info --basetgz /path/to/your/base-environment.tgz /path/to/your/package.deb, and its options are explained in the [piuparts man page](https://manpages.debian.org/man/piuparts "DebianMan").

autopkgtest runs any integration tests you've added to debian/tests. This usually isn't necessary for simple packages - learn more at [autopkgtest](/autopkgtest).

![{i}](/htdocs/debwiki/img/icon-info.png "{i}") if you did not configure pbuilder=True, lintian will run without arguments during the build. You may want to run it again with your preferred arguments anyway.

## Build script

You may want to write a script to automate your build process. Here's an example that shows off several options:

```
#!/bin/sh

# Exit if any programs fail:
set -e

# Can be /var/cache/pbuilder/result for some workflows:
RESULT_DIRECTORY=..

# Get some information from the changelog
SOURCE="$(dpkg-parsechangelog --show-field=Source)"
VERSION="$(dpkg-parsechangelog --show-field=Version)"

# Read "--git-dist=foo" and "--git-arch=bar" from the command-line:
DIST=sid
ARCH="$(dpkg --print-architecture)"
for ARG
do
    case "$ARG" in
        "--git-dist="*)
            DIST="${ARG#--git-dist=}"
            ;;
        "--git-arch="*)
            ARCH="${ARG#--git-arch=}"
            ;;
        "--git-export-dir="*)
            RESULT_DIRECTORY="${ARG#--git-export-dir=}"
            mkdir -p "$RESULT_DIRECTORY"
            ;;
        -h|--h|--he|--hel|--help)
            cat <<EOF
Usage: $0 [--git-dist=<distribution>] [--git-arch=<architecture>]"

Build a Debian package.
See https://wiki.debian.org/PackagingWithGit#Build_script
EOF
            exit 1
            ;;
    esac
done

if grep -q '^Architecture: all' debian/control
then PKG_ARCH=all
else PKG_ARCH="$ARCH"
fi

CHANGES_FILE="$RESULT_DIRECTORY/${SOURCE}_${VERSION}_${ARCH}.changes"
DEB_FILE="$RESULT_DIRECTORY/${SOURCE}_${VERSION}_${PKG_ARCH}.deb"
LOG_FILE="$RESULT_DIRECTORY/${SOURCE}_${VERSION}_${ARCH}.log"

# Calculate the pbuilder base tarball/path:
BASE=/var/cache/pbuilder/base
if [ -n "$DIST" -a "$DIST" != sid ]
then BASE="$BASE-$DIST"
fi
if [ -n "$ARCH" -a "$ARCH" != "$(dpkg --print-architecture)" ]
then BASE="$BASE-$ARCH"
fi

# Run pbuilder with arguments from the command-line:
echo -n "[$(date)] Running gbp buildpackage" >&2
set -o pipefail
BUILDER=pbuilder gbp buildpackage "$@" \
    | tee "$LOG_FILE" \
    | while read LINE ; do echo -n . >&2 ; done
set +o pipefail
echo " OK" >&2
echo >&2

echo "[$(date)] Running piuparts..." >&2
sudo piuparts --log-level info --basetgz "$BASE.tgz" "$DEB_FILE"
echo "[$(date)] piuparts: OK" >&2
echo >&2

echo "[$(date)] Running autopkgtest..." >&2
set +e
sudo autopkgtest --no-built-binaries --apt-upgrade "$CHANGES_FILE" \
    -- unshare --release "$DIST" --arch "$ARCH"
RESULT="$?"
set -e
case "$RESULT" in
    0) echo "autopkgtest: OK" >&2 ;;
    8) echo "autopkgtest: no tests in this package, or all non-superficial tests were skipped" >&2 ;;
    *) exit "$RESULT" >&2
esac
echo >&2

echo "[$(date)] Running lintian..." >&2
lintian --info --display-info --pedantic "$CHANGES_FILE"
echo "[$(date)] lintian: OK" >&2
echo >&2

echo "[$(date)] Success!" >&2
```

![{i}](/htdocs/debwiki/img/icon-info.png "{i}") if you would rather call gbp buildpackage directly, you can call your script from the buildpackage.postbuild option in a gbp.conf file.

# Publish stage

The *publish* stage involves either putting your built files in a repository you control, or requesting someone else (e.g. the Debian project) put it in a repository they control.

If you want to publish your package to Debian itself, [register for a Salsa account](https://salsa.debian.org/users/sign_up) and check the [user registration section of the FAQ](https://wiki.debian.org/Salsa/FAQ#User_registration). While you're waiting, file an [Intent To Package](/ITP) ("ITP") bug and add an entry to your debian/changelog that ends with Closes: #<itp-bug-number>.

Change UNRELEASED in debian/changelog to the distribution(s) your package should be in. The Debian archive [only allows one distribution](https://www.debian.org/doc/debian-policy/ch-controlfields.html#s-f-distribution), so you may need to publish multiple times, updating the version number each time. Other repositories may accept a single version with a space-separated list of distributions.

Commit your change, then build and tag your release:

```
gbp buildpackage --git-tag
```

This will create a tag based on the debian-tag configuration option. By default, it resembles debian/X.Y-Z.

If you want to publish your package to Debian itself, push to [salsa.debian.org](/Salsa) and follow [the sponsoring process](https://mentors.debian.net/sponsors).

Finally, as a precaution, add a new temporary [snapshot commit](https://manpages.debian.org/man/gbp-dch#SNAPSHOT_MODE "DebianMan"):

```
gbp dch --snapshot
git commit -m 'WIP: next version' debian/changelog
```

If all goes well, you can undo this commit before your next merge, by doing git commit --reset HEAD^. But if you accidentally push changes to Salsa, the tests will fail harmlessly instead of releasing unwanted changes to a public repository.

# See also

* the git-buildpackage manual is available [online](https://gbp.sigxcpu.org/manual) or at /usr/share/doc/git-buildpackage/manual-html/
* other guides to packaging with git 
  + [from the Guide for Debian Maintainers](https://www.debian.org/doc/manuals/debmake-doc/ch11.en.html)
  + [from Russ Allbery](https://www.eyrie.org/~eagle/notes/debian/git.html)
  + [from Philipp Huebner](http://people.debian.org/~debalance/packaging-with-git.html)
* discussions about including the upstream git in the package's git 
  + [by Russ Allbery](http://www.eyrie.org/~eagle/journal/2013-04/001.html)
  + [by Joey Hess](http://joeyh.name/blog/entry/upstream_git_repositories/)
* [switching from svn-buildpackage](/PackagingWithGit/Svn-buildpackageConversion)
* general resources about git 
  + [homepage](http://git-scm.com/)
  + [wiki](https://git.wiki.kernel.org/index.php/Main_Page)
  + [manual](http://www.kernel.org/pub/software/scm/git/docs/)

---

* [CategoryDeveloper](/CategoryDeveloper) [CategoryPackaging](/CategoryPackaging) [CategoryGit](/CategoryGit)