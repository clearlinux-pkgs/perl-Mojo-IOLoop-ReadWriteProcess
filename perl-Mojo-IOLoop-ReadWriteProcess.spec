#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Mojo-IOLoop-ReadWriteProcess
Version  : 0.24
Release  : 10
URL      : https://cpan.metacpan.org/authors/id/M/MU/MUDLER/Mojo-IOLoop-ReadWriteProcess-0.24.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MU/MUDLER/Mojo-IOLoop-ReadWriteProcess-0.24.tar.gz
Summary  : 'Execute external programs or internal code blocks as separate process.'
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-1.0
Requires: perl-Mojo-IOLoop-ReadWriteProcess-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Mojolicious)

%description
[![Build Status](https://travis-ci.org/mudler/Mojo-IOLoop-ReadWriteProcess.svg?branch=master)](https://travis-ci.org/mudler/Mojo-IOLoop-ReadWriteProcess) [![Coverage Status](http://codecov.io/github/mudler/Mojo-IOLoop-ReadWriteProcess/coverage.svg?branch=master)](https://codecov.io/github/mudler/Mojo-IOLoop-ReadWriteProcess?branch=master)
# NAME

%package dev
Summary: dev components for the perl-Mojo-IOLoop-ReadWriteProcess package.
Group: Development
Provides: perl-Mojo-IOLoop-ReadWriteProcess-devel = %{version}-%{release}
Requires: perl-Mojo-IOLoop-ReadWriteProcess = %{version}-%{release}
Requires: perl-Mojo-IOLoop-ReadWriteProcess = %{version}-%{release}

%description dev
dev components for the perl-Mojo-IOLoop-ReadWriteProcess package.


%package license
Summary: license components for the perl-Mojo-IOLoop-ReadWriteProcess package.
Group: Default

%description license
license components for the perl-Mojo-IOLoop-ReadWriteProcess package.


%prep
%setup -q -n Mojo-IOLoop-ReadWriteProcess-0.24

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

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Mojo-IOLoop-ReadWriteProcess
cp %{_builddir}/Mojo-IOLoop-ReadWriteProcess-0.24/LICENSE %{buildroot}/usr/share/package-licenses/perl-Mojo-IOLoop-ReadWriteProcess/73e24a2cd5ad78be7ec077f7a151a688f7eb298d
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
/usr/lib/perl5/vendor_perl/5.28.2/Mojo/IOLoop/ReadWriteProcess.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mojo/IOLoop/ReadWriteProcess/CGroup.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mojo/IOLoop/ReadWriteProcess/CGroup/v1.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mojo/IOLoop/ReadWriteProcess/CGroup/v1/Cpuacct.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mojo/IOLoop/ReadWriteProcess/CGroup/v1/Cpuset.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mojo/IOLoop/ReadWriteProcess/CGroup/v1/Devices.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mojo/IOLoop/ReadWriteProcess/CGroup/v1/Freezer.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mojo/IOLoop/ReadWriteProcess/CGroup/v1/Memory.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mojo/IOLoop/ReadWriteProcess/CGroup/v1/Netcls.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mojo/IOLoop/ReadWriteProcess/CGroup/v1/Netprio.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mojo/IOLoop/ReadWriteProcess/CGroup/v1/PID.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mojo/IOLoop/ReadWriteProcess/CGroup/v1/RDMA.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mojo/IOLoop/ReadWriteProcess/CGroup/v2.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mojo/IOLoop/ReadWriteProcess/CGroup/v2/CPU.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mojo/IOLoop/ReadWriteProcess/CGroup/v2/IO.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mojo/IOLoop/ReadWriteProcess/CGroup/v2/Memory.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mojo/IOLoop/ReadWriteProcess/CGroup/v2/PID.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mojo/IOLoop/ReadWriteProcess/CGroup/v2/RDMA.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mojo/IOLoop/ReadWriteProcess/Container.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mojo/IOLoop/ReadWriteProcess/Exception.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mojo/IOLoop/ReadWriteProcess/Namespace.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mojo/IOLoop/ReadWriteProcess/Pool.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mojo/IOLoop/ReadWriteProcess/Queue.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mojo/IOLoop/ReadWriteProcess/Session.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mojo/IOLoop/ReadWriteProcess/Shared/Lock.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mojo/IOLoop/ReadWriteProcess/Shared/Memory.pm
/usr/lib/perl5/vendor_perl/5.28.2/Mojo/IOLoop/ReadWriteProcess/Shared/Semaphore.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Mojo::IOLoop::ReadWriteProcess.3
/usr/share/man/man3/Mojo::IOLoop::ReadWriteProcess::CGroup.3
/usr/share/man/man3/Mojo::IOLoop::ReadWriteProcess::CGroup::v1.3
/usr/share/man/man3/Mojo::IOLoop::ReadWriteProcess::CGroup::v1::Cpuacct.3
/usr/share/man/man3/Mojo::IOLoop::ReadWriteProcess::CGroup::v1::Cpuset.3
/usr/share/man/man3/Mojo::IOLoop::ReadWriteProcess::CGroup::v1::Devices.3
/usr/share/man/man3/Mojo::IOLoop::ReadWriteProcess::CGroup::v1::Freezer.3
/usr/share/man/man3/Mojo::IOLoop::ReadWriteProcess::CGroup::v1::Memory.3
/usr/share/man/man3/Mojo::IOLoop::ReadWriteProcess::CGroup::v1::Netcls.3
/usr/share/man/man3/Mojo::IOLoop::ReadWriteProcess::CGroup::v1::Netprio.3
/usr/share/man/man3/Mojo::IOLoop::ReadWriteProcess::CGroup::v1::PID.3
/usr/share/man/man3/Mojo::IOLoop::ReadWriteProcess::CGroup::v1::RDMA.3
/usr/share/man/man3/Mojo::IOLoop::ReadWriteProcess::CGroup::v2.3
/usr/share/man/man3/Mojo::IOLoop::ReadWriteProcess::CGroup::v2::CPU.3
/usr/share/man/man3/Mojo::IOLoop::ReadWriteProcess::CGroup::v2::IO.3
/usr/share/man/man3/Mojo::IOLoop::ReadWriteProcess::CGroup::v2::Memory.3
/usr/share/man/man3/Mojo::IOLoop::ReadWriteProcess::CGroup::v2::PID.3
/usr/share/man/man3/Mojo::IOLoop::ReadWriteProcess::CGroup::v2::RDMA.3
/usr/share/man/man3/Mojo::IOLoop::ReadWriteProcess::Container.3
/usr/share/man/man3/Mojo::IOLoop::ReadWriteProcess::Exception.3
/usr/share/man/man3/Mojo::IOLoop::ReadWriteProcess::Namespace.3
/usr/share/man/man3/Mojo::IOLoop::ReadWriteProcess::Pool.3
/usr/share/man/man3/Mojo::IOLoop::ReadWriteProcess::Queue.3
/usr/share/man/man3/Mojo::IOLoop::ReadWriteProcess::Session.3
/usr/share/man/man3/Mojo::IOLoop::ReadWriteProcess::Shared::Lock.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Mojo-IOLoop-ReadWriteProcess/73e24a2cd5ad78be7ec077f7a151a688f7eb298d
