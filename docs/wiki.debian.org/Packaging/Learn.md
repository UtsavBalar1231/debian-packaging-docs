# Packaging/Learn - Debian Wiki

**Source:** https://wiki.debian.org/Packaging/Learn

---

[Translations](/DebianWiki/EditorGuide#translation): [English](/Packaging/Learn) - [Español](/es/Packaging/Learn) - [Português (Brasil)](/pt_BR/Packaging/Learn) - [(+)](/DebianWiki/EditorGuide#translation)

---

Note: Taken from [Software Freedom Camp](https://wiki.fsci.in/index.php/Learn_Debian_Packaging).

Contents

1. [Level 0: Basics of release process and setup a development environment](#Level_0:_Basics_of_release_process_and_setup_a_development_environment)
2. [Level 1: Learn basics of Packaging](#Level_1:_Learn_basics_of_Packaging)
3. [Level 2: Update existing packages to new upstream minor or patch versions](#Level_2:_Update_existing_packages_to_new_upstream_minor_or_patch_versions)
4. [Level 3: Packaging more complicated modules](#Level_3:_Packaging_more_complicated_modules)
5. [Level 4: Pick an unpackaged but useful module and upload to archive](#Level_4:_Pick_an_unpackaged_but_useful_module_and_upload_to_archive)

# Level 0: Basics of release process and setup a development environment

1. [How to Install a .Deb File via Command-Line](https://www.wikihow.com/Install-DEB-Files)
2. [Lifecycle of a Release](https://debian-handbook.info/browse/stable/sect.release-lifecycle.html) (the journey of a package from first upload to reaching a user, included in a supported release)
3. [Manage repositories/sources.list](/SourcesList) (managing the list of websites that serve Deb packages)
4. [How to install packages from stable-backports](https://backports.debian.org/Instructions/) (there is some extra steps required to get new upstream versions of popular software on a stable system)
5. apt-file find command to find which package includes a file (usually to find a missing command or header file) - [apt-file tutorial](https://www.computerhope.com/unix/apt-file.htm)
6. Setup Debian Unstable/Sid using [Incus](/Packaging/Pre-Requisites/Incus) (hopefully you are now familiar with Lifecycle of a release from previous steps and know new packages or new upstream versions of existing packages are first uploaded to Sid or Unstable, so we do development on this branch of debian)
7. [Building existing packages from source](/BuildingTutorialSimplified). Learning to build from source is useful when you want to backport a package (for example you want to rebuild a new version of a package from unstable or testing on your stable system). This is also useful if you want to modify an existing package, for example to fix a bug or cherry pick a commit from upstream.

By this time you should be familiar with

1. debuild
2. apt build-dep
3. apt source -b

commands to rebuild an existing debian package from source.

Advanced/Extra/Reference: [Different options for setting up a Debian Sid environment](/Packaging/Pre-Requisites)

# Level 1: Learn basics of Packaging

Understand the basic concepts using debmake/dh\_make (getting source tarballs, creating source package, building the binary package, making it lintian clean)

A high level overview of packaging involves,

1. Downloading source code of the software to be packaged (commonly release tarballs)
2. Creating a debian directory template (using tools like debmake, npm2deb or gem2deb depending on the programming language used)
3. Building the .deb file, combining the above two (using dpkg-buildpackage)

Hands on steps,

1. [Setup your name and email address to be used for packaging](/Packaging/Variables)
2. Then follow [this tutorial](/SimplePackagingTutorial) to create a package from scratch

Extra tutorial with more detailed outputs. [Abraham Raji's simple packaging tutorial](https://wiki.abrahamraji.in/simple-packaging-tutorial.html)

Once you understand the basic concepts, use npm2deb to automate some of those tasks like getting source tarball, a better debian directory template than the ones created by dh\_make/debmake as [npm2deb](https://packages.debian.org/npm2deb "DebianPkg") knows more details specific to node modules. You will still have to fix the remaining issues flagged by lintian.

1. [npm2deb Tutorial](/Javascript/Nodejs/Npm2Deb/Tutorial)

By this time you should know,

1. creating lintian clean packages for simple modules and
2. building it in a clean environment like [sbuild](/Packaging/sbuild).
3. You should also know to [import a dsc file to a git repo](/Javascript/Nodejs/Npm2Deb#Step_6._Build_the_binary_package) (gbp import-dsc --pristine-tar) and
4. push your work to a public git hosting service like <https://salsa.debian.org> (git push -u --all --follow-tags)

# Level 2: Update existing packages to new upstream minor or patch versions

Once you get a clear picture of packaging a simple module, we can move to the next stage of updating existing packages

1. Understand [Semantic Versioning scheme](https://semver.org/) and know when a new upstream release can be a breaking change. Pay special attention to software with 0.x versions - there is no guarantee about compatibility for minor updates as well.
2. Follow this tutorial to [update a package to new upstream version](/Javascript/Nodejs/NewUpstreamUpdate). Make sure you have your [SSH key added to your salsa profile](https://salsa.debian.org/help/user/ssh.md).
3. You can use [gbp pq](https://honk.sigxcpu.org/projects/git-buildpackage/manual-html/gbp.patches.newupstream.html) or [Quilt](/UsingQuilt) in case you need to modify any patch or create a patch. Notes/Tips: If you are already familiar with git branches and rebase, gbp pq would be easier for you. Quilt will take some practice to not miss any steps - if you miss any step, it can be very difficult to recover from a mistake, so better to start over if you see many errors when building the package. A very common mistake is commit upstream changes directly (if you forgot to run quilt pop -a before committing) and dpkg-buildpackage will complain about modified files. Always run debclean and quilt pop -a before committing any changes and make sure you are only committing changes inside debian directory (all upstream changes will be saved as patch files in debian/patches when you run quilt pop -a).
4. Start [signing your git commits](https://salsa.debian.org/help/user/project/repository/signed_commits/gpg.html) and upload your gpg public key to [OpenPGP.org key server](https://keys.openpgp.org/) (this is default key server in gpg and thunderbird so people can easily search your keys using email address. You also need to verify your email address after you upload your public key for the discovery with email to work.)

By this time you should know,

1. How to send RFS mails
2. Using Quilt to modify upstream source if required
3. Sign your git commits

Once you are comfortable with simple updates (say you have done 5-6 updates), ask someone to suggest more challenging updates, like a major update.

# Level 3: Packaging more complicated modules

Next step is packaging more complicated modules that will involve things like, modifying some upstream files, removing some files from source tarball, generating some files from source, getting the source tarball from a git commit etc.

1. [Advanced tutorial for more complicated modules](/Javascript/Nodejs/Npm2Deb/AdvancedTutorial)

By this time you should know,

1. Creating patches with quilt
2. Repacking orig.tar and exclude specific files
3. Use pkg-js-tools options to build from source files
4. Build packages with typescript sources

# Level 4: Pick an unpackaged but useful module and upload to archive

1. [List of node dependencies for gitlab](https://git.fosscommunity.in/debian-ruby/TaskTracker/-/issues/175)
2. Join [Packaging teams](https://wiki.debian.org/Teams/#Packaging_teams) that you find interesting. join their mailing list/irc channels and tell them you like to help with packaging and follow their documentation.

By this time you should know,

1. How to file ITP

---

[CategoryPackaging](/CategoryPackaging)