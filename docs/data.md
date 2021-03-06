# Data

The data in Deeplodocus is splitted into 3 different entries:

- Inputs (input given to your Machine Learning algorithm)
- Labels (Expected Output, optional)
- Additional Data (Additional data given to the loss function if required, optional)


In order to load the data you have to feed Deeplodocus using the `data_config.yaml` file:

```yaml

data.yaml

# _____________________________
#
# ---- DATA CONFIG EXAMPLE ----
# _____________________________
#

dataloader:
  batch_size: 4                                            # Number of instances loaded in on batch
  num_workers: 4                                           # Number of processes or threads used for 
														   # loading the data in memory
dataset:
  train:                                                   # Training entries
      inputs :
        - ["input1-1.txt", "input1-2.txt"]
        - "input2.txt"
      labels :
        - "labels1.txt"
        - "labels2.txt"
      additional_data:
        - "additional.txt"
  validation:                                              # Validation entries
      inputs:
        - ["input1-1.txt", "input1-2.txt"]
        - "input2.txt"
      labels:
        - "labels1.txt"
        - "labels2.txt"
      additional_data:
        - "additional.txt"
  test:                                                    # Test entries
      inputs:
        - ["input1-1.txt", "input1-2.txt"]
        - "input2.txt"
      labels:
        - "labels1.txt"
        - "labels2.txt"
      additional_data:
        - "additional.txt"
```

Deeplodocus accepts to load data referenced in text files (images path, video path, numbers, text, numpy array path, etc...) and also files inside folder.
Therefore you can directly give a file path or a folder path.

```yaml

# Example

train:
    inputs:
      - "input1.txt"            # Works

train:
    inputs:
      - "./path_to_folder/"     # Work as well
```


If you have multiple entries, please add the item below:

```yaml

# Example

train:
    inputs:
      - "input1.txt"            # Input 1
      - "input2.txt"            # Input 2
```

If one entry is splitted in to different location, you can merge these to sources in one using brackets:
```yaml

# Example

train:
    inputs:
      - ["input1-1.txt", "input1-2.txt"]            # Input 1 = input1-1 + input1-2
      - "input2.txt"                                # Input 2
```

 
 
 Data are loaded by Deeplodocus through two interfaces :
 - Dataset
 - Dataloader

## Dataset

The `Dataset` has two main objectives :
- Automatically read, check the completeness and format the data given in the config files in folders and files
- Open, augment/transform the data before being transmitted to the network


## Dataloader

The `Dataloader` can call the `Dataset` in parralel of the training using the CPU.
The data are assembled into batches and then sent to the `Trainer` or the `Tester`

NOTE : Currently the Dataloader is provided by the PyTorch's Dataloader.




## Data Transformation

Data transformation is made using four different `Transformer` classes managed by a `TransformManager`. The following `Transformer` classes are available:
- Sequential
- One Of
- Some Of
- Pointer


### TransformManager 

Here is an example of config file to generate the `TransformManager` for the training, validation and test.
Make sure the three are given in one file.


```yaml

# transform_config.yaml

# ___________________________________
#
# ---- TRANSFORM MANAGER EXAMPLE ----
# ___________________________________
#
train:                                                                              # Training entries
    name: "Train Transform Manager"
    inputs :
      - ".config/transforms/transform_input_train_left.yaml"
      - "*input:0"                                                                  # Example of pointer which points to first transformer of input
    labels :
      - Null                                                                        
      - Null
    additional_data:
      - Null

validation:                                                                        # Validation entries
    name: "Validation Transform Manager"
    inputs :
      - ".config/transforms/transform_input_validation_left.yaml"
      - "*input:0"                                                                  # Example of pointer which points to first transformer of input
    labels :
      - Null
      - Null
    additional_data:
      - Null

test:                                                                               # Test entries
    name: "Validation Transform Manager"
    inputs:
      - Null
      - Null
    labels :
      - Null
      - Null
    additional_data:
      - Null
```

Each entry has to be given a `Transformer`. If none is desired, please enter `Null`.

### Sequential

The `Sequential` transformer applies transformation operations sequentially on the given input.

Here is an example of config file for a `Sequential` transformer:

```yaml

# sequential_example.yaml

# ______________________________________
#
# ---- TRANSFORM SEQUENTIAL EXAMPLE ----
# ______________________________________
#

method: "sequential"
name: "Sequential example"
normalize_output: True

transforms:
  - blur :
      kernel_size : 3
  - random_blur:
      kernel_size_min: 15
      kernel_size_max : 21
```

For more details on each transform please check the corresponding documentation


### One Of

The `Oneof` transformer applies on the given input one transformation operation among the ones available in the given list.

Here is an example of config file for a `OneOf` transformer:

```yaml
# oneof_example.yaml

# _________________________________
#
# ---- TRANSFORM ONEOF EXAMPLE ----
# _________________________________
#

method: "oneof"
name: "OneOf example"
normalize_output: yes

transforms:
  - blur :
      kernel_size : 3
  - random_blur:
      kernel_size_min: 15
      kernel_size_max : 21

```

For more details on each transform please check the corresponding documentation


### Some Of

The `Someof` transformer applies multiple transformation operations to the given input.
The number of operations applied can be fixed if the user specifies `num_transformations`.
The number of transformation can also be a random number between `num_transformations_min` and `num_transformations_max`.

Here is an example of config file for a `SomeOf` transformer:

```yaml
# someof_example.yaml

#___________________________________
#
# ---- TRANSFORM SOMEOF EXAMPLE ----
# __________________________________
#

method: "someof"
name: "SomeOf example"
num_transformations : 3             #If used, comment "num_transformations_min" and  "num_transformations_max"
#num_transformations_min : 1        #If used, comment "num_transformations"
#num_transformations_max : 5        #If used, comment "num_transformations"
normalize_output: yes

transforms:
  - blur :
      kernel_size : 3
  - random_blur:
      kernel_size_min: 15
      kernel_size_max : 21


```

For more details on each transform please check the corresponding documentation

### Pointer

The Pointer consists in redirecting the transformation process to another pointer.
Using a pointer has two major advantages :

- It avoids creating another transformer config file
- It allows multiple entries system to have exactly the same transformation operations applied to all its entries. [1]

[1] - e.g. : Working on a stereo vision system. The input of the network consists in two images (left and right).
If we create to transformers (one for the left image and one for the right image) then the left and right image will not have the same transformations applied (if random operations are used).
Using a pointer for the right image to the left transformer will allow to have exactly the same transformations applied to both the right and left image (even if random operations and done (e.g. random blur)

To define a Pointer, instead of the path to the transformer config file, enter 

```yaml
*category:index
```

```yaml
# * Is necessary so that Deeplodocus understands it is a pointer
# category: "input", "label", "additional_data"
# index: The index of the transformer in the selected category (indexed at 0)

#e.g. : "*input:0" points to the first transformer of the input
```

Note : A `Pointer` cannot point to another `Pointer`




### Offline

Offline data augmentation is not available

### Custom transforms

Currently not available
