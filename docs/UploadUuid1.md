# UploadUuid1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_id** | **int** | The ID of the parent folder to create the file in. If not set the file will be created under the root folder. | [optional] 
**name** | **str** | The Name of the file | [optional] 
**is_tracked** | **bool** | Status if a file should be tracked (true/false) | [optional] [default to False]
**explicit_permissions** | **bool** | Set file to private (true/false) | [optional] 
**description** | **str** | A description of the file | [optional] 
**unique_name** | **bool** | Toggles automatic renaming if the file name is already taken in a folder (unique_name &#x3D; true). Returns a name taken error if a file name is taken in a folder (unique_name &#x3D; false). | [optional] 
**upload_uuid** | **str** | UUID referencing a previously completed Upload. See Company Uploads or Project Uploads for instructions on how use uploads. You should not use both data and upload_uuid fields in the same request. | 
**custom_field_custom_field_definition_id** | [**WorkOrderContractCustomFieldCustomFieldDefinitionId**](WorkOrderContractCustomFieldCustomFieldDefinitionId.md) |  | [optional] 

## Example

```python
from procore_sdk.models.upload_uuid1 import UploadUuid1

# TODO update the JSON string below
json = "{}"
# create an instance of UploadUuid1 from a JSON string
upload_uuid1_instance = UploadUuid1.from_json(json)
# print the JSON string representation of the object
print(UploadUuid1.to_json())

# convert the object into a dict
upload_uuid1_dict = upload_uuid1_instance.to_dict()
# create an instance of UploadUuid1 from a dict
upload_uuid1_from_dict = UploadUuid1.from_dict(upload_uuid1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


