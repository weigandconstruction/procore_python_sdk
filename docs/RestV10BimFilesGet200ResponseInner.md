# RestV10BimFilesGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Name of the file to be associated to a project | [optional] 
**uuid** | **str** | Unique UUID associated with the file | [optional] 
**project_id** | **float** | Unique identifier for the project. | [optional] 
**company_id** | **float** | Company ID | [optional] 
**created_at** | **datetime** | Created date | [optional] 
**updated_at** | **datetime** | Updated date | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_bim_files_get200_response_inner import RestV10BimFilesGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10BimFilesGet200ResponseInner from a JSON string
rest_v10_bim_files_get200_response_inner_instance = RestV10BimFilesGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10BimFilesGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_bim_files_get200_response_inner_dict = rest_v10_bim_files_get200_response_inner_instance.to_dict()
# create an instance of RestV10BimFilesGet200ResponseInner from a dict
rest_v10_bim_files_get200_response_inner_from_dict = RestV10BimFilesGet200ResponseInner.from_dict(rest_v10_bim_files_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


