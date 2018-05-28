Name:           ros-melodic-combined-robot-hw-tests
Version:        0.15.0
Release:        0%{?dist}
Summary:        ROS combined_robot_hw_tests package

Group:          Development/Libraries
License:        BSD
URL:            https://github.com/ros-controls/ros_control/wiki
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-combined-robot-hw
Requires:       ros-melodic-controller-manager
Requires:       ros-melodic-controller-manager-tests
Requires:       ros-melodic-hardware-interface
Requires:       ros-melodic-roscpp
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-combined-robot-hw
BuildRequires:  ros-melodic-controller-manager
BuildRequires:  ros-melodic-controller-manager-tests
BuildRequires:  ros-melodic-hardware-interface
BuildRequires:  ros-melodic-roscpp
BuildRequires:  ros-melodic-rostest

%description
The combined_robot_hw_tests package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Mon May 28 2018 Bence Magyar <bence.magyar.robotics@gmail.com> - 0.15.0-0
- Autogenerated by Bloom

* Thu Apr 26 2018 Bence Magyar <bence.magyar.robotics@gmail.com> - 0.14.2-0
- Autogenerated by Bloom

* Mon Apr 16 2018 Toni Oliver <toni@shadowrobot.com> - 0.14.1-0
- Autogenerated by Bloom

* Mon Mar 26 2018 Toni Oliver <toni@shadowrobot.com> - 0.14.0-0
- Autogenerated by Bloom

