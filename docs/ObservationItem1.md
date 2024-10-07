# ObservationItem1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Observation Item ID | [optional] 
**number** | **str** | Observation Item number | [optional] 
**name** | **str** | Observation Item name | [optional] 
**description** | **str** | Observation Item description | [optional] 
**status** | **str** | Observation Item status | [optional] 
**checklist_item** | [**ObservationItem1ChecklistItem**](ObservationItem1ChecklistItem.md) |  | [optional] 
**checklist_list** | [**ObservationItem1ChecklistList**](ObservationItem1ChecklistList.md) |  | [optional] 
**priority** | **str** | Observation Item priority | [optional] 
**date_notified** | **date** | Date that the Observation Item Assignee was notified | [optional] 
**due_date** | **date** | Observation Item due date | [optional] 
**closed_at** | **datetime** | Closed at | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 
**deleted_at** | **datetime** | Deleted at | [optional] 
**description_rich_text** | **str** | Description | [optional] 
**personal** | **bool** | Observation Item privacy status | [optional] 
**current_drawing_revision_ids** | **List[int]** | Current Drawing Revision IDs associated to the Observation Item | [optional] 
**drawing_revisions** | **List[int]** | Drawing Revision IDs associated to the Observation Item | [optional] 
**drawing_ids** | **List[int]** | Drawing IDs associated to an Observation Item&#39;s Drawing Revisions | [optional] 
**origin** | [**ObservationOrigin1**](ObservationOrigin1.md) |  | [optional] 
**attachments** | [**List[ObservationItem1AttachmentsInner]**](ObservationItem1AttachmentsInner.md) |  | [optional] 
**assignee** | [**ObservationItemAssignee**](ObservationItemAssignee.md) |  | [optional] 
**distribution_members** | [**List[RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy]**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) | Users on the Observation Item distribution list | [optional] 
**created_by** | [**ObservationItemCreator**](ObservationItemCreator.md) |  | [optional] 
**specification_section** | [**ObservationItem1SpecificationSection**](ObservationItem1SpecificationSection.md) |  | [optional] 
**location** | [**Location**](Location.md) |  | [optional] 
**trade** | [**Trade2**](Trade2.md) |  | [optional] 
**type** | [**ObservationType**](ObservationType.md) |  | [optional] 
**contributing_behavior** | [**ContributingBehavior**](ContributingBehavior.md) |  | [optional] 
**contributing_condition** | [**ContributingCondition**](ContributingCondition.md) |  | [optional] 
**hazard** | [**Hazard**](Hazard.md) |  | [optional] 
**custom_fields** | [**RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields**](RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields.md) |  | [optional] 

## Example

```python
from procore_sdk.models.observation_item1 import ObservationItem1

# TODO update the JSON string below
json = "{}"
# create an instance of ObservationItem1 from a JSON string
observation_item1_instance = ObservationItem1.from_json(json)
# print the JSON string representation of the object
print(ObservationItem1.to_json())

# convert the object into a dict
observation_item1_dict = observation_item1_instance.to_dict()
# create an instance of ObservationItem1 from a dict
observation_item1_from_dict = ObservationItem1.from_dict(observation_item1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


