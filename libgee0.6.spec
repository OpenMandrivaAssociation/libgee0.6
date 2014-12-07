%define url_ver %(echo %{version}|cut -d. -f1,2)

%define oname libgee
%define api 0.6
%define major 2
%define gimajor 1.0
%define libname %mklibname gee %{major}
%define girname %mklibname gee-gir %{gimajor}
%define devname %mklibname -d gee %{major}

Summary:	GObject-based collection library
Name:		%{oname}%{api}
Version:	0.6.8
Release:	8
License:	LGPLv2+
Group:		System/Libraries
Url:		http://live.gnome.org/Libgee
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/libgee/%{url_ver}/%{oname}-%{version}.tar.xz
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)

%description
Libgee is a collection library providing GObject-based interfaces and 
classes for commonly used data structures. 

%package -n	%{libname}
Summary:	Collection library providing GObject-based interfaces and classes 
Group:		%{group}

%description -n	%{libname}
Libgee is a collection library providing GObject-based interfaces and 
classes for commonly used data structures. 

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n	%{devname}
Summary:	Libraries and include files for developing with libgee
Group:		Development/C
Requires:	%{libname} = %{version}
Requires:	%{girname} = %{version}

%description -n	%{devname}
This package provides the necessary development libraries and include
files to allow you to develop with libgee.

%prep
%setup -qn %{oname}-%{version}

%build
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libgee.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/Gee-%{gimajor}.typelib

%files -n %{devname}
%doc AUTHORS COPYING NEWS README ChangeLog
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_datadir}/vala/vapi/*.vapi
%{_datadir}/gir-1.0/Gee-%{gimajor}.gir

