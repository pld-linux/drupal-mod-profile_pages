%define		modname profile_pages
Summary:	Drupal Site Profile Directory Module
Summary(pl):	Modu³ katalogu profili dla Drupala
Name:		drupal-mod-%{modname}
Version:	4.6.0
Release:	0.1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://drupal.org/files/projects/%{modname}-%{version}.tar.gz
# Source0-md5:	c47bcd90ead10832acc90771922016f6
URL:		http://drupal.org/node/24879
Requires:	drupal >= 4.6.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_drupaldir	%{_datadir}/drupal
%define		_moddir		%{_drupaldir}/modules

%description
A module that lists every user on the site with a certain
profile_field filled in, similar to a site directory of users with
that information listed (i.e., users with an AOL Instant Messenger or
XFire account).

%description -l pl
Modu³ wy¶wietlaj±cy ka¿dego u¿ytkownika na stronie z wype³nionym
pewnym polem profile_field, podobnie do katalogu strony u¿ytkowników z
podan± t± informacj± (np. u¿ytkowników z kontami komunikatora AOL
Instant Messenger czy XFire).

%prep
%setup -q -n %{modname}
rm -f LICENSE.txt # GPL v2

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_moddir}

install *.module $RPM_BUILD_ROOT%{_moddir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%{_moddir}/*.module
