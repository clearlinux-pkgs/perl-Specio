#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Specio
Version  : 0.45
Release  : 26
URL      : https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/Specio-0.45.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/Specio-0.45.tar.gz
Summary  : 'Type constraints and coercions for Perl'
Group    : Development/Tools
License  : Artistic-2.0
Requires: perl-Specio-license = %{version}-%{release}
Requires: perl-Specio-perl = %{version}-%{release}
Requires: perl(Devel::StackTrace)
Requires: perl(Eval::Closure)
Requires: perl(MRO::Compat)
Requires: perl(Module::Runtime)
Requires: perl(Role::Tiny)
Requires: perl(Role::Tiny::With)
Requires: perl(Sub::Quote)
Requires: perl(Try::Tiny)
Requires: perl(XString)
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
BuildRequires : perl(XString)

%description
# NAME
Specio - Type constraints and coercions for Perl
# VERSION
version 0.45
# SYNOPSIS

%package dev
Summary: dev components for the perl-Specio package.
Group: Development
Provides: perl-Specio-devel = %{version}-%{release}
Requires: perl-Specio = %{version}-%{release}

%description dev
dev components for the perl-Specio package.


%package license
Summary: license components for the perl-Specio package.
Group: Default

%description license
license components for the perl-Specio package.


%package perl
Summary: perl components for the perl-Specio package.
Group: Default
Requires: perl-Specio = %{version}-%{release}

%description perl
perl components for the perl-Specio package.


%prep
%setup -q -n Specio-0.45
cd %{_builddir}/Specio-0.45

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Specio
cp %{_builddir}/Specio-0.45/LICENSE %{buildroot}/usr/share/package-licenses/perl-Specio/6b93bf1e533dec284ed3e0827aa113905883006f
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
/usr/share/package-licenses/perl-Specio/6b93bf1e533dec284ed3e0827aa113905883006f

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/Specio.pm
/usr/lib/perl5/vendor_perl/5.28.2/Specio/Coercion.pm
/usr/lib/perl5/vendor_perl/5.28.2/Specio/Constraint/AnyCan.pm
/usr/lib/perl5/vendor_perl/5.28.2/Specio/Constraint/AnyDoes.pm
/usr/lib/perl5/vendor_perl/5.28.2/Specio/Constraint/AnyIsa.pm
/usr/lib/perl5/vendor_perl/5.28.2/Specio/Constraint/Enum.pm
/usr/lib/perl5/vendor_perl/5.28.2/Specio/Constraint/Intersection.pm
/usr/lib/perl5/vendor_perl/5.28.2/Specio/Constraint/ObjectCan.pm
/usr/lib/perl5/vendor_perl/5.28.2/Specio/Constraint/ObjectDoes.pm
/usr/lib/perl5/vendor_perl/5.28.2/Specio/Constraint/ObjectIsa.pm
/usr/lib/perl5/vendor_perl/5.28.2/Specio/Constraint/Parameterizable.pm
/usr/lib/perl5/vendor_perl/5.28.2/Specio/Constraint/Parameterized.pm
/usr/lib/perl5/vendor_perl/5.28.2/Specio/Constraint/Role/CanType.pm
/usr/lib/perl5/vendor_perl/5.28.2/Specio/Constraint/Role/DoesType.pm
/usr/lib/perl5/vendor_perl/5.28.2/Specio/Constraint/Role/Interface.pm
/usr/lib/perl5/vendor_perl/5.28.2/Specio/Constraint/Role/IsaType.pm
/usr/lib/perl5/vendor_perl/5.28.2/Specio/Constraint/Simple.pm
/usr/lib/perl5/vendor_perl/5.28.2/Specio/Constraint/Structurable.pm
/usr/lib/perl5/vendor_perl/5.28.2/Specio/Constraint/Structured.pm
/usr/lib/perl5/vendor_perl/5.28.2/Specio/Constraint/Union.pm
/usr/lib/perl5/vendor_perl/5.28.2/Specio/Declare.pm
/usr/lib/perl5/vendor_perl/5.28.2/Specio/DeclaredAt.pm
/usr/lib/perl5/vendor_perl/5.28.2/Specio/Exception.pm
/usr/lib/perl5/vendor_perl/5.28.2/Specio/Exporter.pm
/usr/lib/perl5/vendor_perl/5.28.2/Specio/Helpers.pm
/usr/lib/perl5/vendor_perl/5.28.2/Specio/Library/Builtins.pm
/usr/lib/perl5/vendor_perl/5.28.2/Specio/Library/Numeric.pm
/usr/lib/perl5/vendor_perl/5.28.2/Specio/Library/Perl.pm
/usr/lib/perl5/vendor_perl/5.28.2/Specio/Library/String.pm
/usr/lib/perl5/vendor_perl/5.28.2/Specio/Library/Structured.pm
/usr/lib/perl5/vendor_perl/5.28.2/Specio/Library/Structured/Dict.pm
/usr/lib/perl5/vendor_perl/5.28.2/Specio/Library/Structured/Map.pm
/usr/lib/perl5/vendor_perl/5.28.2/Specio/Library/Structured/Tuple.pm
/usr/lib/perl5/vendor_perl/5.28.2/Specio/OO.pm
/usr/lib/perl5/vendor_perl/5.28.2/Specio/PartialDump.pm
/usr/lib/perl5/vendor_perl/5.28.2/Specio/Registry.pm
/usr/lib/perl5/vendor_perl/5.28.2/Specio/Role/Inlinable.pm
/usr/lib/perl5/vendor_perl/5.28.2/Specio/Subs.pm
/usr/lib/perl5/vendor_perl/5.28.2/Specio/TypeChecks.pm
/usr/lib/perl5/vendor_perl/5.28.2/Test/Specio.pm
