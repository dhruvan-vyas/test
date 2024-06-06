# setup for tests
# import setuptools
# setuptools.setup(
#     name="dvs_printf",
#     version="1.3",
#     python_requires=">=3.10",
#     packages=setuptools.find_packages()
# )

import tensorflow as tf


# Create a 5x3x3 tensor filled with random values
tensor = tf.random.uniform(shape=[5,3, 3])

# Print the tensor
from dvs_printf import printf 
print(tensor,"\n\n")
printf(tensor,speed=5,interval=0, getmat="true")
