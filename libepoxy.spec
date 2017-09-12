#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : libepoxy
Version  : 1.4.3
Release  : 21
URL      : https://github.com/anholt/libepoxy/archive/1.4.3.tar.gz
Source0  : https://github.com/anholt/libepoxy/archive/1.4.3.tar.gz
Summary  : epoxy GL dispatch Library
Group    : Development/Tools
License  : MIT
Requires: libepoxy-lib
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : pkgconfig(32egl)
BuildRequires : pkgconfig(32gl)
BuildRequires : pkgconfig(32x11)
BuildRequires : pkgconfig(32xorg-macros)
BuildRequires : pkgconfig(egl)
BuildRequires : pkgconfig(gl)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : python3-dev

%description
[![Build Status](https://travis-ci.org/anholt/libepoxy.svg?branch=master)](https://travis-ci.org/anholt/libepoxy)
[![Build status](https://ci.appveyor.com/api/projects/status/xv6y5jurt5v5ngjx/branch/master?svg=true)](https://ci.appveyor.com/project/ebassi/libepoxy/branch/master)

%package dev
Summary: dev components for the libepoxy package.
Group: Development
Requires: libepoxy-lib
Provides: libepoxy-devel

%description dev
dev components for the libepoxy package.


%package dev32
Summary: dev32 components for the libepoxy package.
Group: Default
Requires: libepoxy-lib32
Requires: libepoxy-dev

%description dev32
dev32 components for the libepoxy package.


%package lib
Summary: lib components for the libepoxy package.
Group: Libraries

%description lib
lib components for the libepoxy package.


%package lib32
Summary: lib32 components for the libepoxy package.
Group: Default

%description lib32
lib32 components for the libepoxy package.


%prep
%setup -q -n libepoxy-1.4.3
pushd ..
cp -a libepoxy-1.4.3 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1505182028
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-semantic-interposition "
%autogen  --enable-static --enable-glx=yes
make V=1  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%autogen  --enable-static --enable-glx=yes  --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make V=1  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1505182028
rm -rf %{buildroot}
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

%files dev
%defattr(-,root,root,-)
/usr/include/epoxy/common.h
/usr/include/epoxy/egl.h
/usr/include/epoxy/egl_generated.h
/usr/include/epoxy/gl.h
/usr/include/epoxy/gl_generated.h
/usr/include/epoxy/glx.h
/usr/include/epoxy/glx_generated.h
/usr/lib64/*.a
/usr/lib64/libepoxy.so
/usr/lib64/pkgconfig/epoxy.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/*.a
/usr/lib32/libepoxy.so
/usr/lib32/pkgconfig/32epoxy.pc
/usr/lib32/pkgconfig/epoxy.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libepoxy.so.0
/usr/lib64/libepoxy.so.0.0.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libepoxy.so.0
/usr/lib32/libepoxy.so.0.0.0
