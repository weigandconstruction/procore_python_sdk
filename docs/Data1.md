# Data1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_id** | **int** | The ID of the parent folder to create the file in. If not set the file will be created under the root folder. | [optional] 
**name** | **str** | The Name of the file | [optional] 
**is_tracked** | **bool** | Status if a file should be tracked (true/false) | [optional] [default to False]
**explicit_permissions** | **bool** | Set file to private (true/false) | [optional] 
**description** | **str** | A description of the file | [optional] 
**data** | **str** | File to use as file data. Note that it&#39;s only possible to post a file using a multipart/form-data body (see RFC 2388). Most HTTP libraries will do the right thing when you pass in an open file or IO stream. Alternatively you can use an upload_uuid (see Company Uploads or Project Uploads). You should not use both file and upload_uuid fields in the same request. | 
**unique_name** | **bool** | Toggles automatic renaming if the file name is already taken in a folder (unique_name &#x3D; true). Returns a name taken error if a file name is taken in a folder (unique_name &#x3D; false). | [optional] 
**custom_field_custom_field_definition_id** | [**WorkOrderContractCustomFieldCustomFieldDefinitionId**](WorkOrderContractCustomFieldCustomFieldDefinitionId.md) |  | [optional] 

## Example

```python
from procore_sdk.models.data1 import Data1

# TODO update the JSON string below
json = "{}"
# create an instance of Data1 from a JSON string
data1_instance = Data1.from_json(json)
# print the JSON string representation of the object
print(Data1.to_json())

# convert the object into a dict
data1_dict = data1_instance.to_dict()
# create an instance of Data1 from a dict
data1_from_dict = Data1.from_dict(data1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


