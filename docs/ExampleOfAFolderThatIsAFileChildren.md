# ExampleOfAFolderThatIsAFileChildren

if folder is implicitly tracked, reflects the folder that is the cause

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_children** | **bool** | whether the Folder has children | [optional] 
**has_children_files** | **bool** | whether the Folder has children that are file | [optional] 
**has_children_folders** | **bool** | whether the Folder has children that are not file | [optional] 

## Example

```python
from procore_sdk.models.example_of_a_folder_that_is_a_file_children import ExampleOfAFolderThatIsAFileChildren

# TODO update the JSON string below
json = "{}"
# create an instance of ExampleOfAFolderThatIsAFileChildren from a JSON string
example_of_a_folder_that_is_a_file_children_instance = ExampleOfAFolderThatIsAFileChildren.from_json(json)
# print the JSON string representation of the object
print(ExampleOfAFolderThatIsAFileChildren.to_json())

# convert the object into a dict
example_of_a_folder_that_is_a_file_children_dict = example_of_a_folder_that_is_a_file_children_instance.to_dict()
# create an instance of ExampleOfAFolderThatIsAFileChildren from a dict
example_of_a_folder_that_is_a_file_children_from_dict = ExampleOfAFolderThatIsAFileChildren.from_dict(example_of_a_folder_that_is_a_file_children_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


