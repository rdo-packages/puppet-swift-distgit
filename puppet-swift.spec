%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
Name:           puppet-swift
Version:        9.6.0
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
%setup -q -n openstack-swift-%{upstream_version}

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
* Wed Jul 05 2017 rdo-trunk <javier.pena@redhat.com> 9.6.0-1
- Update to 9.6.0

* Thu Feb 02 2017 Alfredo Moralejo <amoralej@redhat.com> 9.5.0-1
- Update to 9.5.0

* Tue Jan 17 2017 Haikel Guemar <hguemar@fedoraproject.org> 9.4.4-1
- Update to 9.4.4

* Mon Nov 07 2016 Alfredo Moralejo <amoralej@redhat.com> 9.4.3-1
- Update to 9.4.3

* Fri Oct 14 2016 Haikel Guemar <hguemar@fedoraproject.org> 9.4.2-1
- Update to 9.4.2

* Wed Oct 05 2016 Alan Pevec <alan.pevec@redhat.com> 9.4.1-1
- Update to 9.4.1

* Thu Sep 29 2016 Alfredo Moralejo <amoralej@redhat.com> 9.4.0-1
- Update to 9.4.0

* Thu Sep 22 2016 Haikel Guemar <hguemar@fedoraproject.org> 9.3.0-1
- Update to 9.3.0

* Fri Sep 16 2016 Haikel Guemar <hguemar@fedoraproject.org> 9.2.0-1
- Update to 9.2.0


