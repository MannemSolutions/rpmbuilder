%global _prefix /usr/local
Summary: Tool to manage PostgreSQL Fine Grained Access
Name: pgfga
Version: v2.0.1
Release: 1%{?dist}
License: Apache-2.0
Group: Unspecified
Url: https://github.com/mannemsolutions/pgfga
Source0: pgfga-v2.0.1-linux-amd64.tar.gz
BuildArch: x86_64

%description
Tool to manage PostgreSQL Fine Grained Access

%prep
curl -L https://github.com/MannemSolutions/pgfga/releases/download/v2.0.1/pgfga-v2.0.1-linux-amd64.tar.gz -o %{_sourcedir}/pgfga-v2.0.1-linux-amd64.tar.gz


%install
mkdir -p %{buildroot}/%{_bindir}
tar -xvf %{_sourcedir}/pgfga-v2.0.1-linux-amd64.tar.gz

%{__install} -m 0755 %{_builddir}/pgfga %{buildroot}/%{_bindir}/pgfga


%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/pgfga