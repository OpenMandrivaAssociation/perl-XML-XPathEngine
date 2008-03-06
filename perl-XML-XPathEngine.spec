%define module  XML-XPathEngine
%define name    perl-%{module}
%define version 0.08
%define release %mkrel 2

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        A re-usable XPath engine for DOM-like trees
License:        Artistic and GPL
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{module}/
Source:         http://www.cpan.org/modules/by-module/XML/%{module}-%{version}.tar.bz2
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}


%description
This module provides an XPath engine, that can be re-used by other
module/classes that implement trees.

In order to use the XPath engine, nodes in the user module need to mimick DOM
nodes. The degree of similitude between the user tree and a DOM dictates how
much of the XPath features can be used. A module implementing all of the DOM
should be able to use this module very easily (you might need to add the cmp
method on nodes in order to get ordered result sets).

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/*/*
%{perl_vendorlib}/XML


