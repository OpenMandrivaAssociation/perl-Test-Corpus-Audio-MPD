%define upstream_name    Test-Corpus-Audio-MPD
%define upstream_version 1.120990

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 1.120990
Release:	2

Summary:	Automate launching of fake mdp for testing purposes
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/Test-Corpus-Audio-MPD-1.120990.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(English)
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Copy)
BuildRequires:	perl(File::ShareDir)
BuildRequires:	perl(File::ShareDir::PathClass)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Readonly)
BuildRequires:	perl(Path::Class)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

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
perl Build.PL installdirs=vendor
./Build

%check
./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Fri Jun 17 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.111.260-1mdv2011.0
+ Revision: 685796
- new version

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 1.110.710-2
+ Revision: 657471
- rebuild for updated spec-helper

* Mon Mar 14 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.110.710-1
+ Revision: 644798
- update to new version 1.110710

* Sun Mar 13 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.110.600-1
+ Revision: 644343
- update to new version 1.110600

* Wed Feb 24 2010 Jérôme Quelin <jquelin@mandriva.org> 1.100.500-1mdv2011.0
+ Revision: 510524
- update to 1.100500

* Sat Feb 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.100.430-1mdv2010.1
+ Revision: 505334
- adding missing buildrequires:
- update to 1.100430

* Sat Nov 21 2009 Jérôme Quelin <jquelin@mandriva.org> 1.93.230-1mdv2010.1
+ Revision: 467869
- update to 1.093230

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 1.92.920-1mdv2010.1
+ Revision: 460707
- import perl-Test-Corpus-Audio-MPD


* Fri Nov 06 2009 cpan2dist 1.092920-1mdv
- initial mdv release, generated with cpan2dist

