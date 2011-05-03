%define		status		stable
%define		pearname	Horde_Http
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - Horde HTTP libraries
Name:		php-horde-Horde_Http
Version:	1.0.0
Release:	1
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.horde.org/get/%{pearname}-%{version}.tgz
# Source0-md5:	36c20d27f65c9132c95c6487d82850d0
URL:		https://github.com/horde/horde/tree/master/framework/Http/
BuildRequires:	php-channel(pear.horde.org)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.7.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php-channel(pear.horde.org)
Requires:	php-horde-Horde_Exception < 2.0.0
Requires:	php-horde-Horde_Support < 2.0.0
Requires:	php-pear >= 4:1.3.6-2
Suggests:	php-curl
Suggests:	php-http
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a set of classes for making HTTP requests.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

mv .%{php_pear_dir}/examples/Horde/Http examples

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%{php_pear_dir}/.registry/.channel.*/*.reg
%{php_pear_dir}/Horde/Http.php
%{php_pear_dir}/Horde/Http
%{_examplesdir}/%{name}-%{version}
