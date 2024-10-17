%define modname	XML-XPathEngine
%define modver 0.14

Summary:	A re-usable XPath engine for DOM-like trees
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	8
License:	Artistic and GPLv2
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{modname}/
Source0:	http://www.cpan.org/modules/by-module/XML/XML-XPathEngine-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel

%description
This module provides an XPath engine, that can be re-used by other
module/classes that implement trees.

In order to use the XPath engine, nodes in the user module need to mimick DOM
nodes. The degree of similitude between the user tree and a DOM dictates how
much of the XPath features can be used. A module implementing all of the DOM
should be able to use this module very easily (you might need to add the cmp
method on nodes in order to get ordered result sets).

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/XML
%{_mandir}/man3/*



