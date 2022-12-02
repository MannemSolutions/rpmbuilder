%global _prefix /usr/local
Summary: Postgres router which prevents split brain routing
Name: pgroute66
Version: v0.8.4
Release: 1%{?dist}
License: GPL-3.0
Group: Unspecified
Url: https://github.com/mannemsolutions/pgroute66
Source0: pgroute66-v0.8.4-linux-amd64.tar.gz
BuildArch: x86_64

%description
Postgres router which prevents split brain routing

%prep
curl -L https://github.com/MannemSolutions/pgroute66/releases/download/v0.8.4/pgroute66-v0.8.4-linux-amd64.tar.gz -o %{_sourcedir}/pgroute66-v0.8.4-linux-amd64.tar.gz


%install
mkdir -p %{buildroot}/%{_bindir}
tar -xvf %{_sourcedir}/pgroute66-v0.8.4-linux-amd64.tar.gz

%{__install} -m 0755 %{_builddir}/pgroute66 %{buildroot}/%{_bindir}/pgroute66


%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/pgroute66