from setuptools import setup

package_name = 'param_topic_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='stu2',
    maintainer_email='stu2@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'param_pub_script = param_topic_pkg.param_pub:main',
            'param_calc_script = param_topic_pkg.param_calc:main'
        ],
    },
)
