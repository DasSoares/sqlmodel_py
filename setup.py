from setuptools import setup, find_packages

setup(
    name="SQLModel_test_db",
    version="1.0",
    author="Danilo Carlos Soares",
    packages=[
        "mymodel/src/app",
        "mymodel/src/db",
        "mymodel/src/db/daos",
        "mymodel/src/tests",
    ],
    # packages=find_packages(),
    # packages=[
    #     "mysqlclient==2.2.4",
    #     "sqlmodel==0.0.22",
    # ],
    # ---------------- Exemplos abaixo ------------------
    # name="meu_projeto",
    # version="0.1",
    # packages=find_packages(),
    # install_requires=[
    #     # Adicione aqui as dependências do seu projeto, por exemplo:
    #     # "requests>=2.23.0",
    # ],
    # entry_points={
    #     'console_scripts': [
    #         'meu_projeto=meu_modulo.main:main',
    #     ],
    # },
    # author="Seu Nome",
    # author_email="seu_email@example.com",
    # description="Uma breve descrição do seu projeto.",
    # long_description=open('README.md').read(),
    # long_description_content_type='text/markdown',
    # url="https://github.com/usuario/meu_projeto",
    # classifiers=[
    #     'Programming Language :: Python :: 3',
    #     'License :: OSI Approved :: MIT License',
    #     'Operating System :: OS Independent',
    # ],
    # python_requires='>=3.6'
)
