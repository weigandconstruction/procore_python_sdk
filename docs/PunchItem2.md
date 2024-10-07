# PunchItem2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description | [optional] 
**due** | **date** | Due date | [optional] 
**name** | **str** | Name | 
**schedule_risk** | **str** | Assessed risk level of on-time completion | [optional] 
**position** | **int** | Position | [optional] 
**priority** | **str** | Punch item priority - &#39;low&#39;, &#39;medium&#39;, &#39;high&#39; | [optional] 
**private** | **bool** | Privacy status | [optional] 
**status** | **str** | Status - &#39;open&#39; or &#39;closed&#39; | [optional] 
**date_initiated** | **date** | Date created | [optional] 
**schedule_impact** | **str** | Schedule impact status - yes_known, yes_unknown, no_impact, tbd, n_a | [optional] 
**schedule_impact_days** | **int** | Schedule impact value in days | [optional] 
**reference** | **str** | Used to create a reference point between a Punch Item within Procore and a corresponding Punch Item outside of Procore | [optional] 
**cost_code_id** | **int** | ID of the cost code associated with the punch item. | [optional] 
**cost_impact** | **str** | Cost impact Status - yes_known, yes_unknown, no_impact, tbd, n_a | [optional] 
**cost_impact_amount** | **int** | Cost impact amount | [optional] 
**trade_id** | **int** | Trade IDs | [optional] 
**punch_item_type_id** | **int** | Punch Item Type ID | [optional] 
**login_information_ids** | **List[int]** | Array of the User IDs of the Punch Item Assignments | [optional] 
**distribution_member_ids** | **List[int]** | Array of the User IDs of the Distribution Members | [optional] 
**punch_item_manager_id** | **int** | Punch Item Manager ID | [optional] 
**final_approver_id** | **int** | Punch Item Final Approver ID | [optional] 
**location_id** | **int** | The ID of the Location of the Punch Item. &#x60;location_id&#x60; takes precedence over &#x60;mt_location&#x60; | [optional] 
**mt_location** | **List[str]** | Use this for creating a new multi-tier or single-tier Location. This will be ignored if &#x60;location_id&#x60; is provided. | [optional] 
**images** | **List[str]** | Punch Item Images. *DEPRECATED. Please use attachments instead To upload images you must upload the entire payload as &#x60;multipart/form-data&#x60; content-type and specify each parameter as form-data together with &#x60;punch_item[images][0]&#x60; as files. &#x60;punch_item[images][0]&#x60; and &#x60;punch_item[images][1]&#x60; and so forth if you want to attach multiple images. | [optional] 
**workflow_status** | **str** | Workflow status of the Punch Item. These are more granular statuses in the punch item workflow. | [optional] 
**drawing_revision_ids** | **List[int]** | Drawing Revisions to attach to the response | [optional] 
**file_version_ids** | **List[int]** | File Versions to attach to the response | [optional] 
**form_ids** | **List[int]** | Forms to attach to the response | [optional] 
**image_ids** | **List[int]** | Images to attach to the response | [optional] 
**upload_ids** | **List[str]** | Uploads to attach to the response | [optional] 
**custom_field_custom_field_definition_id** | [**WorkOrderContractCustomFieldCustomFieldDefinitionId**](WorkOrderContractCustomFieldCustomFieldDefinitionId.md) |  | [optional] 

## Example

```python
from procore_sdk.models.punch_item2 import PunchItem2

# TODO update the JSON string below
json = "{}"
# create an instance of PunchItem2 from a JSON string
punch_item2_instance = PunchItem2.from_json(json)
# print the JSON string representation of the object
print(PunchItem2.to_json())

# convert the object into a dict
punch_item2_dict = punch_item2_instance.to_dict()
# create an instance of PunchItem2 from a dict
punch_item2_from_dict = PunchItem2.from_dict(punch_item2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


