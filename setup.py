# -*- coding: utf-8-*-
from setuptools import setup, find_packages
setup(
    # 以下为必需参数
    name='scrapy-rabbitmq-scheduler',  # 模块名
    version='1.0.0',  # 当前版本
    description='Rabbitmq for Distributed scraping',  # 简短描述
    author_email='2387813033@qq.com',
    license='MIT',
    url='https://github.com/aox-lei/scrapy-rabbitmq-scheduler',
    install_requires=[
        'pika',
        'Scrapy>=0.14'
    ],
    packages=['scrapy-rabbitmq-scheduler'],
    package_dir={'src'}
)