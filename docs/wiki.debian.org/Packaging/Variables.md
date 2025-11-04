# Packaging/Variables - Debian Wiki

**Source:** https://wiki.debian.org/Packaging/Variables

---

[Translations](/DebianWiki/EditorGuide#translation): [English](/Packaging/Variables) - [Português (Brasil)](/pt_BR/Packaging/Variables)

---

## Setup your environment

Add the following variables in your ~/.bashrc file. DEBEMAIL and DEBFULLNAME variables are used by debian tools (like debmake, dch etc) to set your name and email.

```
export DEBEMAIL=your@email.domain
export DEBFULLNAME='Your Name'
alias lintian='lintian -iIEcv --pedantic --color auto' # gives more verbose output and helpful hints to solve the problem
alias git-import-dsc='git-import-dsc --author-is-committer --pristine-tar' # optional
alias clean='fakeroot debian/rules clean' # optional
```

Note: You can also use debclean command instead of setting alias for clean.

and update your current environment by running

```
$ source ~/.bashrc
```

---

[CategoryPackaging](/CategoryPackaging)