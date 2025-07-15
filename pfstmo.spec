Summary:	PFS tone mapping operators
Summary(pl.UTF-8):	PFS tone mapping operators - operatory odwzorowania tonów (kompresji dynamiki)
Name:		pfstmo
Version:	1.4
Release:	1
License:	GPL v2+
Group:		Applications/Graphics
Source0:	http://downloads.sourceforge.net/pfstools/%{name}-%{version}.tar.gz
# Source0-md5:	90409a9adda70f59001c04cafcdab8d6
Patch0:		%{name}-c++.patch
Patch1:		%{name}-opt.patch
URL:		http://pfstools.sourceforge.net/pfstmo.html
BuildRequires:	autoconf
BuildRequires:	automake >= 1.6
BuildRequires:	fftw3-single-devel >= 3.0
BuildRequires:	gsl-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	pfstools-devel >= 1.0
BuildRequires:	pkgconfig
%if 0%{?debug:1}
BuildRequires:	gcc-c++ >= 6:4.2
BuildRequires:	libgomp-devel
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pfstmo package contains the implementation of state-of-the-art tone
mapping operators. The motivation here is to provide an implementation
of tone mapping operators suitable for convenient processing of both
static images and animations.

%description -l pl.UTF-8
Pakiet pfstmo zawiera implementacje operatorów odwzorowania tonów
(kompresji dynamiki). Celem jest zapewnienie operatorów nadających się
do wygodnego przetwarzania obrazów statycznych i animacji.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?debug:--enable-debug}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/pfstmo_*
%{_mandir}/man1/pfstmo_*.1*
