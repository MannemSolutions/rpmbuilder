%global _prefix /usr/local
Summary: Cluster aware scheduler for PostgreSQL
Name: pgquartz
Version: v0.5
Release: 1%{?dist}
License: GPL-3.0
Group: Unspecified
Url: https://github.com/mannemsolutions/pgquartz
Source0: pgquartz-v0.5-linux-amd64.tar.gz
BuildArch: x86_64

%description
Cluster aware scheduler for PostgreSQL

%prep
curl -L https://github.com/MannemSolutions/PgQuartz/releases/download/v0.5/pgquartz-v0.5-linux-amd64.tar.gz -o %{_sourcedir}/pgquartz-v0.5-linux-amd64.tar.gz


%install
mkdir -p %{buildroot}/%{_bindir}
tar -xvf %{_sourcedir}/pgquartz-v0.5-linux-amd64.tar.gz

%{__install} -m 0755 %{_builddir}/pgquartz %{buildroot}/%{_bindir}/pgquartz


%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/pgquartz