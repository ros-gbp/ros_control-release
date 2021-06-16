%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-combined-robot-hw
Version:        0.19.5
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS combined_robot_hw package

License:        BSD
URL:            https://github.com/ros-controls/ros_control/wiki
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-noetic-hardware-interface
Requires:       ros-noetic-pluginlib
Requires:       ros-noetic-roscpp
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-hardware-interface
BuildRequires:  ros-noetic-pluginlib
BuildRequires:  ros-noetic-roscpp
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
Combined Robot HW class.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Wed Jun 16 2021 Bence Magyar <bence.magyar.robotics@gmail.com> - 0.19.5-1
- Autogenerated by Bloom

* Sat Dec 05 2020 Bence Magyar <bence.magyar.robotics@gmail.com> - 0.19.4-1
- Autogenerated by Bloom

* Sun Oct 11 2020 Bence Magyar <bence.magyar.robotics@gmail.com> - 0.19.3-2
- Autogenerated by Bloom

* Sun Oct 11 2020 Bence Magyar <bence.magyar.robotics@gmail.com> - 0.19.3-1
- Autogenerated by Bloom

* Mon Aug 17 2020 Bence Magyar <bence.magyar.robotics@gmail.com> - 0.19.2-1
- Autogenerated by Bloom

* Sun May 10 2020 Bence Magyar <bence.magyar.robotics@gmail.com> - 0.19.1-1
- Autogenerated by Bloom

* Thu Apr 23 2020 Bence Magyar <bence.magyar.robotics@gmail.com> - 0.19.0-1
- Autogenerated by Bloom

