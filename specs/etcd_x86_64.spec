%global _prefix /usr/local
Summary: Distributed reliable key-value store for the most critical data of a distributed system
Name: etcd
Version: v3.4.22
Release: 1%{?dist}
License: Apache-2.0
Group: Unspecified
Url: https://github.com/etcd-io/etcd
BuildArch: x86_64

%description
Distributed reliable key-value store for the most critical data of a distributed system

%prep


%install
mkdir -p %{buildroot}/%{_bindir}

%{__install} -m 0755 %{_builddir}/etcd-v3.4.22-linux-amd64/etcdctl %{buildroot}/%{_bindir}/etcdctl
%{__install} -m 0755 %{_builddir}/etcd-v3.4.22-linux-amd64/etcd %{buildroot}/%{_bindir}/etcd


%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/etcdctl
%{_bindir}/etcd