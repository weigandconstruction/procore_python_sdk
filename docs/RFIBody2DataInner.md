# RFIBody2DataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the RFI | [optional] 
**cost_code_id** | **int** | The ID of the Cost Code of the RFI | [optional] 
**cost_impact** | [**RFIBodyRfiCostImpact**](RFIBodyRfiCostImpact.md) |  | [optional] 
**drawing_number** | **str** | The Drawing Number of the RFI | [optional] 
**due_date** | **date** | The Due Date of the RFI *Only admin users can set this field | [optional] 
**location_id** | **int** | The ID of the Location of the RFI | [optional] 
**private** | **bool** | The Private status of the RFI | [optional] [default to False]
**received_from_login_information_id** | **int** | The ID of the Received From User of the RFI | [optional] 
**reference** | **str** | The Reference of the RFI | [optional] 
**responsible_contractor_id** | **int** | The ID of the Responsible Contractor Vendor of the RFI | [optional] 
**rfi_manager_id** | **int** | The ID of the RFI Manager User of the RFI *Only admin users (or standard users, if the project&#39;s configuration allows for it) can set this field | [optional] 
**schedule_impact** | [**RFIBodyRfiScheduleImpact**](RFIBodyRfiScheduleImpact.md) |  | [optional] 
**specification_section_id** | **int** | The ID of the Specification Section of the RFI | [optional] 
**sub_job_id** | **int** | The ID of the Sub Job of the RFI | [optional] 
**subject** | **str** | The Subject of the RFI | [optional] 

## Example

```python
from procore_sdk.models.rfi_body2_data_inner import RFIBody2DataInner

# TODO update the JSON string below
json = "{}"
# create an instance of RFIBody2DataInner from a JSON string
rfi_body2_data_inner_instance = RFIBody2DataInner.from_json(json)
# print the JSON string representation of the object
print(RFIBody2DataInner.to_json())

# convert the object into a dict
rfi_body2_data_inner_dict = rfi_body2_data_inner_instance.to_dict()
# create an instance of RFIBody2DataInner from a dict
rfi_body2_data_inner_from_dict = RFIBody2DataInner.from_dict(rfi_body2_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


