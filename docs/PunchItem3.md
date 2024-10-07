# PunchItem3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**ball_in_court** | [**List[PunchItemBallInCourtInner]**](PunchItemBallInCourtInner.md) | Array of Users | [optional] 
**comments** | [**List[Comment]**](Comment.md) | Punch Item Comments | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**closed_at** | **datetime** | Closed at | [optional] 
**deleted_at** | **datetime** | Deleted at | [optional] 
**description** | **str** | Description | [optional] 
**due_date** | **date** | Due Date | [optional] 
**name** | **str** | Name | [optional] 
**schedule_risk** | **str** | Assessed risk level of on-time completion | [optional] 
**schedule_risk_reason** | **str** | Reason for assessed risk level of on-time completion | [optional] 
**position** | **int** | Position | [optional] 
**priority** | **str** | Punch item priority - &#39;low&#39;, &#39;medium&#39;, &#39;high&#39; | [optional] 
**private** | **bool** | Privacy status | [optional] 
**status** | **str** | Status | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 
**date_initiated** | **date** | Date created | [optional] 
**schedule_impact** | **str** | Schedule impact status | [optional] 
**schedule_impact_days** | **int** | Schedule impact value in days | [optional] 
**reference** | **str** | Used to create a reference point between a Punch Item within Procore and a corresponding Punch Item outside of Procore | [optional] 
**cost_impact** | **str** | Cost impact status | [optional] 
**cost_impact_amount** | **int** | Cost impact amount | [optional] 
**can_email** | **bool** | Punch Item has Punch Item Assignments or distribution members to email to | [optional] 
**drawing_ids** | **List[int]** | Array of Drawing IDs | [optional] 
**current_drawing_revision_ids** | **List[int]** | Array of Current Drawing Revision IDs | [optional] 
**distribution_members** | [**List[RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy]**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) | Users on the Punch Item distribution list | [optional] 
**location** | [**Location**](Location.md) |  | [optional] 
**trade** | [**Trade2**](Trade2.md) |  | [optional] 
**created_by** | [**PunchItemCreator**](PunchItemCreator.md) |  | [optional] 
**punch_item_manager** | [**PunchItemManager**](PunchItemManager.md) |  | [optional] 
**final_approver** | [**PunchItemFinalApprover**](PunchItemFinalApprover.md) |  | [optional] 
**punch_item_type** | [**PunchItemType**](PunchItemType.md) |  | [optional] 
**cost_code** | [**TimecardEntryFullCostCode**](TimecardEntryFullCostCode.md) |  | [optional] 
**assignments** | [**List[PunchItem3AssignmentsInner]**](PunchItem3AssignmentsInner.md) | Array of Punch Item Assignments | [optional] 
**attachments** | [**List[RestV10WorkOrderContractsPost201ResponseAttachmentsInner]**](RestV10WorkOrderContractsPost201ResponseAttachmentsInner.md) | Array of Punch Item Attachments | [optional] 
**images** | [**List[RestV10WorkOrderContractsPost201ResponseAttachmentsInner]**](RestV10WorkOrderContractsPost201ResponseAttachmentsInner.md) | Array of Images *DEPRECATED. Please use attachments instead | [optional] 
**web_images** | [**List[RestV10WorkOrderContractsPost201ResponseAttachmentsInner]**](RestV10WorkOrderContractsPost201ResponseAttachmentsInner.md) | Array of photo Attachments uploaded from the web application | [optional] 
**workflow_status** | **str** | Workflow status of the Punch Item | [optional] 
**custom_fields** | [**RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields**](RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerCustomFields.md) |  | [optional] 

## Example

```python
from procore_sdk.models.punch_item3 import PunchItem3

# TODO update the JSON string below
json = "{}"
# create an instance of PunchItem3 from a JSON string
punch_item3_instance = PunchItem3.from_json(json)
# print the JSON string representation of the object
print(PunchItem3.to_json())

# convert the object into a dict
punch_item3_dict = punch_item3_instance.to_dict()
# create an instance of PunchItem3 from a dict
punch_item3_from_dict = PunchItem3.from_dict(punch_item3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


