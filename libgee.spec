%define oname	libgee
%define api	0.6
%define major	2
%define gimajor 1.0

%define libname %mklibname gee %{major}
%define girname %mklibname gee-gir %{gimajor}
%define devname %mklibname -d gee %{major}

Name:		%{oname}0.6
Summary:	GObject-based collection library
Version:	0.6.6
Release:	1
License: 	LGPLv2+
Group:		System/Libraries
URL: 		http://live.gnome.org/Libgee
Source0: 	ftp://ftp.gnome.org/pub/GNOME/sources/libgee/%{api}/%{oname}-%{version}.tar.xz

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
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%files -n %{libname}
%doc AUTHORS COPYING NEWS README
%{_libdir}/libgee.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/Gee-%{gimajor}.typelib

%files -n %{devname}
%doc ChangeLog
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_datadir}/vala/vapi/*.vapi
%{_datadir}/gir-1.0/Gee-%{gimajor}.gir

%changelog
* Mon Apr 30 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.6.4-2
+ Revision: 794578
- rebuild of stable libgee 0.6
- forking libgee0.6
- still needed
- rebuild
- prep for libgee0.6

* Mon Apr 30 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.7.2-2
+ Revision: 794521
- rebuild
- employed api libname
- fixed gimajor for gir pkg
- fix reqs for gir pkg

* Sun Apr 29 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.7.2-1
+ Revision: 794392
- version update 0.72

* Sun Jan 22 2012 Götz Waschk <waschk@mandriva.org> 0.6.4-1
+ Revision: 764968
- new version

* Wed Dec 07 2011 Matthew Dawkins <mattydaw@mandriva.org> 0.6.3-2
+ Revision: 738654
- rebuild
- cleaned up spec
- removed defattr, BuildRoot, mkrel, clean section
- removed ldconfig scriptlets (why werent they bracketted b4)
- split out gir pkg
- removed .la files

* Wed Nov 09 2011 Götz Waschk <waschk@mandriva.org> 0.6.3-1
+ Revision: 729360
- new version

* Wed Sep 14 2011 Götz Waschk <waschk@mandriva.org> 0.6.2.1-1
+ Revision: 699744
- new version

* Wed Sep 14 2011 Götz Waschk <waschk@mandriva.org> 0.6.2-1
+ Revision: 699727
- new version
- xz tarball

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.6.1-2
+ Revision: 661462
- mass rebuild

* Fri Jan 28 2011 Götz Waschk <waschk@mandriva.org> 0.6.1-1
+ Revision: 633707
- update to new version 0.6.1

* Mon Sep 27 2010 Funda Wang <fwang@mandriva.org> 0.6.0-1mdv2011.0
+ Revision: 581174
- update to new version 0.6.0

* Thu Sep 16 2010 Götz Waschk <waschk@mandriva.org> 0.5.3-1mdv2011.0
+ Revision: 578924
- update to new version 0.5.3

* Mon Aug 02 2010 Götz Waschk <waschk@mandriva.org> 0.5.2-1mdv2011.0
+ Revision: 565039
- new version
- add introspection typelib

* Fri Jul 30 2010 Funda Wang <fwang@mandriva.org> 0.5.1-2mdv2011.0
+ Revision: 563399
- rebuild for new gobject-introspection

* Tue Jul 13 2010 Götz Waschk <waschk@mandriva.org> 0.5.1-1mdv2011.0
+ Revision: 552023
- update to new version 0.5.1

* Thu Oct 01 2009 Götz Waschk <waschk@mandriva.org> 0.5.0-1mdv2010.1
+ Revision: 452040
- new version
- new major

* Mon Sep 28 2009 Götz Waschk <waschk@mandriva.org> 0.4.0-1mdv2010.0
+ Revision: 450618
- update to new version 0.4.0

* Wed Aug 05 2009 Götz Waschk <waschk@mandriva.org> 0.3.0-1mdv2010.0
+ Revision: 410205
- new version
- new major

* Fri Jul 31 2009 Götz Waschk <waschk@mandriva.org> 0.2.0-1mdv2010.0
+ Revision: 405036
- new version
- add introspection support

* Mon Jul 20 2009 Götz Waschk <waschk@mandriva.org> 0.1.6-1mdv2010.0
+ Revision: 398066
- update to new version 0.1.6

* Sat Feb 21 2009 Götz Waschk <waschk@mandriva.org> 0.1.5-1mdv2009.1
+ Revision: 343664
- update to new version 0.1.5

* Wed Dec 03 2008 Frederic Crozat <fcrozat@mandriva.com> 0.1.4-1mdv2009.1
+ Revision: 309707
- import libgee

