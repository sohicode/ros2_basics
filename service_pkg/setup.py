from setuptools import setup

package_name = 'service_pkg'

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
            'service_server = service_pkg.service_server:main',
            'service_client = service_pkg.service_client:main',
            'oe_server = service_pkg.odd_even_server:main',
            'oe_client = service_pkg.odd_even_client:main'
        ],
    },
)
