#
Summary:	Maemo GSF library
Name:		libosso-gsf
Version:	1.11.10.4
Release:	1
License:	LGPL
Group:		Development/Libraries
Source0:	http://hsivonen.iki.fi/maemo-src/%{name}_%{version}-1.tar.gz
# Source0-md5:	4c5b31154943108ba0fecf00c8af9f3c
URL:		http://modest.garage.maemo.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel
BuildRequires:	intltool
BuildRequires:	libtool
#BuildRequires:	python-devel
#BuildRequires:	xulrunner-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
In-place editor library for the Maemo platform.

%package devel
Summary:	Header files for libosso
Group:		Development/Libraries

%description devel
Header files for libosso.

%package static
Summary:	Static libosso-gsf library
Summary(pl.UTF-8):	Statyczna biblioteka libosso-gsf
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static liboss-gsf library.

%description static -l pl.UTF-8
Statyczna biblioteka libosso-gsf.

%prep
%setup -q

%build
%{__glib_gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libosso-gsf-1.so.1.11.10

%files devel
%defattr(644,root,root,755)
%dir %{_includedir}/libosso-gsf-1
%dir %{_includedir}/libosso-gsf-1/gsf
%{_includedir}/libosso-gsf-1/gsf/*.h
%{_libdir}/libosso-gsf-1.la
%{_pkgconfigdir}/libosso-gsf-1.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libosso-gsf-1.a
