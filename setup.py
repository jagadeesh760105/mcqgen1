from setuptools import find_packages,setup

setup(
    name='mcqgenerator',
    version='0.0.1',
    author='jagadeesh naik',
    author_email='jagadeeshnaikpalthya@gmail.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2",'langchain_huggingface','langchain-groq==0.1.9'],
    packages=find_packages()
)