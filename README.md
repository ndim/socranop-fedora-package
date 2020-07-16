The Fedora package for socranop
===============================

This package should broadly work with socranop 0.4.92 and later.


TODOs
=====

  * Upload RPM package to a COPR.

  * Once `socranop` upstream has published a release with the session bus
    (should be the 0.5.0 release), properly submit this package to Fedora.


Cheatsheet
==========

```
sh update-sources.sh && rm -rf results_socranop && fedpkg --release f39 mockbuild && sudo dnf reinstall -y results_socranop/*/*/socranop-*.noarch.rpm
```
