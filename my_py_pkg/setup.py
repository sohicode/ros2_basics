from setuptools import setup

package_name = 'my_py_pkg'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sohi',
    maintainer_email='sohicode@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'py_hello_script = my_py_pkg.hello_ros2:main',
            'py_oop_script = my_py_pkg.oop_ros2:main'
        ],
    },
)
