%define upstream_name    FFI-CheckLib
%define upstream_version 0.25

%{?perl_default_filter}

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    1

Summary:    Check that a library is available for FFI
License:    GPLv1+ or Artistic
Group:      Development/Perl
Url:        http://metacpan.org/release/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/FFI/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Module::Load)
BuildRequires: perl(Test2::API) >= 1.302.15
#BuildRequires: perl(Test2::Mock) >= 0.0.60
#BuildRequires: perl(Test2::Require::EnvVar) >= 0.0.60
#BuildRequires: perl(Test2::Require::Module) >= 0.0.60
#BuildRequires: perl(Test2::V0) >= 0.0.60
BuildArch:  noarch

%description
This module checks whether a particular dynamic library is available for
FFI to use. It is modeled heavily on the Devel::CheckLib manpage, but will
find dynamic libraries even when development packages are not installed. It
also provides a FFI::CheckLib#find_lib function that will return the full
path to the found dynamic library, which can be feed directly into the
FFI::Platypus manpage or the FFI::Raw manpage.

Although intended mainly for FFI modules via the FFI::Platypus manpage and
similar, this module does not actually use any FFI to do its detection and
probing. This modules does not have any non-core dependencies on Perls
5.8-5.18. On Perl 5.20 and newer it has a configure, build and test
dependency on the Module::Build manpage.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make_build


%install
%make_install

%files
%doc Changes INSTALL LICENSE META.json META.yml README example
%{_mandir}/man3/*
%perl_vendorlib/*
