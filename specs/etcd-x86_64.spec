%global _prefix /usr/local
Summary: Distributed reliable key-value store for the most critical data of a distributed system
Name: etcd
Version: v3.5.6
Release: 1%{?dist}
License: Apache-2.0
Group: Unspecified
Url: https://gitHub.com/etcd-io/etcd
Source0: etcd-v3.5.6-linux-amd64.tar.gz
BuildArch: x86_64

%description
Distributed reliable key-value store for the most critical data of a distributed system

%prep
curl -L https://github.com/etcd-io/etcd/releases/download/v3.5.6/etcd-v3.5.6-linux-amd64.tar.gz -o %{_sourcedir}/etcd-v3.5.6-linux-amd64.tar.gz



%install
mkdir -p %{buildroot}/%{_bindir}
tar -xvf %{_sourcedir}/etcd-v3.5.6-linux-amd64.tar.gz

%{__install} -m 0755 %{_builddir}/etcd-v3.5.6-linux-amd64/etcdctl %{buildroot}/%{_bindir}/etcdctl
%{__install} -m 0755 %{_builddir}/etcd-v3.5.6-linux-amd64/etcd %{buildroot}/%{_bindir}/etcd


%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/etcdctl
%{_bindir}/etcd