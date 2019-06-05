#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libtool
Version  : 2.4.6
Release  : 26
URL      : https://mirrors.kernel.org/gnu/libtool/libtool-2.4.6.tar.xz
Source0  : https://mirrors.kernel.org/gnu/libtool/libtool-2.4.6.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.3+ GPL-2.0 GPL-2.0+ LGPL-2.0+ LGPL-2.1
Requires: libtool-bin
Requires: libtool-lib
Requires: libtool-data
Requires: libtool-license
Requires: libtool-man
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : gfortran
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
Patch1: avx2.patch

%description
This is an alpha testing release of [GNU Libtool][libtool], a generic
library support script.  [Libtool][] hides the complexity of using shared
libraries behind a consistent, portable interface.

%package bin
Summary: bin components for the libtool package.
Group: Binaries
Requires: libtool-data
Requires: libtool-license
Requires: libtool-man

%description bin
bin components for the libtool package.


%package data
Summary: data components for the libtool package.
Group: Data

%description data
data components for the libtool package.


%package dev
Summary: dev components for the libtool package.
Group: Development
Requires: libtool-lib
Requires: libtool-bin
Requires: libtool-data
Provides: libtool-devel

%description dev
dev components for the libtool package.


%package dev32
Summary: dev32 components for the libtool package.
Group: Default
Requires: libtool-lib32
Requires: libtool-bin
Requires: libtool-data
Requires: libtool-dev

%description dev32
dev32 components for the libtool package.


%package doc
Summary: doc components for the libtool package.
Group: Documentation
Requires: libtool-man

%description doc
doc components for the libtool package.


%package lib
Summary: lib components for the libtool package.
Group: Libraries
Requires: libtool-data
Requires: libtool-license

%description lib
lib components for the libtool package.


%package lib32
Summary: lib32 components for the libtool package.
Group: Default
Requires: libtool-data
Requires: libtool-license

%description lib32
lib32 components for the libtool package.


%package license
Summary: license components for the libtool package.
Group: Default

%description license
license components for the libtool package.


%package man
Summary: man components for the libtool package.
Group: Default

%description man
man components for the libtool package.


%prep
%setup -q -n libtool-2.4.6
%patch1 -p1
pushd ..
cp -a libtool-2.4.6 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1536139585
%configure --disable-static
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1536139585
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/libtool
cp COPYING %{buildroot}/usr/share/doc/libtool/COPYING
cp libltdl/COPYING.LIB %{buildroot}/usr/share/doc/libtool/libltdl_COPYING.LIB
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/libtool
/usr/bin/libtoolize

%files data
%defattr(-,root,root,-)
/usr/share/aclocal/lt~obsolete.m4
/usr/share/libtool/COPYING.LIB
/usr/share/libtool/Makefile.am
/usr/share/libtool/Makefile.in
/usr/share/libtool/README
/usr/share/libtool/aclocal.m4
/usr/share/libtool/build-aux/compile
/usr/share/libtool/build-aux/config.guess
/usr/share/libtool/build-aux/config.sub
/usr/share/libtool/build-aux/depcomp
/usr/share/libtool/build-aux/install-sh
/usr/share/libtool/build-aux/ltmain.sh
/usr/share/libtool/build-aux/missing
/usr/share/libtool/config-h.in
/usr/share/libtool/configure
/usr/share/libtool/configure.ac
/usr/share/libtool/libltdl/lt__alloc.h
/usr/share/libtool/libltdl/lt__argz_.h
/usr/share/libtool/libltdl/lt__dirent.h
/usr/share/libtool/libltdl/lt__glibc.h
/usr/share/libtool/libltdl/lt__private.h
/usr/share/libtool/libltdl/lt__strl.h
/usr/share/libtool/libltdl/lt_dlloader.h
/usr/share/libtool/libltdl/lt_error.h
/usr/share/libtool/libltdl/lt_system.h
/usr/share/libtool/libltdl/slist.h
/usr/share/libtool/loaders/dld_link.c
/usr/share/libtool/loaders/dlopen.c
/usr/share/libtool/loaders/dyld.c
/usr/share/libtool/loaders/load_add_on.c
/usr/share/libtool/loaders/loadlibrary.c
/usr/share/libtool/loaders/preopen.c
/usr/share/libtool/loaders/shl_load.c
/usr/share/libtool/lt__alloc.c
/usr/share/libtool/lt__argz.c
/usr/share/libtool/lt__dirent.c
/usr/share/libtool/lt__strl.c
/usr/share/libtool/lt_dlloader.c
/usr/share/libtool/lt_error.c
/usr/share/libtool/ltdl.c
/usr/share/libtool/ltdl.h
/usr/share/libtool/ltdl.mk
/usr/share/libtool/slist.c

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/include/libltdl/lt_dlloader.h
/usr/include/libltdl/lt_error.h
/usr/include/libltdl/lt_system.h
/usr/lib64/libltdl.so
/usr/share/aclocal/*.m4

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libltdl.so

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/info/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libltdl.so.7
/usr/lib64/libltdl.so.7.3.1

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libltdl.so.7
/usr/lib32/libltdl.so.7.3.1

%files license
%defattr(-,root,root,-)
/usr/share/doc/libtool/COPYING
/usr/share/doc/libtool/libltdl_COPYING.LIB

%files man
%defattr(-,root,root,-)
/usr/share/man/man1/libtool.1
/usr/share/man/man1/libtoolize.1
