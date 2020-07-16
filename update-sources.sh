#!/bin/sh
#
# This is to update the local source tarball from the local clone of the
# upstream git repo for testing purposes. It will serve no purpose in the
# eventual Fedora package proper.

set -ex

srctree="$(cd ../socranop && pwd)"

cd "$(dirname "$0")"
fedpkg_dir="$PWD"

cd "$srctree"

./tools/dist

for tarball in dist/*.tar.gz
do
	test -f "$tarball"

	tarball_basename="$(basename "$tarball")"

	cp "$tarball" "${fedpkg_dir}/${tarball_basename}"
	
	echo "SHA512 (${tarball_basename}) = $(sha512sum ${tarball} | cut -f1 -d' ')" > "${fedpkg_dir}/sources"

done
