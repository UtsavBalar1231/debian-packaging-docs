# PackagingWithGit/Svn-buildpackageConversion - Debian Wiki

**Source:** https://wiki.debian.org/PackagingWithGit/Svn-buildpackageConversion

---

Contents

1. [Introduction](#Introduction)
2. [Importing using git-svn or git-svnimport](#Importing_using_git-svn_or_git-svnimport)
3. [Importing using svn-all-fast-export](#Importing_using_svn-all-fast-export)
4. [Links](#Links)

# Introduction

Converting a subversion repository created by svn-buildpackage to git (with all history intact), is more difficult than it seems, particularly when the upstream source is included in the svn repository as well. If the svn repository only has debian/ in it (mergeWithUpstream mode) then git-svn can be used to either

* [convert the package to git](http://www.cs.unb.ca/~bremner/blog/posts/svn_to_git/)
* [interact with the central svn while you get to use git locally](http://honk.sigxcpu.org/con/Using_git_svn_and_git_buildpackage_to_build_packages_maintained_in_Subversion.html)

In both cases, the structure of the svn-buildpackage repository is problematic. The typical repository created by svn-buildpackage has a structure like this:

```
mypackage/trunk/
          tags/
          tags/1.0-1/
          branches/
          branches/mybranch/
                   upstream/
                   upstream/current/
                            1.0/
```

Both git-svn and git-svnimport will have problems with this setup due to the subdirectories of upstream in the branches directory. If you need to keep the svn repository and want to continue to work with it (using git to push changes back to the svn repository), then you'll have to use git-svn and live with the strange setup.

Importing the debian/ directory along with the upstream source can be achieved in a number of ways. With a sufficiently good knowledge of git and enough time to stitch the repository back together, you can end up with a git repository that looks like you had used git-buildpackage all along. Two approaches are outlined below using the traditional (but problematic) git-svn or git-svnimport and what appears to be a better approach using svn-all-fast-export.

# Importing using git-svn or git-svnimport

To deal with the odd repository structure used by svn-buildpackage and the differences between svn's idea of a tag (a branch) and git's idea of a tag (a tag), you can rewrite the repository into a simpler format first and then import it into git. If you have a repo that also contains multiple packages such as the one illustrated above, then you must break up the repo by filtering out the package of interest at this stage as the import scripts below can't handle more than one package in the repository. Note that svnadmin is very slow on large repositories and large change sets so keeping large temp files around can be worthwhile as there are parts of this process that could well require several attempts until you are satisfied with the results or there may be several packages in the repo you wish to do at the same time.

```
$ svnadmin dump /path/to/svn | svndumpfilter include mypackage > mypackage.dump
$ svnadmin create tmp-svn
$ ./svnbprewrite < mypackage.dump | svnadmin load tmp-svn
```

The svnbprewrite AWK script (below) changes branches/upstream/current to just branches/upstream and moves branches/upstream/<version> to tags/upstream-<version>.

**Don't use this awk script with binary data**

The awk script below corrupts binary data such as PNGs that are included in the svn dump. Fortunately, svnadmin import realises this and halts the import.

```
#!/usr/bin/awk -f

# print_status = 0  =>  print normally
#                1  =>  skip the current block (look for PROPS-END)
#                2  =>  end of block found, now just skip empty lines

/.+/ {
        # Ready to print data again (non-empty line)
        if (print_status == 2) {
                print_status = 0
        }
}

/^PROPS-END$/ {
        # End of not printing, skip the empty lines though
        if (print_status == 1) {
                print_status = 2
        }
}

/^Node-path:( |.*\/)tags$/ {
        # Make sure the tags directory is not created twice
        if (tags_created == 1) {
                print_status = 1
        }
        tags_created = 1
}

/^Node-path:( |.*\/)branches\/upstream\/current/ {
        # Remove the current from the upstream directory
        sub("/current", "", $2)
        if ($2 ~ /branches\/upstream$/) {
                # Would create the upstream directory again, instead use it
                # to create the tags directory, if necessary, otherwise skip it
                if (tags_created == 1) {
                        print_status = 1
                }
                tags_created = 1
                sub("branches/upstream","tags",$2)
        }
        if (print_status == 0) print $1, $2
        next
}

/^Node-path:( |.*\/)branches\/upstream\// {
        # Switch all upstream tags to the tags directory
        sub("branches/upstream/", "tags/upstream-", $2)
        if (print_status == 0) print $1, $2
        next
}

/^Node-copyfrom-path:( |.*\/)branches\/upstream\/current/ { 
        # Make sure all copies from current now come from upstream
        sub("/current", "", $2)
        if (print_status == 0) print $1, $2
        next
} 

/^Node-copyfrom-path:( |.*\/)branches\/upstream\// {
        # Make sure all copies from upstream tags come from the tags directory
        sub("branches/upstream/", "tags/upstream-", $2)
        if (print_status == 0) print $1, $2
        next
}

{ 
        if (print_status == 0) print
}
```

Either git-svnimport or git svn clone can then be used to import this repository to git. Making an "authors" file means that you'll get a nice list of author names and addresses rather than username@jibberish.

```
$ svn log --quiet file:///$PWD/tmp-svn | grep -v "no author" | awk '/^r/ {print $3}' | sort -u >> authors
$ editor authors
  # The format of authors is:
  # username = Real Name <email@example.org>
$ git svn clone --stdlayout --no-metadata --authors-file=authors file:///$PWD/tmp-svn/mypackage mypackage
```

The resulting repository should contain branches of origin and master (both point to the trunk), mybranch, and upstream. There should also be tags, in this case upstream-1.0 and 1.0-1. Some amount of manual cleaning up of the repository will be necessary to fix up any tags that are misplaced, to prune back some odd branches that are left over from the conversion or to fix up mistakes where svn-inject was mistakenly used instead of svn-upgrade to introduce a new upstream version into the subversion repository.

# Importing using svn-all-fast-export

The utility svn-all-fast-export is an svn to git converter that is both extremely fast and also very flexible in being able to rewrite tags and branches into their git counterparts. This permits a package to be imported without trying to munge the svn dump in between as we did with git-svn. As before, we start off with an svn dump and take the opportunity to filter on the package we are interested in moving to git (actually, svn-all-fast-export can probably even do more than one package at a time into multiple git repos). We also prepare an "authors" file to map usernames to real names and email addresses.

```
$ svnadmin dump /path/to/svn | svndumpfilter include mypackage > mypackage.dump
$ svnadmin create tmp-svn
$ svnadmin load tmp-svn < mypackage.dump

$ svn log --quiet file:///$PWD/tmp-svn | grep -v "no author" | awk '/^r/ {print $3}' | sort -u >> authors
$ editor authors
```

(Note that while git-svn is quite lenient about formatting in authors, svn-all-fast-export doesn't like excess whitespace around the equals sign in particular.)

The next step is to import the svn repo into git:

```
$ svn-all-fast-export --identity-map=authors --rules mypackage.rules tmp-svn
```

To use svn-all-fast-export, we need a "rules" file that describes how to map the bits of the svn repository into a git repository. The rules file below maps trunk to master, upstream/current into a branch upstream in the git repo and the rest of the upstream/$version branches into tags along that upstream branch. The Debian package release tags are also added as debian/$version just as git-buildpackage would have done. Note that ~ is used in Debian package versions and is legal in svn tag names and but not in git tag names so it is remapped to \_ in these rules. The rules file doesn't handle additional branches in the svn repository at all but hopefully it's obvious how to extend these rules to handle this. For more information about the rules files, see the examples in /usr/share/doc/svn-all-fast-export/examples.

```
# mypackage.rules

create repository mypackage
end repository

match /mypackage/trunk/
  repository mypackage
  branch master
end match

match /mypackage/branches/upstream/current/
  repository mypackage
  branch upstream
end match

match /mypackage/branches/upstream/([^/]+)/
  repository mypackage
  branch refs/tags/upstream/\1
  substitute branch s/~/_/
end match

match /mypackage/tags/([^/]+)/
  repository mypackage
  branch refs/tags/debian/\1
  substitute branch s/~/_/
end match
```

After this is complete, a little tidying of the repo may be in order -- use gitk --all to look at what has been imported into git. If, for example, svn-inject had been mistakenly used for version the new upstream 1.2 even though version 1.1 was already in the svn repository, then 1.2 won't be on the upstream branch at all and the upstream branch goes directly from 1.1 to 1.3 as illustrated below. You may chose not to rewrite history and ignore this; however, if there was no "1.3" version imported into the repository, then you may find that importing the next upstream with git-import-orig is unnecessarily hard as the history in the repo is a little confused. Fortunately, for a repo that hasn't been published to anyone yet, it's relatively easy to rewrite history to fix this problem by rewriting the history of the incorrect commit.

```
    actual history                    desired history

* master                          * master
|                                 |         
*_    merge upstream 1.3          *    merge upstream 1.3
| \_                              |\ 
|   * upstream, upstream/1.3      | * upstream, upstream/1.3
|   |                             | |  
|   |                             | |
*   | merge upstream 1.2          * | merge upstream 1.2 
|\  |                             |\|  
| * | upstream/1.2                | * upstream/1.2    
|   |                             | |       
|   |                             | |         
*_  | merge upstream 1.1          * | merge upstream 1.1  
| \_|                             |\|
|   * upstream/1.1                | * upstream/1.1
|   |                             | |
```

First, we need the git commit id for the three upstream imports in question and then we create a "grafts" file that tells git to pretend that two commits are linked. We can then bake the graft into the history by rewriting the history after which the grafts file is no longer needed and can be removed.

The format for the grafts file is "commitid parent1 parent2 parent3...". In our case, the upstream/1.2 has no parent where it should have had upstream/1.1 as its parent; upstream/1.3 currently has upstream/1.1 as its parent where it should have had upstream/1.2 as its parent. Note that if a commit is listed in "grafts", then grafts doesn't list just the extra links between commits, it lists **all** links between commits, so breaking the incorrect 1.1→1.3 link is as simple as omitting it in the grafts file.

```
$ git show-ref upstream/1.1 upstream/1.2 upstream/1.3
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa refs/tags/upstream/1.1
bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb refs/tags/upstream/1.2
cccccccccccccccccccccccccccccccccccccccc refs/tags/upstream/1.3

$ echo "cccccccccccccccccccccccccccccccccccccccc bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" > .git/info/grafts

$ git filter-branch --tag-name-filter cat -- --all
$ rm .git/info/grafts

$ cd ..
$ git clone mypackage mypackage-fixed
```

Following a history rewrite it is recommended that the repo be cloned and the new version used instead. The old one will contain garbage branches from the rewriting as well as backup tags for any cases where svn-buildpackage ended up retagging a release.

# Links

* <http://madduck.net/blog/2007.10.07:converting-a-package-to-git/>