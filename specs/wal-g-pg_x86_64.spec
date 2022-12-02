%global _prefix /usr/local
Summary: Archival and Restoration for databases in the Cloud
Name: wal-g-pg
Version: v2.0.1
Release: 1%{?dist}
License: Apache-2.0
Group: Unspecified
Url: https://github.com/wal-g/wal-g
Source0: wal-g-pg-ubuntu-18.04-amd64.tar.gz
BuildArch: x86_64
Requires: glibc

%description
Archival and Restoration for databases in the Cloud

%prep
curl -L https://github.com/wal-g/wal-g/releases/download/v2.0.1/wal-g-pg-ubuntu-18.04-amd64.tar.gz -o %{_sourcedir}/wal-g-pg-ubuntu-18.04-amd64.tar.gz


%install
mkdir -p %{buildroot}/%{_bindir}
tar -xvf %{_sourcedir}/wal-g-pg-ubuntu-18.04-amd64.tar.gz

%{__install} -m 0755 %{_builddir}/wal-g-pg-ubuntu-18.04-amd64 %{buildroot}/%{_bindir}/wal-g-pg


%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/wal-g-pg
