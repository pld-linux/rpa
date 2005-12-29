# TODO:
# - FHS
# - merge RPA build system with PLD ruby build system
Summary:	RPA-base - a package manager for the Ruby Production Archive
Summary(pl):	RPA-base - zarz±dca pakietów dla archiwum Ruby Production Archive
Name:		rpa
Version:	0.2.3
Release:	2
License:	Ruby
Source0:	http://rubyforge.org/frs/download.php/1904/%{name}-base-%{version}.tar.gz
# Source0-md5:	5a46c4ead6ccd2ac8ba718beae033a63
Patch0:		%{name}-sitedir.patch
Group:		Development/Libraries
URL:		http://www.rubyarchive.org/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-modules
%ruby_mod_ver_requires_eq
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RPA-base is a package manager for the Ruby Production Archive.

%description -l pl
RPA-base to zarz±dca pakietów dla archiwum Ruby Production Archive.

%package base
Summary:	Package database for RPA
Summary(pl):	Baza danych pakietów dla RPA
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description base
Package database for RPA.

%description base -l pl
Baza danych pakietów dla RPA.

%prep
%setup -q -n %{name}-base-%{version}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_rubylibdir}
#install -d rpa/tmp/%{ruby_rubylibdir}
ruby -Ilib -rrpa install.rb --prefix=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rpa
%attr(755,root,root) %{_bindir}/rpa-buildport
%attr(755,root,root) %{_bindir}/rpa-buildrepos.rb
%attr(755,root,root) %{_bindir}/rpaadmin
%{ruby_rubylibdir}/rpa
%{ruby_rubylibdir}/rpa.rb

%files base
%defattr(644,root,root,755)
%dir %{_libdir}/ruby/rpa0.0
%dir %{_libdir}/ruby/rpa0.0/1.8
%dir %{_libdir}/ruby/rpa0.0/info
%dir %{_libdir}/ruby/rpa0.0/tests
%config %{_libdir}/ruby/rpa0.0/installed
%config %{_libdir}/ruby/rpa0.0/lock
%config %{_libdir}/ruby/rpa0.0/transactions
%{_libdir}/ruby/rpa0.0/1.8/rpa*
%{_libdir}/ruby/rpa0.0/info/rpa-base
%{_libdir}/ruby/rpa0.0/tests/rpa-base
%dir %{_datadir}/doc/rpa0.0
%{_datadir}/doc/rpa0.0/rpa-base
