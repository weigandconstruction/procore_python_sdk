# ObservationItemResponseLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Response Log ID | [optional] 
**item_id** | **int** | Observation Item ID | [optional] 
**status** | **str** | Response Log status | [optional] 
**comment** | **str** | Response Log comment | [optional] 
**created_at** | **datetime** | Date-time the Response Log was created | [optional] 
**updated_at** | **datetime** | Date-time the Response Log was last updated | [optional] 
**created_by_name** | **str** | User name | [optional] 
**attachments** | [**List[RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInnerAttachmentsInner]**](RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInnerAttachmentsInner.md) | Response Log Attachments | [optional] 
**created_by** | [**CreatedBy**](CreatedBy.md) |  | [optional] 

## Example

```python
from procore_sdk.models.observation_item_response_log import ObservationItemResponseLog

# TODO update the JSON string below
json = "{}"
# create an instance of ObservationItemResponseLog from a JSON string
observation_item_response_log_instance = ObservationItemResponseLog.from_json(json)
# print the JSON string representation of the object
print(ObservationItemResponseLog.to_json())

# convert the object into a dict
observation_item_response_log_dict = observation_item_response_log_instance.to_dict()
# create an instance of ObservationItemResponseLog from a dict
observation_item_response_log_from_dict = ObservationItemResponseLog.from_dict(observation_item_response_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


