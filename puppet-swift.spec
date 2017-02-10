%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%{?dlrn: %global tarsources %{name}-%{upstream_version}}
%{!?dlrn: %global tarsources openstack-swift-%{upstream_version}}

Name:           puppet-swift
Version:        10.3.0
Release:        1%{?dist}
Summary:        Puppet module for OpenStack Swift
License:        Apache-2.0

URL:            https://launchpad.net/puppet-swift

Source0:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz

BuildArch:      noarch

Requires:       puppet-inifile
Requires:       puppet-keystone
Requires:       puppet-rsync
Requires:       puppet-stdlib
Requires:       puppet-xinetd
Requires:       puppet-concat
Requires:       puppet-memcached
Requires:       puppet >= 2.7.0

%description
Puppet module for OpenStack Swift

%prep
%setup -q -n %{tarsources}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/swift/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/swift/



%files
%{_datadir}/openstack-puppet/modules/swift/


%changelog
* Fri Feb 10 2017 Haikel Guemar <hguemar@fedoraproject.org> 10.3.0-1
- Update to 10.3.0


