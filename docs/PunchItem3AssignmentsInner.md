# PunchItem3AssignmentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**approved** | **bool** | Resolution status | [optional] 
**comment** | **str** | Additional comments | [optional] 
**notified_at** | **date** | Date Assignee was notified | [optional] 
**updated_at** | **date** | Date Assignee response was updated on the Punch Item | [optional] 
**login_information** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**attachments** | [**List[RestV10WorkOrderContractsPost201ResponseAttachmentsInner]**](RestV10WorkOrderContractsPost201ResponseAttachmentsInner.md) | Array of Attachments | [optional] 

## Example

```python
from procore_sdk.models.punch_item3_assignments_inner import PunchItem3AssignmentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PunchItem3AssignmentsInner from a JSON string
punch_item3_assignments_inner_instance = PunchItem3AssignmentsInner.from_json(json)
# print the JSON string representation of the object
print(PunchItem3AssignmentsInner.to_json())

# convert the object into a dict
punch_item3_assignments_inner_dict = punch_item3_assignments_inner_instance.to_dict()
# create an instance of PunchItem3AssignmentsInner from a dict
punch_item3_assignments_inner_from_dict = PunchItem3AssignmentsInner.from_dict(punch_item3_assignments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


