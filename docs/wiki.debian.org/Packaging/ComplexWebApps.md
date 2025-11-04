# Packaging/ComplexWebApps - Debian Wiki

**Source:** https://wiki.debian.org/Packaging/ComplexWebApps

---

## Example 1: Greenlight

* ruby on rails project.
* it starts a web service and needs a systemd unit file
* Home page: <https://github.com/bigbluebutton/greenlight>)

## Package each dependency separately

1. start with packaging dependencies in Gemfile
2. you could make a tracker page like <http://debian.fosscommunity.in/status/gitlab-v12.6.0/> to see which of those are packaged already
3. you can look at gitlab, diaspora, redmine and open-build-system as examples
4. vendor/assets/javascripts will need to be replaced with their packaged versions
5. you should target unstable and later you can try to get it to stable-backports, trying to run it directly on stable will not be a good idea
6. look at diaspora-installer as a quicker PoC to get a working package fast, just runs a bundle install to install all dependencies from rubygems.org instead of using packaged gems
7. you could embed all gems in the package too. bundle install --path vendor/bundle and include that directory in source
8. download source tarball from tag, rename as required 2. extract and run bundle install 3. Include vendor/bundle in the orig.tar, may be rename to +debian.orig.tar 3. debmake 4. dpkg-buildpackage. See <https://wiki.debian.org/SimplePackagingTutorial>
9. rake assets:precompile where to run it? Option 1. in postinst like in gitlab or Option 2 like in rainloop during build