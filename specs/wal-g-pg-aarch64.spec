%global _prefix /usr/local
Summary: Archival and Restoration for databases in the Cloud
Name: wal-g-pg
Version: v2.0.1bb
Release: 1%{?dist}
License: Apache-2.0
Group: Unspecified
Url: https://gitHub.com/wal-g/wal-g
BuildArch: aarch64
Requires: glibc

%description
Archival and Restoration for databases in the Cloud

%prep

bash /gobuild.sh -o sebasmannem -r wal-g -t deps -t pg_build


%install
mkdir -p %{buildroot}/%{_bindir}

%{__install} -m 0755 %{_builddir}/wal-g/main/pg/wal-g %{buildroot}/%{_bindir}/wal-g-pg


%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/wal-g-pg