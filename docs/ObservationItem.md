# ObservationItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Observation Item ID | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**closed_at** | **datetime** | Closed at | [optional] 
**deleted_at** | **datetime** | Deleted at | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 
**number** | **str** | Observation Item number | [optional] 
**name** | **str** | Observation Item name | [optional] 
**description** | **str** | Observation Item description | [optional] 
**description_rich_text** | **str** | Observation Item description | [optional] 
**status** | **str** | Observation Item status | [optional] 
**priority** | **str** | Observation Item priority | [optional] 
**date_notified** | **date** | Date that the Observation Item Assignee was notified | [optional] 
**due_date** | **date** | Date that the Observation Item is due by | [optional] 
**personal** | **bool** | Observation Item privacy status | [optional] 
**origin** | [**ObservationOrigin**](ObservationOrigin.md) |  | [optional] 
**assignee** | [**ObservationItemAssignee**](ObservationItemAssignee.md) |  | [optional] 
**created_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**location** | [**Location**](Location.md) |  | [optional] 
**specification_section** | [**ObservationItemSpecificationSection**](ObservationItemSpecificationSection.md) |  | [optional] 
**trade** | [**Trade2**](Trade2.md) |  | [optional] 
**type** | [**ObservationType**](ObservationType.md) |  | [optional] 
**custom_fields** | [**RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields**](RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields.md) |  | [optional] 

## Example

```python
from procore_sdk.models.observation_item import ObservationItem

# TODO update the JSON string below
json = "{}"
# create an instance of ObservationItem from a JSON string
observation_item_instance = ObservationItem.from_json(json)
# print the JSON string representation of the object
print(ObservationItem.to_json())

# convert the object into a dict
observation_item_dict = observation_item_instance.to_dict()
# create an instance of ObservationItem from a dict
observation_item_from_dict = ObservationItem.from_dict(observation_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


