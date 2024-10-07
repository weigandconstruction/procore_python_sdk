# ChecklistAlternativeResponseSetFull


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Alternative Response Set ID | [optional] 
**conforming_response** | **str** | Term to represent a conforming status on an item, e.g. \&quot;Pass\&quot; or \&quot;Safe\&quot;. This maps to an item status of \&quot;yes\&quot;. | [optional] 
**deficient_response** | **str** | Term to represent a deficient status on an item, e.g. \&quot;Fail\&quot; or \&quot;At Risk\&quot;.  This maps to an item status of \&quot;no\&quot;. | [optional] 
**var_global** | **bool** | Represents whether a response set has been provided by Procore. | [optional] 

## Example

```python
from procore_sdk.models.checklist_alternative_response_set_full import ChecklistAlternativeResponseSetFull

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistAlternativeResponseSetFull from a JSON string
checklist_alternative_response_set_full_instance = ChecklistAlternativeResponseSetFull.from_json(json)
# print the JSON string representation of the object
print(ChecklistAlternativeResponseSetFull.to_json())

# convert the object into a dict
checklist_alternative_response_set_full_dict = checklist_alternative_response_set_full_instance.to_dict()
# create an instance of ChecklistAlternativeResponseSetFull from a dict
checklist_alternative_response_set_full_from_dict = ChecklistAlternativeResponseSetFull.from_dict(checklist_alternative_response_set_full_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


