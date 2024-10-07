# Folder1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Folder id | [optional] 
**name** | **str** | Folder name | [optional] 
**parent_id** | **int** | Folder parent id | [optional] 
**private** | **bool** | Folder private status | [optional] 
**updated_at** | **datetime** | Folder updated at | [optional] 
**is_tracked** | **bool** | Folder is tracked status | [optional] 
**tracked_folder** | **object** | Folder watchers | [optional] 
**name_with_path** | **str** | Full file path with folder name | [optional] 
**folders** | **List[object]** | The child Folders of the Folder | [optional] 
**files** | **List[object]** | The child Files of the Folder | [optional] 
**read_only** | **bool** | Folder read only status | [optional] 
**is_deleted** | **bool** | File is in the recycle bin status | [optional] 
**is_recycle_bin** | **bool** | Folder is recycle bin status | [optional] 
**has_children** | **bool** | Folder has children status | [optional] 
**has_children_files** | **bool** | Folder has at least one child that is a file status | [optional] 
**has_children_folders** | **bool** | Folder has at least one child that is a folder status | [optional] 
**custom_fields** | [**RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields**](RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields.md) |  | [optional] 

## Example

```python
from procore_sdk.models.folder1 import Folder1

# TODO update the JSON string below
json = "{}"
# create an instance of Folder1 from a JSON string
folder1_instance = Folder1.from_json(json)
# print the JSON string representation of the object
print(Folder1.to_json())

# convert the object into a dict
folder1_dict = folder1_instance.to_dict()
# create an instance of Folder1 from a dict
folder1_from_dict = Folder1.from_dict(folder1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


