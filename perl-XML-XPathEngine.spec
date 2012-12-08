%define upstream_name    XML-XPathEngine
%define upstream_version 0.12

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	A re-usable XPath engine for DOM-like trees
License:	Artistic and GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module provides an XPath engine, that can be re-used by other
module/classes that implement trees.

In order to use the XPath engine, nodes in the user module need to mimick DOM
nodes. The degree of similitude between the user tree and a DOM dictates how
much of the XPath features can be used. A module implementing all of the DOM
should be able to use this module very easily (you might need to add the cmp
method on nodes in order to get ordered result sets).

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{_mandir}/*/*
%{perl_vendorlib}/XML


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.120.0-4mdv2012.0
+ Revision: 765859
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.120.0-3
+ Revision: 764394
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.120.0-2
+ Revision: 667463
- mass rebuild

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.120.0-1mdv2011.0
+ Revision: 401813
- rebuild using %%perl_convert_version
- fixed license field

* Fri May 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.12-1mdv2010.0
+ Revision: 370253
- update to new version 0.12

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 0.11-2mdv2009.0
+ Revision: 265467
- rebuild early 2009.0 package (before pixel changes)

* Wed Apr 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.11-1mdv2009.0
+ Revision: 194866
- update to new version 0.11
- update to new version 0.10

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 0.08-2mdv2008.1
+ Revision: 180663
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Thu Jan 25 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.08-1mdv2007.0
+ Revision: 113410
- new version

* Thu Jan 18 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.07-1mdv2007.1
+ Revision: 110100
- new version

* Tue Nov 14 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.05-1mdv2007.1
+ Revision: 84006
- Import perl-XML-XPathEngine

* Tue Nov 14 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.05-1mdv2007.1
- first mdv release

