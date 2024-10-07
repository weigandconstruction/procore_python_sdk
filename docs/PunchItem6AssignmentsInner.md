# PunchItem6AssignmentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**approved** | **bool** | Resolution status | [optional] 
**comment** | **str** | Additional comment | [optional] 
**login_information_id** | **int** |  | [optional] 
**login_information_name** | **str** |  | [optional] 
**login_information** | [**PunchItem6CreatedBy**](PunchItem6CreatedBy.md) |  | [optional] 
**attachments** | [**List[RestV10WorkOrderContractsPost201ResponseAttachmentsInner]**](RestV10WorkOrderContractsPost201ResponseAttachmentsInner.md) | Array of Attachments | [optional] 
**vendor** | [**Compact**](Compact.md) |  | [optional] 
**notified_at** | **datetime** | Date assignee was notified of Punch Item | [optional] 
**responded_at** | **datetime** | Date Assignee responded to the Punch Item | [optional] 
**status** | **str** | Status of Assignment | [optional] 
**manager_accepted_at** | **datetime** | Date Punch Item Manager resolved the Punch Item Assignment | [optional] 
**user_name** | **str** |  | [optional] 
**updated_at** | **datetime** | Date Assignment was updated | [optional] 

## Example

```python
from procore_sdk.models.punch_item6_assignments_inner import PunchItem6AssignmentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PunchItem6AssignmentsInner from a JSON string
punch_item6_assignments_inner_instance = PunchItem6AssignmentsInner.from_json(json)
# print the JSON string representation of the object
print(PunchItem6AssignmentsInner.to_json())

# convert the object into a dict
punch_item6_assignments_inner_dict = punch_item6_assignments_inner_instance.to_dict()
# create an instance of PunchItem6AssignmentsInner from a dict
punch_item6_assignments_inner_from_dict = PunchItem6AssignmentsInner.from_dict(punch_item6_assignments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


