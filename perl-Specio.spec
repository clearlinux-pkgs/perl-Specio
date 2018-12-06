#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Specio
Version  : 0.43
Release  : 16
URL      : https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/Specio-0.43.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/Specio-0.43.tar.gz
Summary  : 'Type constraints and coercions for Perl'
Group    : Development/Tools
License  : Artistic-2.0
Requires: perl-Specio-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Devel::StackTrace)
BuildRequires : perl(Eval::Closure)
BuildRequires : perl(MRO::Compat)
BuildRequires : perl(Module::Runtime)
BuildRequires : perl(Role::Tiny)
BuildRequires : perl(Role::Tiny::With)
BuildRequires : perl(Sub::Quote)
BuildRequires : perl(Test::Fatal)
BuildRequires : perl(Test::Needs)
BuildRequires : perl(Try::Tiny)

%description
# NAME
Specio - Type constraints and coercions for Perl
# VERSION
version 0.43
# SYNOPSIS

%package dev
Summary: dev components for the perl-Specio package.
Group: Development
Provides: perl-Specio-devel = %{version}-%{release}

%description dev
dev components for the perl-Specio package.


%package license
Summary: license components for the perl-Specio package.
Group: Default

%description license
license components for the perl-Specio package.


%prep
%setup -q -n Specio-0.43

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Specio
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Specio/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1Specio.pm
/usr/lib/perl5/vendor_perl/5.28.1Specio/Coercion.pm
/usr/lib/perl5/vendor_perl/5.28.1Specio/Constraint/AnyCan.pm
/usr/lib/perl5/vendor_perl/5.28.1Specio/Constraint/AnyDoes.pm
/usr/lib/perl5/vendor_perl/5.28.1Specio/Constraint/AnyIsa.pm
/usr/lib/perl5/vendor_perl/5.28.1Specio/Constraint/Enum.pm
/usr/lib/perl5/vendor_perl/5.28.1Specio/Constraint/Intersection.pm
/usr/lib/perl5/vendor_perl/5.28.1Specio/Constraint/ObjectCan.pm
/usr/lib/perl5/vendor_perl/5.28.1Specio/Constraint/ObjectDoes.pm
/usr/lib/perl5/vendor_perl/5.28.1Specio/Constraint/ObjectIsa.pm
/usr/lib/perl5/vendor_perl/5.28.1Specio/Constraint/Parameterizable.pm
/usr/lib/perl5/vendor_perl/5.28.1Specio/Constraint/Parameterized.pm
/usr/lib/perl5/vendor_perl/5.28.1Specio/Constraint/Role/CanType.pm
/usr/lib/perl5/vendor_perl/5.28.1Specio/Constraint/Role/DoesType.pm
/usr/lib/perl5/vendor_perl/5.28.1Specio/Constraint/Role/Interface.pm
/usr/lib/perl5/vendor_perl/5.28.1Specio/Constraint/Role/IsaType.pm
/usr/lib/perl5/vendor_perl/5.28.1Specio/Constraint/Simple.pm
/usr/lib/perl5/vendor_perl/5.28.1Specio/Constraint/Structurable.pm
/usr/lib/perl5/vendor_perl/5.28.1Specio/Constraint/Structured.pm
/usr/lib/perl5/vendor_perl/5.28.1Specio/Constraint/Union.pm
/usr/lib/perl5/vendor_perl/5.28.1Specio/Declare.pm
/usr/lib/perl5/vendor_perl/5.28.1Specio/DeclaredAt.pm
/usr/lib/perl5/vendor_perl/5.28.1Specio/Exception.pm
/usr/lib/perl5/vendor_perl/5.28.1Specio/Exporter.pm
/usr/lib/perl5/vendor_perl/5.28.1Specio/Helpers.pm
/usr/lib/perl5/vendor_perl/5.28.1Specio/Library/Builtins.pm
/usr/lib/perl5/vendor_perl/5.28.1Specio/Library/Numeric.pm
/usr/lib/perl5/vendor_perl/5.28.1Specio/Library/Perl.pm
/usr/lib/perl5/vendor_perl/5.28.1Specio/Library/String.pm
/usr/lib/perl5/vendor_perl/5.28.1Specio/Library/Structured.pm
/usr/lib/perl5/vendor_perl/5.28.1Specio/Library/Structured/Dict.pm
/usr/lib/perl5/vendor_perl/5.28.1Specio/Library/Structured/Map.pm
/usr/lib/perl5/vendor_perl/5.28.1Specio/Library/Structured/Tuple.pm
/usr/lib/perl5/vendor_perl/5.28.1Specio/OO.pm
/usr/lib/perl5/vendor_perl/5.28.1Specio/PartialDump.pm
/usr/lib/perl5/vendor_perl/5.28.1Specio/Registry.pm
/usr/lib/perl5/vendor_perl/5.28.1Specio/Role/Inlinable.pm
/usr/lib/perl5/vendor_perl/5.28.1Specio/Subs.pm
/usr/lib/perl5/vendor_perl/5.28.1Specio/TypeChecks.pm
/usr/lib/perl5/vendor_perl/5.28.1Test/Specio.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Specio.3
/usr/share/man/man3/Specio::Coercion.3
/usr/share/man/man3/Specio::Constraint::AnyCan.3
/usr/share/man/man3/Specio::Constraint::AnyDoes.3
/usr/share/man/man3/Specio::Constraint::AnyIsa.3
/usr/share/man/man3/Specio::Constraint::Enum.3
/usr/share/man/man3/Specio::Constraint::Intersection.3
/usr/share/man/man3/Specio::Constraint::ObjectCan.3
/usr/share/man/man3/Specio::Constraint::ObjectDoes.3
/usr/share/man/man3/Specio::Constraint::ObjectIsa.3
/usr/share/man/man3/Specio::Constraint::Parameterizable.3
/usr/share/man/man3/Specio::Constraint::Parameterized.3
/usr/share/man/man3/Specio::Constraint::Role::CanType.3
/usr/share/man/man3/Specio::Constraint::Role::DoesType.3
/usr/share/man/man3/Specio::Constraint::Role::Interface.3
/usr/share/man/man3/Specio::Constraint::Role::IsaType.3
/usr/share/man/man3/Specio::Constraint::Simple.3
/usr/share/man/man3/Specio::Constraint::Structurable.3
/usr/share/man/man3/Specio::Constraint::Structured.3
/usr/share/man/man3/Specio::Constraint::Union.3
/usr/share/man/man3/Specio::Declare.3
/usr/share/man/man3/Specio::DeclaredAt.3
/usr/share/man/man3/Specio::Exception.3
/usr/share/man/man3/Specio::Exporter.3
/usr/share/man/man3/Specio::Helpers.3
/usr/share/man/man3/Specio::Library::Builtins.3
/usr/share/man/man3/Specio::Library::Numeric.3
/usr/share/man/man3/Specio::Library::Perl.3
/usr/share/man/man3/Specio::Library::String.3
/usr/share/man/man3/Specio::Library::Structured.3
/usr/share/man/man3/Specio::Library::Structured::Dict.3
/usr/share/man/man3/Specio::Library::Structured::Map.3
/usr/share/man/man3/Specio::Library::Structured::Tuple.3
/usr/share/man/man3/Specio::OO.3
/usr/share/man/man3/Specio::PartialDump.3
/usr/share/man/man3/Specio::Registry.3
/usr/share/man/man3/Specio::Role::Inlinable.3
/usr/share/man/man3/Specio::Subs.3
/usr/share/man/man3/Specio::TypeChecks.3
/usr/share/man/man3/Test::Specio.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Specio/LICENSE
