# BIMFileUploadCreatedBy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Login Information ID | [optional] 
**company_name** | **str** | User Company name | [optional] 
**name** | **str** | User name | [optional] 
**locale** | **str** | User dictionary | [optional] 
**login** | **str** | User email | [optional] 

## Example

```python
from procore_sdk.models.bim_file_upload_created_by import BIMFileUploadCreatedBy

# TODO update the JSON string below
json = "{}"
# create an instance of BIMFileUploadCreatedBy from a JSON string
bim_file_upload_created_by_instance = BIMFileUploadCreatedBy.from_json(json)
# print the JSON string representation of the object
print(BIMFileUploadCreatedBy.to_json())

# convert the object into a dict
bim_file_upload_created_by_dict = bim_file_upload_created_by_instance.to_dict()
# create an instance of BIMFileUploadCreatedBy from a dict
bim_file_upload_created_by_from_dict = BIMFileUploadCreatedBy.from_dict(bim_file_upload_created_by_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


