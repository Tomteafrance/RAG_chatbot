import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rag_chatbot",
    version="0.0.0",
    author="Tom TEA",
    author_email="tomteafrance@gmail.com",
    description="rag package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.10,<3.11',
    keywords=["Python", "RAG", "CrewAI"],
    install_requires = [
        "pandas >= 2.0.2"
    ],
)
