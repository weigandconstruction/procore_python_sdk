# RestV10FilesPost201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | File id | [optional] 
**name** | **str** | File name | [optional] 
**parent_id** | **int** | File parent id | [optional] 
**size** | **int** | File size | [optional] 
**description** | **str** | File description | [optional] 
**updated_at** | **datetime** | File updated at | [optional] 
**created_at** | **datetime** | File created at | [optional] 
**checked_out_until** | **datetime** | File checked out until | [optional] 
**name_with_path** | **str** | Full file path with filename | [optional] 
**private** | **bool** | File private status | [optional] 
**is_tracked** | **bool** | File is tracked status | [optional] 
**tracked_folder** | **object** | Folder watchers | [optional] 
**checked_out_by** | [**RestV10FilesPost201ResponseCheckedOutBy**](RestV10FilesPost201ResponseCheckedOutBy.md) |  | [optional] 
**file_type** | **str** | File type | [optional] 
**file_versions** | [**List[RestV10FilesPost201ResponseFileVersionsInner]**](RestV10FilesPost201ResponseFileVersionsInner.md) |  | [optional] 
**legacy_id** | **int** | Legacy File id | [optional] 
**is_deleted** | **bool** | File is in the recycle bin status | [optional] 
**custom_fields** | [**RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields**](RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_files_post201_response import RestV10FilesPost201Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10FilesPost201Response from a JSON string
rest_v10_files_post201_response_instance = RestV10FilesPost201Response.from_json(json)
# print the JSON string representation of the object
print(RestV10FilesPost201Response.to_json())

# convert the object into a dict
rest_v10_files_post201_response_dict = rest_v10_files_post201_response_instance.to_dict()
# create an instance of RestV10FilesPost201Response from a dict
rest_v10_files_post201_response_from_dict = RestV10FilesPost201Response.from_dict(rest_v10_files_post201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


