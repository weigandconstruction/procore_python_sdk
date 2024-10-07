# ExampleOfAFolderThatIsAFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Folder id | [optional] 
**name** | **str** | Folder name | [optional] 
**name_with_path** | **str** | Full file path with folder name | [optional] 
**parent_id** | **int** | Folder parent id | [optional] 
**created_at** | **datetime** | Folder created at | [optional] 
**created_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**updated_at** | **datetime** | Folder updated at | [optional] 
**read_only** | **bool** | File is read_only (only updatable via Schedule) | [optional] 
**is_deleted** | **bool** | Folder is in the recycle bin status | [optional] 
**is_recycle_bin** | **bool** | Folder is recycle bin status | [optional] 
**document_type** | **str** | Folder or File | [optional] 
**is_tracked** | **bool** | Status whether Folder is explicitly tracked | [optional] 
**private** | **bool** | Status whether Folder is explicitly private | [optional] 
**private_parent** | [**Folder2**](Folder2.md) |  | [optional] 
**tracked_folder** | [**Folder2**](Folder2.md) |  | [optional] 
**file** | [**ExampleOfAFolderThatIsAFileFile**](ExampleOfAFolderThatIsAFileFile.md) |  | [optional] 
**children** | [**ExampleOfAFolderThatIsAFileChildren**](ExampleOfAFolderThatIsAFileChildren.md) |  | [optional] 
**custom_fields** | [**RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerCustomFields**](RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerCustomFields.md) |  | [optional] 

## Example

```python
from procore_sdk.models.example_of_a_folder_that_is_a_file import ExampleOfAFolderThatIsAFile

# TODO update the JSON string below
json = "{}"
# create an instance of ExampleOfAFolderThatIsAFile from a JSON string
example_of_a_folder_that_is_a_file_instance = ExampleOfAFolderThatIsAFile.from_json(json)
# print the JSON string representation of the object
print(ExampleOfAFolderThatIsAFile.to_json())

# convert the object into a dict
example_of_a_folder_that_is_a_file_dict = example_of_a_folder_that_is_a_file_instance.to_dict()
# create an instance of ExampleOfAFolderThatIsAFile from a dict
example_of_a_folder_that_is_a_file_from_dict = ExampleOfAFolderThatIsAFile.from_dict(example_of_a_folder_that_is_a_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


