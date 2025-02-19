#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: e36a856
#
Name     : perl-Specio
Version  : 0.50
Release  : 50
URL      : https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/Specio-0.50.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/Specio-0.50.tar.gz
Summary  : 'Type constraints and coercions for Perl'
Group    : Development/Tools
License  : Artistic-2.0
Requires: perl-Specio-perl = %{version}-%{release}
Requires: perl(Devel::StackTrace)
Requires: perl(Eval::Closure)
Requires: perl(MRO::Compat)
Requires: perl(Module::Runtime)
Requires: perl(Role::Tiny)
Requires: perl(Role::Tiny::With)
Requires: perl(Sub::Quote)
Requires: perl(Test::Fatal)
Requires: perl(Try::Tiny)
Requires: perl(XString)
BuildRequires : buildreq-cpan
BuildRequires : perl(Clone)
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
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# NAME
Specio - Type constraints and coercions for Perl
# VERSION
version 0.50
# SYNOPSIS

%package dev
Summary: dev components for the perl-Specio package.
Group: Development
Provides: perl-Specio-devel = %{version}-%{release}
Requires: perl-Specio = %{version}-%{release}

%description dev
dev components for the perl-Specio package.


%package perl
Summary: perl components for the perl-Specio package.
Group: Default
Requires: perl-Specio = %{version}-%{release}

%description perl
perl components for the perl-Specio package.


%prep
%setup -q -n Specio-0.50
cd %{_builddir}/Specio-0.50
pushd ..
cp -a Specio-0.50 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
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
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
