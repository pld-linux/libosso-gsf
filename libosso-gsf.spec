Summary:	Maemo GSF library
Summary(pl.UTF-8):	Biblioteka Maemo GSF
Name:		libosso-gsf
Version:	1.11.10.4
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://hsivonen.iki.fi/maemo-src/%{name}_%{version}-1.tar.gz
# Source0-md5:	4c5b31154943108ba0fecf00c8af9f3c
URL:		http://modest.garage.maemo.org/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.0.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Modified version of libgsf for Maemo platform.

%description -l pl.UTF-8
Zmodyfikowana wersja libgsf dla platformy Maemo.

%package devel
Summary:	Header files for libosso-gsf
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libosso-gsf
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.0.0
Requires:	zlib-devel

%description devel
Header files for libosso-gsf.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libosso-gsf

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
%{__autoheader}
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
%attr(755,root,root) %{_libdir}/libosso-gsf-1.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libosso-gsf-1.so
%{_libdir}/libosso-gsf-1.la
%dir %{_includedir}/libosso-gsf-1
%dir %{_includedir}/libosso-gsf-1/gsf
%{_includedir}/libosso-gsf-1/gsf/*.h
%{_pkgconfigdir}/libosso-gsf-1.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libosso-gsf-1.a
