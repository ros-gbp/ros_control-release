Name:           ros-lunar-combined-robot-hw
Version:        0.13.1
Release:        0%{?dist}
Summary:        ROS combined_robot_hw package

Group:          Development/Libraries
License:        BSD
URL:            https://github.com/ros-controls/ros_control/wiki
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-lunar-hardware-interface
Requires:       ros-lunar-pluginlib
Requires:       ros-lunar-roscpp
BuildRequires:  ros-lunar-catkin
BuildRequires:  ros-lunar-hardware-interface
BuildRequires:  ros-lunar-pluginlib
BuildRequires:  ros-lunar-roscpp

%description
Combined Robot HW class.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Mon Mar 26 2018 Toni Oliver <toni@shadowrobot.com> - 0.13.1-0
- Autogenerated by Bloom

* Sat Dec 23 2017 Toni Oliver <toni@shadowrobot.com> - 0.13.0-0
- Autogenerated by Bloom

* Sat Aug 05 2017 Toni Oliver <toni@shadowrobot.com> - 0.12.0-0
- Autogenerated by Bloom

* Wed Jun 28 2017 Toni Oliver <toni@shadowrobot.com> - 0.11.5-0
- Autogenerated by Bloom

* Tue Apr 11 2017 Toni Oliver <toni@shadowrobot.com> - 0.11.4-0
- Autogenerated by Bloom

