# RestV10ChangeEventsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**number** | **int** | Number with alpha characters stripped out | [optional] 
**alphanumeric_number** | **str** | Number including alpha characters | [optional] 
**origin_data** | **str** | Origin data | [optional] 
**origin_id** | **str** | Origin ID | [optional] 
**title** | **str** | Title | [optional] 
**description** | **str** | Description | [optional] 
**status** | **str** | Status | [optional] 
**project_id** | **int** | Unique identifier for the project. | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**deleted_at** | **datetime** | Deleted at | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 
**event_type** | **str** | Event type | [optional] 
**event_scope** | **str** | Event scope | [optional] 
**change_event_origin_id** | **int** | Origin ID | [optional] 
**change_event_origin_type** | **str** | Origin type | [optional] 
**rfi** | [**RFQChangeEventRfi**](RFQChangeEventRfi.md) |  | [optional] 
**change_event_line_items** | [**List[RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInner]**](RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInner.md) |  | [optional] 
**change_order_change_reason** | [**RFQChangeEventChangeOrderChangeReason**](RFQChangeEventChangeOrderChangeReason.md) |  | [optional] 
**change_event_status** | [**RFQChangeEventChangeEventStatus**](RFQChangeEventChangeEventStatus.md) |  | [optional] 
**created_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**attachments** | [**List[RestV10WorkOrderContractsPost201ResponseAttachmentsInner]**](RestV10WorkOrderContractsPost201ResponseAttachmentsInner.md) |  | [optional] 
**rfqs** | [**List[RFQ4]**](RFQ4.md) | Return a list of all Request for Quotes (RFQs) to a specific change event in a project. **NOTE:** If you see &#x60;[]&#x60;, you might not have permissions to see RFQs for Change Events. | [optional] 
**currency_configuration** | [**RFQCurrencyConfiguration**](RFQCurrencyConfiguration.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_change_events_get200_response_inner import RestV10ChangeEventsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ChangeEventsGet200ResponseInner from a JSON string
rest_v10_change_events_get200_response_inner_instance = RestV10ChangeEventsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ChangeEventsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_change_events_get200_response_inner_dict = rest_v10_change_events_get200_response_inner_instance.to_dict()
# create an instance of RestV10ChangeEventsGet200ResponseInner from a dict
rest_v10_change_events_get200_response_inner_from_dict = RestV10ChangeEventsGet200ResponseInner.from_dict(rest_v10_change_events_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


