from setuptools import setup
import glob
import os

package_name = 'topic_pkg'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob.glob(os.path.join('launch', '*.launch.py'))),
        ('share/' + package_name + '/param', glob.glob(os.path.join('param', '*.yaml'))),
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
            'publisher = topic_pkg.publisher:main',
            'subscriber = topic_pkg.subscriber:main',
            'rpm_pub = topic_pkg.rpm_pub:main',
            'speed_calc =  topic_pkg.speed_calc:main',
            'speed_sub =  topic_pkg.speed_sub:main'            
        ],
    },
)
