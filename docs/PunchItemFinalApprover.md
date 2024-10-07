# PunchItemFinalApprover

User in charge of closing the Punch Item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | User ID | [optional] 
**name** | **str** | User Name | [optional] 
**login** | **str** | User Email | [optional] 

## Example

```python
from procore_sdk.models.punch_item_final_approver import PunchItemFinalApprover

# TODO update the JSON string below
json = "{}"
# create an instance of PunchItemFinalApprover from a JSON string
punch_item_final_approver_instance = PunchItemFinalApprover.from_json(json)
# print the JSON string representation of the object
print(PunchItemFinalApprover.to_json())

# convert the object into a dict
punch_item_final_approver_dict = punch_item_final_approver_instance.to_dict()
# create an instance of PunchItemFinalApprover from a dict
punch_item_final_approver_from_dict = PunchItemFinalApprover.from_dict(punch_item_final_approver_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


