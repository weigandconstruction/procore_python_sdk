# PunchItem6


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**ball_in_court** | [**List[PunchItemBallInCourtInner]**](PunchItemBallInCourtInner.md) | Array of Users | [optional] 
**closed_at** | **datetime** | Date time Punch Item was closed | [optional] 
**cost_impact** | **str** | Cost impact status | [optional] 
**cost_impact_amount** | **str** | Cost impact amount | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**deleted_at** | **datetime** | Deleted at | [optional] 
**description** | **str** | Description | [optional] 
**due_date** | **date** | Due date | [optional] 
**name** | **str** | Name | [optional] 
**reference** | **str** | Used to create a reference point between a Punch Item within Procore and a corresponding Punch Item outside of Procore | [optional] 
**schedule_impact** | **str** | Schedule impact status | [optional] 
**schedule_impact_days** | **int** | Schedule impact value in days | [optional] 
**schedule_risk** | **str** | Assessed risk level of on-time completion | [optional] 
**schedule_risk_reason** | **str** | Reason for assessed risk level of on-time completion | [optional] 
**schedule_risk_confidence** | **int** | Confidence of schedule risk assessment | [optional] 
**schedule_risk_probability** | **int** | Probability of schedule risk assessment | [optional] 
**position** | **int** | Position | [optional] 
**priority** | **str** | Punch item priority - &#39;low&#39;, &#39;medium&#39;, &#39;high&#39; | [optional] 
**private** | **bool** | Privacy status | [optional] 
**status** | **str** | Status | [optional] 
**has_resolved_responses** | **bool** | At least one Punch Item Assignment has a status of &#39;resolved | [optional] 
**has_unresolved_responses** | **bool** | At least one Punch Item Assignment has a status of &#39;unresolved&#39; | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 
**location** | [**Location1**](Location1.md) |  | [optional] 
**trade** | [**Trade**](Trade.md) |  | [optional] 
**created_by** | [**PunchItem6CreatedBy**](PunchItem6CreatedBy.md) |  | [optional] 
**punch_item_manager** | [**PunchItemBallInCourtInner**](PunchItemBallInCourtInner.md) |  | [optional] 
**final_approver** | [**PunchItemBallInCourtInner**](PunchItemBallInCourtInner.md) |  | [optional] 
**punch_item_type** | [**PunchItemType**](PunchItemType.md) |  | [optional] 
**cost_code** | [**TimecardEntryFullCostCode**](TimecardEntryFullCostCode.md) |  | [optional] 
**assignments** | [**List[PunchItem6AssignmentsInner]**](PunchItem6AssignmentsInner.md) | Array of Punch Item Assignments | [optional] 
**assignees** | [**List[PunchItem6CreatedBy]**](PunchItem6CreatedBy.md) | Punch Item Assignees | [optional] 
**latitude** | **str** | Latitude of Punch Item (Deprecated) | [optional] 
**longitude** | **str** | Longitude of Punch Item (Deprecated) | [optional] 
**horizontal_accuracy** | **str** | Horizontal Accuracy of Punch Item (Deprecated) | [optional] 
**vertical_accuracy** | **str** | Vertical Accuracy of Punch Item (Deprecated) | [optional] 
**altitude** | **str** | Altitude of Punch Item (Deprecated) | [optional] 
**workflow_status** | **str** | Workflow status of the Punch Item | [optional] 
**custom_fields** | [**RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerCustomFields**](RestV10ProjectsProjectIdVisitorLogsGet200ResponseInnerCustomFields.md) |  | [optional] 

## Example

```python
from procore_sdk.models.punch_item6 import PunchItem6

# TODO update the JSON string below
json = "{}"
# create an instance of PunchItem6 from a JSON string
punch_item6_instance = PunchItem6.from_json(json)
# print the JSON string representation of the object
print(PunchItem6.to_json())

# convert the object into a dict
punch_item6_dict = punch_item6_instance.to_dict()
# create an instance of PunchItem6 from a dict
punch_item6_from_dict = PunchItem6.from_dict(punch_item6_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


