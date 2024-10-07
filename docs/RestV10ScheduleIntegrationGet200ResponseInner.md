# RestV10ScheduleIntegrationGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | id of schedule import | [optional] 
**message** | **str** | In the event that the schedule import failed, this field will contain a description of the failure. Note that if the import was successful, or if the import has not yet been processed, this field will be &#x60;null&#x60;. | [optional] 
**processed_at** | **datetime** | The time at which the schedule import processing completed. | [optional] 
**success** | **bool** | If this field is &#x60;true&#x60;, this indicates that the schedule import was successful. &#x60;false&#x60; indicates that the schedule import failed. The &#x60;message&#x60; field should indicate why the import failed. &#x60;null&#x60; indicates that the schedule has not yet been imported, or the import was skipped as a more recent schedule was imported before this one was processed. | [optional] 
**uploaded_at** | **datetime** | The time at which the schedule was uploaded. | [optional] 
**schedule_source** | **str** | Used schedule upload method | [optional] 
**uploaded_by** | [**RestV10ScheduleIntegrationGet200ResponseInnerUploadedBy**](RestV10ScheduleIntegrationGet200ResponseInnerUploadedBy.md) |  | [optional] 
**file** | [**RestV10ScheduleIntegrationGet200ResponseInnerFile**](RestV10ScheduleIntegrationGet200ResponseInnerFile.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_schedule_integration_get200_response_inner import RestV10ScheduleIntegrationGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ScheduleIntegrationGet200ResponseInner from a JSON string
rest_v10_schedule_integration_get200_response_inner_instance = RestV10ScheduleIntegrationGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ScheduleIntegrationGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_schedule_integration_get200_response_inner_dict = rest_v10_schedule_integration_get200_response_inner_instance.to_dict()
# create an instance of RestV10ScheduleIntegrationGet200ResponseInner from a dict
rest_v10_schedule_integration_get200_response_inner_from_dict = RestV10ScheduleIntegrationGet200ResponseInner.from_dict(rest_v10_schedule_integration_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


