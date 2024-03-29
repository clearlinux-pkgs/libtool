#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x6EAC957F8EEB55C0 (alex.ameen.tx@gmail.com)
#
Name     : libtool
Version  : 2.4.7
Release  : 32
URL      : https://mirrors.kernel.org/gnu/libtool/libtool-2.4.7.tar.xz
Source0  : https://mirrors.kernel.org/gnu/libtool/libtool-2.4.7.tar.xz
Source1  : https://mirrors.kernel.org/gnu/libtool/libtool-2.4.7.tar.xz.sig
Summary  : The GNU Portable Library Tool
Group    : Development/Tools
License  : GFDL-1.3+ GPL-2.0 GPL-2.0+ LGPL-2.0+ LGPL-2.1
Requires: libtool-bin = %{version}-%{release}
Requires: libtool-data = %{version}-%{release}
Requires: libtool-info = %{version}-%{release}
Requires: libtool-lib = %{version}-%{release}
Requires: libtool-license = %{version}-%{release}
Requires: libtool-man = %{version}-%{release}
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : gfortran
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : glibc-staticdev

%description
GNU Libtool is a generic library support script that hides the complexity of
using shared libraries behind a consistent, portable interface. To use Libtool,
add the new generic library building commands to your Makefile, Makefile.in, or
Makefile.am.

%package bin
Summary: bin components for the libtool package.
Group: Binaries
Requires: libtool-data = %{version}-%{release}
Requires: libtool-license = %{version}-%{release}

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
Requires: libtool-lib = %{version}-%{release}
Requires: libtool-bin = %{version}-%{release}
Requires: libtool-data = %{version}-%{release}
Provides: libtool-devel = %{version}-%{release}
Requires: libtool = %{version}-%{release}

%description dev
dev components for the libtool package.


%package dev32
Summary: dev32 components for the libtool package.
Group: Default
Requires: libtool-lib32 = %{version}-%{release}
Requires: libtool-bin = %{version}-%{release}
Requires: libtool-data = %{version}-%{release}
Requires: libtool-dev = %{version}-%{release}

%description dev32
dev32 components for the libtool package.


%package info
Summary: info components for the libtool package.
Group: Default

%description info
info components for the libtool package.


%package lib
Summary: lib components for the libtool package.
Group: Libraries
Requires: libtool-data = %{version}-%{release}
Requires: libtool-license = %{version}-%{release}

%description lib
lib components for the libtool package.


%package lib32
Summary: lib32 components for the libtool package.
Group: Default
Requires: libtool-data = %{version}-%{release}
Requires: libtool-license = %{version}-%{release}

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
%setup -q -n libtool-2.4.7
cd %{_builddir}/libtool-2.4.7
pushd ..
cp -a libtool-2.4.7 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1648753234
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%configure --disable-static --enable-static
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%configure --disable-static --enable-static   --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :
cd ../build32;
make %{?_smp_mflags} check || : || :

%install
export SOURCE_DATE_EPOCH=1648753234
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libtool
cp %{_builddir}/libtool-2.4.7/COPYING %{buildroot}/usr/share/package-licenses/libtool/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/libtool-2.4.7/libltdl/COPYING.LIB %{buildroot}/usr/share/package-licenses/libtool/01a6b4bf79aca9b556822601186afab86e8c4fbf
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
if [ -d %{buildroot}/usr/share/pkgconfig ]
then
pushd %{buildroot}/usr/share/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install
## Remove excluded files
rm -f %{buildroot}*/usr/lib64/libltdl.a
rm -f %{buildroot}*/usr/lib32/libltdl.a

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
/usr/include/libltdl/lt_dlloader.h
/usr/include/libltdl/lt_error.h
/usr/include/libltdl/lt_system.h
/usr/include/ltdl.h
/usr/lib64/libltdl.so
/usr/share/aclocal/*.m4

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libltdl.so

%files info
%defattr(0644,root,root,0755)
/usr/share/info/libtool.info
/usr/share/info/libtool.info-1
/usr/share/info/libtool.info-2

%files lib
%defattr(-,root,root,-)
/usr/lib64/libltdl.so.7
/usr/lib64/libltdl.so.7.3.2

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libltdl.so.7
/usr/lib32/libltdl.so.7.3.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libtool/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/libtool/4cc77b90af91e615a64ae04893fdffa7939db84c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/libtool.1
/usr/share/man/man1/libtoolize.1
