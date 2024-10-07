# Commitment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | Commitment ID | [optional] 
**title** | **str** | Title | [optional] 
**number** | **str** | Number | [optional] 
**status** | **str** | Status | [optional] 
**description** | **str** | Description of the Prime Contract | [optional] 
**executed** | **bool** | Executed status | [optional] 
**delivery_date** | **date** | Delivery date | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**private** | **bool** | If true, visible to admins only; otherwise visible to those with access to the parent contract. | [optional] 
**vendor** | [**RestV10ProjectsProjectIdWasteLogsGet200ResponseInnerVendor**](RestV10ProjectsProjectIdWasteLogsGet200ResponseInnerVendor.md) |  | [optional] 

## Example

```python
from procore_sdk.models.commitment import Commitment

# TODO update the JSON string below
json = "{}"
# create an instance of Commitment from a JSON string
commitment_instance = Commitment.from_json(json)
# print the JSON string representation of the object
print(Commitment.to_json())

# convert the object into a dict
commitment_dict = commitment_instance.to_dict()
# create an instance of Commitment from a dict
commitment_from_dict = Commitment.from_dict(commitment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


