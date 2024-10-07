# RestV10ScheduleIntegrationGet200ResponseInnerFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** | Base name of the file without its path | [optional] 
**content_type** | **str** | A mime type or a file extension | [optional] 
**url** | **str** | URL to download the attached file. HTTP client should be prepared to follow redirects to successfully download the file. | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_schedule_integration_get200_response_inner_file import RestV10ScheduleIntegrationGet200ResponseInnerFile

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ScheduleIntegrationGet200ResponseInnerFile from a JSON string
rest_v10_schedule_integration_get200_response_inner_file_instance = RestV10ScheduleIntegrationGet200ResponseInnerFile.from_json(json)
# print the JSON string representation of the object
print(RestV10ScheduleIntegrationGet200ResponseInnerFile.to_json())

# convert the object into a dict
rest_v10_schedule_integration_get200_response_inner_file_dict = rest_v10_schedule_integration_get200_response_inner_file_instance.to_dict()
# create an instance of RestV10ScheduleIntegrationGet200ResponseInnerFile from a dict
rest_v10_schedule_integration_get200_response_inner_file_from_dict = RestV10ScheduleIntegrationGet200ResponseInnerFile.from_dict(rest_v10_schedule_integration_get200_response_inner_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


