# RequisitionContractItem

Requisition (Subcontractor Invoice) Contract Item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**work_completed_this_period** | **str** | The amount of work completed this period | [optional] 
**materials_presently_stored** | **str** | The amount of materials presently stored | [optional] 
**work_completed_retainage_retained_this_period** | **str** | Work completed retainage amount retained this period (admin user only, work_completed_this_period should be non-zero to hold a retainage) | [optional] 
**materials_stored_retainage_currently_retained** | **str** | Materials stored retainage amount currently retained (admin user, amount accounting only, materials_presently_stored should be non-zero to hold a retainage) | [optional] 
**work_completed_retainage_released_this_period** | **str** | The amount of work completed retainage released this period | [optional] 
**work_completed_this_period_quantity** | **str** | Work completed this period quantity (unit accounting contract only) | [optional] 

## Example

```python
from procore_sdk.models.requisition_contract_item import RequisitionContractItem

# TODO update the JSON string below
json = "{}"
# create an instance of RequisitionContractItem from a JSON string
requisition_contract_item_instance = RequisitionContractItem.from_json(json)
# print the JSON string representation of the object
print(RequisitionContractItem.to_json())

# convert the object into a dict
requisition_contract_item_dict = requisition_contract_item_instance.to_dict()
# create an instance of RequisitionContractItem from a dict
requisition_contract_item_from_dict = RequisitionContractItem.from_dict(requisition_contract_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


