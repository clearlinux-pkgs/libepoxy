#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libepoxy
Version  : 1.3.1
Release  : 6
URL      : https://github.com/anholt/libepoxy/archive/v1.3.1.tar.gz
Source0  : https://github.com/anholt/libepoxy/archive/v1.3.1.tar.gz
Summary  : epoxy GL dispatch Library
Group    : Development/Tools
License  : MIT
Requires: libepoxy-lib
BuildRequires : pkgconfig(egl)
BuildRequires : pkgconfig(gl)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xorg-macros)

%description
Epoxy is a library for handling OpenGL function pointer management for
you.
It hides the complexity of ```dlopen()```, ```dlsym()```,
```glXGetProcAddress()```, ```eglGetProcAddress()```, etc. from the
app developer, with very little knowledge needed on their part.  They
get to read GL specs and write code using undecorated function names
like ```glCompileShader()```.

%package dev
Summary: dev components for the libepoxy package.
Group: Development
Requires: libepoxy-lib

%description dev
dev components for the libepoxy package.


%package lib
Summary: lib components for the libepoxy package.
Group: Libraries

%description lib
lib components for the libepoxy package.


%prep
%setup -q -n libepoxy-1.3.1

%build
%autogen --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/epoxy/egl.h
/usr/include/epoxy/egl_generated.h
/usr/include/epoxy/gl.h
/usr/include/epoxy/gl_generated.h
/usr/include/epoxy/glx.h
/usr/include/epoxy/glx_generated.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
