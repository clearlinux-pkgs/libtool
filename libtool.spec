#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libtool
Version  : 2.4.6
Release  : 19
URL      : http://mirror.team-cymru.org/gnu/libtool/libtool-2.4.6.tar.xz
Source0  : http://mirror.team-cymru.org/gnu/libtool/libtool-2.4.6.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.3 GFDL-1.3+ GPL-2.0 GPL-2.0+ LGPL-2.0+ LGPL-2.1
Requires: libtool-bin
Requires: libtool-lib
Requires: libtool-data
Requires: libtool-doc

%description
This is an alpha testing release of [GNU Libtool][libtool], a generic
library support script.  [Libtool][] hides the complexity of using shared
libraries behind a consistent, portable interface.

%package bin
Summary: bin components for the libtool package.
Group: Binaries
Requires: libtool-data

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


%package doc
Summary: doc components for the libtool package.
Group: Documentation

%description doc
doc components for the libtool package.


%package lib
Summary: lib components for the libtool package.
Group: Libraries
Requires: libtool-data

%description lib
lib components for the libtool package.


%prep
%setup -q -n libtool-2.4.6

%build
export LANG=C
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
rm -rf %{buildroot}
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

%files doc
%defattr(-,root,root,-)
%doc /usr/share/info/*
%doc /usr/share/man/man1/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libltdl.so.7
/usr/lib64/libltdl.so.7.3.1
