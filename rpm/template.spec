Name:           ros-kinetic-transmission-interface
Version:        0.13.3
Release:        0%{?dist}
Summary:        ROS transmission_interface package

Group:          Development/Libraries
License:        BSD
URL:            https://github.com/ros-controls/ros_control/wiki
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-pluginlib
Requires:       ros-kinetic-roscpp
Requires:       tinyxml-devel
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-cmake-modules
BuildRequires:  ros-kinetic-hardware-interface
BuildRequires:  ros-kinetic-pluginlib
BuildRequires:  ros-kinetic-resource-retriever
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-rosunit
BuildRequires:  tinyxml-devel

%description
Transmission Interface.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Thu Apr 26 2018 Bence Magyar <bence.magyar.robotics@gmail.com> - 0.13.3-0
- Autogenerated by Bloom

* Mon Apr 16 2018 Adolfo Rodriguez Tsouroukdissian <adolfo.rodriguez@pal-robotics.com> - 0.13.2-0
- Autogenerated by Bloom

* Mon Mar 26 2018 Adolfo Rodriguez Tsouroukdissian <adolfo.rodriguez@pal-robotics.com> - 0.13.1-0
- Autogenerated by Bloom

* Sat Dec 23 2017 Adolfo Rodriguez Tsouroukdissian <adolfo.rodriguez@pal-robotics.com> - 0.13.0-0
- Autogenerated by Bloom

* Sat Aug 05 2017 Adolfo Rodriguez Tsouroukdissian <adolfo.rodriguez@pal-robotics.com> - 0.12.0-0
- Autogenerated by Bloom

* Wed Jun 28 2017 Adolfo Rodriguez Tsouroukdissian <adolfo.rodriguez@pal-robotics.com> - 0.11.5-0
- Autogenerated by Bloom

* Tue Feb 14 2017 Adolfo Rodriguez Tsouroukdissian <adolfo.rodriguez@pal-robotics.com> - 0.11.4-0
- Autogenerated by Bloom

* Wed Dec 07 2016 Adolfo Rodriguez Tsouroukdissian <adolfo.rodriguez@pal-robotics.com> - 0.11.3-0
- Autogenerated by Bloom

* Tue Nov 29 2016 Adolfo Rodriguez Tsouroukdissian <adolfo.rodriguez@pal-robotics.com> - 0.11.2-0
- Autogenerated by Bloom

* Thu Aug 18 2016 Adolfo Rodriguez Tsouroukdissian <adolfo.rodriguez@pal-robotics.com> - 0.11.1-0
- Autogenerated by Bloom

* Mon May 23 2016 Adolfo Rodriguez Tsouroukdissian <adolfo.rodriguez@pal-robotics.com> - 0.11.0-0
- Autogenerated by Bloom

* Sat Apr 23 2016 Adolfo Rodriguez Tsouroukdissian <adolfo.rodriguez@pal-robotics.com> - 0.10.1-0
- Autogenerated by Bloom

