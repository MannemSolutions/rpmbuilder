%global _prefix /usr/local
Summary: PostgreSQL cloud native High Availability and more.
Name: stolon
Version: v0.17.0b
Release: 1%{?dist}
License: Apache-2.0
Group: Unspecified
Url: https://gitHub.com/sorintlab/stolon
BuildArch: x86_64

%description
PostgreSQL cloud native High Availability and more.

%prep

bash /gobuild.sh -o sebasmannem -r stolon


%install
mkdir -p %{buildroot}/%{_bindir}

%{__install} -m 0755 %{_builddir}/stolon/bin/stolonctl %{buildroot}/%{_bindir}/stolonctl
%{__install} -m 0755 %{_builddir}/stolon/bin/stolon-sentinel %{buildroot}/%{_bindir}/stolon-sentinel
%{__install} -m 0755 %{_builddir}/stolon/bin/stolon-proxy %{buildroot}/%{_bindir}/stolon-proxy
%{__install} -m 0755 %{_builddir}/stolon/bin/stolon-keeper %{buildroot}/%{_bindir}/stolon-keeper


%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/stolonctl
%{_bindir}/stolon-sentinel
%{_bindir}/stolon-proxy
%{_bindir}/stolon-keeper