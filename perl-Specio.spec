#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Specio
Version  : 0.38
Release  : 7
URL      : https://www.cpan.org/authors/id/D/DR/DROLSKY/Specio-0.38.tar.gz
Source0  : https://www.cpan.org/authors/id/D/DR/DROLSKY/Specio-0.38.tar.gz
Summary  : 'Type constraints and coercions for Perl'
Group    : Development/Tools
License  : Artistic-2.0
Requires: perl-Specio-doc
BuildRequires : perl(Devel::StackTrace)
BuildRequires : perl(Eval::Closure)
BuildRequires : perl(MRO::Compat)
BuildRequires : perl(Module::Runtime)
BuildRequires : perl(Role::Tiny)
BuildRequires : perl(Role::Tiny::With)
BuildRequires : perl(Test::Fatal)
BuildRequires : perl(Test::Needs)
BuildRequires : perl(Try::Tiny)

%description
# NAME
Specio - Type constraints and coercions for Perl
# VERSION
version 0.38
# SYNOPSIS

%package doc
Summary: doc components for the perl-Specio package.
Group: Documentation

%description doc
doc components for the perl-Specio package.


%prep
%setup -q -n Specio-0.38

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make V=1  %{?_smp_mflags}
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
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.0/Specio.pm
/usr/lib/perl5/site_perl/5.26.0/Specio/Coercion.pm
/usr/lib/perl5/site_perl/5.26.0/Specio/Constraint/AnyCan.pm
/usr/lib/perl5/site_perl/5.26.0/Specio/Constraint/AnyDoes.pm
/usr/lib/perl5/site_perl/5.26.0/Specio/Constraint/AnyIsa.pm
/usr/lib/perl5/site_perl/5.26.0/Specio/Constraint/Enum.pm
/usr/lib/perl5/site_perl/5.26.0/Specio/Constraint/Intersection.pm
/usr/lib/perl5/site_perl/5.26.0/Specio/Constraint/ObjectCan.pm
/usr/lib/perl5/site_perl/5.26.0/Specio/Constraint/ObjectDoes.pm
/usr/lib/perl5/site_perl/5.26.0/Specio/Constraint/ObjectIsa.pm
/usr/lib/perl5/site_perl/5.26.0/Specio/Constraint/Parameterizable.pm
/usr/lib/perl5/site_perl/5.26.0/Specio/Constraint/Parameterized.pm
/usr/lib/perl5/site_perl/5.26.0/Specio/Constraint/Role/CanType.pm
/usr/lib/perl5/site_perl/5.26.0/Specio/Constraint/Role/DoesType.pm
/usr/lib/perl5/site_perl/5.26.0/Specio/Constraint/Role/Interface.pm
/usr/lib/perl5/site_perl/5.26.0/Specio/Constraint/Role/IsaType.pm
/usr/lib/perl5/site_perl/5.26.0/Specio/Constraint/Simple.pm
/usr/lib/perl5/site_perl/5.26.0/Specio/Constraint/Structurable.pm
/usr/lib/perl5/site_perl/5.26.0/Specio/Constraint/Structured.pm
/usr/lib/perl5/site_perl/5.26.0/Specio/Constraint/Union.pm
/usr/lib/perl5/site_perl/5.26.0/Specio/Declare.pm
/usr/lib/perl5/site_perl/5.26.0/Specio/DeclaredAt.pm
/usr/lib/perl5/site_perl/5.26.0/Specio/Exception.pm
/usr/lib/perl5/site_perl/5.26.0/Specio/Exporter.pm
/usr/lib/perl5/site_perl/5.26.0/Specio/Helpers.pm
/usr/lib/perl5/site_perl/5.26.0/Specio/Library/Builtins.pm
/usr/lib/perl5/site_perl/5.26.0/Specio/Library/Numeric.pm
/usr/lib/perl5/site_perl/5.26.0/Specio/Library/Perl.pm
/usr/lib/perl5/site_perl/5.26.0/Specio/Library/String.pm
/usr/lib/perl5/site_perl/5.26.0/Specio/Library/Structured.pm
/usr/lib/perl5/site_perl/5.26.0/Specio/Library/Structured/Dict.pm
/usr/lib/perl5/site_perl/5.26.0/Specio/Library/Structured/Map.pm
/usr/lib/perl5/site_perl/5.26.0/Specio/Library/Structured/Tuple.pm
/usr/lib/perl5/site_perl/5.26.0/Specio/OO.pm
/usr/lib/perl5/site_perl/5.26.0/Specio/PartialDump.pm
/usr/lib/perl5/site_perl/5.26.0/Specio/Registry.pm
/usr/lib/perl5/site_perl/5.26.0/Specio/Role/Inlinable.pm
/usr/lib/perl5/site_perl/5.26.0/Specio/Subs.pm
/usr/lib/perl5/site_perl/5.26.0/Specio/TypeChecks.pm
/usr/lib/perl5/site_perl/5.26.0/Test/Specio.pm

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*
