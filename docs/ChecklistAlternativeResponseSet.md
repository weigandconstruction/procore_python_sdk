# ChecklistAlternativeResponseSet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conforming_response** | **str** | Term used to represent conforming statuses on items within the current template, e.g. \&quot;Pass\&quot; or \&quot;Safe\&quot;. This maps to an item status of \&quot;yes\&quot;. | [optional] 
**deficient_response** | **str** | Term used to represent deficient statuses on items within the current template, e.g. \&quot;Fail\&quot; or \&quot;At Risk\&quot;.  This maps to an item status of \&quot;no\&quot;. | [optional] 
**var_global** | **bool** | Represents whether a response set has been provided by Procore. | [optional] 

## Example

```python
from procore_sdk.models.checklist_alternative_response_set import ChecklistAlternativeResponseSet

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistAlternativeResponseSet from a JSON string
checklist_alternative_response_set_instance = ChecklistAlternativeResponseSet.from_json(json)
# print the JSON string representation of the object
print(ChecklistAlternativeResponseSet.to_json())

# convert the object into a dict
checklist_alternative_response_set_dict = checklist_alternative_response_set_instance.to_dict()
# create an instance of ChecklistAlternativeResponseSet from a dict
checklist_alternative_response_set_from_dict = ChecklistAlternativeResponseSet.from_dict(checklist_alternative_response_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


