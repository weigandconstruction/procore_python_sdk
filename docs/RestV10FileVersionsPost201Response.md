# RestV10FileVersionsPost201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | File version id | [optional] 
**notes** | **str** | File version notes | [optional] 
**url** | **str** | File version url | [optional] 
**size** | **int** | File version size in bytes | [optional] 
**created_at** | **datetime** | File version created at | [optional] 
**number** | **int** | File version number | [optional] 
**created_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**prostore_file** | [**RestV10FileVersionsPost201ResponseAllOfProstoreFile**](RestV10FileVersionsPost201ResponseAllOfProstoreFile.md) |  | [optional] 
**file_id** | **int** | Parent Files id | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_file_versions_post201_response import RestV10FileVersionsPost201Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10FileVersionsPost201Response from a JSON string
rest_v10_file_versions_post201_response_instance = RestV10FileVersionsPost201Response.from_json(json)
# print the JSON string representation of the object
print(RestV10FileVersionsPost201Response.to_json())

# convert the object into a dict
rest_v10_file_versions_post201_response_dict = rest_v10_file_versions_post201_response_instance.to_dict()
# create an instance of RestV10FileVersionsPost201Response from a dict
rest_v10_file_versions_post201_response_from_dict = RestV10FileVersionsPost201Response.from_dict(rest_v10_file_versions_post201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


