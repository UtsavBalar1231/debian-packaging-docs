# Packaging/EmbeddedCopies - Debian Wiki

**Source:** https://wiki.debian.org/Packaging/EmbeddedCopies

---

**[Debian Policy Manual: 4.13. Embedded code copies](https://www.debian.org/doc/debian-policy/ch-source.html#embedded-code-copies)**  
Some software packages include in their release distributions "convenience" copies of code from other software packages, generally so that users compiling from source don’t have to download multiple archives. Debian packages should not make use of these copies unless the included package is explicitly intended to be used in this way. If the included code is already in the Debian archive in the form of a library, the Debian packaging should ensure that binary packages reference the libraries already in Debian and not the embedded copy. If the included code is not already in Debian, it should be packaged separately as a prerequisite dependency, if possible.

**Embedded copies of code, data, fonts or other things** should be removed from the upstream VCS and source tarballs. Upstream might want to only embed the copies in the binary packages they distribute, script the install of their dependencies and or bundle the dependencies into a single but separate source tarball rather than embedding copies of them. Once upstream has fixed the issue, the Debian package can then be updated to the fixed version. If upstream refuse to remove the embedded copies, then Debian should either repack the upstream tarball using [Files-Excluded](/UscanEnhancements) (if there is a [DFSG](/DebianFreeSoftwareGuidelines) or size issue) or remove the files in [debian/rules](/Teams/Dpkg/DebianRules)' clean target and/or very early in the build target, so that there is no chance of them being used by the build process.

The [list of packages that embed copies (including unused ones) of other projects](https://salsa.debian.org/security-tracker-team/security-tracker/raw/master/data/embedded-code-copies) is maintained in the security-tracker git repository. This list also contains information about forks so that the security team can check if all forks contain the same vulnerabilities.

All Debian members have commit access to the security-tracker repository and others can send suggestions or additions to the [debian-security-tracker mailing list](https://lists.debian.org/debian-security-tracker "DebianList").

## Tools

### Lintian

**[Lintian](/Lintian)** detects embedding of

* Common libraries written in 
  + [C/C++](https://lintian.debian.org/tags/embedded-library.html)
  + [JavaScript](https://lintian.debian.org/tags/embedded-javascript-library.html)
  + [PHP](https://lintian.debian.org/tags/embedded-php-library.html) ([PEAR](https://lintian.debian.org/tags/embedded-pear-module.html))
* [Fonts](https://lintian.debian.org/tags/duplicate-font-file.html)
* PostScript: [copyrighted Adobe font fragments](https://lintian.debian.org/tags/license-problem-font-adobe-copyrighted-fragment.html) ([without credit](https://lintian.debian.org/tags/license-problem-font-adobe-copyrighted-fragment-no-credit.html))
* [feedparser](https://lintian.debian.org/tags/embedded-feedparser-library.html)

### Others

* [check-all-the-things](https://github.com/collab-qa/check-all-the-things/) has a couple of tests (embed-readme, embed-dirs) for finding embedded copies via heuristics, and several ideas for new tests.
* These [Gobby](/gobby.debian.org) pages mention embedded copies: [Embedded modules in inc](https://gobby.debian.org/export/Teams/Perl/Embedded_modules_in_inc) (by the [Debian Perl Team](/Teams/DebianPerlGroup))
* The [Debian duplication detector](/dedup.debian.net) detects duplicate files in binary packages and may be useful for detecting verbatim duplication of files across multiple binary packages.
* [Clonewise](https://github.com/silviocesare/Clonewise) is a tool not yet in Debian that could be used to [find unfixed vulnerabilities because of embedded code copies](https://lists.debian.org/msgid-search/CA+ygN1LxTeSFSt45qDC2KLKbYUWTqPvrm5ZHvEjjoEkuDL4f5g@mail.gmail.com/firsthit).
* [SourcererCC](https://github.com/Mondego/SourcererCC) is another tool for detecting embedded code copies.
* [Sokrates](https://www.sokrates.dev/) can also do [duplication detection](https://www.sokrates.dev/book/duplication).

The [Debian Sources](https://sources.debian.org/) service allows [searching](https://sources.debian.org/advancedsearch/) for specific hashes and ctags throughout all Debian source code, which may be useful for detecting duplication of source code and data.

If you have a particular file with some interesting aspect (security issue, etc.), you can likely find other copies using [Debian Code Search](/DebianCodeSearch) or similar external service, such as [Black Duck Open Hub](https://openhub.net/), [SourceGraph Public Code Search](https://sourcegraph.com/search) or [GitHub Search](https://github.com/search).

If a file has a fairly unique name, you can often find copies of that file by searching the contents of Debian binary or source packages using apt-file:

|  |
| --- |
| apt-file search uniquename.py |
| or |
| apt-file search -I dsc uniquename.c |

## Tracking

Various Debian folks keep track of embedded copies they found via usertags:

[rbrito@ime.usp.br](https://udd.debian.org/cgi-bin/bts-usertags.cgi?tag=embedded-code-copy&user=rbrito@ime.usp.br) [jwilk@debian.org](https://udd.debian.org/cgi-bin/bts-usertags.cgi?tag=embedded-code-copy&user=jwilk@debian.org) [mbehrle@debian.org](https://udd.debian.org/cgi-bin/bts-usertags.cgi?tag=embedded-code-copy&user=mbehrle@debian.org) [pabs@debian.org](https://udd.debian.org/cgi-bin/bts-usertags.cgi?tag=embed&user=pabs@debian.org) [sramacher@debian.org](https://udd.debian.org/cgi-bin/bts-usertags.cgi?tag=embedded-synctex-parser&user=sramacher@debian.org) [dr@jones.dk](https://udd.debian.org/cgi-bin/bts-usertags.cgi?tag=embed&user=dr@jones.dk)

## See also

These wiki pages mention embedded copies: [arc4random](/arc4random)

## External links

* Fedora Packaging Guidelines: [Bundling policy](https://docs.fedoraproject.org/en-US/packaging-guidelines/#bundling)
* Fedora Wiki: [Bundled libraries](https://fedoraproject.org/wiki/Bundled_Libraries)
* Gentoo Wiki: [Bundled dependencies policy](https://wiki.gentoo.org/wiki/Why_not_bundle_dependencies)
* Homebrew Documentation: [Acceptable Formulae § Vendored dependencies policy](https://docs.brew.sh/Acceptable-Formulae#stuff-that-requires-vendored-versions-of-homebrew-formulae)

---

[CategoryPackaging](/CategoryPackaging)