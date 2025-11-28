# Packaging - Debian Wiki

**Source:** https://wiki.debian.org/Packaging

---

[Translation(s)](/DebianWiki/EditorGuide#translation): [English](/Packaging) - [Español](/es/Packaging) - [Português (Brasil)](/pt_BR/Packaging) - [Italiano](/it/Packaging) - [Svenska](/sv/Packaging) - [Русский](/ru/Packaging)

---

![Portal/IDB/icon-wiki-portal.png](/Portal/IDB?action=AttachFile&do=get&target=icon-wiki-portal.png "Portal/IDB/icon-wiki-portal.png")

This is the **packaging portal**, for people who want to create new packages. For commonly-installed packages, see [Software](/Software). Or to install and remove packages, see [package management](/PackageManagement).

Contents

1. [General guides](#General_guides)
   1. [Find your feet](#Find_your_feet)
   2. [Further reading](#Further_reading)
2. [More granular guides](#More_granular_guides)
   1. [Language-specific guides](#Language-specific_guides)
   2. [Topic-specific guides](#Topic-specific_guides)
   3. [Tool guides](#Tool_guides)
   4. [Job guides](#Job_guides)
   5. [File guides](#File_guides)
   6. [Working with other developers](#Working_with_other_developers)
3. [Training Sessions](#Training_Sessions)
4. [External links](#External_links)
   1. [See also](#See_also)
5. [Wiki pages](#Wiki_pages)

# General guides

There are no shortcuts to learning good packaging practices - you can't just throw a trivial packager like [equivs](https://packages.debian.org/equivs "DebianPkg") at the problem and hope for the best.

The links in this section will help you gain a deep understanding of the problems you need to solve if you want to create or maintain a package.

## Find your feet

The first step is to find a basic approach that works for you. [The Debian mentors FAQ](/DebianMentorsFaq#How_do_I_make_my_first_package.3F) advises you to re-consider, clarifies why and how to start, and provides a short overview of the process.

New tools are invented every few years, and the best way to use them depends on the specific projects you want to package and the way you like to work. Here are some guides you can get inspiration from:

* [create a .deb for private use](/MakeAPrivatePackage) shows how to make a basic package in 5 minutes
* a tutorial series from 2010-2011 helps you learn the theory: 
  + [introduction to Debian packaging](/Packaging/Intro) explains packaging from scratch
  + [the building tutorial](/BuildingTutorial) explains applying changes to an existing package
  + [advanced building tips](/AdvancedBuildingTips) covers some details that didn't fit in the other tutorials
* a tutorial series from 2025 by Otto Kekäläinen shows one good packaging workflow: 
  + [Creating Debian packages from upstream Git](https://optimizedbyotto.com/post/debian-packaging-from-git/)
  + [Debian source packages in git explained](https://optimizedbyotto.com/post/debian-source-package-git/)
* [packaging with git](/PackagingWithGit) discusses common git-based workflows
* [the debconf developers guide](https://manpages.debian.org/man/debconf-devel "DebianMan") explains how to ask the user questions during installation
* [Guide for Debian Maintainers](https://www.debian.org/doc/manuals/debmake-doc/index.en.html) provides a reference for common tools discussed in tutorials

  + replaces the outdated [Debian New Maintainers' Guide](https://www.debian.org/doc/manuals/maint-guide/index.en.html)

![{i}](/htdocs/debwiki/img/icon-info.png "{i}") Debian packaging works by example as much as by theory. Find well-maintained packages, and see how they do it!

## Further reading

Once you've found a workflow you can live with, you can optimise it for your personal requirements. These pages might give you some ideas:

* [learn Debian Packaging in steps](/Packaging/Learn) takes you from new to advanced packaging levels (by the JavaScript team)
* [Debian Packaging Tutorial](https://www.debian.org/doc/devel-manuals#packaging-tutorial) tells you what you really need to know about Debian packaging
* [The Developers Reference](https://www.debian.org/doc/manuals/developers-reference/) gives an overview of recommended procedures and available resources
* [How will my package get into Debian?](https://mentors.debian.net/intro-maintainers/) walks you through the process of getting packages accepted by Debian
* [The packaging FAQ](/PackagingFAQ) answers some common questions
* [The upstream guide](/UpstreamGuide) advises upstream maintainers how to support packaging
* [Complex Web Apps](/Packaging/ComplexWebApps) discusses creating Debian packages for complex web applications
* [setting up a Debian unstable system](/Packaging/Pre-Requisites) provides some options for creating a clean package-building environment

These advanced pages explain how packaging works under the hood:

* [the Debian Policy](https://www.debian.org/doc/debian-policy/) - technical requirements that each package must satisfy
* [Projects/DebSrc3.0](/Projects/DebSrc3.0) - details about the "3.0 (quilt)" and "3.0 (native)" source package formats
* [Courses2005/BuildingWithoutHelper](/Courses2005/BuildingWithoutHelper) - how to make a Debian package without using a helper
* [/HackingDependencies](/Packaging/HackingDependencies) - hacking dependencies
* [Diagrams](/Diagrams) - packaging-related diagrams and sketches
* [Debian Trends](https://trends.debian.net/) - how packaging practices have evolved over time

Finally, if you'd like to see the development process for the packaging system itself:

* [PackageConfigUpgrade](/PackageConfigUpgrade) - proposed way to smoothly handle configuration upgrades during package upgrades
* [DataPackages](/DataPackages) - brainstorming about huge data packages

# More granular guides

Once you're comfortable creating packages generally, you'll need to learn the tools and techniques for your particular problem.

## Language-specific guides

Each of Debian's language-specific teams have their own policies and tools:

* [Emacs Lisp](/Teams/DebianEmacsenTeam) team page
* [Golang](https://go-team.pages.debian.net/packaging.html) packaging documentation
* [Haskell](/Teams/DebianHaskellGroup) team page
* [Java](/Java/Packaging) packaging guide

  + see also [Guidelines for Packages Maintained on salsa.debian.org/java-team](/Java/JavaGit)
* [JavaScript](/Javascript/Policy) policy

  + [Node.js](/Javascript/Nodejs) packaging guide
* [Lua](https://salsa.debian.org/lua-team) group page
* [Mono](/Teams/DebianMonoGroup/NewPackage) packaging guide
* [OCaml](/Teams/OCamlTaskForce) maintainers page
* [Perl](https://perl-team.pages.debian.net/git.html) packaging guide
* [Python](/Python/LibraryStyleGuide) library style guide
* [Ruby](/Teams/Ruby/Packaging) packaging guide
* [Rust](/Teams/RustPackaging) team page

![{i}](/htdocs/debwiki/img/icon-info.png "{i}") see also [a comparison of tools that create Debian packages](/AutomaticPackagingTools)

## Topic-specific guides

If your package addresses a specific topic, you may need to read information from people who have been there before:

* [Android tools](/AndroidTools) information
* Debian team guides 
  + [Debian GNOME Team](/Gnome/Git) guide
  + [KDE Team](/PkgQtKde) home page
  + [Debian MATE Packaging Team](/PkgMate/GitPackaging) guide
  + [Debian Med team](https://med-team.pages.debian.net/policy/) policy
  + [Debian Multimedia](/DebianMultimedia/DevelopPackaging) packaging guide
  + [Vim team](https://vim-team.pages.debian.net/vim/index.html) packaging guide
  + [Debian Science](https://science-team.pages.debian.net/policy/) policy manual
  + other [packaging teams](/Teams#Packaging_teams) may have guides
* [fonts](/Fonts/PackagingPolicy) packaging policy
* [repackaging RPM source packages as .deb packages](/Repackage_srcrpm)

  + see also [using RPM in Debian](/RPM)

## Tool guides

You will probably need to use some of these:

* [pbuilder](/pbuilder) or [sbuild](/sbuild) to create environments to build packages in
* [lintian](/Lintian), [piuparts](/piuparts), [autopkgtest](/autopkgtest) and [blhc](/blhc) to debug your packages

You might also want to use some of these:

* [Packaging/ruby-team-meta-build](/Packaging/ruby-team-meta-build) - build scripts used by ruby team, helps testing reverse dependencies easily
* [Quilt](/UsingQuilt) for managing patches without a version control system
* [devscripts](https://packages.debian.org/devscripts "DebianPkg") to make your life easier
* [dh-make](https://packages.debian.org/dh-make "DebianPkg") to convert source archives into Debian package source
* [checkinstall](/CheckInstall) lets you build binary .deb packages from installation scripts (make install...)

## Job guides

If you're trying to achieve a particular outcome:

* [rename a package](/RenamingPackages)
* [transition users from one package to another](/PackageTransition)
* [let files from one package be temporarily replaced by files from another](/DpkgDiversions)
* [make a package for your config files](/ConfigPackages)
* [make a private backport from unstable to stable](/SimpleBackportCreation)
* [make a backport suitable for backports.debian.org](/BuildingFormalBackports)
* [create a package from an Ubuntu PPA](/CreatePackageFromPPA)
* [upload source packages without binary packages](/SourceOnlyUpload)

  + see also [Debian archive](/Services/Debian%20Archive)
* [avoid keeping convenience copies of files from one project in another](/Packaging/EmbeddedCopies)
* [language-specific solutions for versioned -dev packages](/LanguageVersionedDevPackages)
* [write a good package description](/WritingDebianPackageDescriptions)
* [manage differences between your package and upstream](/ManageUpstreamDifferences)

## File guides

If you need help with a particular file in your package's debian/ directory:

* [debian/changelog](/debian/changelog) - changes between versions of your package
* [debian/copyright](/debian/copyright) - copyright information about the upstream package
* [debian/patches](/debian/patches) - debian-specific patches to the upstream code
* [debian/upstream](/debian/upstream) - files describing the upstream project

  + [debian/upstream/edam](/debian/upstream/edam) - formal categorisation from the [EDAM ontology](http://www.edamontology.org)
  + [debian/upstream/metadata](/UpstreamMetadata) - miscellaneous information
* [debian/watch](/debian/watch) - check for upstream updates

To find real-world examples of any debian/ file, go to [codesearch.debian.net](https://codesearch.debian.net/) and search for e.g. [Reference path:debian/control](https://codesearch.debian.net/search?q=Reference+path%3Adebian%2Fcontrol&literal=1).

## Working with other developers

If you want to get involved with the Debian community:

* [Mentors](/Mentors) - sponsors/mentors for packages in specific areas of Debian

  + [introduction for reviewers](https://mentors.debian.net/intro-reviewers/)
* [SponsorChecklist](/SponsorChecklist) - Sponsor Checklist
* [Software that can't be packaged](/Software%20that%20can%27t%20be%20packaged) - projects that have already been found ineligible for inclusion in Debian
* guidelines for processing the [NEW queue](http://ftp-master.debian.org/new.html)

  + [LucaFalavigna's checklist](/LucaFalavigna/NEWChecklist)
  + [Reject FAQ](https://ftp-master.debian.org/REJECT-FAQ.html)
* [DEX](/DEX) - improving Debian and its derivatives through cross-community teamwork
* [how developers can help packagers](/SoftwarePackaging)
* [Work-Needing and Prospective Packages](/WNPP) - packages that have been requested for packaging, or need a new maintainer
* [Salsa](/Salsa) - GitLab-based Debian development server

# Training Sessions

[DebianWomen](/DebianWomen) organise [training sessions](/DebianWomen/Projects/Events/TrainingSessions).

# External links

* [What's in a debian/ directory](https://feeding.cloud.geek.nz/posts/whats-in-a-debian-directory/)
* [Managing Debian package files with cme](https://github.com/dod38fr/config-model/wiki/Managing-Debian-packages-with-cme)
* [Ubuntu Packaging Guide](https://packaging.ubuntu.com/)
* [Debian Binary Package Building HOWTO](https://www.ibiblio.org/pub/Linux/docs/HOWTO/other-formats/html_single/Debian-Binary-Package-Building-HOWTO.html) (2005)
* [How to build and deploy a Debian Package with GitLab CI](https://about.gitlab.com/blog/2016/10/12/automated-debian-package-build-with-gitlab-ci/)
* [fpm](https://github.com/jordansissel/fpm) can build .deb packages from various other package formats ([rubygems](https://github.com/jordansissel/fpm/wiki/ConvertingGems), [pip](https://github.com/jordansissel/fpm/wiki/ConvertingPython), pear, tar, npm, pacman...)
* [Packaging - Ubuntu Wiki](https://wiki.ubuntu.com/Packaging)
* [Debian build tools - Russ's Debian Notes](https://www.eyrie.org/~eagle/notes/debian/build-tools.html)
* [Packaging Scripts for Debian - Russ's Debian Notes](https://www.eyrie.org/~eagle/notes/debian/scripts.html)

## See also

* [Debian adminstration - Rolling your own Debian packages (part 1)](https://www.debian-administration.org/articles/336)
* [Autobuilding non-free packages](https://lists.debian.org/msgid-search/20061129152824.GT2560@mails.so.argh.org)
* [A Debian packaging howto (2010)](https://www.strangeparty.com/2010/06/17/a-debian-packaging-howto/)
* [Avoid a newbie packager mistake: don’t build your Debian packages with dpkg -b](https://raphaelhertzog.com/2010/12/17/do-not-build-a-debian-package-with-dpkg-b/)
* [Debuginfod](/Debuginfod) eliminates the need for users to install debuginfo packages in order to debug programs using GDB, systemtap or other tools
* [Browse through the source code of the Debian operating system](https://sources.debian.org)

# Wiki pages

All pages related to packaging in Debian:

1. [AdvancedBuildingTips](/AdvancedBuildingTips?highlight=%28%5CbCategoryPackaging%5Cb%29)
2. [Alioth](/Alioth?highlight=%28%5CbCategoryPackaging%5Cb%29)
3. [AndroidTools](/AndroidTools?highlight=%28%5CbCategoryPackaging%5Cb%29)
4. [AutomaticPackagingTools](/AutomaticPackagingTools?highlight=%28%5CbCategoryPackaging%5Cb%29)
5. [BuildingFormalBackports](/BuildingFormalBackports?highlight=%28%5CbCategoryPackaging%5Cb%29)
6. [BuildingWithoutFakeroot](/BuildingWithoutFakeroot?highlight=%28%5CbCategoryPackaging%5Cb%29)
7. [BzrBuildpackage/DesignIdeas](/BzrBuildpackage/DesignIdeas?highlight=%28%5CbCategoryPackaging%5Cb%29)
8. [CPEtagPackagesDep](/CPEtagPackagesDep?highlight=%28%5CbCategoryPackaging%5Cb%29)
9. [CheckInstall](/CheckInstall?highlight=%28%5CbCategoryPackaging%5Cb%29)
10. [ConfigPackages](/ConfigPackages?highlight=%28%5CbCategoryPackaging%5Cb%29)
11. [CopyrightReview](/CopyrightReview?highlight=%28%5CbCategoryPackaging%5Cb%29)
12. [CopyrightReviewTools](/CopyrightReviewTools?highlight=%28%5CbCategoryPackaging%5Cb%29)
13. [Courses/MaintainingPackages](/Courses/MaintainingPackages?highlight=%28%5CbCategoryPackaging%5Cb%29)
14. [Courses2005/BuildingWithoutHelper](/Courses2005/BuildingWithoutHelper?highlight=%28%5CbCategoryPackaging%5Cb%29)
15. [CreatePackageFromPPA](/CreatePackageFromPPA?highlight=%28%5CbCategoryPackaging%5Cb%29)
16. [Creating signed GitHub releases](/Creating%20signed%20GitHub%20releases?highlight=%28%5CbCategoryPackaging%5Cb%29)
17. [CrossBuildPackagingGuidelines](/CrossBuildPackagingGuidelines?highlight=%28%5CbCategoryPackaging%5Cb%29)
18. [DDPO](/DDPO?highlight=%28%5CbCategoryPackaging%5Cb%29)
19. [DEX](/DEX?highlight=%28%5CbCategoryPackaging%5Cb%29)
20. [DataPackages](/DataPackages?highlight=%28%5CbCategoryPackaging%5Cb%29)
21. [Debhelper](/Debhelper?highlight=%28%5CbCategoryPackaging%5Cb%29)
22. [DebianAstro/AstropyPackagingTutorial/Packaging](/DebianAstro/AstropyPackagingTutorial/Packaging?highlight=%28%5CbCategoryPackaging%5Cb%29)
23. [DebianAstro/AstropyPackagingTutorial/Preparation](/DebianAstro/AstropyPackagingTutorial/Preparation?highlight=%28%5CbCategoryPackaging%5Cb%29)
24. [DebianChangelog](/DebianChangelog?highlight=%28%5CbCategoryPackaging%5Cb%29)
25. [DebianDevelopment](/DebianDevelopment?highlight=%28%5CbCategoryPackaging%5Cb%29)
26. [DebianGNUstep/TODO](/DebianGNUstep/TODO?highlight=%28%5CbCategoryPackaging%5Cb%29)
27. [DebianMentorsFaq](/DebianMentorsFaq?highlight=%28%5CbCategoryPackaging%5Cb%29)
28. [DebianMultimedia/DevelopPackaging](/DebianMultimedia/DevelopPackaging?highlight=%28%5CbCategoryPackaging%5Cb%29)
29. [DebianRepository/Setup](/DebianRepository/Setup?highlight=%28%5CbCategoryPackaging%5Cb%29)
30. [DebugPackage](/DebugPackage?highlight=%28%5CbCategoryPackaging%5Cb%29)
31. [DevelopersCorner](/DevelopersCorner?highlight=%28%5CbCategoryPackaging%5Cb%29)
32. [Diagrams](/Diagrams?highlight=%28%5CbCategoryPackaging%5Cb%29)
33. [Distcc](/Distcc?highlight=%28%5CbCategoryPackaging%5Cb%29)
34. [DkmsPackaging](/DkmsPackaging?highlight=%28%5CbCategoryPackaging%5Cb%29)
35. [DpkgConffileHandling](/DpkgConffileHandling?highlight=%28%5CbCategoryPackaging%5Cb%29)
36. [DpkgDiversions](/DpkgDiversions?highlight=%28%5CbCategoryPackaging%5Cb%29)
37. [EmacspeakTestingGuide](/EmacspeakTestingGuide?highlight=%28%5CbCategoryPackaging%5Cb%29)
38. [FTBFS](/FTBFS?highlight=%28%5CbCategoryPackaging%5Cb%29)
39. [FastTrack](/FastTrack?highlight=%28%5CbCategoryPackaging%5Cb%29)
40. [Fonts/PackagingPolicy](/Fonts/PackagingPolicy?highlight=%28%5CbCategoryPackaging%5Cb%29)
41. [GettingPorted](/GettingPorted?highlight=%28%5CbCategoryPackaging%5Cb%29)
42. [GitPackaging](/GitPackaging?highlight=%28%5CbCategoryPackaging%5Cb%29)
43. [GitPackagingSurvey](/GitPackagingSurvey?highlight=%28%5CbCategoryPackaging%5Cb%29)
44. [GitPackagingSurvey/bare debian](/GitPackagingSurvey/bare%20debian?highlight=%28%5CbCategoryPackaging%5Cb%29)
45. [GitPackagingSurvey/bare debian monorepo](/GitPackagingSurvey/bare%20debian%20monorepo?highlight=%28%5CbCategoryPackaging%5Cb%29)
46. [GitPackagingSurvey/bare template](/GitPackagingSurvey/bare%20template?highlight=%28%5CbCategoryPackaging%5Cb%29)
47. [GitPackagingSurvey/git-debcherry](/GitPackagingSurvey/git-debcherry?highlight=%28%5CbCategoryPackaging%5Cb%29)
48. [GitPackagingSurvey/git-debrebase](/GitPackagingSurvey/git-debrebase?highlight=%28%5CbCategoryPackaging%5Cb%29)
49. [GitPackagingSurvey/git-dpm](/GitPackagingSurvey/git-dpm?highlight=%28%5CbCategoryPackaging%5Cb%29)
50. [GitPackagingSurvey/manually maintained applied](/GitPackagingSurvey/manually%20maintained%20applied?highlight=%28%5CbCategoryPackaging%5Cb%29)
51. [GitPackagingSurvey/merging](/GitPackagingSurvey/merging?highlight=%28%5CbCategoryPackaging%5Cb%29)
52. [GitPackagingSurvey/modified orig plus further unapplied patches](/GitPackagingSurvey/modified%20orig%20plus%20further%20unapplied%20patches?highlight=%28%5CbCategoryPackaging%5Cb%29)
53. [GitPackagingSurvey/rebasing](/GitPackagingSurvey/rebasing?highlight=%28%5CbCategoryPackaging%5Cb%29)
54. [GitPackagingSurvey/unapplied](/GitPackagingSurvey/unapplied?highlight=%28%5CbCategoryPackaging%5Cb%29)
55. [GitPackagingWorkflow](/GitPackagingWorkflow?highlight=%28%5CbCategoryPackaging%5Cb%29)
56. [GitPackagingWorkflow/DebConf11BOF](/GitPackagingWorkflow/DebConf11BOF?highlight=%28%5CbCategoryPackaging%5Cb%29)
57. [GitSrc](/GitSrc?highlight=%28%5CbCategoryPackaging%5Cb%29)
58. [Gnome/Git](/Gnome/Git?highlight=%28%5CbCategoryPackaging%5Cb%29)
59. [Gnome/Rust\_Packaging](/Gnome/Rust_Packaging?highlight=%28%5CbCategoryPackaging%5Cb%29)
60. [HardeningWalkthrough](/HardeningWalkthrough?highlight=%28%5CbCategoryPackaging%5Cb%29)
61. [HowToPackageForDebian](/HowToPackageForDebian?highlight=%28%5CbCategoryPackaging%5Cb%29)
62. [Java/Packaging](/Java/Packaging?highlight=%28%5CbCategoryPackaging%5Cb%29)
63. [Javascript/Forwading-Patches](/Javascript/Forwading-Patches?highlight=%28%5CbCategoryPackaging%5Cb%29)
64. [Javascript/Policy](/Javascript/Policy?highlight=%28%5CbCategoryPackaging%5Cb%29)
65. [Javascript/Repacking](/Javascript/Repacking?highlight=%28%5CbCategoryPackaging%5Cb%29)
66. [Maintainers](/Maintainers?highlight=%28%5CbCategoryPackaging%5Cb%29)
67. [MakeAPrivatePackage](/MakeAPrivatePackage?highlight=%28%5CbCategoryPackaging%5Cb%29)
68. [ManageUpstreamDifferences](/ManageUpstreamDifferences?highlight=%28%5CbCategoryPackaging%5Cb%29)
69. [Mapping package names across distributions](/Mapping%20package%20names%20across%20distributions?highlight=%28%5CbCategoryPackaging%5Cb%29)
70. [Mentors](/Mentors?highlight=%28%5CbCategoryPackaging%5Cb%29)
71. [Mingw-W64](/Mingw-W64?highlight=%28%5CbCategoryPackaging%5Cb%29)
72. [NonMaintainerUpload](/NonMaintainerUpload?highlight=%28%5CbCategoryPackaging%5Cb%29)
73. [OpenSuseBuildService](/OpenSuseBuildService?highlight=%28%5CbCategoryPackaging%5Cb%29)
74. [PackageConfigUpgrade](/PackageConfigUpgrade?highlight=%28%5CbCategoryPackaging%5Cb%29)
75. [PackageSalvaging](/PackageSalvaging?highlight=%28%5CbCategoryPackaging%5Cb%29)
76. [PackageTransition](/PackageTransition?highlight=%28%5CbCategoryPackaging%5Cb%29)
77. [Packaging](/Packaging?highlight=%28%5CbCategoryPackaging%5Cb%29)
78. [Packaging/EmbeddedCopies](/Packaging/EmbeddedCopies?highlight=%28%5CbCategoryPackaging%5Cb%29)
79. [Packaging/HackingDependencies](/Packaging/HackingDependencies?highlight=%28%5CbCategoryPackaging%5Cb%29)
80. [Packaging/Intro](/Packaging/Intro?highlight=%28%5CbCategoryPackaging%5Cb%29)
81. [Packaging/Learn](/Packaging/Learn?highlight=%28%5CbCategoryPackaging%5Cb%29)
82. [Packaging/Pre-Requisites](/Packaging/Pre-Requisites?highlight=%28%5CbCategoryPackaging%5Cb%29)
83. [Packaging/Pre-Requisites/nspawn](/Packaging/Pre-Requisites/nspawn?highlight=%28%5CbCategoryPackaging%5Cb%29)
84. [Packaging/Variables](/Packaging/Variables?highlight=%28%5CbCategoryPackaging%5Cb%29)
85. [Packaging/ruby-team-meta-build](/Packaging/ruby-team-meta-build?highlight=%28%5CbCategoryPackaging%5Cb%29)
86. [Packaging/sbuild](/Packaging/sbuild?highlight=%28%5CbCategoryPackaging%5Cb%29)
87. [PackagingFAQ](/PackagingFAQ?highlight=%28%5CbCategoryPackaging%5Cb%29)
88. [PackagingTools](/PackagingTools?highlight=%28%5CbCategoryPackaging%5Cb%29)
89. [PackagingWithDarcs](/PackagingWithDarcs?highlight=%28%5CbCategoryPackaging%5Cb%29)
90. [PackagingWithDocker](/PackagingWithDocker?highlight=%28%5CbCategoryPackaging%5Cb%29)
91. [PackagingWithGit](/PackagingWithGit?highlight=%28%5CbCategoryPackaging%5Cb%29)
92. [PbuilderTricks](/PbuilderTricks?highlight=%28%5CbCategoryPackaging%5Cb%29)
93. [PkgQtKde/BookwormReleasePlans](/PkgQtKde/BookwormReleasePlans?highlight=%28%5CbCategoryPackaging%5Cb%29)
94. [PkgQtKde/ForkyReleasePlans](/PkgQtKde/ForkyReleasePlans?highlight=%28%5CbCategoryPackaging%5Cb%29)
95. [PkgQtKde/TrixieReleasePlans](/PkgQtKde/TrixieReleasePlans?highlight=%28%5CbCategoryPackaging%5Cb%29)
96. [Projects/DebSrc3.0](/Projects/DebSrc3.0?highlight=%28%5CbCategoryPackaging%5Cb%29)
97. [Python/DbgBuilds](/Python/DbgBuilds?highlight=%28%5CbCategoryPackaging%5Cb%29)
98. [Python/GitPackaging](/Python/GitPackaging?highlight=%28%5CbCategoryPackaging%5Cb%29)
99. [Python/LibraryStyleGuide](/Python/LibraryStyleGuide?highlight=%28%5CbCategoryPackaging%5Cb%29)
100. [Python/Policy](/Python/Policy?highlight=%28%5CbCategoryPackaging%5Cb%29)
101. [RPM](/RPM?highlight=%28%5CbCategoryPackaging%5Cb%29)
102. [RenamingPackages](/RenamingPackages?highlight=%28%5CbCategoryPackaging%5Cb%29)
103. [Repackage\_srcrpm](/Repackage_srcrpm?highlight=%28%5CbCategoryPackaging%5Cb%29)
104. [Repacking](/Repacking?highlight=%28%5CbCategoryPackaging%5Cb%29)
105. [ReproducibleBuilds](/ReproducibleBuilds?highlight=%28%5CbCategoryPackaging%5Cb%29)
106. [Salsa](/Salsa?highlight=%28%5CbCategoryPackaging%5Cb%29)
107. [Salsa/support](/Salsa/support?highlight=%28%5CbCategoryPackaging%5Cb%29)
108. [ServiceSandboxing](/ServiceSandboxing?highlight=%28%5CbCategoryPackaging%5Cb%29)
109. [Services/wnpp-by-tags.debian.net](/Services/wnpp-by-tags.debian.net?highlight=%28%5CbCategoryPackaging%5Cb%29)
110. [SimpleBackportCreation](/SimpleBackportCreation?highlight=%28%5CbCategoryPackaging%5Cb%29)
111. [SimplePackagingTutorial](/SimplePackagingTutorial?highlight=%28%5CbCategoryPackaging%5Cb%29)
112. [Software that can't be packaged](/Software%20that%20can%27t%20be%20packaged?highlight=%28%5CbCategoryPackaging%5Cb%29)
113. [SoftwarePackaging](/SoftwarePackaging?highlight=%28%5CbCategoryPackaging%5Cb%29)
114. [SponsorChecklist](/SponsorChecklist?highlight=%28%5CbCategoryPackaging%5Cb%29)
115. [Teams](/Teams?highlight=%28%5CbCategoryPackaging%5Cb%29)
116. [Teams/DebianHaskellGroup](/Teams/DebianHaskellGroup?highlight=%28%5CbCategoryPackaging%5Cb%29)
117. [Teams/DebianMonoGroup/NewPackage](/Teams/DebianMonoGroup/NewPackage?highlight=%28%5CbCategoryPackaging%5Cb%29)
118. [Teams/Dpkg/Spec/DeclarativePackaging](/Teams/Dpkg/Spec/DeclarativePackaging?highlight=%28%5CbCategoryPackaging%5Cb%29)
119. [Teams/Foo2zjs](/Teams/Foo2zjs?highlight=%28%5CbCategoryPackaging%5Cb%29)
120. [Teams/Games](/Teams/Games?highlight=%28%5CbCategoryPackaging%5Cb%29)
121. [Teams/MySQL](/Teams/MySQL?highlight=%28%5CbCategoryPackaging%5Cb%29)
122. [Teams/MySQL/MySQL-wsrep](/Teams/MySQL/MySQL-wsrep?highlight=%28%5CbCategoryPackaging%5Cb%29)
123. [Teams/OCamlTaskForce](/Teams/OCamlTaskForce?highlight=%28%5CbCategoryPackaging%5Cb%29)
124. [Teams/Printing](/Teams/Printing?highlight=%28%5CbCategoryPackaging%5Cb%29)
125. [Teams/Ruby/Packaging](/Teams/Ruby/Packaging?highlight=%28%5CbCategoryPackaging%5Cb%29)
126. [UntrustedDebs](/UntrustedDebs?highlight=%28%5CbCategoryPackaging%5Cb%29)
127. [UpstreamGuide](/UpstreamGuide?highlight=%28%5CbCategoryPackaging%5Cb%29)
128. [UpstreamMetadata](/UpstreamMetadata?highlight=%28%5CbCategoryPackaging%5Cb%29)
129. [UscanEnhancements](/UscanEnhancements?highlight=%28%5CbCategoryPackaging%5Cb%29)
130. [UsingQuilt](/UsingQuilt?highlight=%28%5CbCategoryPackaging%5Cb%29)
131. [WNPP](/WNPP?highlight=%28%5CbCategoryPackaging%5Cb%29)
132. [WritingDebianPackageDescriptions](/WritingDebianPackageDescriptions?highlight=%28%5CbCategoryPackaging%5Cb%29)
133. [binNMU](/binNMU?highlight=%28%5CbCategoryPackaging%5Cb%29)
134. [debian/copyright](/debian/copyright?highlight=%28%5CbCategoryPackaging%5Cb%29)
135. [debian/patches](/debian/patches?highlight=%28%5CbCategoryPackaging%5Cb%29)
136. [debian/upstream](/debian/upstream?highlight=%28%5CbCategoryPackaging%5Cb%29)
137. [debian/upstream/edam](/debian/upstream/edam?highlight=%28%5CbCategoryPackaging%5Cb%29)
138. [debian/watch](/debian/watch?highlight=%28%5CbCategoryPackaging%5Cb%29)
139. [pbuilder](/pbuilder?highlight=%28%5CbCategoryPackaging%5Cb%29)
140. [piuparts](/piuparts?highlight=%28%5CbCategoryPackaging%5Cb%29)
141. [pt\_BR/AdvancedBuildingTips](/pt_BR/AdvancedBuildingTips?highlight=%28%5CbCategoryPackaging%5Cb%29)
142. [pt\_PT/Teams](/pt_PT/Teams?highlight=%28%5CbCategoryPackaging%5Cb%29)
143. [sbuild](/sbuild?highlight=%28%5CbCategoryPackaging%5Cb%29)
144. [tag2upload](/tag2upload?highlight=%28%5CbCategoryPackaging%5Cb%29)
145. [udeb](/udeb?highlight=%28%5CbCategoryPackaging%5Cb%29)
146. [zh\_CN/DebianRepository/Setup](/zh_CN/DebianRepository/Setup?highlight=%28%5CbCategoryPackaging%5Cb%29)

---

[CategoryPackaging](/CategoryPackaging) | [CategoryPortal](/CategoryPortal)