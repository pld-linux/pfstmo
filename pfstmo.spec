# NOTE: obsolete, included in pfstools 2.x
Summary:	PFS tone mapping operators
Summary(pl.UTF-8):	PFS tone mapping operators - operatory odwzorowania tonów (kompresji dynamiki)
Name:		pfstmo
Version:	1.5
Release:	0.1
License:	GPL v2+
Group:		Applications/Graphics
Source0:	https://downloads.sourceforge.net/pfstools/%{name}-%{version}.tar.gz
# Source0-md5:	f0dc0baee2be66b1eedf77a45864c0e9
Patch1:		%{name}-opt.patch
URL:		https://pfstools.sourceforge.net/pfstmo.html
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1.6
BuildRequires:	fftw3-devel >= 3.0
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
%patch -P1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
CXXFLAGS="%{rpmcxxflags} -std=c++98"
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
