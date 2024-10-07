# RestV10FoldersPostRequestFolder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_id** | **int** | The ID of the parent folder to create the folder in. If not set the folder will be created under the root folder. | [optional] 
**name** | **str** | The Name of the folder | 
**is_tracked** | **bool** | Status if a folder should be tracked (true/false) | [optional] [default to False]
**explicit_permissions** | **bool** | Set folder to private (true/false) | [optional] 
**custom_field_custom_field_definition_id** | [**WorkOrderContractCustomFieldCustomFieldDefinitionId**](WorkOrderContractCustomFieldCustomFieldDefinitionId.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_folders_post_request_folder import RestV10FoldersPostRequestFolder

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10FoldersPostRequestFolder from a JSON string
rest_v10_folders_post_request_folder_instance = RestV10FoldersPostRequestFolder.from_json(json)
# print the JSON string representation of the object
print(RestV10FoldersPostRequestFolder.to_json())

# convert the object into a dict
rest_v10_folders_post_request_folder_dict = rest_v10_folders_post_request_folder_instance.to_dict()
# create an instance of RestV10FoldersPostRequestFolder from a dict
rest_v10_folders_post_request_folder_from_dict = RestV10FoldersPostRequestFolder.from_dict(rest_v10_folders_post_request_folder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


