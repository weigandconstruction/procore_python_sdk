# ExampleOfAFolderThatIsAFileFile

will be filled if document_type is a file

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checked_out_by** | [**ExampleOfAFolderThatIsAFileFileCheckedOutBy**](ExampleOfAFolderThatIsAFileFileCheckedOutBy.md) |  | [optional] 
**checked_out_until** | **str** | File checked out time | [optional] 
**current_version** | [**RestV10FileVersionsPost201Response**](RestV10FileVersionsPost201Response.md) |  | [optional] 
**description** | **str** | File name | [optional] 
**file_type** | **str** | File type | [optional] 

## Example

```python
from procore_sdk.models.example_of_a_folder_that_is_a_file_file import ExampleOfAFolderThatIsAFileFile

# TODO update the JSON string below
json = "{}"
# create an instance of ExampleOfAFolderThatIsAFileFile from a JSON string
example_of_a_folder_that_is_a_file_file_instance = ExampleOfAFolderThatIsAFileFile.from_json(json)
# print the JSON string representation of the object
print(ExampleOfAFolderThatIsAFileFile.to_json())

# convert the object into a dict
example_of_a_folder_that_is_a_file_file_dict = example_of_a_folder_that_is_a_file_file_instance.to_dict()
# create an instance of ExampleOfAFolderThatIsAFileFile from a dict
example_of_a_folder_that_is_a_file_file_from_dict = ExampleOfAFolderThatIsAFileFile.from_dict(example_of_a_folder_that_is_a_file_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


