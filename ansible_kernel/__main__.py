import logging
logging.basicConfig(filename='ansible_kernel.log',level=logging.DEBUG)
from ipykernel.kernelapp import IPKernelApp
from .kernel import AnsibleKernel
IPKernelApp.launch_instance(kernel_class=AnsibleKernel)
