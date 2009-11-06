%define upstream_name    Test-Corpus-Audio-MPD
%define upstream_version 1.092920

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Automate launching of fake mdp for testing purposes
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(English)
BuildRequires: perl(File::Basename)
BuildRequires: perl(File::Copy)
BuildRequires: perl(File::Spec::Functions)
BuildRequires: perl(File::Temp)
BuildRequires: perl(Module::Util)
BuildRequires: perl(Readonly)
BuildRequires: perl(Test::More)
BuildRequires: perl(base)

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module will try to launch a new mpd server for testing purposes. This
mpd server will then be used during the POE::Component::Client::MPD manpage
or the Audio::MPD manpage tests.

In order to achieve this, the module will create a fake _mpd.conf_ file
with the correct pathes (ie, where you untarred the module tarball). It
will then check if some mpd server is already running, and stop it if the
'MPD_TEST_OVERRIDE' environment variable is true (die otherwise). Last it
will run the test mpd with its newly created configuration file.

Everything described above is done automatically when the module is
'use'-d.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*

